from pytube import YouTube

def download_video_as_mp3(video_url):
    yt = YouTube(video_url)
    audio_stream = yt.streams.filter(only_audio=True).first()
    audio_stream.download(output_path=".", filename=yt.title + ".mp3")

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    download_video_as_mp3(video_url)
