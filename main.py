from pytube import YouTube
import time as t

url = input("enter the url of youtube video: ")
video = YouTube(url)
detans = input("do you want to see video details: ")
if detans == "yes":
    #detail of video

    print("the detail is: ")
    print("the author of this video is", video.author)
    print("the length of this video is", f'{video.length/60} minutes')
    print("views of this video is", video.views)
t.sleep(.3)
print("video is availble in three diffrent mode: \n 1. highest quality \n2.Lowest quality \n 3.audio ")
valueofk = input("enter the mode you want to download: (eg. highest quality, lowest quality, audio) :").lower()
if valueofk == "highest quality":
    video.streams.get_highest_resolution().download()
    print("downloaded at highest quality, check the folder: ")
elif valueofk == "lowest quality".lower():
    video.streams.get_lowest_resolution().download()
    print("downloaded at lowest quality, check the folder: ")
elif valueofk == "audio":
    video.streams.get_audio_only().download()
    print("downloaded at audio quality, check the folder: ")
else:
    print("enter some value ")



