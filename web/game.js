// Game Variables
const API_BASE = 'http://localhost:8000';
let gameRunning = true;
let gameData = null;
const keys = {
    left: false,
    right: false
};
let lastMovementTime = 0;
const MOVEMENT_INTERVAL = 50; // milliseconds between movements

// Initialize Game
document.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowLeft' || e.key === 'a' || e.key === 'A') {
        keys.left = true;
        e.preventDefault();
    } else if (e.key === 'ArrowRight' || e.key === 'd' || e.key === 'D') {
        keys.right = true;
        e.preventDefault();
    }
});

document.addEventListener('keyup', (e) => {
    if (e.key === 'ArrowLeft' || e.key === 'a' || e.key === 'A') {
        keys.left = false;
        e.preventDefault();
    } else if (e.key === 'ArrowRight' || e.key === 'd' || e.key === 'D') {
        keys.right = false;
        e.preventDefault();
    }
});

// Button Press Handlers
function buttonLeftDown() {
    keys.left = true;
    document.querySelector('.btn-left').classList.add('active');
}

function buttonLeftUp() {
    keys.left = false;
    document.querySelector('.btn-left').classList.remove('active');
}

function buttonRightDown() {
    keys.right = true;
    document.querySelector('.btn-right').classList.add('active');
}

function buttonRightUp() {
    keys.right = false;
    document.querySelector('.btn-right').classList.remove('active');
}

// Move Functions
function moveLeft() {
    if (gameRunning && gameData && !gameData.gameOver) {
        fetch(`${API_BASE}/api/movePlayer?direction=-1`)
            .catch(err => console.error('Error moving left:', err));
    }
}

function moveRight() {
    if (gameRunning && gameData && !gameData.gameOver) {
        fetch(`${API_BASE}/api/movePlayer?direction=1`)
            .catch(err => console.error('Error moving right:', err));
    }
}

// Continuous Movement Handler
function handleContinuousMovement() {
    const now = Date.now();
    if (now - lastMovementTime > MOVEMENT_INTERVAL) {
        if (keys.left) {
            moveLeft();
        }
        if (keys.right) {
            moveRight();
        }
        lastMovementTime = now;
    }
}

// Fetch Game State from Server
async function fetchGameState() {
    try {
        const response = await fetch(`${API_BASE}/api/gameState`);
        if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
        gameData = await response.json();
        return gameData;
    } catch (error) {
        console.error('Error fetching game state:', error);
        return null;
    }
}

// Update Game
async function updateGame() {
    try {
        const response = await fetch(`${API_BASE}/api/updateGame`);
        if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
        return await response.json();
    } catch (error) {
        console.error('Error updating game:', error);
        return null;
    }
}

// Reset Game
async function restartGame() {
    try {
        const response = await fetch(`${API_BASE}/api/resetGame`);
        if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
        gameRunning = true;
        document.getElementById('gameOverScreen').classList.add('hidden');
        await fetchGameState();
        renderGame();
    } catch (error) {
        console.error('Error resetting game:', error);
    }
}

// Render Game
function renderGame() {
    if (!gameData) return;

    // Update Stats
    document.getElementById('score').textContent = gameData.score;
    document.getElementById('level').textContent = gameData.level;

    // Update Player Position
    const player = document.getElementById('player');
    player.style.left = gameData.playerX + 'px';
    player.style.top = gameData.playerY + 'px';

    // Update Obstacles
    const container = document.getElementById('obstacles-container');
    const existingObstacles = container.querySelectorAll('.obstacle');

    // Remove old obstacles if needed
    if (existingObstacles.length !== gameData.obstacles.length) {
        container.innerHTML = '';
    }

    // Update or create obstacles
    gameData.obstacles.forEach((obstacle, index) => {
        let obstacleEl = existingObstacles[index];

        if (!obstacleEl) {
            obstacleEl = document.createElement('div');
            obstacleEl.className = 'obstacle';
            container.appendChild(obstacleEl);
        }

        obstacleEl.style.left = obstacle.x + 'px';
        obstacleEl.style.top = obstacle.y + 'px';
    });

    // Check if game is over
    if (gameData.gameOver && gameRunning) {
        endGame();
    }
}

// End Game
function endGame() {
    gameRunning = false;
    document.getElementById('finalScore').textContent = `Final Score: ${gameData.score}`;
    document.getElementById('finalLevel').textContent = `Level Reached: ${gameData.level}`;
    document.getElementById('status').textContent = 'GAME OVER';
    document.getElementById('status').style.color = '#FF6B6B';
    document.getElementById('gameOverScreen').classList.remove('hidden');
}

// Game Loop
async function gameLoop() {
    if (gameRunning && !gameData?.gameOver) {
        // Handle continuous movement
        handleContinuousMovement();
        
        // Update game state
        await updateGame();
        await fetchGameState();
        renderGame();
    }
    requestAnimationFrame(gameLoop);
}

// Initialize Game on Page Load
window.addEventListener('load', async () => {
    console.log('Game initializing...');
    
    // Wait a moment for server to be ready
    await new Promise(resolve => setTimeout(resolve, 500));
    
    const initialState = await fetchGameState();
    
    if (!initialState) {
        console.error('Failed to initialize game. Make sure the Java server is running on http://localhost:8000');
        document.body.innerHTML = '<div style="text-align: center; padding: 50px; font-size: 18px; color: red;"><h1>⚠️ Server Connection Error</h1><p>Make sure to start the Java server first!</p><p>Run: javac src/*.java && java -cp src GameServer</p></div>';
        return;
    }
    
    gameData = initialState;
    renderGame();
    gameLoop();
});

// Pause on visibility change
document.addEventListener('visibilitychange', () => {
    if (document.hidden) {
        gameRunning = false;
    } else {
        gameRunning = true;
    }
});
