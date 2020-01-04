def get_video_sample(path):
    import cv2
    img = cv2.imread(path)
    height = img.shape[0]
    width = img.shape[1]

    crop_img = img[int(0.3 * height):int(0.55 * height), :int(0.3 * width)]
    cv2.imshow("cropped", crop_img)
    cv2.waitKey(0)

#TODO need to adjust box for every video...

def export_video_to_frames(video_path):
    """takes the video file at video path and converts it into individual frames in the folder data"""

    import cv2
    import os

    video = cv2.VideoCapture(video_path)
    global fps
    fps = int(video.get(cv2.CAP_PROP_FPS))

    try:
        if not os.path.exists('training_data'):
            os.makedirs('training_data')
            os.chdir('training_data')
        else:
            os.chdir('training_data')

    except OSError:
        print ('Error')

    current_frame = 0
    while(True):
        ret, frame = video.read()

        if not ret:
            break
        if current_frame%fps==0:
            name = str(current_frame) + '.png'
            print ('Creating...' + name)
            resized = cv2.resize(frame, (240, 135))
            height = resized.shape[0]
            width = resized.shape[1]
            cropped = resized[int(0.3 * height):int(0.55 * height), :int(0.3 * width)]
            cv2.imwrite(name, cropped)

        current_frame += 1

    video.release()
    cv2.destroyAllWindows()


def is_action(image_name):
    """checks the image for matching pixels in the provided range of colors"""

    from PIL import Image
    im = Image.open(image_name)
    pix = im.load()

    # print('checking image: ' + image_name)
    width, height = im.size

    for x in range(0, width):
        for y in range(0, height):
            color = pix[x, y]
            # TODO: use conditional unpacking to deal with the potential last var
            red, green, blue  = color
            if (110 < red < 165) and (235 < green < 255) and (225 < blue < 255):
                return True

    return False

import shutil
import os
target_folder = 'dataset/test_set/action'
# export_video_to_frames('/Users/apple/Downloads/TURNING FINAL ZONE INTO TARGET PRACTICE ZONE WITH M16 + SKS!😨 _ 25 KILLS VICTORY! 👍_ PUBG Mobile.mp4')
#problem with images of the same name
for f in os.listdir('training_data'):
    if is_action('training_data/' + f):
        shutil.move('training_data/' + f, target_folder)

