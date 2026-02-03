import java.util.Random;

public class GameEngine {
    private int playerX;
    private int playerY;
    private int score;
    private int level;
    private boolean gameOver;
    private Random random;
    private int[] obstacleX;
    private int[] obstacleY;
    private int obstacleCount;
    private int gameWidth;
    private int gameHeight;
    private int playerSpeed;
    private int obstacleSpeed;

    public GameEngine(int width, int height) {
        this.gameWidth = width;
        this.gameHeight = height;
        this.playerX = width / 2 - 25;
        this.playerY = height - 100;
        this.score = 0;
        this.level = 1;
        this.gameOver = false;
        this.random = new Random();
        this.playerSpeed = 15;
        this.obstacleSpeed = 5 + level;
        this.obstacleCount = 3;
        this.obstacleX = new int[obstacleCount];
        this.obstacleY = new int[obstacleCount];
        initializeObstacles();
    }

    private void initializeObstacles() {
        for (int i = 0; i < obstacleCount; i++) {
            obstacleX[i] = random.nextInt(gameWidth - 50);
            obstacleY[i] = -50 - (i * 150);
        }
    }

    public void movePlayer(int direction) {
        // direction: -1 for left, 1 for right
        playerX += direction * playerSpeed;

        // Keep player within bounds
        if (playerX < 0) {
            playerX = 0;
        }
        if (playerX + 50 > gameWidth) {
            playerX = gameWidth - 50;
        }
    }

    public void updateGame() {
        if (gameOver) return;

        // Move obstacles
        for (int i = 0; i < obstacleCount; i++) {
            obstacleY[i] += obstacleSpeed;

            // Reset obstacle if it goes off screen
            if (obstacleY[i] > gameHeight) {
                obstacleY[i] = -50;
                obstacleX[i] = random.nextInt(gameWidth - 50);
                score += 10 + (level * 5);
                checkLevelUp();
            }

            // Check collision
            if (checkCollision(playerX, playerY, 50, 50, obstacleX[i], obstacleY[i], 50, 50)) {
                gameOver = true;
            }
        }
    }

    private boolean checkCollision(int x1, int y1, int w1, int h1, int x2, int y2, int w2, int h2) {
        return x1 < x2 + w2 && x1 + w1 > x2 && y1 < y2 + h2 && y1 + h1 > y2;
    }

    private void checkLevelUp() {
        if (score > level * 100) {
            level++;
            obstacleSpeed = 5 + level;
        }
    }

    public void resetGame() {
        playerX = gameWidth / 2 - 25;
        playerY = gameHeight - 100;
        score = 0;
        level = 1;
        gameOver = false;
        obstacleSpeed = 5;
        initializeObstacles();
    }

    // Getters
    public int getPlayerX() { return playerX; }
    public int getPlayerY() { return playerY; }
    public int getScore() { return score; }
    public int getLevel() { return level; }
    public boolean isGameOver() { return gameOver; }
    public int[] getObstacleX() { return obstacleX; }
    public int[] getObstacleY() { return obstacleY; }
    public int getGameWidth() { return gameWidth; }
    public int getGameHeight() { return gameHeight; }
    public int getObstacleCount() { return obstacleCount; }
}
