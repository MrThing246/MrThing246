###-----IMPORTANT-----###
#This is my first program. Use at your own discretion 
#This script is intended to delete files parsed from badsongs.txt. It shouldn't delete other files, but the coding instructions will delete the files that it's fed. Be careful
#
#This script only works if badsongs.txt is in the same directory as your songs. 
#I ran into an issue with badsongs.txt being generated by ScoreSpy while my songs were located in the Clone Hero directory. 
#I probably won't fix it. This script was successful enough to clean my bad songs, which is all I wanted


import os
import shutil

def del_dir(path): 
    try:
        os.path.exists(path)
    except FileNotFoundError as err: 
        print(f'File does not exist at \'{path}\' \nSystem error: {err}')
        return
    else:
        shutil.rmtree(path)
        print(f'Deleted file at \'{path}\'') 
        return
    finally:
        return

while 1 == 1: #While loop to handle user input. Detects (1) if folder exists and (2) if directory contains badsongs.txt. If both are true, then the loop breaks and the program continues

    badsongs_dir = input('Type \'quit\' to exit the program.\nThis program is intended to remove duplicate songs files inside if your Clone Hero directory. \nPlease enter the full path of your badsongs.txt file. This can be located in the main directory of Clone Hero: \n') 
    if badsongs_dir.lower() == 'quit':
        break 
    
    if os.path.exists(badsongs_dir) == False: 
        print(f'\nDirectory does not exist: \'{badsongs_dir}\' \n') 
        continue
    elif 'badsongs.txt' not in badsongs_dir: 
        print(f'\nCould not find \'badsongs.txt\' \n')
        continue

    break

input(f'\n\'badsongs.txt\' found in {badsongs_dir}. Press Enter to continue\n') #Input does not do anything. It's just to pause the program to verify that the given directory is correct 

with open(badsongs_dir, encoding = "utf8") as badsongs: #Opens badsongs.txt. badsong_lines saves each line as a unique string, then badsong_lines_stripped removes '\n' from each entry in original list
    badsong_lines = badsongs.readlines()
    badsong_lines_stripped = [line.strip('\n') for line in badsong_lines]

songs_to_delete = badsong_lines_stripped[badsong_lines_stripped.index('ERROR: These folders have no notes.mid or notes.chart files!'):] #badsongs.txt contains different error codes. This locates the first error where song folders have missing files. new_list = old_list[(index of 'error') -> and beyond]

ch_dir = badsongs_dir[:badsongs_dir.find('\\badsongs.txt')].lower() #i.e. c:\program files\clone hero

badsongs_fixed = [] #Duplicate songs in badsongs.txt have an addendum in parentheses to show where the other song file is. This for loop deletes the content in parentheses and returns the string containing only a directory with the bad song 
for dir in songs_to_delete:
    if f' ({ch_dir}' in dir: 
        badsongs_fixed.append(dir[:dir.find(f' ({ch_dir}')])
    else: 
        badsongs_fixed.append(dir)

badsongs_count = [os.path.exists(dir) for dir in badsongs_fixed]

for song in badsongs_fixed:
    del_dir(song)

print(f'Approximately {badsongs_count.count(True)} out of {len(badsongs_count)} songs deleted')




