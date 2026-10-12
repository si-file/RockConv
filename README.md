# RockConv
a simple video converter for rockbox ipods built in python!

# How it works:
RockConv converts all the videos in a given directory into a video format compatible for ipods with rockbox installed. all converted videos are placed in a folder named "converted" in the same directory as the original videos. its as simple as entering the directory containing ffmpeg, the directory of the target videos, and the format of the videos you want to convert!

# What I'm working on:
- windows edition: fully working, not what i'm focusing on rn
- linux edition: being currently worked on!
- macos edition: no progress yet

# Important info:

videos that RockConv outputs are confirmed to work with ipod classic 7th gens, however the command i used is an altered command straight from the rockbox wiki so this program *should* work with all compatible ipod models too!

ffmpeg is required to run this: https://ffmpeg.org/

RockConv is intended to run on windows, however altering this program to run on linux is simple. therefore, i might make a linux version of this (or feel free to fork this and make your own!)

zero gen-ai or other types of ai were used other than duck.ai for fixing an issue i had with the ffmpeg conversion command. i (myself) heavily altered what it gave me to allow it to be implemented into RockConv.

# Sources I used:
- the rockbox user manual: https://www.rockbox.org/download/data/rockbox-ipod6gmanual.pdf
- the PluginMpegplayer wiki: https://www.rockbox.org/wiki/PluginMpegplayer <-- this page is very informative about compatible formats, resolutions, etc for different players! (it is possibly a little outdated with video performance, since i have yet to encounter any frame drops below 30fps during playback)

#
enjoy! :D
