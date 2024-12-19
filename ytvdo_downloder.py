from sys import argv
import yt_dlp

link = argv[1]
ydl = yt_dlp.YoutubeDL()

info_dict = ydl.extract_info(link, download=False)
video_title = info_dict.get('title', None)
video_views = info_dict.get('view_count', None)

print("Title: ", video_title)
print("Views: ", video_views)

ydl_opts = {
    'format': 'best',
}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])
