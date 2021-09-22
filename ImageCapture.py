from djitellopy import tello
import cv2

drone = tello.Tello()
drone.connect()
print(drone.get_battery())

drone.streamon()

while True:
    vis = drone.get_frame_read().frame
    img = drone.get_video_capture()


