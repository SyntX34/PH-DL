LICENSE = """
Copyright © 2021 Drillenissen#4268 - logicguy.mailandcontact@gmail.com
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

__version__ = "1.1"
__author__  = "Drillenissen#4268"

import modules.utilities as utilities
import os
import shutil
import time

def add_cat():
    """Add a new category"""
    name = input("\n [?] Name: ").strip()
    
    if not name:
        print(" [!] Category name cannot be empty")
        time.sleep(1)
        return
    
    path = f"Videos/{name}"
    
    if os.path.exists(path):
        print(f" [!] Category '{name}' already exists")
        time.sleep(1)
        return
    
    os.mkdir(path)
    print(f" [+] Created category '{name}'")
    time.sleep(1)

def del_cat():
    """Delete a category"""
    name = input("\n [?] Category name: ").strip()
    
    if not name:
        print(" [!] Category name cannot be empty")
        time.sleep(1)
        return
    
    path = f"Videos/{name}"
    
    if not os.path.exists(path):
        print(f" [!] Category '{name}' does not exist")
        time.sleep(1)
        return
    
    # Check if directory is empty
    if os.listdir(path):
        print(f" [!] Category '{name}' is not empty")
        inp = input(" [?] Delete all files in this category? (y/N) ")
        if "y" in inp.lower():
            shutil.rmtree(path)
            print(f" [!] Removed '{name}' and all its contents")
        else:
            print(" [-] Canceled")
    else:
        inp = input(f" [!] Are you sure you want to remove '{name}'? (Y/n) ")
        if "y" in inp.lower() or inp == "":
            os.rmdir(path)
            print(f" [!] Removed '{name}'")
        else:
            print(" [-] Canceled")
    
    time.sleep(1)

def mer_cat():
    """Merge two categories"""
    name1 = input("\n [?] Category name 1 (source): ").strip()
    name2 = input(" [?] Category name 2 (destination): ").strip()
    
    if not name1 or not name2:
        print(" [!] Category names cannot be empty")
        time.sleep(1)
        return
    
    path1 = f"Videos/{name1}"
    path2 = f"Videos/{name2}"
    
    if not os.path.exists(path1):
        print(f" [!] Source category '{name1}' does not exist")
        time.sleep(1)
        return
    
    if not os.path.exists(path2):
        inp = input(f" [?] Destination category '{name2}' doesn't exist. Create it? (Y/n) ")
        if "y" in inp.lower() or inp == "":
            os.mkdir(path2)
        else:
            return
    
    print(" [+] Started processing, stand by\n")
    
    ka = False  # Keep Always
    sa = False  # Skip Always
    
    files = os.listdir(path1)
    
    for i in files:
        source = os.path.join(path1, i)
        
        # Skip if it's a directory
        if os.path.isdir(source):
            continue
            
        destination = os.path.join(path2, i)
        
        if ka:
            shutil.copy2(source, destination)
            print(f" [+] Copied: {i}")
        elif sa and os.path.exists(destination):
            print(f" [-] Skipped: {i}")
            continue
        elif os.path.exists(destination):
            print(f"\n [!] Conflict: {i} already exists at destination")
            inp = input(" (K)eep, (S)kip, (KA) Keep Always, (SA) Skip Always: ")
            
            if inp.lower() == "s":
                print(f" [-] Skipped: {i}")
                continue
            elif inp.lower() == "k":
                shutil.copy2(source, destination)
                print(f" [+] Copied: {i}")
            elif inp.lower() == "ka":
                ka = True
                shutil.copy2(source, destination)
                print(f" [+] Copied: {i} (Keep Always enabled)")
            elif inp.lower() == "sa":
                sa = True
                print(f" [-] Skipped: {i} (Skip Always enabled)")
            else:
                print(" [!] Invalid option, skipping")
        else:
            shutil.copy2(source, destination)
            print(f" [+] Copied: {i}")
    
    print(f"\n [+] Merge completed. {len(files)} files processed.")
    time.sleep(1)

def ren_cat():
    """Rename a category"""
    name1 = input("\n [?] Current category name: ").strip()
    name2 = input(" [?] New category name: ").strip()
    
    if not name1 or not name2:
        print(" [!] Category names cannot be empty")
        time.sleep(1)
        return
    
    path1 = f"Videos/{name1}"
    path2 = f"Videos/{name2}"
    
    if not os.path.exists(path1):
        print(f" [!] Category '{name1}' does not exist")
        time.sleep(1)
        return
    
    if os.path.exists(path2):
        print(f" [!] Category '{name2}' already exists")
        time.sleep(1)
        return
    
    shutil.move(path1, path2)
    print(f" [+] Renamed '{name1}' to '{name2}'")
    time.sleep(1)

def main():
    utilities.clear()
    
    print(" [+] Current categories\n")
    utilities.display_categories(aditionalInfo=False)
    print()
    
    print(""" [1] Add category     [2] Remove category
 [3] Merge category   [4] Rename category
 [5] Back to main menu""")
    
    inp = input("\n>>> ").strip()
    
    if inp == "1":
        add_cat()
    elif inp == "2":
        del_cat()
    elif inp == "3":
        mer_cat()
    elif inp == "4":
        ren_cat()
    elif inp == "5":
        return
    else:
        print(" [!] Invalid option")
        time.sleep(1)