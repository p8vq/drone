# Introduction

This Python script is designed to control a Tello drone using the 'djitellopy' library. It features keyboard-based flight control, real-time video display, average color detection and color name recognition.

# Features

- Live video feed from the drone's camera
- Keyboard control for directional flight and altitude
- Flipping
- Average color detection from the camera frame
- Color recognition
- Clean and comprehensive shutdown with the 'L' key

# Controls

 ---------------------------------------------
| Key         | Action                        |
|-------------|-------------------------------|
| `W`         | Move forward                  |
| `S`         | Move backward                 |
| `A`         | Move left                     |
| `D`         | Move right                    |
| `Q`         | Move down                     |
| `E`         | Move up                       |
| `←`         | Rotate counter-clockwise      |
| `→`         | Rotate clockwise              |
| `F`         | Flip forward                  |
| `C`         | Close video window            |
| `X`         | Land and stop the drone       |
 ---------------------------------------------

> The movement is continous while the keys are held down. The movement stops when the keys are released.

# How to Get Started

1. Install the dependencies: 

> ```bash
> pip install opencv-python djitellopy keyboard numpy

2. Run the script:

> python tello_control.py

# Color Detection

The drone uses HSV color threseholds to detect the most dominant color in view. The detected colors are overlaid on the video feed.

The following colors are as follows:

- Red
- Orange
- Yellow
- Green
- Blue
- Purple

# Safety Notes

- Always fly in a clear and open space.
- Check the battery before use.
- Always land using 'x' instead of force-closing the script.

# Credits

Created by Alexander Goodwine and Caleb Goffney