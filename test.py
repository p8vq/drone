# This script is a long distance test
import cv2
from djitellopy import tello
import keyboard
import time
import threading


drone = tello.Tello()

def show_camera_frames():
    # Shows the camera frames through cv2
    while True:
        frame = drone.get_frame_read().frame
        cv2.imshow("Frame", frame)
        # While it is running, cv2 gets the current frame on the camera and outputs it to a window
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
            drone.rotate_counter_clockwise(30)
            time.sleep(0.6)             
        
    if keyboard.is_pressed('e'):
            drone.rotate_clockwise(30)
            time.sleep(0.6) 
               
    if keyboard.is_pressed('l'):
            drone.land()
            drone.streamoff()
            break
