from pygame import mixer
from tkinter import *
from tkinter import ttk
import random

song_menu=[]
string=0
root = Tk()
root.title("Luke's Music Player!")
root.geometry('800x500')
root['background']='#202020'

file = open('Musicplayerfiles.txt', 'r')
f = file.readlines()
file.close()
mixer.init()
time = 0
shuffleval = []

for line in f:
    song_menu.append(line[0:-1] + '.mp3')

l = Label(root, text='Music Player!')
l.pack

label=Label(root, bg=root['background'], fg='white', text='Please Select a Song')
label.pack()
u = 0
for i in song_menu:
    songlist = Label(root, bg=root['background'],fg='white',text=str(u+1) + '. ' + song_menu[u])
    songlist.pack()
    u+=1

def john():
    
    global entry
    entry1 = entry.get()
    if len(entry1) > 0:
        
        entry1 = int(entry1)
        
        label.configure(text='Now playing: ' + str(song_menu[entry1-1]))
        play(entry1)
       
def play(string):
    
    mixer.music.load(song_menu[string-1])
    mixer.music.play()   
    
def button2():
    mixer.music.pause()
def button3():
    mixer.music.unpause()
def addsongs():
    
    file = open('Musicplayerfiles.txt', 'a')
    while True:
        j = input('Please enter the title of the song: ')
        file.write(j + '\n')
        h = input('Would you like to add another song? Y for yes: ')
        if h != 'Y':
            file.close()
            file = open('Musicplayerfiles.txt', 'r')
            f = file.readlines()
            file.close()
            for line in f:
                song_menu.append(line[0:-1] + '.mp3')
            kill = input('To update song list, press enter to restart the software.')
            if kill == '':
                exit()
        else:
            continue

def deletesongs():
    delnum = input('Enter corresponding number of song you wish to remove: ')
    if delnum == 0:
        print('Error: 0 is an invalid answer')
    i = 1
    f = open('Musicplayerfiles.txt', 'r')
    lines = f.readlines()
    f.close()
        
    h = open('Musicplayerfiles.txt', 'w')
    for line in lines:
        if i == delnum:
            h.delete(line)
            song_menu.remove(i)
            i += 1
        else:
            h.write(line)
            i += 1
    h.close()
    contin = print(input('Would yosu like to delete another track? Y if yes: '))
    if contin == 'Y':
        deletesongs()
    else:
        exit()
        
    
                   

def entry_update(a):
    entry.delete(0)
    entry.insert(str(a),a)

def skip():
    if len(shuffleval)==1:
        nextsong = random.choice(song_menu)  
        mixer.music.stop()
        mixer.music.load(nextsong)
        mixer.music.play()
        label.configure(text='Now playing: ' + str(nextsong))

    elif len(shuffleval)==0:

        nextsong = int(entry.get())
        nextsong += 1
        entry_update(str(nextsong))
        mixer.music.stop()
        mixer.music.load(song_menu[nextsong-1])
        mixer.music.play()
        label.configure(text='Now playing: ' + str(song_menu[nextsong-1]))

         

def shuffle():
    if len(shuffleval)==0:
        shuffleval.append('shuffle will turn on')
        h.configure(text='Shuffle: On')
    elif len(shuffleval)==1:
        shuffleval.clear()
        h.configure(text='Shuffle: Off')


                           
entry = Entry(width=4)
entry.focus_set()
entry.pack()

a = Button(root, bg=root['background'], fg='white', text= 'Play!', command=john)
a.pack(side=TOP)


c = Button(root, bg=root['background'], fg='white', text='Pause', command=button2)
c.place(x=25,y=450) 

d = Button(root, bg=root['background'], fg='white', text='Resume', command=button3)
d.place(x=125, y=450)

e = Button(root, bg=root['background'], fg='white', text='Add Songs', command=addsongs)
e.place(x=225, y=450)

'''b = Button(root,text='Delete Songs', command=deletesongs)
b.pack(side=BOTTOM)'''

g = Button(root, bg=root['background'], fg='white', text='Skip', command=skip)
g.place(x=425, y=450)

h = Button(root, bg=root['background'], fg='white', text='Shuffle', command=shuffle)
h.place(x=550, y=450)  





root.mainloop()
