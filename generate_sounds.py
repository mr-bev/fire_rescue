"""
Sound Effect Generator for Fire Rescue Game
============================================

This script generates simple sound effects using sine waves.
Requires: numpy and scipy

Usage: python generate_sounds.py

This will create a 'sounds/' folder with 4 .wav files:
- catch.wav (positive feedback)
- miss.wav (negative feedback)  
- start.wav (game start)
- game_over.wav (game over)
"""

import numpy as np
from scipy.io import wavfile
import os

def generate_catch_sound():
    """Generate a pleasant 'catch' sound - rising pitch"""
    sample_rate = 22050
    duration = 0.2  # seconds
    
    # Generate rising tone (A4 to A5)
    t = np.linspace(0, duration, int(sample_rate * duration))
    frequency_start = 440  # A4
    frequency_end = 880    # A5
    frequency = np.linspace(frequency_start, frequency_end, len(t))
    
    # Generate sine wave
    wave = np.sin(2 * np.pi * frequency * t)
    
    # Apply envelope (fade out)
    envelope = np.linspace(1, 0, len(t))
    wave = wave * envelope
    
    # Convert to 16-bit PCM
    wave = np.int16(wave * 32767)
    
    wavfile.write('sounds/catch.wav', sample_rate, wave)
    print("✓ Created catch.wav (rising tone - success sound)")

def generate_miss_sound():
    """Generate a 'miss' sound - descending pitch"""
    sample_rate = 22050
    duration = 0.3  # seconds
    
    # Generate descending tone (A4 to A3)
    t = np.linspace(0, duration, int(sample_rate * duration))
    frequency_start = 440  # A4
    frequency_end = 220    # A3
    frequency = np.linspace(frequency_start, frequency_end, len(t))
    
    # Generate sine wave
    wave = np.sin(2 * np.pi * frequency * t)
    
    # Apply envelope
    envelope = np.linspace(1, 0.3, len(t))
    wave = wave * envelope
    
    # Convert to 16-bit PCM
    wave = np.int16(wave * 32767)
    
    wavfile.write('sounds/miss.wav', sample_rate, wave)
    print("✓ Created miss.wav (descending tone - failure sound)")

def generate_game_over_sound():
    """Generate a 'game over' sound - sad descending arpeggio"""
    sample_rate = 22050
    duration = 0.8
    
    # Three descending notes (C, A, F)
    frequencies = [523, 440, 349]  
    wave = np.array([])
    
    for freq in frequencies:
        t = np.linspace(0, duration/3, int(sample_rate * duration/3))
        note = np.sin(2 * np.pi * freq * t)
        # Exponential decay for each note
        envelope = np.exp(-3 * t)
        note = note * envelope
        wave = np.concatenate([wave, note])
    
    # Convert to 16-bit PCM (reduce volume to 50%)
    wave = np.int16(wave * 32767 * 0.5)
    
    wavfile.write('sounds/game_over.wav', sample_rate, wave)
    print("✓ Created game_over.wav (sad arpeggio - game over)")

def generate_start_sound():
    """Generate a 'start game' sound - cheerful ascending notes"""
    sample_rate = 22050
    duration = 0.4
    
    # Two ascending notes (A4, D5)
    frequencies = [440, 587]  
    wave = np.array([])
    
    for freq in frequencies:
        t = np.linspace(0, duration/2, int(sample_rate * duration/2))
        note = np.sin(2 * np.pi * freq * t)
        # Crescendo effect
        envelope = np.linspace(0.5, 1, len(t))
        note = note * envelope
        wave = np.concatenate([wave, note])
    
    # Convert to 16-bit PCM (reduce volume to 50%)
    wave = np.int16(wave * 32767 * 0.5)
    
    wavfile.write('sounds/start.wav', sample_rate, wave)
    print("✓ Created start.wav (ascending notes - game start)")

def main():
    """Generate all sound effects"""
    print("Fire Rescue Sound Effect Generator")
    print("=" * 40)
    
    # Create sounds directory if it doesn't exist
    if not os.path.exists('sounds'):
        os.makedirs('sounds')
        print("Created 'sounds' directory\n")
    
    # Generate all sounds
    try:
        generate_catch_sound()
        generate_miss_sound()
        generate_game_over_sound()
        generate_start_sound()
        
        print("\n" + "=" * 40)
        print("All sound files created successfully!")
        print("Location: sounds/")
        print("\nFiles created:")
        print("  - catch.wav")
        print("  - miss.wav")
        print("  - game_over.wav")
        print("  - start.wav")
        
    except Exception as e:
        print(f"\nError generating sounds: {e}")
        print("Make sure numpy and scipy are installed:")
        print("  pip install numpy scipy")

if __name__ == "__main__":
    main()
