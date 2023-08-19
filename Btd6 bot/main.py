import pyautogui
import time
import random

notfree = []
newX = 999
newY = 999
monkey = 0
ratio = (1, 0.5625)
screensize = str(pyautogui.size())
screensizeX = float(screensize[11:15])
print("Screensize - ", screensizeX)


def PosCalcX(oldX):
    return float(( oldX / 2560 ) * screensizeX)



def PosCalcY(oldY):
    return float(( oldY / 2560) * screensizeX)


time.sleep(4) 
placementPosition = { 
    "1X":547, 
    "1Y":457,
    "2X":873,
    "2Y":709,
    "3X":621,
    "3Y":719,
    "4X":869,
    "4Y":456,
    "5X":838,
    "5Y":480,
    "6X":579,
    "6Y":973,
    "7X":1244,
    "7Y":676,
    "8X":197,
    "8Y":720,
    "heroX":230,
    "heroY":506,

}
towerLocations = {
    "heroX":2254,
    "heroY":287,
    "dartX":2449,
    "dartY":287,
    "boomerangX":2253,
    "boomerangY":442,
    "cannonX":2457,
    "cannonY":484,
    "tackX":2286,
    "tackY":650,
    "iceX":2449,
    "iceY":646,
    "glueX":2301,
    "glueY":834
}
startX = float(2418)
startY = float(1385)
pyautogui.click((PosCalcX(startX), PosCalcY(startY)))
pyautogui.click((PosCalcX(startX), PosCalcY(startY)))
while(1):
    if monkey <= 5:
        randTower = random.randint(1, 6)
        randPos = random.randint(1,8)

        print(randPos)
        print(randTower)
        if str(randPos) in notfree:
            randPos = random.randint(1, 8)
        else:
            if randTower == 1:
                pyautogui.click((PosCalcX(towerLocations["dartX"])), (PosCalcY(towerLocations["dartY"])))
            elif randTower == 2:
                pyautogui.click((PosCalcX(towerLocations["boomerangX"])), (PosCalcY(towerLocations["boomerangY"])))
            elif randTower == 3:
                pyautogui.click((PosCalcX(towerLocations["cannonX"])), (PosCalcY(towerLocations["cannonY"])))    
            elif randTower == 4:
                pyautogui.click((PosCalcX(towerLocations["tackX"])), (PosCalcY(towerLocations["tackY"])))    
            elif randTower == 5:
                pyautogui.click((PosCalcX(towerLocations["iceX"])), (PosCalcY(towerLocations["iceY"])))    
            elif randTower == 6:
                pyautogui.click((PosCalcX(towerLocations["glueX"])), (PosCalcY(towerLocations["glueY"])))   
            if randPos == 1:
                pyautogui.click((PosCalcX(placementPosition["1X"]), PosCalcY(placementPosition["1Y"])))
                monkey += 1
                notfree.append("1")
                time.sleep(15)
            elif randPos == 2:
                pyautogui.click((PosCalcX(placementPosition["2X"]), PosCalcY(placementPosition["2Y"])))
                monkey += 1
                notfree.append("2")
                time.sleep(15)
            elif randPos == 3:
                pyautogui.click((PosCalcX(placementPosition["3X"]), PosCalcY(placementPosition["3Y"])))
                monkey += 1
                notfree.append("3")
                time.sleep(15)
            elif randPos == 4:
                pyautogui.click((PosCalcX(placementPosition["4X"]), PosCalcY(placementPosition["4Y"])))
                monkey += 1
                notfree.append("4")
                time.sleep(15)
            elif randPos == 5:
                pyautogui.click((PosCalcX(placementPosition["5X"]), PosCalcY(placementPosition["5Y"])))
                monkey += 1
                notfree.append("5")
                time.sleep(15)
            elif randPos == 6:
                pyautogui.click((PosCalcX(placementPosition["6X"]), PosCalcY(placementPosition["6Y"])))
                monkey += 1
                notfree.append("6")
                time.sleep(15)
            elif randPos == 7:
                pyautogui.click((PosCalcX(placementPosition["7X"]), PosCalcY(placementPosition["7Y"])))
                monkey += 1
                notfree.append("7")
                time.sleep(15)
            elif randPos == 8:
                pyautogui.click((PosCalcX(placementPosition["8X"]), PosCalcY(placementPosition["8Y"])))
                monkey += 1
                notfree.append("8")
                time.sleep(15)
    if monkey >= 5:
        time.sleep(30)
        pyautogui.click((PosCalcX(towerLocations["heroX"]), PosCalcY(towerLocations["heroY"])))
        pyautogui.click((PosCalcX(placementPosition["heroX"]), (PosCalcY(placementPosition["heroY"]))))
        