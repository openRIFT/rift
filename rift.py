#############################################################
#                                                           #
# File created by 0hStormy                                  #
#                                                           #
#############################################################

# Packages
from colorama import Fore, Back, Style
import requests
import os
import platform
import time
import subprocess
import json


# Variables
listItem = 0
RIFTVersion = '1.0-dev'

# Determine clear command
if platform.system() == 'Windows':
    clearCMD = 'cls'
else:
    clearCMD = 'clear'

# cls Screen
os.system(clearCMD)

# Functions ↓

# Load config
def loadConfig():
    f = open("assets/config.json", "r")
    tmp_j = f.read()
    cfginfo = json.loads(tmp_j)

    global DefaultTE
    global DefaultShell
    DefaultTE = (cfginfo['DefaultTextEditor'])
    DefaultShell = (cfginfo['DefaultShell'])

# Welcome Screen
def welcomeScreen():
    print(f'{Back.MAGENTA}Welcome to RIFT {RIFTVersion}')
    print(Style.RESET_ALL)

# Repo downloader    
def downloadRIFTfileList():
    global RIFTURL
    RIFTURL = input("Provide a file repo: ")
    
    # If skipDownload is enabled
    if RIFTURL == 'local':
        print(Back.RED + 'Beware, this can crash RIFT!', Style.RESET_ALL)
        time.sleep(0.5)
        return
    
    os.system(clearCMD)
    print(Fore.YELLOW + 'Loading Repo...')
    
    try:
        r = requests.get(('https://' + RIFTURL), allow_redirects=True)
        open('assets/repo.rift', 'wb').write(r.content)
    except:
        uhohCrash("Invalid URL")
    
# File lister
def refresh():
    
    os.system(clearCMD)
    
    repoFileExists()
    
    # Get terminal size
    terminalY = os.get_terminal_size().lines
    terminalX = os.get_terminal_size().columns
    int(terminalX)
    int(terminalY)
    
    with open('assets/repo.rift', 'r') as f:
        lines = len(f.readlines())
        lines = str(lines)
        
    print(Back.LIGHTGREEN_EX, Fore.BLACK + lines + " files available", Back.RED, Fore.WHITE + "Type exit to close", Style.RESET_ALL + '|')
    print(Style.RESET_ALL + "-" * (terminalX - 2))
    lines = int(lines)
    
    with open('assets/repo.rift', 'r') as f:
        file = f.readlines()
        
    for i in range(lines):
        fileList = file[i]
        fileItem = fileList.split(';')
        fileItem = fileItem[0].replace('\n', '')
        
        if i == listItem:
            global fileURL
            fileList = fileList.split(';')
            fileURL = fileList[1]
            fileURL = fileURL.replace('\n', '')
            
            # Checks for content invalid data
            if fileItem == '':
                uhohCrash('Invalid repo.rift contents (Try redownloading it?)')
            
            
            print(str(i + 1) + ': ' + Fore.GREEN + fileItem, Back.WHITE, Fore.MAGENTA + "")

        else:
            print(Style.RESET_ALL + str(i + 1) + ': ' + fileItem)
        
    print(Style.RESET_ALL + "-" * (terminalX - 2))
    
    
# Key listener        
def keyListener():
    while True:
        command = input('Command: ')
        if command == 'i':
            global listItem
            indexInput = input('Index: ')
            listItem = (int(indexInput) - 1)
            refresh()

        elif command == 'dl':
             fileDownloader()

        elif command == 'exit':
            os.system(clearCMD)
            exit(0)
        elif command == 'rf':
            refresh()
        elif command == 'conf':
            subprocess.run([DefaultTE, 'assets/config.json'])
            loadConfig()
            refresh()
        else:
            sh = command.split()
            if len(sh) == 1:
                subprocess.run(DefaultShell)
                refresh()
            elif sh[0] == 's':
                sh.pop(0)
                subprocess.run(sh)
                refresh()
            else:
                os.system(clearCMD)
                refresh()
                print(f'{Back.RED}Invalid Command{Style.RESET_ALL}')
            
        time.sleep(0.1)    
        
# Repo file checker
def repoFileExists():
     if os.path.isfile('assets/repo.rift') == False:
        uhohCrash('Repo file is missing (Could have been deleted)')

# Crash
def uhohCrash(error):
    print(Fore.RED + 'Rift has errored! Error: ' + error)
    time.sleep(3)
    
# Downloads file
def fileDownloader():
    print(Fore.MAGENTA + 'Downloading...')
    fileName = os.path.basename(fileURL)
    
    # Checks for invalid url data
    try:
        r = requests.get(fileURL)
        open(fileName, 'wb').write(r.content)
    except:
        uhohCrash(f'Invalid Download URL {Fore.YELLOW}{fileURL}')
    refresh()

# Call Weclome Screen and run the Repo downloader
loadConfig()
welcomeScreen()
downloadRIFTfileList()

# Run Repo Lister and Key Listener
refresh()
keyListener()