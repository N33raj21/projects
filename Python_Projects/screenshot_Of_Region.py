import pyautogui
region = (0,0,2080,1200) #the region(left,top,width,height)
screenshot = pyautogui.screenshot(region=region)
screenshot.save("region_screenshot.png")