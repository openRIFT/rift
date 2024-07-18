#!/usr/bin/env python3

#############################################################
#                                                           #
# File created by 0hStormy                                  #
#                                                           #
#############################################################

# Packages
from colorama import Style

# Parse
def parseMD():
    # Opens Markdown file
    with open('README.md', 'r') as md:
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

            else:
                 mdOut = f'{Style.RESET_ALL}{line}'

            mdOut = mdOut.replace('\n', '')

            print(f'{mdOut}{Style.RESET_ALL}')

parseMD()
