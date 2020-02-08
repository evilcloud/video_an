import pafy

# def get_url():
#     url = input("YouTube URL: ")
#     if not url:
#         # return False
#         url = "https://www.youtube.com/watch?v=ighghZIoP1k"
#     vPafy = pafy.new(url, gdata=True)
#     print(f"Capturing {vPafy.title} {vPafy.duration}")
#     video = vPafy.getbest()
#     print(f"Loading {video.extension} {video.mediatype} in {video.resolution}")
#     print(f"Lenght: {vPafy.length}")
#     return video, vPafy

def get_url():
    url = input("YouTube URL: ")
    if not url:
        print("Running test video -- 3 seconds, 70 frames")
        url= "https://www.youtube.com/watch?v=ighghZIoP1k"
    return url

def get_best_video(url):
    vPafy = pafy.new(url, gdata=True)
    print(f"Loading {video.title} {vPafy.duration}")
    video = vPafy.getbest()
    print(f"Best case {video.extension} {video.mediatype} in {video.resolution}")
    print(f"Length: {vPafy.length}")
    return video, vPafy

def download_video(video, vPafy):
    best.dowload(quiet=False)
    return 

url = get_url()
video, vPafy = get_best_video(url)
download_video(video)
