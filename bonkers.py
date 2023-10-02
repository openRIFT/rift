# bonk.py

# Packages
from colorama import Fore, Back, Style
import requests
import os
import keyboard
import cursor
import time

# Variables
listItem = 0

# Clear Screen
os.system('cls')

# Functions
def welcomeScreen():
    print(Back.MAGENTA + "Welcome to bonk v0.1.0")
    print(Style.RESET_ALL)
 
# Bonk downloader    
def downloadBonkAppList():
    global bonkURL
    bonkURL = input("Provide a file repo: ")
    os.system('cls')
    print(Fore.YELLOW + 'Loading...')
    r = requests.get(bonkURL, allow_redirects=True)
    open('list.bal', 'wb').write(r.content)
    
# Bonk list
def bonkLister():
    
    os.system('cls')
    
    with open('list.bal', 'r') as f:
        lines = len(f.readlines())
        lines = str(lines)
        
    print(Back.LIGHTGREEN_EX, Fore.BLACK + lines + " files available", Back.RED, Fore.WHITE + "ESC to close", Back.YELLOW, Fore.BLACK + bonkURL, Style.RESET_ALL)
    print(Style.RESET_ALL + "--------------------")
    lines = int(lines)
    
    with open('list.bal', 'r') as f:
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
            print(Fore.GREEN + appItem)
            
        else:
            print(Style.RESET_ALL + appItem)
            
    print(Style.RESET_ALL + "--------------------")
    cursor.hide()
            
# Bonk key listener        
def bonkKeyListener():
    with open('list.bal', 'r') as f:
        app = f.readlines()
    
    while True:
        if keyboard.is_pressed("down"):
            global listItem
            listItem = listItem + 1
            bonkLister()
        
        if keyboard.is_pressed("up"):
            listItem = listItem - 1
            bonkLister()
            
        if keyboard.is_pressed("enter"):
            print(Fore.MAGENTA + 'Downloading...')
            appName = os.path.basename(appURL)
            r = requests.get(appURL, allow_redirects=True)
            open(appName, 'wb').write(r.content)
            bonkLister()
        
        if keyboard.is_pressed("esc"):
            os.system("cls")
            exit(0)
            
        time.sleep(0.1)        
            
# Call Weclome Screen and run the Bonk downloader
welcomeScreen()
downloadBonkAppList()

# Run Bonk Lister
bonkLister()
bonkKeyListener()