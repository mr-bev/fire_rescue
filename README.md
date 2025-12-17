# Fire Rescue Game - Pygame Zero Exemplar

## Overview
This is a complete Game & Watch style rescue game built with Pygame Zero. It demonstrates all the assessment requirements for the mini project.

## Assessment Requirements Met
✅ Menu screen (press SPACE to start)  
✅ Game screen (main gameplay)  
✅ Game over screen (shows final score, restart option)  
✅ Score tracking system  
✅ Clear objective (catch falling people before they hit the ground)  

## Installation

### 1. Install Python
Make sure Python 3.7 or higher is installed on your computer.

### 2. Install Pygame Zero
Open a terminal/command prompt and run:
```bash
pip install pgzero
```

Or on some systems:
```bash
pip3 install pgzero
```

### 3. Install PIL (for image creation)
```bash
pip install pillow
```

## File Structure
```
fire_rescue_game/
├── fire_rescue_game.py    (main game code)
├── images/
│   ├── trampoline.png     (player sprite)
│   └── person.png         (falling person sprite)
├── sounds/
│   ├── catch.wav          (success sound)
│   ├── miss.wav           (failure sound)
│   ├── game_over.wav      (game over sound)
│   └── start.wav          (game start sound)
├── generate_sounds.py     (script to create sound files)
└── README.md              (this file)
```

## How to Run

### Method 1: Using pgzrun (recommended)
```bash
pgzrun fire_rescue_game.py
```

### Method 2: Using Python directly
```bash
python -m pgzero fire_rescue_game.py
```

Or:
```bash
python3 -m pgzero fire_rescue_game.py
```

## How to Play
- **LEFT/RIGHT arrow keys**: Move the trampoline
- **SPACE**: Start game / Restart after game over
- **Objective**: Catch people jumping from the burning building
- **Scoring**: 10 points per person caught
- **Lives**: You have 3 lives - miss 3 people and it's game over!
- **Difficulty**: The game speeds up as your score increases

## Code Structure (For Students)

### Key Components:
1. **Game States**: MENU, PLAYING, GAME_OVER
2. **Main Functions**:
   - `update()` - called every frame, handles game logic
   - `draw()` - called every frame, draws everything on screen
   - `start_game()` - initializes/resets the game
   - `spawn_person()` - creates new falling people

3. **Classes**:
   - `FallingPerson` - represents each person falling from the building

### Game Flow:
```
MENU → (press SPACE) → PLAYING → (lose 3 lives) → GAME_OVER → (press SPACE) → PLAYING
```

## Customization Ideas for Students
- Change the spawn delay to make it harder/easier
- Change the point value for catching people
- Add sound effects (already included!)
- Change the colors/theme
- Add power-ups
- Add different types of people (faster/slower)
- Add a high score system
- Create your own sound effects using the generate_sounds.py script

## Portfolio Documentation
This game can be used as a reference for your portfolio requirements:
- **Problem definition**: Create an engaging rescue game suitable for all ages
- **Game mechanics**: Timing, collision detection, scoring, progressive difficulty
- **Testing areas**: Boundary testing (edges of screen), collision accuracy, game state transitions
