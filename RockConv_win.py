import os
import time

def ffmpeg_check():
    os.system('cls')
    while True:
        global ffmpeg_dir
        ffmpeg_dir = input('enter the directory containing ffmpeg.exe\n'
        '(ensure when entering any directories use "\\" NOT "/")\n'
        '>>')
        ffmpeg_check = os.system(f'cd {ffmpeg_dir}\\')
        if ffmpeg_check == 1:
            print('ffmpeg NOT found!')
            time.sleep(5)
            exit()
        else:
            print('ffmpeg found!\n')
            break
        
def main():
    os.system(f'cd {ffmpeg_dir}')
    conv_dir = input('in-dir>>')
    file_format = input('in-format>>')
    os.system(f'mkdir {conv_dir}\\converted')
    os.system(f'for %a in ("{conv_dir}\\*.{file_format}") do ffmpeg -i "%a" -s 320x240 -vcodec mpeg2video -b:v 400k -ab 200k -ac 2 -ar 44100 -acodec mp3 "{conv_dir}/converted\%~na.mpg"')
    print('\nconversion done!')

ffmpeg_check()
main()
