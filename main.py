import cv2 
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

    return img

def get_brightness_lvl(img):
    
    # resizing the image so it's easy to deal with 
    img = cv2.resize(img, (10,10))
    
    # use the HSL model 
    hsl_model = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)

    # L channel of HSL represents highlights quite well (brightness on image)   
    L_channel = hsl_model[:,:,1]
    
    # calculating the mean of the l channel 
    l_value = cv2.mean(L_channel)[0] / 100

    return l_value

def is_dark(brt_lvl):

    return True if brt_lvl < BRIGHTNESS_FACTOR else False 




def main():
    
    for i in range(100):
        img = capture_img("test.png")
        brightness = get_brightness_lvl(img)
        dark = is_dark(brightness)

        if dark:
            print(f"Dark : {brightness}")
        else:
            print(f"Bright : {brightness}")

        time.sleep(1)

if __name__ == "__main__":
    main()
