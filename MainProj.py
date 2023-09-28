from pathlib import Path
import pygame
from pygame import mixer
from tkinter import *
import os
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, filedialog, messagebox

pygame.init()
pygame.mixer.init()

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\husai\Desktop\Project\FINAL PROJECT\HomepageAssets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1100x765")
window.configure(bg = "#322C4F")
window.title("Substantially LRG Music Player")

track = StringVar()
status = StringVar()

global paused
paused = False

def playsong():
    track.set(playlist.get(ACTIVE))
    status.set("-Playing")
    pygame.mixer.music.load(playlist.get(ACTIVE))
    pygame.mixer.music.play()

def playwithloop():
    track.set(playlist.get(ACTIVE))
    status.set("-Playing")
    pygame.mixer.music.load(playlist.get(ACTIVE))
    pygame.mixer.music.play(loops=-1)

def stopsong():
    status.set("-Stopped")
    pygame.mixer.music.stop()

def pausesong(is_paused):
    global paused
    paused = is_paused

    if paused:
        pygame.mixer.music.pause()
        paused = False
    else:
        pygame.mixer.music.unpause()
        paused = True

def unpausesong():    
    status.set("-Playing")
    pygame.mixer.music.unpause()

def nextsong():
    pygame.mixer.music.stop()
    #Getting current song no
    next_song = playlist.curselection()
    #Setting next song to the value of next song
    next_song = next_song[0] + 1
    track.set(playlist.get(next_song))

    playlist.selection_clear(0, END)
    playlist.activate(next_song)
    playlist.selection_set(next_song, last=None)

    #playing prev song
    pygame.mixer.music.load(playlist.get(ACTIVE))
    pygame.mixer.music.play()

def prevsong():
    #Getting current song no
    prev_song = playlist.curselection()
    #Setting prev song to the value of next song
    prev_song = prev_song[0] - 1
    track.set(playlist.get(prev_song))

    playlist.selection_clear(0, END)
    playlist.activate(prev_song)
    playlist.selection_set(prev_song, last=None)

    #Playing prev song
    pygame.mixer.music.load(playlist.get(ACTIVE))
    pygame.mixer.music.play()

def Search():
    os.system('start cmd /c python main.py')

#Add song function
def add_a_song():
    track = filedialog.askopenfilename( title="Choose a song", filetypes=(("mp3 Files", "*.mp3"), ))
    playlist.insert(END,track)

def add_many_songs():
    tracks = filedialog.askopenfilenames(title="Choose your Songs",filetypes=(("mp3 Files", '*.mp3'), ))
    for track in tracks:
        playlist.insert(END,track)

def logout():
    response = messagebox.askyesno('Sign Out','Do you want to sign out?')
    if response == 1:
        window.destroy()
        import signin
    

canvas = Canvas(
    window,
    bg = "#322C4F",
    height = 765,
    width = 1100,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    51.0,
    65.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    599.0,
    382.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    824.0,
    383.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    332.0,
    517.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    827.0,
    189.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    332.0,
    442.0,
    image=image_image_6
)

canvas.create_text(
    584.0,
    21.0,
    anchor="nw",
    text="Home",
    fill="#000000",
    font=("Marmelad Regular", 65 * -1)
)

canvas.create_text(
    122.0,
    25.0,
    anchor="nw",
    text="Your Playlist",
    fill="#FFFFFF",
    font=("Marmelad Regular", 55 * -1)
)

canvas.create_text(
    233.0,
    568.0,
    anchor="nw",
    text="now playing",
    fill="#FFFFFF",
    font=("Marmelad Regular", 36 * -1)
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    700.0,
    393.0,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    919.0,
    528.0,
    image=image_image_8
)

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    700.0,
    528.0,
    image=image_image_9
)

