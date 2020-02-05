import cv2
import pafy
from filesys_helper import valid_dir

class VideoProvider:
    def __init__(self, self.url, option='stream'):
        self._option = option
        self.self.url = url
        
    def getFrame():
        if option=='stream':
            cap = cv2.VideoCapture(self.url)
        elif option =='file':
            cap = cv2.VideoCapture(downloadVideo)
        else:
            return False
        return cap.read
    def get_url(self):
        self.url = input("YouTube URL: ")
        if not self.url:
            # return False
            self.url = "https://www.youtube.com/watch?v=ighghZIoP1k"
        vPafy = pafy.new(self.url, gdata=True)
        print(f"Capturing {vPafy.title} {vPafy.duration}")
        video = vPafy.getbest()
        print(f"Loading {video.extension} {video.mediatype} in {video.resolution}")
        print(f"Lenght: {vPafy.length}")
        return video, vPafy
        
    def downloadVideo(self):
        video, vPafy = get_url()
        return video.download(valid_dir(vPafy.videoid))
        
