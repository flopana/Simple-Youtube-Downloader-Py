import youtube_dlc
import os


def download(ydl_opts, link):
    with youtube_dlc.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
        menu()


def update():
    os.system('git checkout master')
    os.system('git pull')
    os.system('pip install --upgrade youtube-dlc')
    os.system('gsudo choco upgrade ffmpeg -y')
    os.system('cls')
    menu()


def menu():
    print("1. Download and convert to MP3\n"
          "2. Download and convert to MP4\n"
          "3. Just Download the video\n"
          "4. Update\n")
    option = int(input("Option: "))
    if option == 1:
        link = input("Link:\n")
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': 'audio/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'ignoreerrors': True
        }
        download(ydl_opts, link)
    elif option == 2:
        link = input("Link:\n")
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': 'video/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4'
            }],
            'ignoreerrors': True
        }
        download(ydl_opts, link)
    elif option == 3:
        link = input("Link:\n")
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': 'video/%(title)s.%(ext)s',
            'ignoreerrors': True
        }
        download(ydl_opts, link)
    elif option == 4:
        update()
    else:
        print("\nInvalid option!\n")
        menu()


if __name__ == '__main__':
    menu()
