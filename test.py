# This script is a long distance test
import cv2
from djitellopy import tello
import keyboard
import time
import threading

import numpy as np

drone = tello.Tello()

COLOR_RANGES = {
    "Red":      [(0, 120, 70), (10, 255, 255), (170, 120, 70), (180, 255, 255)],
    "Green":    [(40, 40, 40), (85, 255, 255)],
    "Blue":     [(100, 150, 0), (130, 255, 255)],
    "Yellow":   [(20, 100, 100), (30, 255, 255)],
    "Orange":   [(10, 100, 20), (20, 255, 255)],
    "Purple":   [(130, 50, 50), (160, 255, 255)]
}

def detect_dominant_color(hsv_frame):
    max_area = 0
    detected_color = "None"

    for color, ranges in COLOR_RANGES.items():
        if len(ranges) == 4:  # red has two ranges
            lower1, upper1, lower2, upper2 = ranges
            mask1 = cv2.inRange(hsv_frame, np.array(lower1), np.array(upper1))
            mask2 = cv2.inRange(hsv_frame, np.array(lower2), np.array(upper2))
            mask = cv2.bitwise_or(mask1, mask2)
        else:
            lower, upper = ranges
            mask = cv2.inRange(hsv_frame, np.array(lower), np.array(upper))

        area = cv2.countNonZero(mask)
        if area > max_area:
            max_area = area
            detected_color = color

    return detected_color

def show_camera_frames():
    # Shows the camera frames through cv2
    
    while True:
        frame = drone.get_frame_read().frame
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Detect dominant color
        color_name = detect_dominant_color(hsv)

        # Average BGR color for reference
        average_color_per_row = np.average(frame, axis=0)
        average_color = np.average(average_color_per_row, axis=0)
        average_color = np.uint8(average_color)
        print(f"Average color (BGR): {average_color}, Detected: {color_name}")

        # Show text overlay
        cv2.putText(frame, f"Detected: {color_name}", (30, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Display video frame
        cv2.imshow("Frame", frame)

        if cv2.waitKey(1) & 0xFF == ord('c'):
            break

    cv2.destroyAllWindows()


drone.connect()
# connects and sleeps to ensure it is ready
drone.takeoff()
drone.streamon()
camera_thread = threading.Thread(target=show_camera_frames, args=())
camera_thread.start()
time.sleep(2)
# takes off

# connects and takes off

while True:
    if keyboard.is_pressed('w'):
            drone.move_forward(30)
            time.sleep(0.6)
            
    if keyboard.is_pressed('s'):
            drone.move_back(30)
            time.sleep(0.6)
            
    if keyboard.is_pressed('a'):
            drone.move_left(30)
            time.sleep(0.6)   
            
    if keyboard.is_pressed('d'):
            drone.move_right(30)
            time.sleep(0.6)      
            
    if keyboard.is_pressed('q'):
            drone.rotate_counter_clockwise(160)
            time.sleep(0.6)             
        
    if keyboard.is_pressed('e'):
            drone.rotate_clockwise(160)
            time.sleep(0.6) 
            
    if keyboard.is_pressed('up'):
            drone.move_up(30)
            time.sleep(0.6) 
            
    if keyboard.is_pressed('down'):
            drone.move_down(30)
            time.sleep(0.6) 
               
    if keyboard.is_pressed('l'):
            drone.land()
            drone.streamoff()
            break
