import com.sun.net.httpserver.*;
import java.io.*;
import java.net.InetSocketAddress;
import java.nio.charset.StandardCharsets;
import java.util.HashMap;
import java.util.Map;

public class GameServer {
    private GameEngine gameEngine;
    private HttpServer server;
    private static final int GAME_WIDTH = 400;
    private static final int GAME_HEIGHT = 600;

    public GameServer() throws IOException {
        gameEngine = new GameEngine(GAME_WIDTH, GAME_HEIGHT);
        server = HttpServer.create(new InetSocketAddress(8000), 0);
        
        // Set up handlers
        server.createContext("/", new StaticFileHandler());
        server.createContext("/api/gameState", new GameStateHandler());
        server.createContext("/api/movePlayer", new MovePlayerHandler());
        server.createContext("/api/updateGame", new UpdateGameHandler());
        server.createContext("/api/resetGame", new ResetGameHandler());
        
        server.setExecutor(null); // Use default executor
    }

    public void start() {
        server.start();
        System.out.println("Game Server started on http://localhost:8000");
        System.out.println("Open your browser and navigate to http://localhost:8000");
    }

    public static void main(String[] args) throws IOException {
        GameServer gameServer = new GameServer();
        gameServer.start();
    }

    private class StaticFileHandler implements HttpHandler {
        @Override
        public void handle(HttpExchange exchange) throws IOException {
            String path = exchange.getRequestURI().getPath();
            if (path.equals("/")) {
                path = "/index.html";
            }

            File file = new File("web" + path);

            if (file.exists() && !file.isDirectory()) {
                exchange.getResponseHeaders().set("Content-Type", getContentType(path));
                exchange.sendResponseHeaders(200, file.length());
                try (FileInputStream fis = new FileInputStream(file)) {
                    exchange.getResponseBody().write(fis.readAllBytes());
                }
            } else {
                String response = "File not found";
                exchange.sendResponseHeaders(404, response.length());
                exchange.getResponseBody().write(response.getBytes());
            }
            exchange.close();
        }

        private String getContentType(String filePath) {
            if (filePath.endsWith(".html")) return "text/html";
            if (filePath.endsWith(".css")) return "text/css";
            if (filePath.endsWith(".js")) return "application/javascript";
            if (filePath.endsWith(".json")) return "application/json";
            if (filePath.endsWith(".png")) return "image/png";
            if (filePath.endsWith(".jpg")) return "image/jpeg";
            if (filePath.endsWith(".gif")) return "image/gif";
            return "text/plain";
        }
    }

    private class GameStateHandler implements HttpHandler {
        @Override
        public void handle(HttpExchange exchange) throws IOException {
            String response = buildGameStateJson();
            exchange.getResponseHeaders().set("Content-Type", "application/json");
            exchange.getResponseHeaders().set("Access-Control-Allow-Origin", "*");
            exchange.sendResponseHeaders(200, response.length());
            exchange.getResponseBody().write(response.getBytes(StandardCharsets.UTF_8));
            exchange.close();
        }

        private String buildGameStateJson() {
            StringBuilder json = new StringBuilder();
            json.append("{");
            json.append("\"playerX\":").append(gameEngine.getPlayerX()).append(",");
            json.append("\"playerY\":").append(gameEngine.getPlayerY()).append(",");
            json.append("\"score\":").append(gameEngine.getScore()).append(",");
            json.append("\"level\":").append(gameEngine.getLevel()).append(",");
            json.append("\"gameOver\":").append(gameEngine.isGameOver()).append(",");
            json.append("\"gameWidth\":").append(gameEngine.getGameWidth()).append(",");
            json.append("\"gameHeight\":").append(gameEngine.getGameHeight()).append(",");
            json.append("\"obstacles\":[");

            int[] obsX = gameEngine.getObstacleX();
            int[] obsY = gameEngine.getObstacleY();
            for (int i = 0; i < gameEngine.getObstacleCount(); i++) {
                if (i > 0) json.append(",");
                json.append("{\"x\":").append(obsX[i]).append(",\"y\":").append(obsY[i]).append("}");
            }
            json.append("]");
            json.append("}");
            return json.toString();
        }
    }

    private class MovePlayerHandler implements HttpHandler {
        @Override
        public void handle(HttpExchange exchange) throws IOException {
            String query = exchange.getRequestURI().getQuery();
            int direction = 0;
            if (query != null && query.contains("direction=")) {
                String dirStr = query.split("=")[1];
                direction = Integer.parseInt(dirStr);
            }
            gameEngine.movePlayer(direction);

            String response = "{\"status\":\"success\"}";
            exchange.getResponseHeaders().set("Content-Type", "application/json");
            exchange.getResponseHeaders().set("Access-Control-Allow-Origin", "*");
            exchange.sendResponseHeaders(200, response.length());
            exchange.getResponseBody().write(response.getBytes(StandardCharsets.UTF_8));
            exchange.close();
        }
    }

    private class UpdateGameHandler implements HttpHandler {
        @Override
        public void handle(HttpExchange exchange) throws IOException {
            gameEngine.updateGame();

            String response = "{\"status\":\"updated\"}";
            exchange.getResponseHeaders().set("Content-Type", "application/json");
            exchange.getResponseHeaders().set("Access-Control-Allow-Origin", "*");
            exchange.sendResponseHeaders(200, response.length());
            exchange.getResponseBody().write(response.getBytes(StandardCharsets.UTF_8));
            exchange.close();
        }
    }

    private class ResetGameHandler implements HttpHandler {
        @Override
        public void handle(HttpExchange exchange) throws IOException {
            gameEngine.resetGame();

            String response = "{\"status\":\"reset\"}";
            exchange.getResponseHeaders().set("Content-Type", "application/json");
            exchange.getResponseHeaders().set("Access-Control-Allow-Origin", "*");
            exchange.sendResponseHeaders(200, response.length());
            exchange.getResponseBody().write(response.getBytes(StandardCharsets.UTF_8));
            exchange.close();
        }
    }
}
