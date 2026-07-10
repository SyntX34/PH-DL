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
from yt_dlp.networking.impersonate import ImpersonateTarget
import os
import shutil
import traceback
from pynotifier import Notification

def sanitize_filename(filename):
    """Remove invalid characters from filename"""
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        filename = filename.replace(char, '_')
    filename = filename.strip()
    return filename

def check_curl_cffi():
    """Check if curl-cffi is available for impersonate feature"""
    try:
        import curl_cffi
        return True
    except ImportError:
        return False

def download_video(url):
    """Download a video using yt-dlp."""
    try:
        ydl_opts = {
            "impersonate": ImpersonateTarget.from_str("chrome"),
            "no_cookies": True,
            "outtmpl": "Video Downloads/%(uploader)s - %(title)s - %(id)s.%(ext)s",
            "format": "bestvideo+bestaudio/best",
            "merge_output_format": "mp4",
            "progress_hooks": [progress_hook],
            "concurrent_fragment_downloads": 16,
            "retries": 10,
            "fragment_retries": 10,
            "socket_timeout": 30,
            "buffersize": 1024 * 1024,
            "geo_bypass": True,
            "quiet": False,
            "no_warnings": False,
        }
        print(" [+] Starting download...")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            result = ydl.extract_info(url, download=True)
        if result is None:
            raise Exception("Download failed.")
        print(f"\n [+] Finished downloading: {result.get('title', 'Unknown title')}")
        return result
    except yt_dlp.utils.DownloadError as e:
        error = str(e)
        if "410" in error:
            print(" [!] HTTP 410: The video has been removed or is no longer available.")
        elif "403" in error:
            print(" [!] HTTP 403: Access denied.")
        else:
            print(f" [!] yt-dlp error: {error}")
        return None
    except Exception as e:
        print(f" [!] Download error: {e}")
        traceback.print_exc()
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