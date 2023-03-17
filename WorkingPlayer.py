import pygame
from pygame import mixer
from tkinter import *
from tkinter import filedialog
import os

root = Tk()     
root.title("Substantially LRG MusicPlayer")
root.geometry("1000x400")
# Initiating Pygame
pygame.init()
pygame.mixer.init()
# Declaring Status Variable
status = StringVar()
track = StringVar()

def playsong():
    track.set(playlist.get(ACTIVE))
    status.set("-Playing")
    pygame.mixer.music.load(playlist.get(ACTIVE))
    pygame.mixer.music.play()

def stopsong():
    status.set("-Stopped")
    pygame.mixer.music.stop()

def pausesong():
    status.set("-Paused")
    pygame.mixer.music.pause()

def unpausesong():    
    status.set("-Playing")
    pygame.mixer.music.unpause()

#Add song function
def add_a_song():
  track = filedialog.askopenfilename( title="Choose a song", filetypes=(("mp3 Files", "*.mp3"), ))
  playlist.insert(END,track)

# Creating the Track Frames for Song label & status label
trackframe = LabelFrame(root,text="Song Name",font=("Verdana",15,"bold"),bg="LightBlue",fg="white",bd=5,relief=GROOVE)
trackframe.place(x=0,y=0,width=600,height=200)
# Inserting Song Track Label
songtrack = Label(trackframe,textvariable=track,width=30,font=("Verdana",12,"bold"),bg="Orange",fg="gold").grid(row=0,column=0,padx=20,pady=5)
# Inserting Status Label
trackstatus = Label(trackframe,textvariable=status,font=("Verdana",12,"bold"),bg="orange",fg="gold").grid(row=0,column=1,padx=20,pady=5)

#Creating Menu
mymenu = Menu(root)
root.config(menu=mymenu)

#Add Song Menu
add_song = Menu(mymenu)
mymenu.add_cascade(label="Add Songs", menu=add_song)
add_song.add_command(label="Add one song to playlist", command=add_a_song)

# Creating Button Frame
buttonframe = LabelFrame(root,text="Controls",font=("Verdana",15,"bold"),bg="steelblue",fg="white",bd=5,relief=GROOVE)
buttonframe.place(x=0,y=200,width=600,height=200)
# Inserting Play Button
playbtn = Button(buttonframe,text="Play",command=playsong,width=10,height=1,font=("Verdana",16,"bold","italic"),fg="navyblue",bg="peru").grid(row=0,column=0,padx=10,pady=5)
# Inserting Pause Button
playbtn = Button(buttonframe,text="Pause",command=pausesong,width=10,height=1,font=("Verdana",16,"bold","italic"),fg="navyblue",bg="peru").grid(row=0,column=1,padx=10,pady=5)
# Inserting Unpause Button
playbtn = Button(buttonframe,text="Resume",command=unpausesong,width=10,height=1,font=("Verdana",16,"bold","italic"),fg="navyblue",bg="peru").grid(row=1,column=0,padx=10,pady=5)
# Inserting Stop Button
playbtn = Button(buttonframe,text="Stop",command=stopsong,width=10,height=1,font=("Verdana",16,"bold","italic"),fg="navyblue",bg="peru").grid(row=1,column=1,padx=10,pady=5)

# Creating Playlist Frame
songsframe = LabelFrame(root,text="Song Playlist",font=("Verdana",15,"bold"),bg="steelblue",fg="white",bd=5,relief=GROOVE)
songsframe.place(x=600,y=0,width=400,height=400)
# Inserting scrollbar
scrol_y = Scrollbar(songsframe,orient=VERTICAL)
# Inserting Playlist listbox
playlist = Listbox(songsframe,yscrollcommand=scrol_y.set,selectbackground="gold",selectmode=SINGLE,font=("Verdana",12,"bold"),bg="silver",fg="navyblue",bd=5,relief=GROOVE)
# Applying Scrollbar to listbox
scrol_y.pack(side=RIGHT,fill=Y)
scrol_y.config(command=playlist.yview)
playlist.pack(fill=BOTH)

#Add song function

root.mainloop()
