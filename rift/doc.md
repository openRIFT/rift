# Home

Welcome to the RIFT documentation, here you will find how to use the program, and how to create your very own repository! Ready?

## Table of Contents

* Home: Starting place and Table of Contents
* Dependencies: What you need before you start
* Introduction: Learn the basics
* Repositories: Learn how to make a repo

# Dependencies

You may skip this if you are reading this in the program.

Before you start, you will need a couple things installed:

* Python 3+ (No Python 2 support)
* Colorama (Installed automatically with `run.sh`)
* Windows or Linux (No offical MacOS support currently)

Once you have all of those, you can start using RIFT!

# Introduction

To start, you're probably here because you don't know how to do anything. Don't worry, this guide will teach you all the basics of how to use RIFT. From how to download your first file to navagating RIFT.

You'll see something like this

`Welcome to RIFT [VERSION]`
`Please provide file repo:`

If you need an example, try `0hstormy.github.io` and press enter.

Now that you're in the main part of the program, here are the follow commands that are available to use.

### Commands

* i: Choose a file to download
* dl: Downloads the chosen file
* exit: Exits the program
* rf: Refreshs the screen
* conf: Edit config file, Vim is the default editor (Built-in interface planned)
* edit: Enters the repostiory editor
* play: Plays a specified file or the last file you downloaded (VLC used by default)
* about: Shows README.md file
* help: Shows this documentation

# Repositories

So, you want to create a repository now huh? Well you're in luck because creating file repositories in RIFT is pretty simple, there are 2 ways to do it currently. You can use the in-built editor, or edit a `repo.rift` file manually.

## Built-in edtior

Using the built-in editor is very simple, open up rift, you can either clear out your current `repo.rift` file or you can simply just work off the on you last opened by typing `local` into the URL input. From there you can just type `edit` and it will open up the editor mode. Use `append` to create a new entry, or use `del` to remove an entry at a specific index. All download URL's must be direct file downloads.

### Editor specifc commands

* append: creates a new repository entry
* del: removes an entry at a specific index

## Manually editing

You may choose the manually edit the `repo.rift` file, this way isn't reccomend but is possible. First, you want find where RIFT is installed, then go into the `rift/` folder, there you will find `repo.rift`. You want to open the file and clear it out. After that you can add entries like this: `[LABEL];[URL]`. All download URL's must be direct file downloads.

*RIFT documentation created by 0Stormy 7/21/24*