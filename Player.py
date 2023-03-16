import pygame
from pygame import mixer
from tkinter import *
import os

class MusicPlayer():
  def __init__(self,root):
      self.root = root
      self.root.title("MusicPlayer")
      self.root.geometry("1000x400")
      # Initiating Pygame
      pygame.init()
      pygame.mixer.init()
      # Declaring track Variable
      self.track = StringVar()
      # Declaring Status Variable
      self.status = StringVar()

      # Creating the Track Frames for Song label & status label
      trackframe = LabelFrame(self.root,text="Song Name",font=("Verdana",15,"bold"),bg="LightBlue",fg="white",bd=5,relief=GROOVE)
      trackframe.place(x=0,y=0,width=600,height=200)
      # Inserting Song Track Label
      songtrack = Label(trackframe,textvariable=self.track,width=20,font=("Verdana",24,"bold"),bg="Orange",fg="gold").grid(row=0,column=0,padx=10,pady=5)
      # Inserting Status Label
      trackstatus = Label(trackframe,textvariable=self.status,font=("Verdana",24,"bold"),bg="orange",fg="gold").grid(row=0,column=1,padx=10,pady=5)

      # Creating Button Frame
      buttonframe = LabelFrame(self.root,text="Controls",font=("Verdana",15,"bold"),bg="steelblue",fg="white",bd=5,relief=GROOVE)
      buttonframe.place(x=0,y=200,width=600,height=200)
      # Inserting Play Button
      playbtn = Button(buttonframe,text="Play",command=self.playsong,width=10,height=1,font=("Verdana",16,"bold","italic"),fg="navyblue",bg="peru").grid(row=0,column=0,padx=10,pady=5)
      # Inserting Pause Button
      playbtn = Button(buttonframe,text="Pause",command=self.pausesong,width=10,height=1,font=("Verdana",16,"bold","italic"),fg="navyblue",bg="peru").grid(row=0,column=1,padx=10,pady=5)
      # Inserting Unpause Button
      playbtn = Button(buttonframe,text="Resume",command=self.unpausesong,width=10,height=1,font=("Verdana",16,"bold","italic"),fg="navyblue",bg="peru").grid(row=1,column=0,padx=10,pady=5)
      # Inserting Stop Button
      playbtn = Button(buttonframe,text="Stop",command=self.stopsong,width=10,height=1,font=("Verdana",16,"bold","italic"),fg="navyblue",bg="peru").grid(row=1,column=1,padx=10,pady=5)

      # Creating Playlist Frame
      songsframe = LabelFrame(self.root,text="Song Playlist",font=("Verdana",15,"bold"),bg="steelblue",fg="white",bd=5,relief=GROOVE)
      songsframe.place(x=600,y=0,width=400,height=400)
      # Inserting scrollbar
      scrol_y = Scrollbar(songsframe,orient=VERTICAL)
      # Inserting Playlist listbox
      self.playlist = Listbox(songsframe,yscrollcommand=scrol_y.set,selectbackground="gold",selectmode=SINGLE,font=("Verdana",12,"bold"),bg="silver",fg="navyblue",bd=5,relief=GROOVE)
      # Applying Scrollbar to listbox
      scrol_y.pack(side=RIGHT,fill=Y)
      scrol_y.config(command=self.playlist.yview)
      self.playlist.pack(fill=BOTH)


      #VERY IMPORTANT CHANGE THIS WHEN YOU TRY TO RUN-----------------
      os.chdir(r'C:\Users\husai\Desktop\Project')
      #VERY IMPORTANT CHANGE THIS WHEN YOU TRY TO RUN-----------------
      #AND DONT FORGET TO ADD SONGS TO THAT DIRECTORY


      # Fetching Songs
      songtracks = os.listdir()
      # Inserting Songs into Playlist
      for track in songtracks:
        self.playlist.insert(END,track)

  def playsong(self):
    self.track.set(self.playlist.get(ACTIVE))
    self.status.set("-Playing")
    pygame.mixer.music.load(self.playlist.get(ACTIVE))
    pygame.mixer.music.play()

  def stopsong(self):
    self.status.set("-Stopped")
    pygame.mixer.music.stop()

  def pausesong(self):
    self.status.set("-Paused")
    pygame.mixer.music.pause()

  def unpausesong(self):    
    self.status.set("-Playing")
    pygame.mixer.music.unpause()


root = Tk()
MusicPlayer(root)

root.mainloop()