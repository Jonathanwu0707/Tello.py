import KeyBoardsetting as kbset
from djitellopy import tello
from time import sleep
import cv2

kbset.init()
drone = tello.Tello()
drone.connect()
drone.streamon()

def getKeyBoardInput():
    lr, fb, ud, yaw = 0, 0, 0, 0
    move = 100
    if kbset.keyPressed("a"):lr    = move         #move left
    elif kbset.keyPressed("d"):lr  = -move        #move right
    else : lr = 0
    if kbset.keyPressed("w"): fb   = move         #move forward
    elif kbset.keyPressed("s"): fb = -move        #move backward
    else : fb = 0
    if kbset.keyPressed("q"):yaw   = -move        #turn left
    elif kbset.keyPressed("e"):yaw = move         #turn right
    else : yaw = 0
    if kbset.keyPressed("z"): ud   = move         #up
    elif kbset.keyPressed("c"): ud = -move        #down
    if kbset.keyPressed("l"):  drone.land()
    if kbset.keyPressed("f"): drone.takeoff()

    return [lr, fb, ud, yaw]

while True:
     value = getKeyBoardInput()
     drone.send_rc_control(value[0], value[1], value[2], value[3])
     print(drone.get_battery())
     img = drone.get_frame_read().frame
     # cv2.imshow("Image", img)
     # cv2.resize()
     sleep(0.05)