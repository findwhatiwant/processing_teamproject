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

#scene31 variable
scene31locations = []
knockcnt = 0
backgroundtype = 0

#scene4 variable
getkeystate = 0
pickupstate = 0
scene4handx = 0
scene4handy = 0
justcheck = 0

#scene5 variable
boxopened = 0
scene4pickupstate = 0

#scene6 variable
textY = 200

nowscene = 6

#effect---------------------------------------------------------------------------------------------------------
def seasons():
    global globaltime,bright,daystate,backgroundtype
    bright = 255 - globaltime
    globaltime += 1
    if(globaltime > 254):
        if (backgroundtype < 3):
            backgroundtype += 1
        elif (backgroundtype == 3):
            backgroundtype = 0
        globaltime = 0


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

def scene31():
    global nowscene,settingstate
    if (knockcnt <= 10):
        seasons()
    if(knockcnt > 10):
        p5.tint(bright)
    p5.image(scene31background4, -173, 0, 1146, 800)
    if(knockcnt <= 10):
        if (backgroundtype == 2):
            p5.tint(255, bright)
        elif (backgroundtype > 2):
            p5.tint(255, 0)
        else:
            p5.tint(255, 255)
    p5.image(scene31background3, -173, 0, 1146, 800)
    if (knockcnt <= 10):
        if (backgroundtype == 1):
            p5.tint(255, bright)
        elif (backgroundtype > 1):
            p5.tint(255, 0)
        else:
            p5.tint(255,255)
    p5.image(scene31background2, -173, 0, 1146, 800)
    if (knockcnt <= 10):
        if (backgroundtype == 0):
            p5.tint(255, bright)
        elif (backgroundtype > 0):
            p5.tint(255, 0)
    p5.image(scene31background1, -173, 0, 1146, 800)
    if (knockcnt <= 10):
        p5.tint(255)

    p5.image(hotel, 400-278,335,556,417)


    if(309 < scene4handx < 400 and 460 < scene4handy < 620):
        p5.tint(255,255)
    else:
        p5.tint(255,0)

    p5.image(window1, 309, 595, 11, 15)
    p5.image(window1, 330, 595, 11, 15)

    p5.image(window1, 309, 559, 11, 15)
    p5.image(window1, 309, 523, 11, 15)
    p5.image(window1, 309, 487, 11, 15)

    p5.image(window1, 329, 559, 11, 15)
    p5.image(window1, 329, 523, 11, 15)
    p5.image(window1, 329, 487, 11, 15)

    p5.image(window1, 349, 559, 11, 15)
    p5.image(window1, 349, 523, 11, 15)
    p5.image(window1, 349, 487, 11, 15)

    p5.image(window1, 369, 559, 11, 15)
    p5.image(window1, 369, 523, 11, 15)
    p5.image(window1, 369, 487, 11, 15)

    if (412 < scene4handx < 490 and 460 < scene4handy < 620):
        p5.tint(255, 255)
    else:
        p5.tint(255, 0)

    p5.image(window1, 412, 559, 11, 15)
    p5.image(window1, 412, 523, 11, 15)
    p5.image(window1, 412, 487, 11, 15)

    p5.image(window1, 432, 559, 11, 15)
    p5.image(window1, 432, 523, 11, 15)
    p5.image(window1, 432, 487, 11, 15)

    p5.image(window1, 452, 559, 11, 15)
    p5.image(window1, 452, 523, 11, 15)
    p5.image(window1, 452, 487, 11, 15)

    p5.image(window1, 474, 595, 11, 15)
    p5.image(window1, 454, 595, 11, 15)

    p5.image(window1, 472, 559, 11, 15)
    p5.image(window1, 472, 523, 11, 15)
    p5.image(window1, 472, 487, 11, 15)

    if (210 < scene4handx < 280 and 520 < scene4handy < 610):
        p5.tint(255, 255)
    else:
        p5.tint(255, 0)

    p5.image(window1, 274, 598, 11, 15)
    p5.image(window1, 274, 562, 11, 15)
    p5.image(window1, 274, 526, 11, 15)

    p5.image(window1, 254, 598, 11, 15)
    p5.image(window1, 254, 562, 11, 15)
    p5.image(window1, 254, 526, 11, 15)

    p5.image(window1, 234, 598, 11, 15)
    p5.image(window1, 234, 562, 11, 15)
    p5.image(window1, 234, 526, 11, 15)

    p5.image(window1, 214, 598, 11, 15)
    p5.image(window1, 214, 562, 11, 15)
    p5.image(window1, 214, 526, 11, 15)

    if (500 < scene4handx < 570 and 520 < scene4handy < 610):
        p5.tint(255, 255)
    else:
        p5.tint(255, 0)

    p5.image(window1, 564, 598, 11, 15)
    p5.image(window1, 564, 562, 11, 15)
    p5.image(window1, 564, 526, 11, 15)

    p5.image(window1, 544, 598, 11, 15)
    p5.image(window1, 544, 562, 11, 15)
    p5.image(window1, 544, 526, 11, 15)

    p5.image(window1, 524, 598, 11, 15)
    p5.image(window1, 524, 562, 11, 15)
    p5.image(window1, 524, 526, 11, 15)

    p5.image(window1, 504, 598, 11, 15)
    p5.image(window1, 504, 562, 11, 15)
    p5.image(window1, 504, 526, 11, 15)

    p5.tint(255,255)
    p5.circle(scene4handx,scene4handy, 30)
    if(knockcnt > 10):
        fadeout()
        print(bright)
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
    p5.no_stroke()
    p5.fill(255,0,0)
    p5.circle(scene4handx, scene4handy, 50)

