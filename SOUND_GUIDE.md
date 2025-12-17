# Sound Effects Guide

## Overview
This game includes 4 simple sound effects to enhance the gameplay experience. All sounds were generated programmatically using Python.

## Sound Files

### 1. catch.wav
**When it plays**: When you successfully catch a falling person  
**Description**: A pleasant rising tone (A4 to A5)  
**Duration**: 0.2 seconds  
**Effect**: Positive feedback for good gameplay

### 2. miss.wav
**When it plays**: When a person falls past the trampoline  
**Description**: A descending tone (A4 to A3)  
**Duration**: 0.3 seconds  
**Effect**: Negative feedback for missed catch

### 3. start.wav
**When it plays**: When you press SPACE to start the game  
**Description**: Two ascending notes (A to D)  
**Duration**: 0.4 seconds  
**Effect**: Cheerful game start signal

### 4. game_over.wav
**When it plays**: When you lose all 3 lives  
**Description**: Three descending notes (C, A, F)  
**Duration**: 0.8 seconds  
**Effect**: "Sad" game over signal

## How Pygame Zero Handles Sound

Pygame Zero makes sound effects very easy:

```python
# Play a sound
sounds.catch.play()

# Pygame Zero automatically:
# 1. Looks in the 'sounds/' folder
# 2. Finds 'catch.wav'
# 3. Plays it
```

**Important**: The sound file name (without .wav) becomes the attribute name.
- `sounds/catch.wav` → `sounds.catch.play()`
- `sounds/miss.wav` → `sounds.miss.play()`

## Adding Sound to Your Game

### Step 1: Create a sounds folder
```
your_game/
├── your_game.py
├── images/
│   └── ...
└── sounds/          ← Create this folder
    ├── catch.wav
    └── miss.wav
```

### Step 2: Add sound to your code
```python
# When something good happens:
sounds.catch.play()

# When something bad happens:
sounds.miss.play()
```

### Step 3: Handle missing sounds gracefully
```python
# Use try-except in case sound files are missing
try:
    sounds.catch.play()
except:
    pass  # Game still works without sound
```

## Where to Get Sound Effects

### Option 1: Generate them (like this example)
- Use the Python script in `generate_sounds.py`
- Requires numpy and scipy libraries
- Good for learning how sound works

### Option 2: Free sound libraries
- **Freesound.org** - Creative Commons sounds
- **OpenGameArt.org** - Free game assets
- **Zapsplat.com** - Free sound effects (with attribution)

### Option 3: Record them yourself
- Use Audacity (free software)
- Record simple sounds
- Export as .wav files

## Sound Format Requirements

Pygame Zero works best with:
- **Format**: WAV files (.wav)
- **Sample Rate**: 22050 Hz or 44100 Hz
- **Bit Depth**: 16-bit
- **Channels**: Mono or Stereo

## Tips for Students

1. **Keep sounds short**: Game sound effects should be under 1 second (usually 0.1-0.5 seconds)

2. **Match the action**: 
   - Good events = rising pitch, major keys
   - Bad events = falling pitch, minor keys

3. **Test volume**: Make sure sounds aren't too loud or too quiet

4. **Error handling**: Always use try-except when playing sounds so your game doesn't crash if a sound file is missing

5. **Attribution**: If you use sounds from the internet, credit the creator in your portfolio!

## Example Code Patterns

### Play sound on collision:
```python
if player.colliderect(coin):
    score += 10
    sounds.coin.play()  # Positive sound
    coins.remove(coin)
```

### Play sound on game over:
```python
if lives <= 0:
    game_state = GAME_OVER
    sounds.game_over.play()  # Sad sound
```

### Play background music (optional):
```python
# In your game setup
music.play('background_music')  # Loops automatically

# Stop music
music.stop()
```

## Portfolio Notes

When documenting sound in your portfolio:

**In Research Section**: 
"I researched [Game X] and noted how sound effects provided feedback for player actions."

**In Implementation Section**:
"Added 4 sound effects: catch, miss, start, and game_over. Used try-except blocks to ensure game runs even if sound files are missing."

**In Testing Section**:
"Tested sound effects on different computers. Verified game functions correctly even when sound files are absent."

## Common Issues and Solutions

### "No sound plays"
- Check that sounds folder exists in same directory as .py file
- Check that sound files are .wav format
- Check computer volume isn't muted
- Try: `sounds.catch.play()` in interactive Python to test

### "AttributeError: 'Sounds' object has no attribute 'catch'"
- Sound file doesn't exist or has wrong name
- Check exact spelling (case-sensitive on some systems)
- Verify file is in sounds/ folder

### "Game crashes when playing sound"
- Add try-except blocks around sound.play() calls
- Check that pygame is properly installed

### "Sound is too quiet/loud"
```python
# Adjust sound volume (0.0 to 1.0)
sounds.catch.play()
sounds.catch.set_volume(0.5)  # 50% volume
```

## Advanced: How the Sounds Were Generated

The sounds in this game were created using sine waves at different frequencies:

```python
import numpy as np
from scipy.io import wavfile

# Generate a simple beep at 440 Hz (A note)
sample_rate = 22050
duration = 0.2
t = np.linspace(0, duration, int(sample_rate * duration))
frequency = 440
wave = np.sin(2 * np.pi * frequency * t)
wave = np.int16(wave * 32767)
wavfile.write('beep.wav', sample_rate, wave)
```

**Note**: You don't need to understand this code to use sound effects! This is just for students who are curious about how digital sound works.

## Summary

Sound effects are a simple but powerful way to:
- Give players feedback
- Make your game more engaging
- Show attention to polish
- Demonstrate understanding of game design principles

They're optional but highly recommended for your game project!
