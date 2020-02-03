import os
import cv2
import pafy
import youtube_dl
import time
from datetime import timedelta

# cd "/Applications/Python 3.8/"
# sudo "./Install Certificates.command"


def detect_haar_faces(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face_cascasde = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    faces = face_cascasde.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10, minSize=(30, 30), flags = cv2.CASCADE_SCALE_IMAGE)
    return faces


def detect(image):
    objects = detect_haar_faces(image)
    return objects


def frame_text(text, vertical):
    cv2.putText(
        frame, text, (10, vertical), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1,
    )
    return

# def get_url():
#     url = input("YouTube URL: ")
#     if not url:
#         print("Running test video -- 3 seconds, 70 frames")
#         url= "https://www.youtube.com/watch?v=ighghZIoP1k"
#     return url

# def get_best_video(url):
#     vPafy = pafy.new(url, gdata=True)
#     print(f"Loading {video.title} {vPafy.duration}")
#     video = vPafy.getbest()
#     print(f"Best case {video.extension} {video.mediatype} in {video.resolution}")
#     print(f"Length: {vPafy.length}")
#     return video, vPafy

# def download_video(video, vPafy):
#     best.dowload(quiet=False)
#     return 
    

def get_url():
    url = input("YouTube URL: ")
    if not url:
        # return False
        url = "https://www.youtube.com/watch?v=ighghZIoP1k"
    vPafy = pafy.new(url, gdata=True)
    print(f"Capturing {vPafy.title} {vPafy.duration}")
    video = vPafy.getbest()
    print(f"Loading {video.extension} {video.mediatype} in {video.resolution}")
    print(f"Lenght: {vPafy.length}")
    return video, vPafy


def draw_objects(objects, frame):
    for i, (x, y, w, h) in enumerate(objects):
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(
            frame,
            str(i+1),
            (x + 10, y + 20),
            cv2.FONT_HERSHEY_PLAIN,
            1.5,
            (0, 255, 0),
            2,
        )
    return

# def draw_edges(objects, frame):
#     for i, (x, y, w, h) in enumerate(objects):
#         selection = frame[x:x+w, y:y+h]
#         cv2.

def valid_dir(root, directory):
    if not os.path.exists(root):
        print(f"Creating {root}")
        os.mkdir(root)
    full_path = root + directory
    if not os.path.exists(full_path):
        print(f"Creating {full_path}")
        os.mkdir(full_path)
    return full_path


ROOT = "work_files/"
video, vPafy = get_url()
cap = cv2.VideoCapture(video.url)
count = 0
current_objects = 0
max_objects = 0
screen_time = 0
start_time = time.time()
directory = valid_dir(ROOT, vPafy.videoid)

while True:
    count += 1
    run_time = time.time() - start_time
    ret, frame = cap.read()

    if not ret:
        print(f"\nEnd of file reached")
        break

    frame_text("frame:   {}".format(count), 30)
    objects = detect(frame)

    frame_text(
        "screentime: {} {}%".format(screen_time, int((100 * screen_time) / count)), 50
    )
    frame_text("runtime: {}".format(run_time), 70)
    frame_text("objects max: {} curr {}".format(max_objects, current_objects), 90)

    draw_objects(objects, frame)

    current_objects = len(objects)
    if current_objects > max_objects:
        cv2.imwrite(directory + "/" + str(current_objects) + "_" + str(count) + ".png", frame)
    max_objects = max(current_objects, max_objects)

    screen_time += 1
    cv2.imshow(vPafy.title, frame)

    if cv2.waitKey(20) & 0xFF == ord("q"):
        print(f"\nCancellation initiated.\nExiting...")
        break


# Done here
cv2.destroyAllWindows()
print(f"Total frames      {count}")
print(f"Total runtime     {timedelta(seconds=run_time)}")
print(f"Original speed {vPafy.length} sec -- {int(100 * vPafy.length / run_time)}%")
print(f"Total screentime  {screen_time}")
print(f"Max objects shown {max_objects}")
