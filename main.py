import yt_dlp
import os


def download_vid(url="https://www.youtube.com/shorts/s2PK245Q7uw", vid_name="random69"):
    # Get the Desktop directory dynamically
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")

    # Getting a new vid and custom video name from user
    vid_url = input("Enter url: ") or url
    vid_name = input("Enter video name: ") or vid_name

    # Construct the path to the desired folder on the Desktop
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    folder_name = os.path.join(desktop, "Saved_Videos")
    video_name_path = os.path.join(folder_name, f'{vid_name}.%(ext)s')

    # Construct the path to the desired folder on the Desktop
    if not os.path.exists(folder_name):
        os.makedirs(folder_name, exist_ok=True)  # Create the folder if it doesn't exist

    # Here you can choose in what format and the location the video will be saved
    options = {
        'format': 'best',
        'outtmpl': f'{video_name_path}'
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([vid_url])
    pass


def main():
    # Downloading the vid and asking for the next one... ctrl+c to exit the loop
    while True:
        download_vid()
    pass


if __name__ == "__main__":
    main()
