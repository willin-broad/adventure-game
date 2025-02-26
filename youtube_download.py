import yt_dlp

link = input("Paste your YOUTUBE video URL here: ")

# Create options for yt-dlp to download the best available single format
options = {
    'format': 'best',  # This will download the best available single file (video + audio)
    'noplaylist': True,  # Avoid downloading entire playlists if it's a playlist link
}

with yt_dlp.YoutubeDL(options) as ydl:
    ydl.download([link])

print("Download complete!")
