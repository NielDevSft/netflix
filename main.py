import pyautogui
import time
serviceList= ["youtube", "netflix"]

def getServiceOpened():
    serviceSelected= None
    coords = None
    try:
        try:
            coords = pyautogui.locateCenterOnScreen('skip_youtube_image.png', confidence=.8)
        except:
            coords = pyautogui.locateCenterOnScreen('keep_watchin.png', confidence=.8)
            coords = None #ainda não funciona
            
        if coords: 
            print('Youtube aberto!')
            serviceSelected = 0
    except pyautogui.ImageNotFoundException:
        try:
            # aguardando print
            # coords = pyautogui.locateCenterOnScreen('skip_netflix_image.png', confidence=.8)
            if coords: 
                print('Youtube aberto!')
                serviceSelected = 1
        except pyautogui.ImageNotFoundException:
            print('Nada aberto!')
    return [coords, serviceSelected]

def skip():
    
    coordsNService = getServiceOpened()
    if coordsNService[0] is not None:
        pyautogui.moveTo(coordsNService[0])
        pyautogui.click()
        print('Abertura do '+ str(serviceList[coordsNService[1]]) + ' pulada')    
    else:
        print('Por hora não achei nada. ;>')
        time.sleep(1)


while True:
    skip()

