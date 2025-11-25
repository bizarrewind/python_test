import os
from concurrent.futures import ThreadPoolExecutor

import yt_dlp

# configuration
max_parallel_videos = 3  # how many videos ot downolad at once
aria_conns = 8  # how many chunks per video


def download_video(url):
    print(f"Starting [Aria2c]:{url}")
    opts = {
        "format": "bestvideo+bestaudio/best",
        "external_downloader": "aria2c",
        # Arguments to pass to aria2c:
        # -x 8: Max 8 connections
        # -s 8: Split files into 8 pieces
        # -k 1M: Min split size 1 M
        "external_downloader_args": [f"-x{aria_conns}", f"-s{aria_conns}", f"-k1M"],
        "outtmpl": "%(title)s.%(ext)s",
        "quiet": True,  # keep terminal clean
        "no_warnings": True,
    }
    try:
        with yt_dlp.YoutubeDL(opts) as ydl:
            ydl.download([url])
        return f"Finished Downloading {url}"
    except Exception as e:
        return f"Error {url}| {e}"


if __name__ == "__main__":
    print("Youtube Downloader (Python + Aria2c)")
    raw_input = input("Paste URLs (space separated)")
    if not raw_input.strip():
        print("No url Provided")
        exit()
    urls = raw_input.split(" ")
    # thread pool to manage videos
    # Also manage aria2 subprocess
    with ThreadPoolExecutor(max_workers=max_parallel_videos) as executor:
        results = executor.map(download_video, urls)

        for result in results:
            print(result)
    print("All Downloads Complete")
