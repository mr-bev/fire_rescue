# TEACHER'S GUIDE - Fire Rescue Game Exemplar

## Overview
This exemplar demonstrates a complete mini-project submission that meets all assessment requirements. It's designed to show students what "good" looks like without being so polished that it's intimidating.

## What's Included

### 1. Working Game (`fire_rescue_game.py`)
- Fully functional Pygame Zero game
- ~280 lines of well-commented code
- Demonstrates all required features
- Simple enough for beginners to understand

### 2. Complete Portfolio (`PORTFOLIO_EXEMPLAR.md`)
- All four development stages documented
- Examples of problem definition, research, planning, testing
- Shows appropriate level of detail for assessment
- Includes self-reflection

### 3. Image Assets (`images/` folder)
- Simple sprites created with code (students can see how)
- trampoline.png
- person.png

### 4. Documentation (`README.md`)
- Installation instructions
- How to run the game
- Customization ideas

---

## How to Use This Exemplar

### Week 1: Introduction

**Lesson 1: Show the Exemplar**
- Play the game for students (live demonstration)
- DON'T show the code yet
- Discuss: "What do you notice? What makes this a complete game?"
- Show the portfolio document - walk through the four stages
- Emphasize: "This is achievable in 5 weeks"

**Key Message**: "You're not trying to make the next Fortnite. You're making a simple, complete game that works."

### Week 2-3: During Development

**Use as Reference**:
- When students ask "How do I make a menu?" → Show them the menu code in the exemplar
- When they're stuck on collision → Show the collision function
- When they're confused about game states → Diagram the MENU/PLAYING/GAME_OVER flow

**Don't**: Give them the exemplar code to copy. They should reference it, understand it, then write their own.

### Week 5: Portfolio Completion

**Use as Template**:
- Show them the portfolio structure
- Point out: "See how they documented their bugs? That's what I'm looking for."
- Emphasize the self-reflection section

---

## Teaching Points by Code Section

### Game States (Lines 20-23)
```python
MENU = 0
PLAYING = 1
GAME_OVER = 2
```

**Teaching Point**: "Games need to track what 'mode' they're in. Are we showing a menu? Playing? Game over? This is called state management."

**Common Student Mistake**: Trying to do everything in one mode, getting confused.

### The FallingPerson Class (Lines 38-63)
**Teaching Point**: "When you have multiple things that are similar (like multiple falling people), use a class. It's like a blueprint."

**Explain**:
- `__init__` = setup when created
- `update()` = what happens every frame
- `check_collision()` = specific behavior

**Common Student Mistake**: Trying to manage each person with separate variables (person1_x, person2_x, etc.)

### The update() Function (Lines 77-129)
**Teaching Point**: "This is called EVERY FRAME (60 times per second). It's where all your game logic lives."

**Key Pattern**:
```
IF game is in MENU state:
    Do menu stuff
ELSE IF game is PLAYING:
    Do game stuff
ELSE IF game is GAME_OVER:
    Do game over stuff
```

**Common Student Mistake**: Putting all logic directly in update() without checking game_state first.

### Collision Detection (Lines 105-111)
**Teaching Point**: "Pygame Zero gives us `colliderect()` for free. It checks if two rectangles overlap."

**Show students**:
```python
if person.actor.colliderect(trampoline):
    # They touched!
```

**Common Student Mistake**: Trying to write their own collision detection with complicated math.

### Progressive Difficulty (Lines 109-111)
```python
if score % 50 == 0 and spawn_delay > 20:
    spawn_delay -= 5
```

**Teaching Point**: "The `%` operator (modulo) checks if a number divides evenly. So `score % 50 == 0` means 'every 50 points'."

**Why minimum check?**: "We don't want it to get TOO fast, so we stop at 20."

---

## Assessment Rubric Alignment

### This exemplar demonstrates:

**Menu Screen** (✓)
- Clear title
- Instructions
- Start prompt
Lines 150-169

**Game Screen** (✓)
- Visual game environment
- Player control
- Dynamic objects (falling people)
- HUD (score, lives)
Lines 172-213

**Game Over Screen** (✓)
- Final score display
- Performance message
- Restart option
Lines 216-242

**Score Tracking** (✓)
- Increments correctly (line 107)
- Displayed during play (line 204)
- Shown at game over (line 228)

**Clear Objective** (✓)
- Explicitly stated in menu
- Visually obvious during play
- Success/failure conditions clear

---

## Common Questions from Students

### "Can I use this code?"
**Answer**: "You can READ it and LEARN from it, but your game needs to be YOUR work. You're making a different game - maybe Frogger or Lunar Lander. This shows you the patterns."

### "Why is it so simple? Real games are more complex."
**Answer**: "Professional game studios have teams of 100+ people and years of time. You have 5 weeks and you're learning. This shows that 'simple and complete' beats 'complex and broken'."

### "Do I need to make my portfolio this detailed?"
**Answer**: "This is a GOOD example, not a MAXIMUM example. Your portfolio should be thorough but doesn't need to be longer than this."

