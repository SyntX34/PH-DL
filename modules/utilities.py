LICNECE = """
Copyright © 2021 Drillenissen#4268 - logicguy.mailandcontact@gmail.com
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

__version__ = "1.1"
__author__ = "Drillenissen#4268"

import os
import subprocess
import sys

def clear():
    """Clear the screen and show banner"""
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
 ██████╗ ██╗  ██╗      ██████╗ ██╗
 ██╔══██╗██║  ██║      ██╔══██╗██║
 ██████╔╝███████║█████╗██║  ██║██║
 ██╔═══╝ ██╔══██║╚════╝██║  ██║██║
 ██║     ██║  ██║      ██████╔╝███████╗
 ╚═╝     ╚═╝  ╚═╝      ╚═════╝ ╚══════╝
""")

def display_categories(additionalInfo=True):
    """Display the categories"""
    if additionalInfo:
        print("\n [+] Current categories:\n")

    try:
        categories = [f" [-] {x[0][7:]}" for x in os.walk("Videos/")][1:]
        if categories:
            print("\n".join(categories))
        else:
            print(" [-] No categories found")
    except Exception as e:
        print(f" [!] Error reading categories: {str(e)}")

    if additionalInfo:
        print("\n [+] Type any of the above (case insensitive) or a new category and it will be created for you")

def install(package):
    """Install a package using pip"""
    try:
        print(f" [+] Installing {package}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", package])
        print(f" [+] Successfully installed {package}")
        return True
    except subprocess.CalledProcessError as e:
        print(f" [!] Failed to install {package}: {str(e)}")
        return False
    except Exception as e:
        print(f" [!] Unexpected error installing {package}: {str(e)}")
        return False