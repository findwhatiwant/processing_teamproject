import cv2
import p5
# mediapipe
# [Tools]--[Manage Plugins] --> mediapipe
# Restart "Thonny"
import mediapipe as mp

whatSeason = 0
globaltime = 0
bright = 0
daystate = 0
zoom = 1

def seasons():
    global globaltime,bright,daystate
    bright = 255 - globaltime
    if(daystate == 0):
        globaltime += 1
    else:
        globaltime -= 1
    if(globaltime > 255):
        daystate = 1
    elif(globaltime < 0):
        daystate = 0


def setup():
    global mpHands, hands, mpDraw, cap
    global BHT, hotel, tree
    p5.size(800, 800)
    BHT = p5.loadImage("HOTEL GB.png")
    hotel = p5.loadImage("hotel.png")
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Could not open webcam")
        exit()

    mpHands = mp.solutions.hands
    hands = mpHands.Hands()
    mpDraw = mp.solutions.drawing_utils

def draw():
    global mpHands, hands, mpDraw, cap, zoom
    p5.background(255)
    global BHT, hotel, globaltime, bright
    seasons()
    success, img = cap.read()
    img = cv2.flip(img, 1)  ## JUNG
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
            temp1 = handLms.landmark[4].x * 800
            temp2 = handLms.landmark[12].x * 800
            zoom = int(abs(temp2-temp1))+1

    cv2.imshow("Image", img)
    p5.tint(bright)
    p5.image_mode('center')
    p5.image(BHT, 0, 0, 800+zoom, 800+zoom)
    #p5.image(hotel, 0, 0, 370 * zoom, 278 * zoom)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cap.release()
        # Destroy all the windows
        cv2.destroyAllWindows()
        return

p5.run()

