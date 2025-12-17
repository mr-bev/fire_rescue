# FIRE RESCUE GAME - PORTFOLIO EXEMPLAR
**Student Name**: [Example Student]  
**Subject**: Digital Technologies  
**Assessment**: Mini Project (15%)

---

## STAGE 1: IDENTIFYING AND DEFINING

### Need for the Game
There is a need for an engaging, simple arcade-style game that:
- Can be played in short sessions (3-5 minutes)
- Is suitable for all ages
- Teaches quick decision-making and hand-eye coordination
- Provides a sense of achievement through progressive difficulty

### Problem Statement
Create a rescue-themed arcade game where players must catch falling people using a trampoline, featuring:
- Simple left/right controls
- Clear visual feedback
- Progressive difficulty
- Score tracking to encourage replay

### Requirements

#### Functional Requirements:
- Menu screen with game instructions
- Player-controlled trampoline that moves left and right
- People that spawn randomly and fall from building windows
- Collision detection between people and trampoline
- Score system (points awarded for successful catches)
- Lives system (game ends after 3 misses)
- Game over screen showing final score and restart option
- Progressive difficulty (spawn rate increases as score increases)

#### Technical Requirements:
- Built using Python and Pygame Zero
- Three distinct screens (menu, game, game over)
- Keyboard controls (arrow keys for movement, space for start/restart)
- Frame-based animation at 60 FPS
- Clear visual representation of game elements

#### Success Criteria:
- Game runs without crashes
- Controls are responsive
- Collision detection is accurate
- Score and lives display correctly
- Game becomes progressively more challenging

---

## STAGE 2: RESEARCH AND PLANNING

### Research: Existing Arcade Games

#### Game 1: Fire (Game & Watch, 1980)
**Overview**: Original Nintendo Game & Watch game where players catch people jumping from a burning building.

**Key Elements Analysed**:
- **Spawn System**: People appear randomly from different windows
- **Movement**: Simple left/right positioning for the rescue device
- **Difficulty Progression**: Speed increases over time
- **Lives System**: Limited number of misses allowed
- **Visual Clarity**: Clear distinction between background and interactive elements

**Elements to Implement**:
- Random spawn positions from predefined locations
- Simple two-direction movement
- Progressive speed increase based on score
- Three-strike system for lives

#### Game 2: Kaboom! (Atari 2600, 1981)
**Overview**: Players catch bombs dropped by a criminal using buckets of water.

**Key Elements Analysed**:
- **Catching Mechanic**: Precise positioning required for catches
- **Visual Feedback**: Clear indication when objects are caught vs missed
- **Scoring**: Points awarded based on catches
- **Game Over Condition**: Specific number of misses ends game
- **Multiple Spawn Points**: Objects can fall from different positions

**Elements to Implement**:
- Precise collision detection
- Visual score display during gameplay
- Multiple window positions for variety
- Clear game over state with score display

### Game Design Decisions
Based on research, my game will include:
1. **5 spawn positions** (window locations) for variety
2. **Progressive difficulty** - spawn delay decreases every 50 points
3. **3 lives** - balanced between too easy and too frustrating
4. **10 points per catch** - clear, simple scoring
5. **Visual building representation** with windows showing spawn points

---

### Flowchart: Main Game Loop

