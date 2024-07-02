#!/usr/bin/env python3

#############################################################
#                                                           #
# File created by 0hStormy                                  #
#                                                           #
#############################################################

# Packages
from colorama import Fore, Back, Style
import os
import platform
import time
import subprocess
import json


# Variables
listItem = 0
lines = []

# Determine clear command
if platform.system() == 'Windows':
    clearCMD = 'cls'
else:
    clearCMD = 'clear'

# cls Screen
os.system(clearCMD)

# Functions ↓

# Make config
def makeConfig():
    configcontents = {
        "DefaultTextEditor": "vim",
        "DefaultShell": "bash",
        
        "NerdFontIcons": False,

        "AudioPlayer": "vlc",

        "DownloadsFolder": "@HOME/Documents/",
        "ProgramFiles": "rift/"
    }

    cfgdump = json.dumps(configcontents, indent=4)
    f = open("rift/config.json", "w+")
    f.write(cfgdump)
    f.close()

# Load config
def loadConfig():
    f = open("rift/config.json", "r")
    tmp_j = f.read()
    cfginfo = json.loads(tmp_j)

    global DefaultTE
    global DefaultShell
    global DownloadsFolder
    global ProgramFiles
    global NerdFontIcons
    DefaultTE = (cfginfo['DefaultTextEditor'])
    DefaultShell = (cfginfo['DefaultShell'])
    DownloadsFolder = (cfginfo['DownloadsFolder'])
    ProgramFiles = (cfginfo['ProgramFiles'])
    NerdFontIcons = (cfginfo['NerdFontIcons'])

    if '@HOME' in DownloadsFolder:
        DownloadsFolder = DownloadsFolder.replace('@HOME', os.path.expanduser('~'))
    
# File lister
def refresh():
    
    os.system(clearCMD)
    
    repoFileExists()
    
    # Get terminal size
    terminalY = os.get_terminal_size().lines
    terminalX = os.get_terminal_size().columns
    int(terminalX)
    int(terminalY)
    
    with open(f'{ProgramFiles}/repo.rift', 'r') as f:
        lines = len(f.readlines())
        lines = str(lines)
        
    print(Fore.BLACK + Back.LIGHTBLUE_EX + "EDITOR MODE", Back.LIGHTGREEN_EX, lines + " files available", Back.RED, Fore.WHITE + "Type exit to close", Back.WHITE, Style.DIM)
    print(Style.RESET_ALL + "-" * (terminalX - 2))
    lines = int(lines)
    
    with open(f'{ProgramFiles}/repo.rift', 'r') as f:
        file = f.readlines()
        
    # Checks if Repository is Empty
    if len(file) == 0:
        print(f'{Fore.YELLOW}Empty Repository')
        print('''Type "append" to start adding entries''')

    for i in range(lines):
        fileList = file[i]
        fileItem = fileList.split(';')
        fileItem = fileItem[0].replace('\n', '')
        
        if i == listItem:
            try:
                global fileURL
                fileList = fileList.split(';')
                fileURL = fileList[1]
                fileURL = fileURL.replace('\n', '')
            except IndexError:
                fileURL = ''
                fileItem = ''

            # Checks for content invalid data
            if fileItem == '':
                print(f'{Fore.GREEN}{str(i + 1)}: ---')
            
            
            print(f'{str(i + 1)}:{Fore.GREEN} {fileItem} [{nerdFontGrabber(os.path.basename(fileURL))}]{Back.WHITE}')

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
        # Exit
        elif command == 'exit':
            os.system(clearCMD)
            exit(0)
        # Refresh
        elif command == 'rf':
            refresh()
        # Config
        elif command == 'conf':
            subprocess.run([DefaultTE, f'{ProgramFiles}/config.json'])
            loadConfig()
            refresh()
        # Append
        elif command == 'append':
            nameInput = input('Label: ')
            urlInput = input('Download Link: ')
            with open(f'{ProgramFiles}/repo.rift', 'a') as repoFile:
                repoFile.write(f'\n{nameInput};{urlInput}')
            refresh()
        # Delete
        elif command == 'del':
            indexInput = input('Index: ')
            with open(f'{ProgramFiles}/repo.rift', 'r') as repoFile:
                lines = repoFile.readlines()
            # iterate each line
            with open(f'{ProgramFiles}/repo.rift', 'w') as repoFile:
                for delIndex, line in enumerate(lines):
                    if delIndex != (int(indexInput) - 1):
                        repoFile.write(line)
            refresh()

        else:
            # Shell
            try:
                sh = command.split()
                if len(sh) == 1:
                    if sh[0] == 'sh':
                        subprocess.run(DefaultShell)
                        refresh()
                    else:
                        print(f'{Fore.YELLOW}Invalid Command{Style.RESET_ALL}')

                elif sh[0] == 'sh':
                    sh.pop(0)
                    subprocess.run(sh)
                    refresh()
            except IndexError:
                print(f'{Fore.YELLOW}Invalid Command{Style.RESET_ALL}')
            
        time.sleep(0.1)    
        
# Repo file checker
def repoFileExists():
     if os.path.isfile(f'{ProgramFiles}/repo.rift') is False:
        uhohCrash('Repo file is missing (Could have been deleted)')

# Crash
def uhohCrash(error):
    print(Fore.RED + 'Rift has errored! Error: ' + error)
    time.sleep(3)

# Grab Nerd Font Icon
def nerdFontGrabber(fileEx):
    if not NerdFontIcons:
        return ''

    f = open("rift/fileicons.json", "r")
    nerd_json = f.read()
    iconList = json.loads(nerd_json)

    try:
        returnIcon = (iconList[fileEx[fileEx.find('.'):]])
    except KeyError:
        returnIcon = (iconList['fallback'])
    return returnIcon

    
# Checks if config file exists
if os.path.isfile('rift/config.json') is False:
    makeConfig()

# Load Config
loadConfig()

# Run Repo Lister and Key Listener
refresh()
keyListener()