def scene5():
    global nowscene
    fadein()
    p5.tint(bright)
    p5.image(scene1background,0,0,800,800)
    if(boxopened == 0):
        p5.image(boxclose,250,400,300,300)
    elif(boxopened == 1):
        p5.image(boxopen, 250, 400, 300, 300)
    p5.circle(scene4handx, scene4handy, 50)
    if(scene4pickupstate == 1):
        fadeout()
        print(bright)
        if (bright < 8):
            nowscene += 1

def scene6():
    global textY
    p5.background(0)
    p5.fill(255)
    p5.text_font(font1)
    p5.text("GRAND BUDAPEST HOTEL \n\n\n\n\n\n Develop: Woosik joe \n\n Sub Develop: Sangmin Oh \n\n Design & Drawing: Yeonju Oh, Sangmin Oh"
            + "\n\n\nHotel image: Yeonju Oh\n\ninvitation image: Yeonju Oh\n\ninvitation background: Yeonju Oh\n\ntrain image: Sangmin Oh\n\nscene2man image: sangmin Oh\n\nticket image: Woosik Joe"
            + "\n\nscene4man image: Sangmin Oh\n\nHotel background: Yeonju Oh\n\nbox image: Woosik Joe"
            + "\n\n\n\n\n\n\n\n\n Thank you for Watching \n\n Happy End of class",50,textY)
    textY -= 2

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

def scene31_process(handLms):
    global scene4handx,scene4handy,scene31locations, knockcnt,settingstate,justcheck
    scene4handx = int(handLms.landmark[12].x*800)
    scene4handy = int(handLms.landmark[12].y*800)

    temp1 = int(handLms.landmark[10].y*800)
    temp2 = int(handLms.landmark[9].y*800)

    scene31locations.append(temp2)
    print(knockcnt)
    if(len(scene31locations) == 10):
        scene31locations.pop(0)
        if(temp2 > temp1 and scene31locations[0]+200 < scene31locations[-1]):
            knockcnt += 1
    if(knockcnt > 10 and justcheck == 0):
        settingstate = 0
        justcheck = 1




def scene4_process(handLms):
    global getkeystate, pickupstate,settingstate,scene4handx, scene4handy
    temp1 = int(handLms.landmark[0].x*800)
    temp2 = int(handLms.landmark[12].x*800)
    temp3 = int(handLms.landmark[0].y*800)
    temp4 = int(handLms.landmark[12].y*800)

    temp5 = int(handLms.landmark[4].x*800)
    temp6 = int(handLms.landmark[8].x * 800)
    temp7 = int(handLms.landmark[16].x * 800)
    temp8 = int(handLms.landmark[20].x * 800)

    scene4handx = int(handLms.landmark[12].x*800)
    scene4handy = int(handLms.landmark[12].y*800)
    if(abs(temp1-temp2) < 50 and temp4 > temp3 and getkeystate == 0):
        getkeystate = 1
    if(getkeystate == 1 and pickupstate == 0 and abs(temp5-temp6) < 100 and abs(temp5-temp7) < 100 and abs(temp5-temp8) < 100 and abs(temp5-temp4) < 100 and 450 < scene4handx< 650 and 450 < scene4handy < 650):
        pickupstate = 1
        settingstate = 0

def scene5_process(handLms):
    global boxopened,scene4handy, scene4handx,scene4pickupstate,settingstate
    temp1 = handLms.landmark[4].x * 800
    temp2 = handLms.landmark[12].x * 800
    temp4 = int(handLms.landmark[12].y * 800)
    temp5 = int(handLms.landmark[4].x * 800)
    temp6 = int(handLms.landmark[8].x * 800)
    temp7 = int(handLms.landmark[16].x * 800)
    temp8 = int(handLms.landmark[20].x * 800)
    if(abs(temp1-temp2) > 400):
        boxopened = 1

    if (boxopened == 1 and scene4pickupstate == 0 and abs(temp5 - temp6) < 100 and abs(temp5 - temp7) < 100 and abs(
            temp5 - temp8) < 100 and abs(temp5 - temp4) < 100 and 250 < scene4handx < 550 and 300 < scene4handy < 600):
        settingstate = 0
        scene4pickupstate = 1

    scene4handx = int(handLms.landmark[12].x * 800)
    scene4handy = int(handLms.landmark[12].y * 800)





def setup():
    global mpHands, hands, mpDraw, cap
    global BHT,invitationin, invitationout1, invitationout2, scene1background, scene2background,scene4background, scene2man, train, ticket, ticketcheck, scene4man, scene4man1, scene4key, hotel,scene31background1,scene31background2,scene31background3,scene31background4,window1
    global boxopen, boxclose,font1
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

    scene31background1 = p5.load_image("scene31background1.jpg")
    scene31background2 = p5.load_image("scene31background2.jpg")
    scene31background3 = p5.load_image("scene31background3.jpg")
    scene31background4 = p5.load_image("scene31background4.jpg")

    font1 = p5.create_font("NanumGothic.ttf", 20)

    window1 = p5.load_image("window1.png")

    scene4background = p5.load_image("scene4background.png")

    boxopen = p5.load_image("boxopen.png")
    boxclose = p5.load_image("boxclose.png")

    BHT = p5.loadImage("HOTEL GB.png")
    hotel = p5.load_image("hotel.png")

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
                scene31_process(handLms)
            elif(nowscene == 6):
                scene4_process(handLms)
            elif(nowscene == 7):
                scene5_process(handLms)

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
        scene31()
    elif(nowscene == 6):
        scene4()
    elif(nowscene == 7):
        scene5()
    elif(nowscene == 8):
        scene6()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        cap.release()
        # Destroy all the windows
        cv2.destroyAllWindows()
        return

p5.run()