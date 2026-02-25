LICNECE = """
Copyright © 2021 Drillenissen#4268 - logicguy.mailandcontact@gmail.com
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

__version__ = "Cloased Beta 1.2"
__author__ = "Drillenissen#4268"

import time

print(LICNECE)

time.sleep(1)

import os
from sys import exit
import traceback
import modules.utilities as utilities

os.system('cls' if os.name == 'nt' else 'clear')

DEBUG = True

print(" [+] Checking required folders")

if not os.path.exists("Video Downloads/") or not os.path.exists("Videos/") or not os.path.exists("Pictures/"):
    inp = input(" [!] Missing folders detected, do you wish to create the required folders? (Y/n) ")
    if "y" not in inp.lower() and inp != "":
        exit()

    for folder in ["Video Downloads", "Videos", "Pictures"]:
        if not os.path.exists(folder + "/"):
            try:
                os.mkdir(folder)
                print(f" [+] Created {folder}/ folder")
            except Exception as e:
                print(f" [!] Failed to create {folder}/: {str(e)}")
                exit()
else:
    print(" [+] Found all required folders")

packages = {
    "yt_dlp": "yt-dlp",
    "requests": "requests",
    "pynotifier": "py-notifier",
    "bs4": "beautifulsoup4"
}

print("\n [+] Checking required packages")

while True:
    try:
        import yt_dlp 
        from pynotifier import Notification
        from bs4 import BeautifulSoup
        import requests

        print(" [+] All required packages are installed")
        break
    except ImportError as e:
        error_str = str(e)
        if "No module named" in error_str:
            package = error_str.split("'")[1]
        else:
            package = error_str[17:-1] if len(error_str) > 17 else "unknown"
        
        pip_package = packages.get(package, package)
        
        inp = input(f" [!] Missing '{package}', do you wish to install {pip_package}? (Y/n) ")
        
        if "y" not in inp.lower() and inp != "":
            print(" [!] Cannot continue without required packages. Exiting...")
            exit()
        
        if utilities.install(pip_package):
            print(f" [+] Successfully installed {pip_package}")
        else:
            print(f" [!] Failed to install {pip_package}")
            exit()

print("\n [+] Loading Modules")
try:
    import modules.videoDownloader as videoDownloader
    import modules.pictureDownloader as pictureDownloader
    import modules.shuffler as shuffler
    import modules.categorieEditor as categoryEditor

    print(" [+] All modules imported successfully")
except ImportError as e:
    if DEBUG:
        exc_info = sys.exc_info()
        traceback.print_exception(*exc_info)
        del exc_info

    input(" [!] Failed loading modules, make sure you cloned all the files from the github, press enter to exit")
    exit()

modules = {
    "1": {"function": videoDownloader.main, "name": "Download Video"},
    "2": {"function": pictureDownloader.main, "name": "Download album or picture"},
    "3": {"function": shuffler.main, "name": "Shuffle / Unshuffle videos"},
    "4": {"function": categoryEditor.main, "name": "Manage categories"},
    "5": {"function": exit, "name": "Exit"}
}

while True:
    try:
        utilities.clear()

        indx = 0
        for key, val in modules.items():
            num = f"[{key}]"
            print(
                f" {num:<6} {val['name']:<{35 if int(key) < 10 else 34}}",
                end="" if indx % 2 == 0 else "\n"
            )
            indx += 1

        if indx % 2 == 1:
            print("")

        option = input("\n>>> ").strip()

        if option not in modules:
            print(" [!] Invalid option!")
            time.sleep(1)
            continue

        modules[option]["function"]()

    except KeyboardInterrupt:
        print("\n\n [!] Interrupted by user")
        break
    except Exception as e:
        print(f"\n [!] An error occurred: {str(e)}")
        if DEBUG:
            traceback.print_exc()
        input("\n [!] Press enter to continue...")