```mermaid
flowchart TD
    Start([START]) --> Init[Set game_state to MENU]
    Init --> MenuLoop{MENU LOOP}
    
    MenuLoop --> DisplayMenu[Display menu screen]
    DisplayMenu --> WaitSpace1[Wait for SPACE key press]
    WaitSpace1 --> SpacePressed1{SPACE pressed?}
    SpacePressed1 -->|No| DisplayMenu
    SpacePressed1 -->|Yes| StartGame[Set game_state to PLAYING<br/>Reset score to 0<br/>Reset lives to 3<br/>Play start sound]
    
    StartGame --> GameLoop{GAME LOOP}
    
    GameLoop --> UpdatePlayer[Update player position<br/>LEFT/RIGHT arrow keys]
    UpdatePlayer --> IncrementTimer[Increment spawn_timer]
    IncrementTimer --> CheckTimer{spawn_timer ≥<br/>spawn_delay?}
    
    CheckTimer -->|Yes| SpawnPerson[Create new falling person<br/>Reset spawn_timer to 0]
    CheckTimer -->|No| UpdatePeople
    SpawnPerson --> UpdatePeople[For each falling person:<br/>Move person downward]
    
    UpdatePeople --> CheckCollision{Person collide<br/>with trampoline?}
    
    CheckCollision -->|Yes| AddScore[Add 10 to score<br/>Remove person<br/>Play catch sound]
    AddScore --> CheckScore{Score divisible<br/>by 50?}
    CheckScore -->|Yes| SpeedUp[Decrease spawn_delay<br/>if > 20]
    CheckScore -->|No| DrawScreen
    SpeedUp --> DrawScreen
    
    CheckCollision -->|No| CheckMissed{Person below<br/>screen?}
    CheckMissed -->|No| DrawScreen
    CheckMissed -->|Yes| LoseLives[Decrease lives by 1<br/>Remove person<br/>Play miss sound]
    LoseLives --> CheckGameOver{Lives ≤ 0?}
    
    CheckGameOver -->|Yes| SetGameOver[Set game_state to GAME_OVER<br/>Play game over sound]
    CheckGameOver -->|No| DrawScreen
    SetGameOver --> DrawScreen
    
    DrawScreen[Draw everything on screen]
    DrawScreen --> StillPlaying{game_state still<br/>PLAYING?}
    
    StillPlaying -->|Yes| GameLoop
    StillPlaying -->|No| GameOverLoop{GAME OVER LOOP}
    
    GameOverLoop --> DisplayGameOver[Display game over screen<br/>Display final score]
    DisplayGameOver --> WaitSpace2[Wait for SPACE key press]
    WaitSpace2 --> SpacePressed2{SPACE pressed?}
    SpacePressed2 -->|No| DisplayGameOver
    SpacePressed2 -->|Yes| MenuLoop
    
    style Start fill:#0173B2,stroke:#000,stroke-width:3px,color:#fff
    style MenuLoop fill:#DE8F05,stroke:#000,stroke-width:3px,color:#fff
    style GameLoop fill:#029E73,stroke:#000,stroke-width:3px,color:#fff
    style GameOverLoop fill:#CC78BC,stroke:#000,stroke-width:3px,color:#fff
    style SetGameOver fill:#CA5050,stroke:#000,stroke-width:3px,color:#fff
    style AddScore fill:#56B4E9,stroke:#000,stroke-width:3px,color:#000
```

**Note**: This flowchart shows the complete game logic from start to finish, including all three game states (Menu, Playing, Game Over) and the main game loop.


**Simplified State Diagram** (alternative view focusing on game states):

```mermaid
flowchart TD
    Start([START GAME]) --> Menu
    
    subgraph Menu [MENU STATE]
        M1[Show title and instructions]
        M2{Player presses<br/>SPACE?}
        M1 --> M2
        M2 -->|No| M1
    end
    
    M2 -->|Yes| InitGame[Initialize:<br/>score = 0<br/>lives = 3<br/>spawn_delay = 60]
    
    InitGame --> Playing
    
    subgraph Playing [PLAYING STATE]
        P1[Move trampoline<br/>with arrow keys]
        P2[Spawn falling people<br/>from random windows]
        P3[Update falling people positions]
        P4{Collision<br/>detected?}
        P5[score += 10<br/>Play catch sound]
        P6{Person<br/>missed?}
        P7[lives -= 1<br/>Play miss sound]
        P8{lives == 0?}
        
        P1 --> P2
        P2 --> P3
        P3 --> P4
        P4 -->|Yes| P5
        P4 -->|No| P6
        P5 --> P2
        P6 -->|No| P2
        P6 -->|Yes| P7
        P7 --> P8
        P8 -->|No| P2
    end
    
    P8 -->|Yes| GameOver
    
    subgraph GameOver [GAME OVER STATE]
        G1[Show final score<br/>Play game over sound]
        G2{Player presses<br/>SPACE?}
        G1 --> G2
        G2 -->|No| G1
    end
    
    G2 -->|Yes| Menu
    
    style Start fill:#0173B2,stroke:#000,stroke-width:3px,color:#fff
    style Menu fill:#DE8F05,stroke:#000,stroke-width:3px
    style Playing fill:#029E73,stroke:#000,stroke-width:3px
    style GameOver fill:#CC78BC,stroke:#000,stroke-width:3px
    style P5 fill:#56B4E9,stroke:#000,stroke-width:3px,color:#000
    style P7 fill:#CA5050,stroke:#000,stroke-width:3px,color:#fff
```

