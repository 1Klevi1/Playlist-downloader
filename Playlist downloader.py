from pytube import YouTube
from pytube import Playlist
from pytube import Search

# where to save
SAVE_PATH = r'C:\Users\E-store\OneDrive\Desktop\Yotube video'
#to_do
 
# link of the video to be downloaded
playlist_url='https://www.youtube.com/watch?v=h2VaLM85L3g&list=PLRe9ARNnYSY45g8gtWQcC7pNX10TgEUfy'
p=Playlist(playlist_url)
for video in p:
    try:
        # object creation using YouTube
        # which was imported in the beginning
        yt = YouTube(video)
    except:
        print("Connection Error") #to handle exception
        
        # filters out all the files with "mp4" extension
    mp4files = yt.streams.filter(file_extension='mp4')
        
        # get the video with the extension and
        # resolution passed in the get() function
    d_video=mp4files.get_by_resolution('720p')
    try:
        #downloading the video
        d_video.download(SAVE_PATH)
        print(yt.title + " has been successfully downloaded.") 
    except:
        print("Some Error!")
    print('Task Completed!') 