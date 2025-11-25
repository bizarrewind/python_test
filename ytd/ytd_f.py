import os
from concurrent.futures import ThreadPoolExecutor
from itertools import repeat

import yt_dlp

max_downloads = 3
aria_conns = 8


def get_opts(mode):
    opts ={

        "playlist_items":"1-20",
        "external_downloader":"aria2c",
        "external_downloader_args":[f"-x{aria_conns}",f"-s{aria_conns}",f"-k1M"],
        'quiet':True,
        'no_warnings':True
    }
    if mode =="audio":
        opts.update({
        'format': 'bestaudio[acodec=opus]/bestaudio',
        'outtmpl':'%(title)s.opus',
        })
    elif mode =="video":
        opts.update({
        "format":"bestaudio+bestvideo/best",
        "outtmpl":'%(title)s.%(ext)s',
        })
    return opts

def download_from(url,mode):
    print(f"Starting Download:{url}")
    opts=get_opts(mode)
    try:
        with yt_dlp.YoutubeDL(opts) as ydl:
            ydl.download([url])
        return f"Finished {url}"
    except Exception as e:
        return f" Error {url} | {e}"

if __name__ == "__main__":
    print("Youtube Downloader")
    x = input("Audio/Video (a/v): ").strip().lower()
    mode = "video" if x == 'v' else "audio"
    print("Selected Mode = }",mode.upper())

    url_list=[]
    try:
        while True:
            url= input("Enter URL:")
            try:
                with yt_dlp.YoutubeDL(action[mode]()) as ydl:
                    info = ydl.extract_info(url, download=False,process = False)

                    if info.get('_type')=='playlist':
                        print("Playlist Info: ")
                        entries = list(info['entries'])
                        max_entries = 20
                        for i,video in enumerate(entries[:max_entries],start=1):
                        #for i,video in enumerate(info['entries'],start=1):
                            print(f"{i}.Title:{video.get('title')} || Length:{video.get('duration')}")

                    else:
                        print(f" Title :{info.get('title')}")
                        print(f" Codec :{info.get('acodec')},{info.get('vcodec')}")
                        #print("Uploader:", info.get('uploader'))
                        #print("Duration (seconds):", info.get('duration'))
                        #print("Available formats:")
                        #for f in info.get('formats', []):
                        #    print(f" - {f['format_id']} : {f['ext']} : {f.get('resolution') or f.get('height')}p")
            except Exception as e:
                print(f"Error Fetching Details | {e}")

            url_list.append(url)

            x=input("Continue(y/n/e/r) :").strip()
            if x == 'n':
                break
            elif x == 'e':
                exit(1)
            elif x=='r':
                url_list = []
                print("Url List Cleared")
                continue

        for url in url_list:
            print(url)

        input("Press any key to continue downloading.......")

        with ThreadPoolExecutor(max_workers=max_downloads) as executor:

            result_list = executor.map(download_from,url_list,repeat(mode))
            for result in result_list:
                print(result)
            print("All Download Complete")

    except Exception as KeyboardInterrupt :
        print(" force stopped by User ")