---

### Flowchart: Collision Detection Algorithm

```mermaid
flowchart TD
    Start([Collision Detection Algorithm]) --> GetPersonPos[Get person position:<br/>person_x, person_y<br/>person_width, person_height]
    
    GetPersonPos --> GetTrampPos[Get trampoline position:<br/>tramp_x, tramp_y<br/>tramp_width, tramp_height]
    
    GetTrampPos --> CalcBounds[Calculate boundaries:<br/>person_left = person_x - width/2<br/>person_right = person_x + width/2<br/>person_top = person_y - height/2<br/>person_bottom = person_y + height/2<br/><br/>Same for trampoline]
    
    CalcBounds --> Check1{person_right ><br/>tramp_left?}
    
    Check1 -->|No| NoCollision[Return FALSE<br/>No collision]
    Check1 -->|Yes| Check2{person_left <<br/>tramp_right?}
    
    Check2 -->|No| NoCollision
    Check2 -->|Yes| Check3{person_bottom ><br/>tramp_top?}
    
    Check3 -->|No| NoCollision
    Check3 -->|Yes| Check4{person_top <<br/>tramp_bottom?}
    
    Check4 -->|No| NoCollision
    Check4 -->|Yes| Collision[Return TRUE<br/>Collision detected!]
    
    Collision --> Action[Add score<br/>Remove person<br/>Play sound]
    NoCollision --> Continue[Continue checking<br/>other people]
    Action --> End([END])
    Continue --> End
    
    style Start fill:#0173B2,stroke:#000,stroke-width:3px,color:#fff
    style Collision fill:#DE8F05,stroke:#000,stroke-width:3px,color:#fff
    style NoCollision fill:#CC78BC,stroke:#000,stroke-width:3px,color:#fff
    style Action fill:#56B4E9,stroke:#000,stroke-width:3px,color:#000
    style End fill:#029E73,stroke:#000,stroke-width:3px,color:#fff
```

---

### Pseudocode: Collision Detection Function

```
FUNCTION check_collision(person, trampoline):
    // Get the positions and sizes of both objects
    person_left = person.x - (person.width / 2)
    person_right = person.x + (person.width / 2)
    person_top = person.y - (person.height / 2)
    person_bottom = person.y + (person.height / 2)
    
    trampoline_left = trampoline.x - (trampoline.width / 2)
    trampoline_right = trampoline.x + (trampoline.width / 2)
    trampoline_top = trampoline.y - (trampoline.height / 2)
    trampoline_bottom = trampoline.y + (trampoline.height / 2)
    
    // Check if rectangles overlap
    IF person_right > trampoline_left AND
       person_left < trampoline_right AND
       person_bottom > trampoline_top AND
       person_top < trampoline_bottom THEN
        RETURN True  // Collision detected
    ELSE
        RETURN False  // No collision
    END IF
END FUNCTION
```

---

### Pseudocode: Spawn System

