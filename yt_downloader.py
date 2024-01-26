from pytube import YouTube
import tkinter as tk
from tkinter import filedialog
from tqdm import tqdm
from threading import Thread

def download_video(url, path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension='mp4')
        highest_res_stream = streams.get_highest_resolution()

        with tqdm(total=highest_res_stream.filesize, unit='B', unit_scale=True, desc='Downloading') as pbar:
            highest_res_stream.download(output_path=path, filename='video')
            pbar.update(highest_res_stream.filesize)

        print("Video downloaded successfully!")
    except Exception as e:
        print(f"Error: {e}")

def open_file_dialog(entry_var):
    folder = filedialog.askdirectory()
    if folder:
        entry_var.set(folder)

def start_download(entry_url, entry_save_dir):
    video_url = entry_url.get()
    save_dir = entry_save_dir.get()

    if video_url and save_dir:
        print("Download started...")
        download_video(video_url, save_dir)
    else:
        print("Invalid URL or save location.")
        print("Download failed...")

def create_gui():
    root = tk.Tk()
    root.title("YouTube Video Downloader")

    entry_url_label = tk.Label(root, text="YouTube URL:")
    entry_url_label.pack()

    entry_url = tk.Entry(root, width=50)
    entry_url.pack()

    entry_save_dir_label = tk.Label(root, text="Save Directory:")
    entry_save_dir_label.pack()

    entry_save_dir_var = tk.StringVar()  # StringVar to store the save directory
    entry_save_dir = tk.Entry(root, width=50, textvariable=entry_save_dir_var)
    entry_save_dir.pack()

    save_dir_button = tk.Button(root, text="Browse", command=lambda: open_file_dialog(entry_save_dir_var))
    save_dir_button.pack()

    download_button = tk.Button(root, text="Download", command=lambda: start_download(entry_url, entry_save_dir_var))
    download_button.pack()

    root.geometry("400x200")
    root.mainloop()

if __name__ == "__main__":
    create_gui()
