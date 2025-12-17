"""
FIRE RESCUE GAME - Pygame Zero Exemplar
========================================
A Game & Watch style rescue game where players catch people jumping from a burning building.

Assessment Requirements Met:
- Menu screen (press SPACE to start)
- Game screen (main gameplay)
- Game over screen (shows final score, restart option)
- Score tracking system
- Clear objective (catch falling people)
- Sound effects (catch, miss, game over, start)

Controls:
- LEFT/RIGHT arrow keys to move the rescue trampoline
- SPACE to start game / restart after game over

Game Rules:
- People jump from random windows in the burning building
- Move the trampoline to catch them
- Each successful catch = 10 points
- Miss 3 people and it's game over
- Game speeds up as score increases

Sound Effects:
- Start: Cheerful ascending notes when game begins
- Catch: Pleasant rising tone when you catch someone
- Miss: Descending tone when you miss someone
- Game Over: Sad arpeggio when you lose all lives
"""

import random
from pgzero.builtins import Actor, sounds, keyboard, Rect

import pgzero.screen
screen : pgzero.screen.Screen

# Game constants
WIDTH = 600
HEIGHT = 500
TITLE = "Fire Rescue"

# Game states
MENU = 0
PLAYING = 1
GAME_OVER = 2

# Initialize game state
game_state = MENU
score = 0
lives = 3
spawn_timer = 0
spawn_delay = 60  # frames between spawns (60 = 1 second at 60fps)

# Trampoline (player controlled)
trampoline = Actor('trampoline')
trampoline.x = WIDTH // 2
trampoline.y = HEIGHT - 50
trampoline_speed = 5

# List to hold falling people
falling_people = []

# Building windows positions (where people can jump from)
WINDOW_POSITIONS = [100, 200, 300, 400, 500]
JUMP_HEIGHT = 100


class FallingPerson:
    """Represents a person falling from the building"""
    def __init__(self, x_position):
        self.actor = Actor('person')
        self.actor.x = x_position
        self.actor.y = JUMP_HEIGHT
        self.speed = 3
        self.caught = False
        self.missed = False
    
    def update(self):
        """Move the person downward"""
        self.actor.y += self.speed
        
        # Check if person has fallen past the trampoline
        if self.actor.y > HEIGHT:
            self.missed = True
    
    def check_collision(self, trampoline_actor):
        """Check if person collides with trampoline"""
        if self.actor.colliderect(trampoline_actor):
            self.caught = True
            return True
        return False


def start_game():
    """Initialize/reset game to starting state"""
    global game_state, score, lives, spawn_timer, falling_people, spawn_delay
    game_state = PLAYING
    score = 0
    lives = 3
    spawn_timer = 0
    spawn_delay = 60
    falling_people = []
    
    # Play start sound
    try:
        sounds.start.play()
    except:
        pass  # Sound file might not exist


def spawn_person():
    """Create a new falling person at random window"""
    x_pos = random.choice(WINDOW_POSITIONS)
    new_person = FallingPerson(x_pos)
    falling_people.append(new_person)


def update():
    """Main game update loop - called every frame"""
    global game_state, score, lives, spawn_timer, spawn_delay
    
    if game_state == MENU:
        # Menu state - waiting for player to start
        if keyboard.space:
            start_game()
    
    elif game_state == PLAYING:
        # Handle player movement
        if keyboard.left and trampoline.x > 50:
            trampoline.x -= trampoline_speed
        if keyboard.right and trampoline.x < WIDTH - 50:
            trampoline.x += trampoline_speed
        
        # Spawn new people on timer
        spawn_timer += 1
        if spawn_timer >= spawn_delay:
            spawn_person()
            spawn_timer = 0
        
        # Update all falling people
        people_to_remove = []
        for person in falling_people:
            person.update()
            
            # Check if caught
            if person.check_collision(trampoline):
                score += 10
                people_to_remove.append(person)
                # Play catch sound
                try:
                    sounds.catch.play()
                except:
                    pass
                # Speed up game as score increases
                if score % 50 == 0 and spawn_delay > 20:
                    spawn_delay -= 5
            
            # Check if missed
            elif person.missed:
                lives -= 1
                people_to_remove.append(person)
                # Play miss sound
                try:
                    sounds.miss.play()
                except:
                    pass
                
                # Check for game over
                if lives <= 0:
                    game_state = GAME_OVER
                    # Play game over sound
                    try:
                        sounds.game_over.play()
                    except:
                        pass
        
        # Remove caught or missed people
        for person in people_to_remove:
            falling_people.remove(person)
    
    elif game_state == GAME_OVER:
        # Game over state - waiting for restart
        if keyboard.space:
            start_game()


