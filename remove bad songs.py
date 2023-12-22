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
        print('Error') 
        return


######Body 


#While loop to handle user input. Detects (1) if folder exists and (2) if directory contains badsongs.txt. If both are true, then the loop breaks and the program continues
while 1 == 1:

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



#Input does not do anything. It's just to pause the program to verify that the given directory is correct 
input(f'\n\'badsongs.txt\' found in {badsongs_dir}. Press Enter to continue\n') 

#Opens badsongs.txt. badsong_lines saves each line as a unique string, then badsong_lines_stripped removes '\n' from each entry in original list
with open(badsongs_dir, encoding = "utf8") as badsongs: 
    badsong_lines = badsongs.readlines()
    badsong_lines_stripped = [line.strip('\n') for line in badsong_lines]

#badsongs.txt contains different error codes. This locates the first error where song folders have missing files. new_list = old_list[(index of 'error') -> and beyond]
songs_to_delete = badsong_lines_stripped[badsong_lines_stripped.index('ERROR: These folders have no notes.mid or notes.chart files!'):]

#Returns a boolean list. Elements describe whether or not os.path.exists can detect a directory given a string element in songs_to_delete
file_exists = [os.path.exists(dir) for dir in songs_to_delete]
#print(f'{file_exists.count(True)} out of {len(songs_to_delete)} directories exist')

#Finds index value of first 'True' entry in file_exists. Indicates that the index contains a directory that exists on the computer
#Then, returns string containing file path of a valid directory 

#print(file_exists)


#Truncates valid directory path to derive the Clone Hero folder 
ch_dir = badsongs_dir[:badsongs_dir.find('\\badsongs.txt')].lower() #i.e. c:\program files\clone hero

#Duplicate songs in badsongs.txt have an addendum in parentheses to show where the other song file is. This for loop deletes the content in parentheses and returns the string containing only a directory with the bad song 
badsongs_fixed = [] 
for dir in songs_to_delete:
    if f' ({ch_dir}' in dir: 
        badsongs_fixed.append(dir[:dir.find(f' ({ch_dir}')])
    else: 
        badsongs_fixed.append(dir)

badsongs_count = [os.path.exists(dir) for dir in badsongs_fixed]
print(badsongs_count)
print(f'{badsongs_count.count(True)} out of {len(badsongs_count)} directories exist')

input() 


###Delete bad songs 

for song in badsongs_fixed:
    del_dir(song)

print(f'{badsongs_count.count(True)} out of {len(badsongs_count)} directories exist')




