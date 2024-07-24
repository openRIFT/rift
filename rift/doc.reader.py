#!/usr/bin/env python3

#############################################################
#                                                           #
# File created by 0hStormy                                  #
#                                                           #
#############################################################

# Packages
from colorama import Style
import json

# Load config
def loadConfig():
    f = open("rift/config.json", "r")
    tmp_j = f.read()
    cfginfo = json.loads(tmp_j)

    global ProgramFiles
    ProgramFiles = (cfginfo['ProgramFiles'])

# Parse
def parseMD():
    # Opens Markdown file
    with open(f'{ProgramFiles}/doc.md', 'r') as md:
        mdLines = md.readlines()

        # Checks each line for markdown
        for line in mdLines:
            mdOut = line
            if line.startswith('# '): # Bold Purple
                mdOut = line.replace('# ', '\033[1m' + '\033[95m')

            elif line.startswith('## '): # Bold Aqua
                mdOut = line.replace('## ', '\033[1m' + '\033[96m')

            elif line.startswith('### '): # Bold
                mdOut = line.replace('### ', '\033[1m')

            elif line.startswith('**'): # Also Bold
                mdOut = line.replace('**', '\033[1m')

            elif line.startswith('*'): # Remove italics as they're not supported by Windows
                mdOut = line.replace('*', '')

            elif line.startswith('* '):
                mdOut = line.replace('* ', ' *')
            
            elif line.startswith('!['): # Any images
                mdOut = line.replace(line, '[image]')

            else:
                 mdOut = f'{Style.RESET_ALL}{line}'

            mdOut = mdOut.replace('\n', '')

            print(f'{mdOut}{Style.RESET_ALL}')

loadConfig()
parseMD()
