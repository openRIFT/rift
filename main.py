# bonk.py

# Packages
from colorama import Fore, Back, Style
import requests
import os
import keyboard
import cursor
import time
import PyQt6

# Variables
listItem = 0

# Clear Screen
os.system('cls')

# Functions ↓

# Welcome Screen
def welcomeScreen():
    print(Back.MAGENTA + "Welcome to RIFT v0.1.0")
    print(Style.RESET_ALL)
 
# Repo downloader    
def downloadBonkAppList():
    global bonkURL
    bonkURL = input("Provide a file repo: ")
    
    # If skipDownload is enabled
    if bonkURL == 'db.skip':
        print(Back.RED + 'Beware, this command can crash Bonkers!', Style.RESET_ALL)
        time.sleep(0.5)
        return
    
    # If New GUI is enabled
    if bonkURL == 'db.gui':
        global bonkersGuiEnabled
        bonkersGuiEnabled = True
        print(Back.RED + 'Beware, this command may crash Bonkers!', Style.RESET_ALL)
        time.sleep(0.5)
        return
    
    os.system('cls')
    print(Fore.YELLOW + 'Loading Repo...')
    r = requests.get(bonkURL, allow_redirects=True)
    open('userFiles/repo.rift', 'wb').write(r.content)
    
# Bonk list
def fileLister():
    
    os.system('cls')
    
    # Get terminal size
    terminalY = os.get_terminal_size().lines
    terminalX = os.get_terminal_size().columns
    int(terminalX)
    int(terminalY)
    
    with open('repo.rift', 'r') as f:
        lines = len(f.readlines())
        lines = str(lines)
        
    print(Back.LIGHTGREEN_EX, Fore.BLACK + lines + " files available", Back.RED, Fore.WHITE + "ESC to close", Back.YELLOW, Fore.BLACK + bonkURL, Style.RESET_ALL + '|')
    print(Style.RESET_ALL + "⎯" * (terminalX - 2))
    lines = int(lines)
    
    with open('repo.rift', 'r') as f:
        app = f.readlines()
        
    for i in range(lines):
        appList = app[i]
        appItem = appList.split(';')
        appItem = appItem[0].replace('\n', '')
        
        if i == listItem:
            global appURL
            appList = appList.split(';')
            appURL = appList[1]
            appURL = appURL.replace('\n', '')
            print(Fore.GREEN + appItem, Back.WHITE, Fore.MAGENTA + "")
            
        else:
            print(Style.RESET_ALL + appItem)
            
    print(Style.RESET_ALL + "⎯" * (terminalX - 2))
    
    cursor.hide()
    
# Bonk key listener        
def keyListener():
    with open('repo.rift', 'r') as f:
        app = f.readlines()
    
    while True:
        if keyboard.is_pressed("down"):
            global listItem
            listItem = listItem + 1
            fileLister()
        
        if keyboard.is_pressed("up"):
            listItem = listItem - 1
            fileLister()
            
        if keyboard.is_pressed("enter"):
            fileDownloader()
        
        if keyboard.is_pressed("esc"):
            os.system("cls")
            exit(0)
            
        time.sleep(0.1)            

# Downloads file
def fileDownloader():
    print(Fore.MAGENTA + 'Downloading...')
    appName = os.path.basename(appURL)
    r = requests.get(appURL, allow_redirects=True)
    open(appName, 'wb').write(r.content)
    fileLister()

# Call Weclome Screen and run the Bonk downloader
welcomeScreen()
downloadBonkAppList()

# Run Bonk Lister
fileLister()
keyListener()