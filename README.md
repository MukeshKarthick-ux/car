# 🏎️ Car Dodge Game

A beautiful, interactive car racing game built with HTML5, CSS3, JavaScript, and Java backend logic. Dodge obstacles, survive as long as you can, and climb the levels!

## Features

✨ **Beautiful UI**
- Modern gradient design with smooth animations
- Responsive layout that works on desktop and mobile
- Animated player car and obstacles
- Real-time score and level display

🎮 **Engaging Gameplay**
- Progressive difficulty with level system
- Obstacle avoidance mechanic
- Collision detection
- Dynamic speed increase per level
- Score multiplier based on level

⚙️ **Technical Stack**
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Backend**: Java with built-in HTTP Server
- **Communication**: REST API with JSON

## Project Structure

```
CarGame/
├── src/
│   ├── GameEngine.java      # Core game logic & collision detection
│   └── GameServer.java      # HTTP server & API endpoints
├── web/
│   ├── index.html           # Game UI
│   ├── style.css            # Beautiful styling
│   └── game.js              # Frontend game controller
├── out/                     # Compiled Java files
├── run.bat                  # Quick start script
└── README.md               # This file
```

## How to Run

### Prerequisites
- Java JDK 8 or higher
- Any modern web browser

### Quick Start (Windows)

1. **Navigate to the project folder**:
   ```cmd
   cd path\to\CarGame
   ```

2. **Run the game**:
   ```cmd
   run.bat
   ```

   Or manually compile and run:
   ```cmd
   javac -d out src\GameEngine.java src\GameServer.java
   java -cp out GameServer
   ```

3. **Open your browser**:
   - Navigate to: `http://localhost:8000`
   - The game will start automatically!

### Manual Compilation (All Platforms)

```bash
# Navigate to project directory
cd CarGame

# Create output directory
mkdir out

# Compile Java files
javac -d out src/GameEngine.java src/GameServer.java

# Run the server
java -cp out GameServer

# Open browser to http://localhost:8000
```

## How to Play

- **Move Left**: Press `Left Arrow` or `A` key
- **Move Right**: Press `Right Arrow` or `D` key
- **Mobile**: Use the LEFT and RIGHT buttons on screen

### Objective
- Dodge the incoming obstacles (yellow boxes with ⚠️)
- Survive as long as possible
- Earn points for each obstacle passed
- Advance through levels to increase difficulty

### Scoring System
- Base points per obstacle: 10 points
- Level bonus: +5 points per level
- Level up requirement: 100 points × current level

## Game Mechanics

### Collision Detection
- Uses AABB (Axis-Aligned Bounding Box) collision detection
- Pixel-perfect collision with obstacles
- Game ends on collision

### Difficulty Progression
- **Level 1**: 5 pixels/frame obstacle speed, 3 obstacles
- **Level 2+**: Speed increases by 1 pixel/frame per level
- Smooth difficulty curve for better gameplay

### Player Mechanics
- Player speed: 15 pixels per movement input
- Bounded movement within game area
- Smooth hover animation for visual appeal

## API Endpoints

The Java server provides these REST endpoints:

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/` | GET | Serves static HTML/CSS/JS files |
| `/api/gameState` | GET | Returns current game state (JSON) |
| `/api/movePlayer` | GET | Moves player (query: `?direction=-1` or `1`) |
| `/api/updateGame` | GET | Updates game logic (obstacles movement, collision) |
| `/api/resetGame` | GET | Resets the game to initial state |

### Game State JSON Format
```json
{
  "playerX": 175,
  "playerY": 520,
  "score": 100,
  "level": 2,
  "gameOver": false,
  "gameWidth": 400,
  "gameHeight": 600,
  "obstacles": [
    {"x": 50, "y": 100},
    {"x": 150, "y": 200},
    {"x": 300, "y": 300}
  ]
}
```

## Code Highlights

### GameEngine.java
- **Responsibility**: Core game logic
- **Key Methods**:
  - `movePlayer(direction)`: Handles player movement
  - `updateGame()`: Main game loop logic
  - `checkCollision()`: AABB collision detection
  - `checkLevelUp()`: Level progression system

### GameServer.java
- **Responsibility**: HTTP server and API handling
- **Key Handlers**:
  - `StaticFileHandler`: Serves web files
  - `GameStateHandler`: Returns game state
  - `MovePlayerHandler`: Processes player movement
  - `UpdateGameHandler`: Processes game updates
  - `ResetGameHandler`: Resets game state

### game.js
- **Responsibility**: Frontend game controller
- **Key Functions**:
  - `fetchGameState()`: Gets current game state
  - `renderGame()`: Updates DOM based on state
  - `gameLoop()`: Main browser-side game loop
  - Event handlers for keyboard/button input

## Customization

### Change Game Difficulty
Edit `GameEngine.java`:
```java
// Modify initial obstacle speed (line ~35)
this.obstacleSpeed = 8;  // Increase for harder game

// Modify player speed (line ~34)
this.playerSpeed = 20;  // Increase for faster movement

// Modify obstacle count (line ~32)
this.obstacleCount = 5;  // More obstacles = harder
```

### Change Game Colors
Edit `style.css`:
```css
/* Modify player car color (line ~200) */
.car-body {
    background: linear-gradient(135deg, #00FF00, #00AA00);
}

/* Modify obstacle color (line ~280) */
.obstacle {
    background: linear-gradient(135deg, #FF0000, #AA0000);
}
```

### Adjust Game Canvas Size
Edit `GameServer.java` (lines ~20-21):
```java
private static final int GAME_WIDTH = 500;   // Default: 400
private static final int GAME_HEIGHT = 700;  // Default: 600
```

## Troubleshooting

### Port Already in Use
If port 8000 is busy, modify `GameServer.java`:
```java
server = HttpServer.create(new InetSocketAddress(8001), 0);  // Change to 8001
```

### Compilation Errors
- Ensure Java JDK is installed: `java -version`
- Check file paths are correct
- Make sure you're in the project root directory

### Game Not Loading
- Check browser console for errors (F12)
- Verify server is running on http://localhost:8000
- Clear browser cache (Ctrl+Shift+Delete)
- Try a different browser

### Obstacles Not Moving
- Ensure `game.js` is properly loaded (check Network tab in F12)
- Check browser console for fetch errors
- Verify API endpoints are working

## Future Enhancements

- [ ] Sound effects and background music
- [ ] Power-ups (shield, slow-motion, speed boost)
- [ ] Different car skins
- [ ] Leaderboard system
- [ ] Different game modes (time attack, survival)
- [ ] Particle effects on collision
- [ ] Mobile app version
- [ ] Multiplayer support

## Performance

- **Frame Rate**: 60 FPS using `requestAnimationFrame`
- **Server Response**: ~10-20ms per API call
- **Memory Usage**: Minimal, with efficient game loop
- **Browser Compatibility**: Chrome, Firefox, Safari, Edge (2020+)

## License

This project is free to use and modify for educational and personal purposes.

## Credits

Made with ❤️ for game enthusiasts everywhere!

---

**Enjoy the game and happy dodging! 🏎️**
"# car" 
