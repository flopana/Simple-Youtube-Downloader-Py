import youtube_dlc
import os


def download(ydl_opts):
    with youtube_dlc.YoutubeDL(ydl_opts) as ydl:
        link = input("Link:\n")
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
          "2. Just Download\n"
          "3. Update\n")
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
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': 'video/%(title)s.%(ext)s',
            # 'postprocessors': [{
            #     'key': 'FFmpegVideoConvertor',
            #     'preferedformat': 'mp4'
            # }]
        }
        download(ydl_opts)
    elif option == 3:
        update()
    else:
        print("Invalid option!")
        menu()


if __name__ == '__main__':
    menu()
