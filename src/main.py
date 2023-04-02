import os
from cv2 import cv2


images = [
    {"file": "/home/roman/auto1.mp4", "name": "Auto0", "frame": 800+1026, "last_point": ()},
    {"file": "/home/roman/auto0.mp4", "name": "Auto1", "frame": 800, "last_point": ()}
]



coordinates = []

def mouse_event(event, x, y, flags, param):
    #print(event, x, y, flags, param)
    if event == 1:
        param["last_point"] = (x, y)

for i in images:
    i["cv2"] = cv2.VideoCapture(i['file'])
    i["frames"] = i["cv2"].get(cv2.CAP_PROP_FRAME_COUNT)
    i["cv2"].set(cv2.CAP_PROP_POS_FRAMES, i["frame"])

    cv2.namedWindow(i["name"])
    cv2.setMouseCallback(i["name"], mouse_event, i)

while True:
    for i in images:
        ret, frame = i["cv2"].read()

        if frame is None:
            continue

        if ret is False:
            cv2.destroyAllWindows()
            cap.release()
            break

        frame= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow(i["name"], frame)

    while 1:
        key = cv2.waitKey(1)
        if key == -1:
            continue
        if key == ord(' '):
            break

        if key == ord(','):
            for i in images:
                i["cv2"].set(cv2.CAP_PROP_POS_FRAMES, i["cv2"].get(cv2.CAP_PROP_POS_FRAMES) - 2)
            break
        if key == ord('.'):
            break


        if key == ord('o'):
            for i in images:
                i["cv2"].set(cv2.CAP_PROP_POS_FRAMES, i["cv2"].get(cv2.CAP_PROP_POS_FRAMES) - 100-1)
            break
        if key == ord('e'):
            for i in images:
                i["cv2"].set(cv2.CAP_PROP_POS_FRAMES, i["cv2"].get(cv2.CAP_PROP_POS_FRAMES) + 100-1)
            break
        if key == ord('1'):
            data = []
            for i in images:
                data.append(i["last_point"])
            coordinates.append(data)
            print(coordinates)


cap.release()

