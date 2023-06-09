from yt_dlp import YoutubeDL

	#where to save
SAVE_PATH = "data/v10" #to_do

	#link of the video to be downloaded
links="https://youtu.be/WzBoJ2xQl3Q"

# Set the options for post-processing
ydl_opts = {
    'outtmpl': SAVE_PATH + '/%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
        'preferredquality': '192',
    }],
}

with YoutubeDL(ydl_opts) as ydl:
    ydl.download(links)

print('Task Completed!')