```
// Global variables
spawn_timer = 0
spawn_delay = 60  // frames between spawns (1 second at 60 FPS)
window_positions = [100, 200, 300, 400, 500]
falling_people = []  // list to store active falling people

FUNCTION update_spawn_system():
    // Increment timer each frame
    spawn_timer = spawn_timer + 1
    
    // Check if it's time to spawn a new person
    IF spawn_timer >= spawn_delay THEN
        // Choose random window position
        random_index = RANDOM_INTEGER(0, 4)
        spawn_x = window_positions[random_index]
        
        // Create new falling person at that position
        new_person = CREATE FallingPerson(spawn_x, JUMP_HEIGHT)
        
        // Add to active list
        ADD new_person TO falling_people
        
        // Reset timer
        spawn_timer = 0
    END IF
END FUNCTION
```

---

## STAGE 3: IMPLEMENTING

### Development Process

The game was implemented in Python using Pygame Zero framework. Key implementation highlights:

#### Code Structure
- **Main game file**: `fire_rescue_game.py` (approximately 280 lines)
- **Asset folder**: `images/` containing trampoline.png and person.png
- **Sound folder**: `sounds/` containing catch.wav, miss.wav, game_over.wav, start.wav
- **State management**: Three game states (MENU, PLAYING, GAME_OVER)

#### Key Features Implemented

**1. Three Screens**
- Menu screen with title, instructions, and start prompt
- Game screen with building, falling people, trampoline, and HUD
- Game over screen with final score and restart option

**2. Score Tracking**
- Score increases by 10 points for each person caught
- Displayed in top-left corner during gameplay
- Final score shown on game over screen

**3. Player Controls**
- LEFT/RIGHT arrow keys for trampoline movement
- SPACE key to start game and restart after game over
- Movement bounded to screen edges

**4. Game Mechanics**
- Random person spawning from 5 window positions
- Gravity-based falling motion
- Collision detection using Pygame Zero's `colliderect()` method
- Lives system (3 lives, game over when depleted)
- Progressive difficulty (spawn delay decreases every 50 points)

**5. Sound Effects**
- Start sound: Plays when game begins
- Catch sound: Positive feedback when catching a person
- Miss sound: Negative feedback when missing a person
- Game over sound: Plays when all lives are lost
- All sounds wrapped in try-except to prevent crashes if sound files missing

#### Technical Implementation Details

**FallingPerson Class**:
```python
class FallingPerson:
    def __init__(self, x_position):
        self.actor = Actor('person')
        self.actor.x = x_position
        self.actor.y = JUMP_HEIGHT
        self.speed = 3
```
This class encapsulates all data and behaviour for falling people, making the code organised and easy to manage.

**Game State Management**:
Using integer constants (MENU=0, PLAYING=1, GAME_OVER=2) to track which screen is active, with conditional logic in `update()` and `draw()` functions.

**Sound Implementation**:
```python
try:
    sounds.catch.play()
except:
    pass  # Game still works if sound files missing
```
Used try-except blocks to ensure game functions correctly even if sound files are absent or if audio drivers are unavailable.

**Progressive Difficulty**:
```python
if score % 50 == 0 and spawn_delay > 20:
    spawn_delay -= 5
```
Every 50 points, the spawn delay decreases, making people fall more frequently.

### Challenges Encountered

1. **Initial Collision Detection Issue**: 
   - Problem: People were sometimes passing through the trampoline
   - Solution: Used Pygame Zero's built-in `colliderect()` method which is more reliable than manual rectangle checking

2. **Spawn Rate Too Fast**:
   - Problem: Game became too difficult too quickly
   - Solution: Adjusted initial spawn_delay to 60 frames and minimum to 20 frames

3. **Screen Boundary Management**:
   - Problem: Trampoline could move partially off-screen
   - Solution: Added boundary checks in movement code (trampoline.x > 50 and < WIDTH-50)

---

## STAGE 4: TESTING AND EVALUATING

### Error Testing and Correction

#### Test 1: Syntax Error in Update Function
**Date**: [Example date]

**Error Found**:
```
NameError: name 'spawn_delay' is not defined
```

**Screenshot**: [In actual portfolio, include screenshot of error message]

**Cause**: Forgot to declare `spawn_delay` as a global variable inside the `start_game()` function.

