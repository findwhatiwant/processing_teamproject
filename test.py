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


handx = 0
handss = 0

nowscene = 1

#effect---------------------------------------------------------------------------------------------------------
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


#scene--------------------------------------------------------------------------------------------------------------
def scene1():
    p5.image(scene1background,0,0,800,800)
    p5.image(invitationin,400,200,238,391)
    if(handx < 238):
        p5.image(invitationout1,400,200,238-handx,391)
    else:
        p5.image(invitationout2,162+(476-handx),200,238-(476-handx),391)

def scene30():
    p5.image(BHT,0,0,800,800)

def scene3():
    global bright
    p5.tint(bright)
    p5.image(BHT, 0-zoom/2, 0-zoom/2, 800 + zoom, 800 + zoom)

#hand process-------------------------------------------------------------------------------------------------------------

def scene1_process(handLms):
    global handx, handss
    if(200 < handLms.landmark[0].x * 800 < 600):
        temp1 = int(handLms.landmark[0].x * 800)
        if(handx < 400):
            handss = 0
        else:
            handss = 1
    else:
        if(handss == 0):
            temp1 = 201
        else:
            temp1 = 599
    handx = int(((temp1 - 200)/400)*476)

def scene3_process(handLms):
    global zoom
    temp1 = handLms.landmark[4].x * 800
    temp2 = handLms.landmark[12].x * 800
    zoom = int(abs(temp2 - temp1)) + 1


def setup():
    global mpHands, hands, mpDraw, cap
    global BHT,invitationin, invitationout1, invitationout2, scene1background
    p5.size(800, 800)

    scene1background = p5.load_image("scene1background.png")
    invitationin = p5.load_image("invitation3.png")
    invitationout1 = p5.load_image("invitation.png")
    invitationout2 = p5.load_image("invitation1.jpg")
    BHT = p5.loadImage("HOTEL GB.png")

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
            if(nowscene == 1):
                scene1_process(handLms)
            elif(nowscene == 3):
                scene3_process(handLms)

    cv2.imshow("Image", img)

    if(nowscene == 1):
        scene1()
    elif(nowscene == 3):
        scene3()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        cap.release()
        # Destroy all the windows
        cv2.destroyAllWindows()
        return

p5.run()

