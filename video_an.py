import os
import cv2
import pafy
import time
from datetime import timedelta

# cd "/Applications/Python 3.8/"
# sudo "./Install Certificates.command"


def detect_haar_faces(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face_cascasde = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    faces = face_cascasde.detectMultiScale(gray, 1.1, 4)
    return faces


def detect(image):
    faces = detect_haar_faces(image)
    return faces


def frame_text(text, vertical):
    cv2.putText(
        frame, text, (10, vertical), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1,
    )
    return


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


def draw_faces(faces, frame):
    for i, (x, y, w, h) in enumerate(faces):
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 1)
        cv2.putText(
            frame,
            str(i),
            (x + 10, y + 20),
            cv2.FONT_HERSHEY_PLAIN,
            1.5,
            (0, 255, 0),
            2,
        )
    return


def valid_dir(root, directory):
    if not os.path.exists(root):
        print(f"Creating {root}")
        os.mkdir(root)
    if not os.path.exists(root + directory):
        print(f"Creating {root + directory}")
        os.mkdir(root + directory)
    return root + directory


root = "work_files/"
video, vPafy = get_url()
cap = cv2.VideoCapture(video.url)
count = 0
current_faces = 0
max_faces = 0
screen_time = 0
start_time = time.time()
directory = valid_dir(root, vPafy.videoid)
while True:
    count += 1
    run_time = time.time() - start_time
    ret, frame = cap.read()

    if not ret:
        print(f"\nEnd of file reached")
        break

    frame_text("frame:   {}".format(count), 30)
    faces = detect(frame)

    frame_text(
        "screentime: {} {}%".format(screen_time, int((100 * screen_time) / count)), 50
    )
    frame_text("runtime: {}".format(run_time), 70)
    frame_text("faces max: {} curr {}".format(max_faces, current_faces), 90)

    draw_faces(faces, frame)

    current_faces = len(faces)
    if max_faces < current_faces:
        cv2.imwrite(directory + "/" + str(max_faces) + "_" + str(count) + ".png", frame)
        max_faces = current_faces
    screen_time += 1
    cv2.imshow(vPafy.title, frame)

    if cv2.waitKey(20) & 0xFF == ord("q"):
        print(f"\nCancellation initiated.\nExiting...")
        break


# Done here
print(f"Total frames      {count}")
print(f"Total runtime     {timedelta(seconds=run_time)}")
print(f"Original speed {vPafy.length} sec -- {int(100 * vPafy.length / run_time)}%")
print(f"Total screentime  {screen_time}")
print(f"Max objects shown {max_faces}")
