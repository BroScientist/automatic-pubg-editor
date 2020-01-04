SECONDS_BEFORE = 5
SECONDS_AFTER = 2
global fps
fps = 0
# experiment with different SECONDS_AFTER values
# TODO: known bugs - detects blue in blue zone, poor accuracy when dealing with small images


class Helper():
    def get_pixels(image_name):
        from PIL import Image
        im = Image.open(image_name) # Can be many different formats.
        pix = im.load()

        print('checking image: ' + image_name)
        width, height = im.size

        x1 = y1 = z1 = []

        for x in range(0, width):
            for y in range(0, height):
                pixel = pix[x, y]
                # if pixel != (255, 255, 255, 0):
                print(pix[x,y])
                    # x1.append(pixel[0])
                    # y1.append(pixel[1])
                    # z1.append(pixel[2])
        print('done')
        # return x1, y1, z1


def export_video_to_frames(video_path):
    """takes the video file at video path and converts it into individual frames in the folder data"""

    import cv2
    import os

    video = cv2.VideoCapture(video_path)
    global fps
    fps = int(video.get(cv2.CAP_PROP_FPS))

    try:
        if not os.path.exists('data'):
            os.makedirs('data')
            os.chdir('data')
        else:
            os.chdir('data')

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
            cv2.imwrite(name, resized)

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

    for x in range(0, 60):
        for y in range(0, 70):
            color = pix[x, y]
            # TODO: use conditional unpacking to deal with the potential last var
            red, green, blue  = color
            if (110 < red < 165) and (235 < green < 255) and (225 < blue < 255):
                # print('pixel found')
                # print(x, y)
                # print('found')
                return True
    return False
    # print('done')


def find_action_points():
    """goes through every image in the data folder and appneds the identified action points to action_point_list, whichi represents all the frames at which actions occur in the video"""
    import os
    action_point_list = []
    folder_path = '/Users/apple/PycharmProjects/Automatic_PUBG_Cutter/data/'
    for f in os.listdir(folder_path):
        if is_action(folder_path + f):
            print(f)
            frame = ''.join([char for char in f if char.isdigit()])
            action_point_list.append(int(frame))
    return action_point_list





def convert_action_points(action_point_list):
    """takes all the action points and converts them into a format where points that are less than 125 frames apart are merged"""
    action_point_list.sort()
    new = []
    index = 0
    while index != len(action_point_list):
        try:
            group = []
            curr = action_point_list[index]
            next = action_point_list[index + 1]
            while (curr + 125) > next:
                group.append(curr)
                index += 1
                curr = action_point_list[index]
                next = action_point_list[index + 1]
            new.append(group)
        except IndexError:
            pass
        finally:
            index += 1

        print(index)

    results = []
    for item in new:
        try:
            print(item[0], item[-1])
            results.append((item[0], item[-1]))
        except IndexError:
            pass
    print(results)
    return results


def build_highlight_reel(action_point_list):
    """takes a list of converted action points and goes to each correspoinding timestamp in the video to produce a highlight reel"""
    from moviepy.editor import VideoFileClip, concatenate_videoclips
    clips = []
    video = VideoFileClip(PATH)
    for action_point in action_point_list:
        start_time = action_point[0] / fps
        end_time = action_point[1] / fps
        print(start_time, end_time)
        if end_time + SECONDS_AFTER < video.duration:
            clip = video.subclip(start_time - SECONDS_BEFORE, end_time + SECONDS_AFTER)
            clips.append(clip)

    video = concatenate_videoclips(clips)
    video.write_videofile('/Users/apple/PycharmProjects/Automatic_PUBG_Cutter/highlights_sept25.mp4')


if __name__ == '__main__':
    import time
    t1 = time.time()

    PATH = '/Users/apple/Downloads/KING LEVEL OPERATION!🔥 UNSCATHED! DESTROYED THE TEAM OF 4 PEOPLE!😱 _ PUBG MOBILE.mp4'
    export_video_to_frames(PATH)
    action_point_list = find_action_points()
    converted_points = convert_action_points(action_point_list)
    build_highlight_reel(converted_points)
    t2 = time.time()
    print(t2-t1)