**Fix**: Added `global spawn_delay` to the function:
```python
def start_game():
    global game_state, score, lives, spawn_timer, falling_people, spawn_delay
```

**Result**: Error resolved, game runs correctly.

---

#### Test 2: Logic Error - Collision Detection
**Date**: [Example date]

**Error Found**: Sometimes people were caught even when they were slightly to the side of the trampoline.

**Screenshot**: [In actual portfolio, include screenshot showing the issue]

**Cause**: Collision detection was too generous due to large sprite hitboxes.

**Fix**: While Pygame Zero's `colliderect()` was working correctly, I realised the issue was visual - the trampoline sprite had transparent pixels. This was actually working as designed, so no code change needed, but I made a note for future sprite design.

**Result**: Understood that collision detection was accurate, but sprites could be refined for better visual feedback.

---

#### Test 3: Game Over Not Triggering
**Date**: [Example date]

**Error Found**: Game continued even after lives reached 0.

**Screenshot**: [In actual portfolio, include screenshot or description]

**Cause**: Game over check was inside the wrong part of the loop - it only checked when a person was missed, not continuously.

**Fix**: Moved the game over check to happen immediately when lives <= 0:
```python
elif person.missed:
    lives -= 1
    people_to_remove.append(person)
    
    # Check for game over
    if lives <= 0:
        game_state = GAME_OVER
```

**Result**: Game correctly ends when all lives are lost.

---

### Boundary Testing

#### Boundary Test 1: Screen Edges
**Test**: Move trampoline to far left and far right of screen

**Expected Result**: Trampoline should stop at screen edges and not disappear

**Actual Result**: 
- Left edge: Trampoline stops at x=50 ✓
- Right edge: Trampoline stops at x=550 ✓

**Pass/Fail**: PASS

---

#### Boundary Test 2: Score Threshold for Difficulty Increase
**Test**: Play game and check if difficulty increases at score = 50, 100, 150

**Expected Result**: Spawn delay should decrease by 5 frames at each milestone

**Actual Result**: 
- At score 50: spawn_delay changed from 60 to 55 ✓
- At score 100: spawn_delay changed from 55 to 50 ✓
- At score 150: spawn_delay changed from 50 to 45 ✓

**Pass/Fail**: PASS

---

#### Boundary Test 3: Lives System
**Test**: 
- Start with 3 lives
- Miss one person (should have 2 lives)
- Miss second person (should have 1 life)
- Miss third person (should trigger game over)

**Expected Result**: Lives should decrease correctly and game should end at 0

**Actual Result**: Lives decreased correctly, game over triggered at 0 lives ✓

**Pass/Fail**: PASS

---

#### Boundary Test 4: Minimum Spawn Delay
**Test**: Play game until score > 200 to see if spawn_delay continues to decrease

**Expected Result**: spawn_delay should stop decreasing at 20 frames (minimum value)

**Actual Result**: spawn_delay reached 20 and stopped decreasing ✓

**Code responsible**:
```python
if score % 50 == 0 and spawn_delay > 20:
    spawn_delay -= 5
```

**Pass/Fail**: PASS

---

### Peer Feedback

#### Feedback from Peer 1: [Student Name]
**Date**: [Example date]

**What did you like about the game?**
"I really enjoyed the simple controls and how the game got progressively harder. The graphics were clear and I could easily tell what was happening. The scoring system made me want to keep playing to beat my high score."

**What could be improved?**
"It would be cool if there were sound effects when you catch someone or when you miss. Also, maybe different types of people that are worth different points?"

**Was the objective clear?**
"Yes, very clear. The menu screen explained everything I needed to know."

**Rating (1-5)**: 4/5

---

#### Feedback from Peer 2: [Student Name]
**Date**: [Example date]

**What did you like about the game?**
"The game was addictive! I liked how it started easy but got challenging. The three lives gave me enough chances to improve without making it too easy."

**What could be improved?**
"Sometimes I found it hard to judge exactly where the trampoline needed to be. Maybe make the trampoline slightly wider or add a shadow under the falling people?"

