import cv2 
import subprocess as sp
import os
import time

#to find if image is dark or not : simply calculate the average intensity and judge it.

#img name
IMG_NAME = "test.png"

#greater than this would be bright, less dark
BRIGHTNESS_FACTOR = 0.5

def capture_img(img_name):

    # video 0 is the index of the connected cam
    cam = cv2.VideoCapture(0)

    # Capturing the img
    ret, img = cam.read()
    
    # No errors ? save the image
    if ret:
        # Writing the img
        cv2.imwrite(img_name, img)
        time.sleep(1)

    return img

def get_brightness_lvl(img):
    
    # resizing the image so it's easy to deal with 
    img = cv2.resize(img, (100,100))
    
    # use the HSL model 
    hsl_model = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)

    # L channel of HSL represents highlights quite well (brightness on image)   
    L_channel = hsl_model[:,:,1]
    
    # calculating the mean of the l channel 
    l_value = cv2.mean(L_channel)[0] / 100

    return l_value

def is_dark(brt_lvl):

    return True if brt_lvl < BRIGHTNESS_FACTOR else False 


def change_brightness(dark_):
    '''Change the screen brightness'''
    
    #get the brightness of the screen 
    #current_brightness = int(sp.getoutput('xbacklight -get'))
    current_brightness = 1 
    
    choice = "inc" if dark_ == 0 else "dec"
    os.system(f"xbacklight -{choice} {current_brightness*2}")

    for i in range(current_brightness):
        os.system(f"xbacklight -{choice} {current_brightness//2}")
        time.sleep(0.2)

    #exit(0)

def main():
    
    for i in range(100):
        img = capture_img("test.png")
        brightness = get_brightness_lvl(img)
        dark = is_dark(brightness)

        if dark:
            print(f"Dark : {brightness}")
            change_brightness(dark)
        else:
            print(f"Bright : {brightness}")
            change_brightness(dark)

        time.sleep(1)

if __name__ == "__main__":
    main()
