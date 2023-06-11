import cv2
import p5

import mediapipe as mp

#seasons variable
whatSeason = 0
globaltime = 0
daystate = 0

#bright
bright = 0

#fade variable
settingstate = 0
stop = 0

#scene1 variable
handx = 0
handss = 0
skipstate = 0

#scene2 variable
manX = 50
processstate = 0
doticket = 0

#scene30 variable
scene30x = 40
scene30y = 752-40
scene30ax = 1.6
scene30ay = 1.7
scene30tt = 60
scene30tr = 90
scene30v = 0

#scene3 variable
zoom = 1
stopstate = 0

#scene4 variable
getkeystate = 0
pickupstate = 0

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

def fadein():
    global bright, settingstate, stop
    if(settingstate == 0):
        bright = 0
        settingstate = 1
        stop = 0
    if(stop == 0):
        bright += 4
    if(bright > 252):
        stop = 1

def fadeout():
    global bright, settingstate, stop
    if(settingstate == 0):
        bright = 255
        stop = 0
        settingstate = 1
    if(stop == 0):
        bright -= 4
    if(bright < 8):
        stop = 1


#scene--------------------------------------------------------------------------------------------------------------
def scene1():
    p5.image(scene1background,0,0,800,800)
    p5.image(invitationin,400,200,238,391)
    if(handx < 238):
        p5.image(invitationout1,400,200,238-handx,391)
    else:
        p5.image(invitationout2,162+(476-handx),200,238-(476-handx),391)

def scene2():
    global manX, processstate, nowscene, settingstate
    if(doticket == 0):
        fadein()
    p5.tint(bright)
    p5.image(scene2background, 0, 0, 800, 800)
    if(manX < 470):
        processstate = 1
        p5.image(scene2man,manX,535,139,199)
        manX += 3
    else:
        if(doticket == 0):
            p5.image(ticket, 200, 120, 400, 250)
        elif(doticket == 1):
            p5.image(ticketcheck,200,120,400,250)
            fadeout()
            print(bright)
            if (bright < 8):
                settingstate = 0
                nowscene += 1
    p5.image(train,470,300,321,520)

def scene30():
    global scene30x, scene30y, scene30ax, scene30ay, nowscene,settingstate
    fadein()
    p5.tint(bright)

    p5.image(BHT, 0, 0, 800, 800)
    p5.image(train, scene30x, scene30y, scene30tt, scene30tr)

    scene30x = scene30x + scene30ax
    scene30y = scene30y - scene30ay

    if scene30x >= 460:
        scene30ax = scene30ay = 0
        settingstate = 0
        nowscene += 1

def scene3():
    global bright,settingstate, stopstate, nowscene
    p5.tint(bright)
    p5.image(BHT, 0-zoom/2, 0-zoom/2, 800 + zoom, 800 + zoom)
    print(zoom)
    if(zoom > 700):
        stopstate = 1
    if(stopstate == 1):
        fadeout()
        if (bright < 8):
            settingstate = 0
            nowscene += 1

def scene4():
    global settingstate, nowscene
    if(pickupstate == 0):
        fadein()
    p5.tint(bright)
    p5.image(scene4background,0,0,800,800)
    if(getkeystate == 0):
        p5.image(scene4man,400-155,212)
    elif(getkeystate == 1):
        p5.image(scene4man1,400-187,260)
        if(pickupstate == 0):
            p5.image(scene4key, 500,500)
    if(pickupstate == 1):
        fadeout()
        print(bright)
        if (bright < 8):
            settingstate = 0
            nowscene += 1



#hand process-------------------------------------------------------------------------------------------------------------

def scene1_process(handLms):
    global handx, handss, skipstate, nowscene, settingstate
    if(skipstate == 1):
        temp1 = 599
        print(bright)
        fadeout()
        p5.tint(bright)
        if (bright < 8):
            settingstate = 0
            nowscene += 1
    elif(200 < handLms.landmark[0].x * 800 < 600 and skipstate == 0):
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
            skipstate = 1
    handx = int(((temp1 - 200)/400)*476)

def scene2_process(handLms):
    global processstate, doticket, settingstate
    temp1 = int(handLms.landmark[8].y * 800)
    temp2 = int(handLms.landmark[4].y * 800)
    if(abs(temp2 - temp1) < 50 and processstate == 1 and bright > 252):
        processstate = 0
        doticket = 1
        settingstate = 0

def scene30_process(handLms):
    pass

def scene3_process(handLms):
    global zoom
    if(stopstate == 0):
        temp1 = handLms.landmark[4].x * 800
        temp2 = handLms.landmark[12].x * 800
        zoom = int(abs(temp2 - temp1)) + 1
    else:
        zoom = 700

def scene4_process(handLms):
    global getkeystate, pickupstate,settingstate
    temp1 = int(handLms.landmark[0].x*800)
    temp2 = int(handLms.landmark[12].x*800)
    temp3 = int(handLms.landmark[0].y*800)
    temp4 = int(handLms.landmark[12].y*800)

    temp5 = int(handLms.landmark[4].x*800)
    temp6 = int(handLms.landmark[8].x * 800)
    temp7 = int(handLms.landmark[16].x * 800)
    temp8 = int(handLms.landmark[20].x * 800)
    if(abs(temp1-temp2) < 50 and temp4 > temp3 and getkeystate == 0):
        getkeystate = 1
    if(getkeystate == 1 and pickupstate == 0 and abs(temp5-temp6) < 100 and abs(temp5-temp7) < 100 and abs(temp5-temp8) < 100 and abs(temp5-temp4) < 100):
        pickupstate = 1
        settingstate = 0





def setup():
    global mpHands, hands, mpDraw, cap
    global BHT,invitationin, invitationout1, invitationout2, scene1background, scene2background,scene4background, scene2man, train, ticket, ticketcheck, scene4man, scene4man1, scene4key
    p5.size(800, 800)

    invitationin = p5.load_image("invitation3.png")
    invitationout1 = p5.load_image("invitation.png")
    invitationout2 = p5.load_image("invitation1.jpg")

    scene2man = p5.load_image("scene2man.png")
    train = p5.load_image("train.png")
    ticket = p5.load_image("ticket.png")
    ticketcheck = p5.load_image("ticketcheck.png")

    scene4man = p5.load_image("scene4man.png")
    scene4man1 = p5.load_image("scene4man_1.png")
    scene4key = p5.load_image("scene4key.png")

    scene1background = p5.load_image("scene1background.png")
    scene2background = p5.load_image("scene2background.jpg")
    scene4background = p5.load_image("scene4background.png")

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

    success, img = cap.read()
    img = cv2.flip(img, 1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
            if(nowscene == 1):
                scene1_process(handLms)
            elif(nowscene == 2):
                scene2_process(handLms)
            elif(nowscene == 3):
                scene30_process(handLms)
            elif(nowscene == 4):
                scene3_process(handLms)
            elif(nowscene == 5):
                scene4_process(handLms)

    cv2.imshow("Image", img)

    if(nowscene == 1):
        scene1()
    elif(nowscene == 2):
        scene2()
    elif(nowscene == 3):
        scene30()
    elif(nowscene == 4):
        scene3()
    elif(nowscene == 5):
        scene4()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        cap.release()
        # Destroy all the windows
        cv2.destroyAllWindows()
        return

p5.run()