**Was the objective clear?**
"Absolutely. The menu was helpful and the game was self-explanatory."

**Rating (1-5)**: 5/5

---

### Self-Evaluation

#### How well does your game meet the original requirements?

**Functional Requirements**: ✓ All Met
- ✓ Menu screen with instructions
- ✓ Player-controlled trampoline with left/right movement
- ✓ Random person spawning from building windows
- ✓ Collision detection working accurately
- ✓ Score system (10 points per catch)
- ✓ Lives system (3 lives, game over on depletion)
- ✓ Game over screen with final score and restart
- ✓ Progressive difficulty (spawn rate increases with score)

**Technical Requirements**: ✓ All Met
- ✓ Built using Python and Pygame Zero
- ✓ Three distinct screens implemented
- ✓ Keyboard controls functioning correctly
- ✓ Smooth animation at 60 FPS
- ✓ Clear visual representation of all game elements

**Success Criteria**: ✓ All Met
- ✓ Game runs without crashes
- ✓ Controls are responsive (tested with peers)
- ✓ Collision detection is accurate (boundary tested)
- ✓ Score and lives display correctly (verified in testing)
- ✓ Progressive difficulty working as intended

#### What worked well?

1. **Pygame Zero Framework**: The framework made it much easier to create a working game quickly. The Actor system and built-in collision detection saved a lot of time.

2. **Class Structure**: Using a `FallingPerson` class to manage each falling person made the code much more organised and easier to debug.

3. **Progressive Difficulty**: The increasing spawn rate creates good replay value and keeps players engaged.

4. **Three-Screen Structure**: Having clear separation between menu, game, and game over states made the code easier to manage and met the assessment requirements clearly.

#### What could be improved?

1. **Visual Polish**: The graphics are functional but basic. With more time, I could create better sprites and add animations.

2. **Audio**: The game has no sound effects or music. Adding audio would significantly improve player engagement.

3. **High Score System**: Currently, there's no way to track the best score across game sessions. Adding a high score would encourage more replay.

4. **Visual Feedback**: Adding particle effects or animations when catching people would make success more satisfying.

5. **Code Comments**: While I have some comments, more detailed documentation would help others understand the code better.

#### What did you learn about programming?

1. **State Management**: I learned how important it is to clearly track what "state" the program is in (menu, playing, game over) and handle each state differently.

2. **Object-Oriented Programming**: Using classes to represent game objects (like FallingPerson) made the code much cleaner than trying to manage everything with separate variables.

3. **Game Loops**: Understanding the update-draw loop pattern helped me see how games continuously refresh and respond to input.

4. **Collision Detection**: I learned that collision detection needs to be precise and that built-in functions often work better than trying to write your own.

5. **Debugging Process**: Testing revealed bugs I didn't expect. I learned to test boundary cases (edge of screen, zero lives, maximum score) systematically.

6. **Code Organization**: Breaking code into functions (draw_menu, draw_game, draw_game_over) made it much easier to find and fix problems.

#### Would you continue studying programming?

Yes, I found this project engaging and satisfying. The problem-solving aspect of debugging was challenging but rewarding. I enjoyed seeing my code come to life as a playable game. I would like to learn more about:
- Creating more complex games with multiple levels
- Adding sound and better graphics
- Learning more about object-oriented programming
- Exploring other types of programming beyond games

The most satisfying moment was when I finally got the collision detection working correctly and could actually play the game without bugs. Programming requires patience and careful thinking, but the ability to create something interactive from nothing is very rewarding.

---

## APPENDIX: Code Listing

[In actual portfolio, include complete, well-commented code here]

See separate file: `fire_rescue_game.py`

---

## REFERENCES

- Pygame Zero Documentation: https://pygame-zero.readthedocs.io/
- Fire (Game & Watch): https://en.wikipedia.org/wiki/Fire_(Game_%26_Watch)
- Kaboom! (Atari): https://en.wikipedia.org/wiki/Kaboom!_(video_game)
- Python Documentation: https://docs.python.org/3/

---

**End of Portfolio**