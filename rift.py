#!/usr/bin/env python3

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
RIFTVersion = '24.7.1'
execFiles = ['.exe', 'msi', '.dmg', '.sh', '.deb', '.rpm', '.AppImage', '.flatpak', '.flatpakref', '.pkg']

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

        "ExecDownloadWarn": True,

        "DownloadsFolder": "@HOME/Downloads/",
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
    global AudioPlayer
    global ExecWarn
    DefaultTE = (cfginfo['DefaultTextEditor'])
    DefaultShell = (cfginfo['DefaultShell'])
    DownloadsFolder = (cfginfo['DownloadsFolder'])
    ProgramFiles = (cfginfo['ProgramFiles'])
    NerdFontIcons = (cfginfo['NerdFontIcons'])
    AudioPlayer = (cfginfo['AudioPlayer'])
    ExecWarn = (cfginfo['ExecDownloadWarn'])

    if '@HOME' in DownloadsFolder:
        DownloadsFolder = DownloadsFolder.replace('@HOME', os.path.expanduser('~'))

# Welcome Screen
def welcomeScreen():
    print(f'{Back.MAGENTA}Welcome to RIFT {RIFTVersion}')
    print(Style.RESET_ALL)

# Repo downloader
def downloadRIFTfileList():
    global RIFTURL
    RIFTURL = f'{input("Provide a file repo: ")}/repo.rift'

    # If skipDownload is enabled
    if RIFTURL == 'local/repo.rift':
        print(Back.RED + 'Beware, this can crash RIFT!', Style.RESET_ALL)
        time.sleep(0.5)
        return

    os.system(clearCMD)
    print(Fore.YELLOW + 'Loading Repo...')

    try:
        r = requests.get(('https://' + RIFTURL), allow_redirects=True)
        open(f'{ProgramFiles}/repo.rift', 'wb').write(r.content)
    except:  # noqa: E722
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

    with open(f'{ProgramFiles}/repo.rift', 'r') as f:
        lines = len(f.readlines())
        lines = str(lines)

    print(Back.LIGHTGREEN_EX, Fore.BLACK + lines + " files available", Back.RED, Fore.WHITE + "Type exit to close", Back.WHITE, Style.DIM)
    print(Style.RESET_ALL + "-" * (terminalX - 2))
    lines = int(lines)

    with open(f'{ProgramFiles}/repo.rift', 'r') as f:
        file = f.readlines()

    # Checks if Repository is Empty
    if len(file) == 0:
        print(f'{Fore.YELLOW}Empty Repository')
        print('''Type "edit" to edit the repository file''')

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
            else:
                print(f'{str(i + 1)}:{Fore.GREEN} {fileItem} [{nerdFontGrabber(os.path.basename(fileURL))}]{Back.WHITE}')

        else:
            print(Style.RESET_ALL + str(i + 1) + ': ' + fileItem)

    print(Style.RESET_ALL + "-" * (terminalX - 2))


# Key listener
def keyListener():
    while True:
        global commandSuccess
        commandSuccess = False
        command = input('Command: ')
        if command == 'i':
            global listItem
            indexInput = input('Index: ')
            listItem = (int(indexInput) - 1)
            refresh()
        # Download
        elif command == 'dl':
             fileDownloader()
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
        # Repo Editor Tool
        elif command == 'edit':
            subprocess.run(['python', f'{ProgramFiles}/repotool.py'])
            refresh()
        elif command == 'play':
            audioInput = input('File (Leave blank most recent download): ')
            if audioInput == '':
                subprocess.run([AudioPlayer, f'{DownloadsFolder}/{fileName}'])
            else:
                subprocess.run([AudioPlayer, audioInput])

        # External plugins
        pluginsList = os.listdir(f'{ProgramFiles}plugins/')
        for plugin in pluginsList:
            if plugin == f'{command}.py':
                subprocess.run(['python', f'{ProgramFiles}/plugins/{plugin}'])
                commandSuccess = True

        else:
            # Shell
            try:
                sh = command.split()
                if len(sh) == 1:
                    if sh[0] == 'sh':
                        subprocess.run(DefaultShell)
                        refresh()
                    else:
                        if commandSuccess is False:
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
    time.sleep(2)

# Downloads file
def fileDownloader():
    global fileName
    fileName = os.path.basename(fileURL)

    if ExecWarn is True:
        if any(ext in fileName for ext in execFiles):
            warnInput = input(f'{Fore.RED}This file could be harmful to your computer, download? RIFT IS NOT LIABLE FOR DAMAGE DONE TO YOUR COMPUTER! (y/n): {Style.RESET_ALL}')
            if warnInput == 'y':
                print('Compute safely!')
            else:
                print(f'{Fore.YELLOW}Operation Canceled{Style.RESET_ALL}')
                return
    print(Fore.MAGENTA + 'Downloading...')

    # Checks for invalid url data
    try:
        r = requests.get(fileURL)
        open(f'{DownloadsFolder}{fileName}', 'wb').write(r.content)
    except:
        uhohCrash(f'Invalid Download URL {Fore.YELLOW}{fileURL}')
    refresh()

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

# Call Weclome Screen and run the Repo downloader
loadConfig()
welcomeScreen()
downloadRIFTfileList()

# Run Repo Lister and Key Listener
refresh()
keyListener()