image_image_10 = PhotoImage(
    file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(
    700.0,
    663.0,
    image=image_image_10
)

image_image_11 = PhotoImage(
    file=relative_to_assets("image_11.png"))
image_11 = canvas.create_image(
    919.0,
    393.0,
    image=image_image_11
)

canvas.create_text(
    584.0,
    282.0,
    anchor="nw",
    text="Top Artists",
    fill="#000000",
    font=("Marmelad Regular", 50 * -1)
)

canvas.create_text(
    631.0,
    703.0,
    anchor="nw",
    text="TAYLOR SWIFT",
    fill="#000000",
    font=("Marmelad Regular", 20 * -1)
)

canvas.create_text(
    631.0,
    568.0,
    anchor="nw",
    text="JUSTIN BIEBER",
    fill="#000000",
    font=("Marmelad Regular", 20 * -1)
)

canvas.create_text(
    631.0,
    433.0,
    anchor="nw",
    text="CAMILA CABELLO",
    fill="#000000",
    font=("Marmelad Regular", 20 * -1)
)

canvas.create_text(
    866.0,
    703.0,
    anchor="nw",
    text="ANUV JAIN",
    fill="#000000",
    font=("Marmelad Regular", 20 * -1)
)

canvas.create_text(
    845.0,
    568.0,
    anchor="nw",
    text="HARRY STYLES",
    fill="#000000",
    font=("Marmelad Regular", 20 * -1)
)

canvas.create_text(
    845.0,
    433.0,
    anchor="nw",
    text="THE WEEKEND",
    fill="#000000",
    font=("Marmelad Regular", 20 * -1)
)

image_image_12 = PhotoImage(
    file=relative_to_assets("image_12.png"))
image_12 = canvas.create_image(
    919.0,
    663.0,
    image=image_image_12
)

image_image_13 = PhotoImage(
    file=relative_to_assets("image_13.png"))
image_13 = canvas.create_image(
    330.1793212890625,
    199.20315551757812,
    image=image_image_13
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=playwithloop,
    relief="flat"
)
button_1.place(
    x=432.0,
    y=642.0,
    width=51.0,
    height=55.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=nextsong,
    relief="flat"
)
button_2.place(
    x=363.0,
    y=649.0,
    width=71.0,
    height=42.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=playsong,
    relief="flat"
)
button_3.place(
    x=302.0,
    y=640.0,
    width=61.0,
    height=57.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=prevsong,
    relief="flat"
)
button_4.place(
    x=237.0,
    y=652.0,
    width=60.0,
    height=33.682861328125
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: pausesong(paused),
    relief="flat"
)
button_5.place(
    x=182.0,
    y=640.0,
    width=55.0,
    height=60.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=22.0,
    y=639.0,
    width=57.0,
    height=55.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat"
)
button_7.place(
    x=24.0,
    y=428.0,
    width=57.0,
    height=55.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=Search,
    relief="flat"
)
button_8.place(
    x=24.0,
    y=361.0,
    width=57.0,
    height=55.0
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=add_many_songs,
    relief="flat"
)
button_9.place(
    x=21.0,
    y=290.0,
    width=57.0,
    height=55.0
)

button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=logout,
    relief="flat"
)
button_10.place(
    x=23.0,
    y=221.0,
    width=57.0,
    height=55.0
)

# Creating Playlist Frame
songsframe = LabelFrame(window,bg="white",fg="white",bd=5)
songsframe.place(x=136,y=118,width=392,height=162)
# Inserting scrollbar
scrol_y = Scrollbar(songsframe,orient=VERTICAL)
# Inserting Playlist listbox
playlist = Listbox(songsframe,yscrollcommand=scrol_y.set,selectbackground="gold",selectmode=SINGLE,font=("Verdana",12,"bold"),bg="silver",fg="navyblue",bd=5,relief=GROOVE)
# Applying Scrollbar to listbox
scrol_y.pack(side=RIGHT,fill=Y)
scrol_y.config(command=playlist.yview)
playlist.pack(fill=BOTH)

window.resizable(False, False)
window.mainloop()