def draw():
    """Draw everything on screen"""
    screen.clear()
    
    if game_state == MENU:
        draw_menu()
    elif game_state == PLAYING:
        draw_game()
    elif game_state == GAME_OVER:
        draw_game_over()


def draw_menu():
    """Draw the menu screen"""
    screen.fill((20, 20, 40))
    
    # Title
    screen.draw.text("FIRE RESCUE", 
                     center=(WIDTH//2, 150), 
                     fontsize=60, 
                     color="orange")
    
    # Instructions
    screen.draw.text("Catch people jumping from the burning building!", 
                     center=(WIDTH//2, 250), 
                     fontsize=24, 
                     color="white")
    
    screen.draw.text("Use LEFT and RIGHT arrows to move", 
                     center=(WIDTH//2, 290), 
                     fontsize=20, 
                     color="lightblue")
    
    screen.draw.text("Don't miss more than 3 people!", 
                     center=(WIDTH//2, 330), 
                     fontsize=20, 
                     color="lightblue")
    
    # Start prompt
    screen.draw.text("Press SPACE to start", 
                     center=(WIDTH//2, 400), 
                     fontsize=30, 
                     color="yellow")


def draw_game():
    """Draw the main game screen"""
    # Sky background
    screen.fill((135, 206, 235))
    
    # Draw building (simple representation)
    screen.draw.filled_rect(Rect(50, 50, 500, 200), (139, 69, 19))
    
    # Draw windows
    for x_pos in WINDOW_POSITIONS:
        screen.draw.filled_rect(Rect(x_pos - 15, 80, 30, 40), (255, 200, 0))
    
    # Draw flames at top of building
    for i in range(5):
        x = 100 + i * 100
        screen.draw.filled_circle((x, 50), 20, (255, 100, 0))
    
    # Draw ground
    screen.draw.filled_rect(Rect(0, HEIGHT - 80, WIDTH, 80), (34, 139, 34))
    
    # Draw trampoline
    trampoline.draw()
    
    # Draw all falling people
    for person in falling_people:
        person.actor.draw()
    
    # Draw score and lives (HUD)
    screen.draw.text(f"Score: {score}", 
                     topleft=(10, 10), 
                     fontsize=30, 
                     color="white",
                     owidth=1,
                     ocolor="black")
    
    screen.draw.text(f"Lives: {lives}", 
                     topleft=(10, 45), 
                     fontsize=30, 
                     color="red",
                     owidth=1,
                     ocolor="black")


def draw_game_over():
    """Draw the game over screen"""
    screen.fill((40, 20, 20))
    
    # Game over message
    screen.draw.text("GAME OVER", 
                     center=(WIDTH//2, 150), 
                     fontsize=60, 
                     color="red")
    
    # Final score
    screen.draw.text(f"Final Score: {score}", 
                     center=(WIDTH//2, 250), 
                     fontsize=40, 
                     color="white")
    
    # Performance message
    if score >= 100:
        message = "Excellent work, hero!"
        color = "gold"
    elif score >= 50:
        message = "Good effort!"
        color = "lightblue"
    else:
        message = "Keep practicing!"
        color = "white"
    
    screen.draw.text(message, 
                     center=(WIDTH//2, 310), 
                     fontsize=30, 
                     color=color)
    
    # Restart prompt
    screen.draw.text("Press SPACE to play again", 
                     center=(WIDTH//2, 400), 
                     fontsize=25, 
                     color="yellow")
