from pygame import mixer
from tkinter import *
from tkinter import ttk
import random

song_menu=[]
string=0
root = Tk()
root.title("Luke's Music Player!")
root.geometry('800x500')
file = open('Musicplayerfiles.txt', 'r')
f = file.readlines()
file.close()
mixer.init()
time = 0
for line in f:
    song_menu.append(line[0:-1] + '.mp3')
l = Label(root, text='Music Player!')
l.pack

label=Label(root, text='Please Select a Song')
label.pack()
u = 0
for i in song_menu:
    songlist = Label(root, text=str(u+1) + '. ' + song_menu[u])
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
        
def skip():
    nextsong = random.choice(song_menu)
    mixer.music.stop()
    mixer.music.load(nextsong)
    mixer.music.play()
    label.configure(text='Now playing: ' + str(nextsong))

def slidertext(something):
    a = float(something)
    b = round(a)
    c = str(b)
    slider_label.configure(text=c)
                           
entry = Entry(width=4)
entry.focus_set()
entry.pack()

a = Button(root, text= 'Play!', command=john)
a.pack(side=TOP)


c = Button(root, text='Pause', command=button2)
c.pack(side=BOTTOM) 

d = Button(root, text='Resume', command=button3)
d.pack(side=BOTTOM)

e = Button(root, text='Add Songs', command=addsongs)
e.pack(side=BOTTOM)

g = Button(root, text='Skip', command=skip)
g.pack(side=BOTTOM)

ttk.Scale(root)
slider = ttk.Scale(root,length=400,orient='horizontal', command=slidertext)
slider.pack(side=BOTTOM)
slider_label = Label(root, text=slider.get())
slider_label.pack(side=BOTTOM)



root.mainloop()
