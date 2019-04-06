import cv2
import numpy as np
from matplotlib import pyplot as plt
import pyautogui
import math

global img_rgb
global img_gray


def findItem(templateLocation, threshold):
    template = cv2.imread(templateLocation,0)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    loc = np.where( res >= threshold)

    coord = []

    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
        coord.append([pt[0], pt[1]])
    return coord

img_rgb = pyautogui.screenshot()
img_rgb = cv2.cvtColor(np.array(img_rgb), cv2.COLOR_RGB2BGR)

#Intermediate: 0:750 , 0:600,  beginner: 0:550 , 0:410
img_rgb = img_rgb[0:1000 , 0:1400]

img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)

findItem('location of unknown.png', 0.9)


cv2.imwrite('res.png', img_rgb)

cv2.imshow('result', img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()

#print(findItem('location of unknown.png'))

#cv2.imshow('result', output)
#cv2.waitKey(0)  
#cv2.destroyAllWindows()

hasbeenclicked = []
while True:

    img_rgb = pyautogui.screenshot()
    img_rgb = cv2.cvtColor(np.array(img_rgb), cv2.COLOR_RGB2BGR)
    img_rgb = img_rgb[0:800 , 0:580]

    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)

    ones = findItem('location of 1.png', 0.9)
    twos = findItem('location of 2.png', 0.9)
    threes = findItem('location of 3.png', 0.9)
    fours = findItem('location of 4.png', 0.9)
    fives = findItem(location of 5.png', 0.9)
    unknowns = findItem('location of unknown.png', 0.9)
    flags = findItem('location of flag.png', 0.9)

    #image = pyautogui.screenshot()
    #image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    #image = image[210:510 , 80:370]

    aroundOne = {}
    aroundThisOne = []

    for o in ones:
        #print(o)
        for u in unknowns:
            if math.sqrt((o[0] - u[0])**2 + (o[1] - u[1])**2) < 50:
                aroundThisOne.append(u)
                aroundOne[str(o)] = aroundThisOne
        aroundThisOne = []  

    flagsAroundOne = {}
    aroundThisOne = []

    for o in ones:
        #print(o)
        for f in flags:
            if math.sqrt((o[0] - f[0])**2 + (o[1] - f[1])**2) < 50:
                aroundThisOne.append(f)
                flagsAroundOne[str(o)] = aroundThisOne
        aroundThisOne = []


    aroundTwo = {}
    aroundThisOne = []

    for o in twos:
        #print(o)
        for u in unknowns:
            if math.sqrt((o[0] - u[0])**2 + (o[1] - u[1])**2) < 50:
                aroundThisOne.append(u)
                aroundTwo[str(o)] = aroundThisOne
        aroundThisOne = []


    flagsAroundTwo = {}
    aroundThisOne = []

    for o in twos:
        #print(o)
        for f in flags:
            if math.sqrt((o[0] - f[0])**2 + (o[1] - f[1])**2) < 50:
                aroundThisOne.append(f)
                flagsAroundTwo[str(o)] = aroundThisOne
        aroundThisOne = []


    aroundThree = {}
    aroundThisOne = []

    for o in threes:
        #print(o)
        for u in unknowns:
            if math.sqrt((o[0] - u[0])**2 + (o[1] - u[1])**2) < 50:
                aroundThisOne.append(u)
                aroundThree[str(o)] = aroundThisOne
        aroundThisOne = []


    flagsAroundThree = {}
    aroundThisOne = []

    for o in threes:
        #print(o)
        for f in flags:
            if math.sqrt((o[0] - f[0])**2 + (o[1] - f[1])**2) < 50:
                aroundThisOne.append(f)
                flagsAroundThree[str(o)] = aroundThisOne
        aroundThisOne = []

    

    aroundFour = {}
    aroundThisOne = []

    for o in fours:
        #print(o)
        for u in unknowns:
            if math.sqrt((o[0] - u[0])**2 + (o[1] - u[1])**2) < 50:
                aroundThisOne.append(u)
                aroundFour[str(o)] = aroundThisOne
        aroundThisOne = []


    flagsAroundFour = {}
    aroundThisOne = []

    for o in fours:
        #print(o)
        for f in flags:
            if math.sqrt((o[0] - f[0])**2 + (o[1] - f[1])**2) < 50:
                aroundThisOne.append(f)
                flagsAroundFour[str(o)] = aroundThisOne
        aroundThisOne = []

    
    aroundFive = {}
    aroundThisOne = []

    for o in fives:
        #print(o)
        for u in unknowns:
            if math.sqrt((o[0] - u[0])**2 + (o[1] - u[1])**2) < 50:
                aroundThisOne.append(u)
                aroundFive[str(o)] = aroundThisOne
        aroundThisOne = []

    flagsAroundFive = {}
    aroundThisOne = []

    for o in fives:
        #print(o)
        for f in flags:
            if math.sqrt((o[0] - f[0])**2 + (o[1] - f[1])**2) < 50:
                aroundThisOne.append(f)
                flagsAroundFive[str(o)] = aroundThisOne
        aroundThisOne = []

    

    #cv2.circle(image,(143,16), 3, (0,255,255), -1)
    #cv2.circle(image,(13,78), 3, (255,255,255), -1)
    #cv2.imwrite('res.png', image)

    #cv2.imshow('result', image)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

    #print(aroundOne)


    #print(len(flagsAroundOne[str([181,253])]))

    for n in aroundOne.keys():
        if n not in flagsAroundOne:
            if (len(aroundOne[n]) == 1) and (aroundOne[n][0] not in hasbeenclicked):
                pyautogui.click(aroundOne[n][0][0], aroundOne[n][0][1], button='right')
                hasbeenclicked.append(aroundOne[n][0])
                #print('right')
                del aroundOne[n][0]
    for n in aroundOne.keys():
        if n in flagsAroundOne:
            if (len(aroundOne[n]) >= 1) and (aroundOne[n][0] not in hasbeenclicked) and (len(flagsAroundOne[n]) == 1):
                pyautogui.click(aroundOne[n][0][0], aroundOne[n][0][1], button='left')
                hasbeenclicked.append(aroundOne[n][0])
                #print('left')
                del aroundOne[n][0]



    for n in aroundTwo.keys():
        if n not in flagsAroundTwo:
            if (len(aroundTwo[n]) == 2) and (aroundTwo[n][0] not in hasbeenclicked):
                pyautogui.click(aroundTwo[n][0][0], aroundTwo[n][0][1], button='right')
                hasbeenclicked.append(aroundTwo[n][0])
                #print('right')
                del aroundTwo[n][0]
    
    for n in aroundTwo.keys():  
        if n in flagsAroundTwo:
            if (len(aroundTwo[n]) + len(flagsAroundTwo[n]) == 2) and (aroundTwo[n][0] not in hasbeenclicked):
                pyautogui.click(aroundTwo[n][0][0], aroundTwo[n][0][1], button='right')
                hasbeenclicked.append(aroundTwo[n][0])
                #print('right')
                del aroundTwo[n][0]

    for n in aroundTwo.keys():
        if n in flagsAroundTwo:
            if (len(aroundTwo[n]) >= 1) and (aroundTwo[n][0] not in hasbeenclicked) and (len(flagsAroundTwo[n]) == 2):
                pyautogui.click(aroundTwo[n][0][0], aroundTwo[n][0][1], button='left')
                hasbeenclicked.append(aroundTwo[n][0])
                #print('left')
                del aroundTwo[n][0]
    

    for n in aroundThree.keys():
        if n not in flagsAroundThree:
            if (len(aroundThree[n]) == 3) and (aroundThree[n][0] not in hasbeenclicked):
                pyautogui.click(aroundThree[n][0][0], aroundThree[n][0][1], button='right')
                hasbeenclicked.append(aroundThree[n][0])
                #print('right')
                del aroundThree[n][0]
        if n in flagsAroundThree:
            if (len(aroundThree[n]) + len(flagsAroundThree[n]) == 3) and (aroundThree[n][0] not in hasbeenclicked):
                pyautogui.click(aroundThree[n][0][0], aroundThree[n][0][1], button='right')
                hasbeenclicked.append(aroundThree[n][0])
                #print('right')
                del aroundThree[n][0]

    for n in aroundThree.keys():
        if n in flagsAroundThree:
            if (len(aroundThree[n]) >= 1) and (aroundThree[n][0] not in hasbeenclicked) and (len(flagsAroundThree[n]) == 3):
                pyautogui.click(aroundThree[n][0][0], aroundThree[n][0][1], button='left')
                hasbeenclicked.append(aroundThree[n][0])
                #print('left')
                del aroundThree[n][0]

    for n in aroundFour.keys():
        if n not in flagsAroundFour:
            if (len(aroundFour[n]) == 4) and (aroundFour[n][0] not in hasbeenclicked):
                pyautogui.click(aroundFour[n][0][0], aroundFour[n][0][1], button='right')
                hasbeenclicked.append(aroundFour[n][0])
                #print('right')
                del aroundFour[n][0]
        if n in flagsAroundFour:
            if (len(aroundFour[n]) + len(flagsAroundFour[n]) == 4) and (aroundFour[n][0] not in hasbeenclicked):
                pyautogui.click(aroundFour[n][0][0], aroundFour[n][0][1], button='right')
                hasbeenclicked.append(aroundFour[n][0])
                #print('right')
                del aroundFour[n][0]

    for n in aroundFour.keys():
        if n in flagsAroundFour:
            if (len(aroundFour[n]) >= 1) and (aroundFour[n][0] not in hasbeenclicked) and (len(flagsAroundFour[n]) == 4):
                pyautogui.click(aroundFour[n][0][0], aroundFour[n][0][1], button='left')
                hasbeenclicked.append(aroundFour[n][0])
                #print('left')
                del aroundFour[n][0]

    for n in aroundFive.keys():
        if n not in flagsAroundFive:
            if (len(aroundFive[n]) == 5) and (aroundFive[n][0] not in hasbeenclicked):
                pyautogui.click(aroundFive[n][0][0], aroundFour[n][0][1], button='right')
                hasbeenclicked.append(aroundFive[n][0])
                #print('right')
                del aroundFive[n][0]
        if n in flagsAroundFive:
            if (len(aroundFive[n]) + len(flagsAroundFive[n]) == 5) and (aroundFive[n][0] not in hasbeenclicked):
                pyautogui.click(aroundFive[n][0][0], aroundFive[n][0][1], button='right')
                hasbeenclicked.append(aroundFive[n][0])
                #print('right')
                del aroundFive[n][0]

    for n in aroundFive.keys():
        if n in flagsAroundFive:
            if (len(aroundFive[n]) >= 1) and (aroundFive[n][0] not in hasbeenclicked) and (len(flagsAroundFive[n]) == 5):
                pyautogui.click(aroundFive[n][0][0], aroundFive[n][0][1], button='left')
                hasbeenclicked.append(aroundFive[n][0])
                #print('left')
                del aroundFive[n][0]















