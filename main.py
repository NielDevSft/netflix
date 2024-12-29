import pyautogui
import time
serviceList= ["youtube", "netflix", "mercado_play"]

def getServiceOpened():
    serviceSelected= None
    coords = None
    try:
        try:
            coords = pyautogui.locateCenterOnScreen('skip_youtube_image.png', confidence=.8)
            print('Youtube aberto!')
            serviceSelected = 0
        except:
            try:
                coords = pyautogui.locateCenterOnScreen('skip_mercado_play.png', confidence=.8)
                print('Mercado play aberto!')
                serviceSelected = 2
            except pyautogui.ImageNotFoundException:
                print('Nada aberto!')
        
            
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

