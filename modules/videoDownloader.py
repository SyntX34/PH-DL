LICNECE = """
Copyright © 2021 Drillenissen#4268 - logicguy.mailandcontact@gmail.com
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

__version__ = "1.1"
__author__ = "Drillenissen#4268"

import modules.utilities as utilities
import yt_dlp
import os
import shutil
from pynotifier import Notification

def sanitize_filename(filename):
    """Remove invalid characters from filename"""
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        filename = filename.replace(char, '_')
    filename = filename.strip()
    return filename

def download_video(url):
    """Download video using yt-dlp with better error handling and bypass options"""
    try:
        ydl_opts = {
            'outtmpl': 'Video Downloads/%(uploader)s - %(title)s - %(id)s.%(ext)s',
            'progress_hooks': [progress_hook],
            'quiet': True,
            'no_warnings': True,
            'extract_flat': False,
            'ignoreerrors': True,
            'no_color': True,
            'geo_bypass': True,
            'no_check_certificate': True,
            'retries': 5,
            'fragment_retries': 10,
            'http_chunk_size': 1024 * 1024,
            'format': 'bestvideo+bestaudio/best',
            'merge_output_format': 'mp4',
            'writethumbnail': False,
            'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
            'socket_timeout': 30,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(" [+] Extracting video information...")

            try:
                info = ydl.extract_info(url, download=False)
                if info is None:
                    raise Exception("Could not extract video information - the video may be unavailable or the site's structure has changed.")
                
                print(f" [+] Found: {info.get('title', 'Unknown title')}")
                
                if 'formats' in info:
                    print(" [!] Available formats:")
                    for fmt in info['formats']:
                        print(f"  - {fmt['format_id']} ({fmt['ext']}, {fmt.get('vcodec', 'No video codec')}, {fmt.get('acodec', 'No audio codec')})")

                print(" [+] Starting download...")
                result = ydl.extract_info(url, download=True)

                if result is None:
                    raise Exception("Download failed")

                return result
            except yt_dlp.utils.DownloadError as e:
                error_msg = str(e)
                if 'HTTP Error 410' in error_msg or '410' in error_msg:
                    print(f" [!] HTTP 410 Error: This video has been removed or is no longer available.")
                    print(f" [!] The video may no longer exist on the source website.")
                else:
                    print(f" [!] Download error: {error_msg}")
                return None
            except Exception as e:
                print(f" [!] Error during extraction: {str(e)}")
                return None
    except Exception as e:
        print(f" [!] Download error: {str(e)}")
        return None

def progress_hook(d):
    """Display download progress"""
    if d['status'] == 'downloading':
        if '_percent_str' in d:
            percent = d['_percent_str'].strip()
            print(f" [+] Downloading... {percent}", end='\r')
    elif d['status'] == 'finished':
        print("\n [+] Download complete, now processing...")

def main():
    utilities.clear()
    url = input(" [?] Video URL: ").strip()

    if not url:
        print(" [!] No URL provided!")
        input("\n [!] Press enter to continue...")
        return

    print("\n [+] Starting download process...\n")

    result = download_video(url)
    
    if result is None:
        print("\n [!] Failed to download video!")
        input("\n [!] Press enter to continue...")
        return

    uploader = sanitize_filename(result.get('uploader', 'Unknown'))
    title = sanitize_filename(result.get('title', 'Unknown'))
    video_id = result.get('id', 'unknown')
    ext = result.get('ext', 'mp4')

    base_filename = f"{uploader} - {title} - {video_id}"
    downloaded_video_file = None

    video_downloads_dir = "Video Downloads/"
    if os.path.exists(video_downloads_dir):
        for file in os.listdir(video_downloads_dir):
            if file.startswith(base_filename) and (file.endswith(".mp4") or file.endswith(".webm")):
                downloaded_video_file = os.path.join(video_downloads_dir, file)

    if downloaded_video_file is None:
        print("\n [!] Could not locate video file!")
        input("\n [!] Press enter to continue...")
        return

    try:
        Notification(
            title='Download Complete',
            description=f'Finished downloading: {title[:50]}...',
            duration=5,
            urgency='normal'
        ).send()
    except:
        pass

    print(f"\n\n [+] Finished downloading: {title}")
    
    while True:
        inp = input("\n [?] Do you want to keep the video? (Y/n): ").strip().lower()
        if inp in ['', 'y', 'yes', 'n', 'no']:
            break
        print(" [!] Please answer with Y or N")

    if inp in ['', 'y', 'yes']:
        utilities.display_categories()  # Show the available categories to the user
        
        while True:
            category = input("\n [?] Category: ").strip()
            
            if not category:
                print(" [!] Category cannot be empty!")
                continue
                
            category_path = f"Videos/{category}"

            if not os.path.exists(category_path):
                inp = input(f" [?] Create new category '{category}'? (Y/n): ").strip().lower()
                if inp in ['', 'y', 'yes']:
                    try:
                        os.mkdir(category_path)
                        print(f" [+] Created category '{category}'")
                        break
                    except Exception as e:
                        print(f" [!] Failed to create category: {str(e)}")
                        continue
            else:
                break

        try:
            dest_filename = os.path.basename(downloaded_video_file)
            dest_path = os.path.join(category_path, dest_filename)

            if os.path.exists(dest_path):
                base, ext = os.path.splitext(dest_path)
                counter = 1
                while os.path.exists(f"{base}_{counter}{ext}"):
                    counter += 1
                dest_path = f"{base}_{counter}{ext}"

            shutil.move(downloaded_video_file, dest_path)
            print(f" [+] Video saved to: {dest_path}")

            # try:
            #     os.remove(downloaded_video_file)
            #     print(" [+] Removed from downloads folder")
            # except Exception as e:
            #     print(f" [!] Failed to remove file from downloads folder: {str(e)}")

        except Exception as e:
            print(f" [!] Failed to move video to category: {str(e)}")
            inp = input(" [?] Keep the file in downloads folder? (Y/n): ").strip().lower()
            if inp not in ['', 'y', 'yes']:
                try:
                    os.remove(downloaded_video_file)
                    print(" [+] Removed from downloads folder")
                except Exception as e:
                    print(f" [!] Failed to remove file: {str(e)}")

    else:
        try:
            os.remove(downloaded_video_file)
            print(" [+] Video deleted from downloads folder")
        except Exception as e:
            print(f" [!] Failed to delete video: {str(e)}")

    input("\n [!] Press enter to continue...")