### "What if I can't get my game working?"
**Answer**: "That's what testing and evaluation is for. Document what you TRIED, what went wrong, and what you learned. A well-documented struggle can still score well."

---

## Differentiation Strategies

### For Struggling Students:
- Point them to the simpler parts of the code (menu screen is simplest)
- Suggest they start with the Fire game template (if you provide templates)
- Focus more on portfolio completion - they can still score well on documentation
- Reduce complexity: "Your game can have just ONE spawn position"

### For Advanced Students:
- "Can you add sound effects?" (new skill)
- "Can you add a high score that persists?" (file I/O)
- "Can you add power-ups?" (more complex game logic)
- "Can you add levels?" (state management)
- Point them to Pygame (not Pygame Zero) for next year

### For Students Using AI:
- "Use this exemplar to check if the AI code makes sense"
- "If AI gives you something more complex than this, it's probably over-complicated"
- "Can you explain line 107? If not, you need to break it down more."

---

## Assessment Tips

### What to Look For:

**Understanding** (not just completion):
- Can they explain their collision detection?
- Do they know WHY their spawn system works?
- Can they modify their code (e.g., change score from 10 to 15)?

**Process** (not just product):
- Is their portfolio showing genuine development stages?
- Are their "bugs found" realistic or made up?
- Does their self-reflection show actual learning?

**Completeness**:
- All three screens present?
- Score system working?
- Portfolio has all four stages?

### Red Flags:
- Code way more complex than exemplar (probably copied from internet/AI without understanding)
- Portfolio written after the fact (all dates the same, too perfect)
- Can't explain basic parts of their own code

### Green Flags:
- Code has their personal touches (unique theme, creative additions)
- Portfolio shows actual iteration (bug fixes, changes)
- Can explain their code even if it's not perfect
- Shows genuine reflection in self-evaluation

---

## Installation Instructions for School Computers

### Method 1: Individual Install (if students have permissions)
```bash
pip install pgzero --user
```

### Method 2: Virtual Environment (recommended for school labs)
```bash
python -m venv game_env
source game_env/bin/activate  # On Windows: game_env\Scripts\activate
pip install pgzero
```

### Method 3: Portable Installation (if no permissions)
- Download portable Python
- Install Pygame Zero to that Python
- Students can run from USB drive

### Testing Installation:
```bash
python -c "import pgzero; print('Success!')"
```

---

## Troubleshooting Common Issues

### "ModuleNotFoundError: No module named 'pgzero'"
- Pygame Zero not installed
- Solution: `pip install pgzero`

### "No module named 'pygame'"
- Dependency issue
- Solution: `pip install pygame`

### "Images not loading"
- Wrong directory structure
- Solution: Ensure `images/` folder is in same directory as .py file

### "Game window doesn't open"
- Display issue
- Solution: Check if `WIDTH` and `HEIGHT` are set
- Try running with `pgzrun fire_rescue_game.py` instead of `python fire_rescue_game.py`

### "Controls don't work"
- Focus issue - click on game window
- Or keyboard module issue - reinstall Pygame Zero

---

## Time Allocation Suggestions

### Week 1 (Foundations)
- Lesson 1: Show exemplar, discuss assessment (30 min show, 15 min discuss)
- Lesson 2: Python basics (variables, conditionals)
- Lesson 3: Python basics (loops, lists)

### Week 2 (Planning)
- Lesson 1: Pygame Zero intro + draw simple shapes
- Lesson 2: Movement and keyboard input
- Lesson 3: Students complete their flowchart/pseudocode (with your feedback)

### Week 3-4 (Implementation)
- Mini-lessons on specific topics (10-15 min)
- Work time with individual help
- Reference exemplar as needed

### Week 5 (Testing & Portfolio)
- Lesson 1: Testing protocols, document bugs
- Lesson 2: Peer feedback, portfolio compilation
- Lesson 3: Final touches, submission

---

## Extension Resources

If students finish early or want to learn more:

### Pygame Zero Resources:
- Official docs: https://pygame-zero.readthedocs.io/
- Tutorial: https://pygame-zero.readthedocs.io/en/stable/introduction.html
- Example games: https://github.com/lordmauve/pgzero

### Next Steps:
- Transition to Pygame (more professional)
- Learn about sprite sheets
- Add sound effects (Pygame Zero supports sound easily)
- Explore game design theory

---

## Final Notes

**Remember**: This exemplar is meant to be:
- ✓ Achievable (students can realistically make this)
- ✓ Clear (they can understand all the code)
- ✓ Complete (meets all assessment requirements)
- ✗ NOT intimidating (it's simple by design)
- ✗ NOT the only way (students should make different games)

**Your role**: 
- Guide students to understand patterns, not copy code
- Help them see that "simple and working" is better than "complex and broken"
- Encourage their creativity within the constraints

**Success looks like**:
- Students submit working games (even if simple)
- They can explain how their code works
- They've learned whether programming is for them
- Their portfolios show genuine learning process

Good luck! This is a challenging but rewarding project for students.
