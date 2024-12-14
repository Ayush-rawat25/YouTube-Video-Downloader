import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube

class YouTubeDownloader:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Video Downloader")
        self.root.configure(bg='#222222')
        self.root.geometry('400x400')  

        url_label = tk.Label(self.root, text="Enter YouTube URL:", bg='#222222', fg='white')
        url_label.grid(row=0, column=0, padx=5, pady=5)
        self.url_entry = tk.Entry(self.root, width=30)
        self.url_entry.grid(row=0, column=1, padx=5, pady=5)

        quality_label = tk.Label(self.root, text="Select Quality:", bg='#222222', fg='white')
        quality_label.grid(row=1, column=0, padx=5, pady=5)
        self.quality_var = tk.StringVar()
        quality_combo = ttk.Combobox(self.root, textvariable=self.quality_var, width=15)
        quality_combo['values'] = ("360p", "480p", "720p", "1080p")
        quality_combo.current(0)
        quality_combo.grid(row=1, column=1, padx=5, pady=5)

        download_button = tk.Button(self.root, text="Download", command=self.download_video, bg='#3333ff', fg='white', width=30, height=2)
        download_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        self.status_label = tk.Label(self.root, text="", bg='#222222', fg='white')
        self.status_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    def download_video(self):
        url = self.url_entry.get()
        quality = self.quality_var.get()
        download_directory = filedialog.askdirectory()  

        if not download_directory:
            self.status_label.config(text="Download cancelled.", fg='white')
            return

        try:
            yt = YouTube(url)
            stream = yt.streams.filter(res=quality).first()
            stream.download(output_path=download_directory)
            self.status_label.config(text="Download successful!", fg='#33ff33')
        except Exception as e:
            self.status_label.config(text=f"Error: {str(e)}", fg='#ff3333')

def main():
    root = tk.Tk()
    app = YouTubeDownloader(root)
    root.mainloop()

if __name__ == "__main__":
    main()
