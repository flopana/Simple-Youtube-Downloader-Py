from __future__ import unicode_literals
import youtube_dl
import os


def download(ydl_opts):
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        link = input("Link:\n")
        ydl.download([link])
        menu()


def update():
    os.system('git checkout master')
    os.system('git pull')
    os.system('pip install --upgrade youtube-dl')
    os.system('gsudo choco upgrade ffmpeg -y')
    os.system('cls')
    menu()


def menu():
    print("1. Download and convert to MP3\n"
          "2. Download and convert to MP4\n"
          "3. Update\n"
          "4. Exit\n")
    option = int(input("Option: "))
    if option == 1:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': 'audio/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        }
        download(ydl_opts)
    elif option == 2:
        ydl_opts = {
            'format': 'best',
            'outtmpl': 'video/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4'
            }]
        }
        download(ydl_opts)
    elif option == 3:
        update()
    elif option == 4:
        exit(0)
    else:
        print("Invalid option!")
        menu()


if __name__ == '__main__':
    menu()
