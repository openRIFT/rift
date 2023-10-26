# makegui.py

# Packages
import os
import webbrowser
    
 # Open html file   
htmlF = open('assets/html/repo.html', 'w+')

# Write first block of code
htmlF.write("""
<!DOCTYPE html>
<!--[if lt IE 7]>      <html class="no-js lt-ie9 lt-ie8 lt-ie7"> <![endif]-->
<!--[if IE 7]>         <html class="no-js lt-ie9 lt-ie8"> <![endif]-->
<!--[if IE 8]>         <html class="no-js lt-ie9"> <![endif]-->
<!--[if gt IE 8]>      <html class="no-js"> <!--<![endif]-->
<html>
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title></title>
        <meta name="description" content="">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="../css/styling.css">
    </head>
    <body>
        <!--[if lt IE 7]>
            <p class="browsehappy">You are using an <strong>outdated</strong> browser. Please <a href="#">upgrade your browser</a> to improve your experience.</p>
        <![endif]-->
        
        <div class="titleBar">
            <h1>RIFT</h1>
            <button class="github" onclick="window.location.href='https://github.com/Kinda-Stormy/RIFT';"><img width="58px" src="../images/github-mark-white.svg"></button>
        </div>
""")

# Open repo.rift
repoF = open("repo.rift", 'r')
lines = len(repoF.readlines())
lines = str(lines)
lines = int(lines)

with open('repo.rift', 'r') as repoF:
    app = repoF.readlines()
    
print()

# Write App list    
for i in range(lines):
    appList = app[i]
    appItem = appList.split(';')
    appURL = appItem[1].replace('\n', '')    
    appItem = appItem[0].replace('\n', '')
    
    htmlF.write("""<div class="content"><div class="file"><h1>""" + appItem + """</h1> <button onclick="window.location.href='""" + appURL + """'"><img src="../images/download.svg"></button></div></div>""")

# Write last block of code            
htmlF.write("""

    </body>
</html>            
""")

# Close Files
htmlF.close()
repoF.close()

# Open webbrowser
webbrowser.open(os.getcwd() + '/assets/html/repo.html')