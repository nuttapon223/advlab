import yt_dlp

def download_youtube_video(url, save_path="."):
    ydl_opts = {
        'outtmpl': f'{save_path}/%(title)s.%(ext)s',
        'format': 'best'
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Example usage
# video_url = ""
# print("Youtube URL : ") 
# input(video_url)
video_url = input("Enter the YouTube video URL: ")
# video_url = "https://www.youtube.com/watch?v=DhuGP_-zMxU"
download_youtube_video(video_url, save_path=".")