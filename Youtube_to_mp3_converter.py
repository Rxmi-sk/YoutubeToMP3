import youtube_dl

def youtube_to_mp3():
    vid_link=input("Please enter the Youtube video's link:")
    vid_information=youtube_dl.YoutubeDL().extract_info(url = vid_link,download=False)
    filename=f"{vid_information['title']}.mp3"

    options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':filename,
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([vid_information['webpage_url']])

    print("Download complete... {}".format(filename))
    
