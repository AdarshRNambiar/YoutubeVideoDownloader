from pytube import YouTube
def Download(link):
    youtubeObj=YouTube(link)
    youtubeObj=youtubeObj.streams.get_highest_resolution()
    try:
        youtubeObj.download()
    except:
        print("Error has occured")
    print("Download Succesfull")

link=input("Enter youtube URL")
Download(link)