import moviepy
import os

FRAME_RATE = 25
SECONDS_BEFORE = 5
SECONDS_AFTER = 2
PATH = '/Users/apple/PycharmProjects/Automatic_PUBG_Cutter/test_clip.MOV'

def export_to_frames():
    import cv2
    import numpy as np
    import os

    cap = cv2.VideoCapture(PATH)

    try:
        if not os.path.exists('data'):
            os.makedirs('data')
            os.chdir('data')
    except OSError:
        print ('Error: Creating directory of data')

    currentFrame = 0
    while(True):

        # Capture frame-by-frame
        ret, frame = cap.read()

        if not ret:
            break
        if currentFrame%25==0:
            # Saves image of the current frame in jpg file
            name = str(currentFrame) + '.png'
            print ('Creating...' + name)
            cv2.imwrite(name, frame)

        # To stop duplicate images
        currentFrame += 1

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

def find_pixel(image_name):
    from PIL import Image
    im = Image.open(image_name) # Can be many different formats.
    pix = im.load()

    print('checking image: ' + image_name)
    width, height = im.size
    target = (142, 234, 241)
    target = (71, 54, 57)
    for x in range(0, width):
        for y in range(0, height):
            if pix[x, y] == target:
                print('pixel found')
                print(x, y)
                print('found')
                break

if __name__ == '__main__':
    # export_to_frames()
    import os
    # os.chdir('data')
    # list = []
    # for item in os.listdir():
    #     num = ''.join([char for char in item if char.isdigit()])
    #     num = int(num)
    #     list.append(num)
    # list.sort()
    # list = [str(item) + '.jpg' for item in list]
    # for item in list:
    #     find_pixel(item)