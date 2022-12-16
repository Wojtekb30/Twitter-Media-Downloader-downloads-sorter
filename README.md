# Twitter-Media-Downloader-downloads-sorter (SivSort)
Program for sorting files downloaded with Twitter Media Downloader (memo.furyutei.work) into individual folders.

Created as commission for Siv. They chose the program's name (SivSort) and icon (which is Minecraft Hopper).

----------------------------------------------------------------------------

<b> What does it do?: </b>

This program reads first part of the file's name (until "-"), then (depending on settings and if such subfolder already exists in the destination) creates subfolder based on that part of the file name (it's the file author's name in case of downloads from the Twitter Media Downloader) and puts the file in it. It works until it sorts (moves into proper subfolders) all matching files from the source folder.

It sorts only jpg, png, mp4 and zip files, ignoring the rest. It also ignores a file if a file with same name already in the destination. Files without any "-" in their name are ignored too.

----------------------------------------------------------------------------

<b> How to use it?: </b>

Download the .exe or .py and run it. Follow instructions displayed in the terminal window:

First, choose folder the files to sort are in (source folder). 

Second, choose destination folder in which there are (or will be) subfolders this program will sort into (destination folder).

Then type 1 if you'd like the program to create new folders if necessary (for example if you run it for the first time). 

Confirm and wait for the program to finish.
