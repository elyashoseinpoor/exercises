#import
from tkinter import *
import keyboard
import time
import threading
import pygame



def af_main():
    def key(event):
        #play sound's
        def play_sound(sound_file):
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

        # for key's
        if event.name == "caps lock":
            sound_file = "nots/01c.mp3"  
            play_sound(sound_file)
        elif event.name == "a":
            sound_file = "nots/02c#.mp3"  
            play_sound(sound_file)
        elif event.name == "A":
            sound_file = "nots/02c#.mp3"  
            play_sound2(sound_file)
        elif event.name == "s":
            sound_file = "nots/03d.mp3"  
            play_sound(sound_file)
        elif event.name == "S":
            sound_file = "nots/03d.mp3"  
            play_sound(sound_file)
        elif event.name == "d":
            sound_file = "nots/04d#.mp3"  
            play_sound(sound_file)
        elif event.name == "D":
            sound_file = "nots/04d#.mp3"  
            play_sound(sound_file)
        elif event.name == "f":
            sound_file = "nots/05e.mp3"  
            play_sound(sound_file)
        elif event.name == "F":
            sound_file = "nots/05e.mp3"  
            play_sound(sound_file)
        elif event.name == "g": 
            sound_file = "nots/06f.mp3"  
            play_sound(sound_file)
        elif event.name == "G":
            sound_file = "nots/06f.mp3"  
            play_sound(sound_file)
        elif event.name == "h":
            sound_file = "nots/07f#.mp3"  
            play_sound(sound_file)
        elif event.name == "H":
            sound_file = "nots/07f#.mp3"  
            play_sound(sound_file)
        elif event.name == "j":
            sound_file = "nots/08g.mp3"  
            play_sound(sound_file)
        elif event.name == "J":
            sound_file = "nots/08g.mp3"  
            play_sound(sound_file)
        elif event.name == "k":
            sound_file = "nots/09g#.mp3"  
            play_sound(sound_file)
        elif event.name == "K":
            sound_file = "nots/09g#.mp3"  
            play_sound(sound_file)
        elif event.name == "l":
            sound_file = "nots/10a.mp3"  
            play_sound(sound_file)
        elif event.name == "L":
            sound_file = "nots/10a.mp3"  
            play_sound(sound_file)
        elif event.name == ";":
            sound_file = "nots/11a#.mp3"  
            play_sound(sound_file)
        elif event.name == ":":
            sound_file = "nots/11a#.mp3"  
            play_sound(sound_file)
        elif event.name == "'":
            sound_file = "nots/12b.mp3"  
            play_sound(sound_file)
        elif event.name == '"':
            sound_file = "nots/12b.mp3"  
            play_sound(sound_file)
        else:
            pass

    #listening for key
    keyboard.on_press(key)
    #listening for after press
    keyboard.wait()
    #end listening
    keyboard.unhook_all()




def main():
    #main window
    win = Tk()
    win.maxsize(450,450)
    win.minsize(450,450)
    win.title("piano")
    win.configure(bg="#00FF00")

    #about toplevel 
    def about():
        top = Toplevel()
        top.maxsize(350,100)
        top.minsize(350,100)
        top.title("about!!!")
        top.configure(bg="#00FF00")
        label1 = Label(top,text="Hello,from the CAPS LOCK key to",bg="#00FF00",font=("tahoma",12, "bold"))
        label1.place(x=10, y=10)
        label2 = Label(top,text="the quotation mark on the keyboard",bg="#00FF00",font=("tahoma",12, "bold"))
        label2.place(x=10, y=30)
        label3 = Label(top,text="are the notes",bg="#00FF00",font=("tahoma",12, "bold"))
        label3.place(x=10, y=50)
        label4 = Label(top,text="I hope you enjoy!",bg="#00FF00",font=("tahoma",12, "bold"))
        label4.place(x=10, y=70)
        top.mainloop()


    #play sound's
    def play_sound(sound_file):
        pygame.mixer.init()
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play()

    #click's on the Button
    def A():
        sound_file = "nots/01c.mp3"  
        play_sound(sound_file)

    def B():
        sound_file = "nots/02c#.mp3"  
        play_sound(sound_file)
        
    def C():
        sound_file = "nots/03d.mp3"  
        play_sound(sound_file)

    def D():
        sound_file = "nots/04d#.mp3"  
        play_sound(sound_file)        

    def E():
        sound_file = "nots/05e.mp3"  
        play_sound(sound_file)            

    def F():
        sound_file = "nots/06f.mp3"  
        play_sound(sound_file)       

    def G():
        sound_file = "nots/07f#.mp3"  
        play_sound(sound_file)

    def H():
        sound_file = "nots/08g.mp3"  
        play_sound(sound_file)

    def I():
        sound_file = "nots/09g#.mp3"  
        play_sound(sound_file)
        
    def J():
        sound_file = "nots/10a.mp3"  
        play_sound(sound_file)

    def K():
        sound_file = "nots/11a#.mp3"  
        play_sound(sound_file)

    def L():
        sound_file = "nots/12b.mp3"  
        play_sound(sound_file)

    def M():
        sound_file = "nots/12b.mp3"  
        play_sound(sound_file)

        
    #piano buttons
    B1 = Button(win,text="A",font=("Helvetica",20, "bold"),command=A)
    B1.place(x=40, y=130, width=30, height=120)
    B2 = Button(win,text="B",bg="black",fg="white",font=("Helvetica",20, "bold"),command=B)
    B2.place(x=70, y=130, width=30, height=120)
    B3 = Button(win,text="C",font=("Helvetica",20, "bold"),command=C)
    B3.place(x=100, y=130, width=30, height=120)
    B4 = Button(win,text="D",bg="black",fg="white",font=("Helvetica",20, "bold"),command=D)
    B4.place(x=130, y=130, width=30, height=120)
    B5 = Button(win,text="E",font=("Helvetica",20, "bold"),command=E)
    B5.place(x=160, y=130, width=30, height=120)
    B6 = Button(win,text="F",bg="black",fg="white",font=("Helvetica",20, "bold"),command=F)
    B6.place(x=190, y=130, width=30, height=120)
    B7 = Button(win,text="G",font=("Helvetica",20, "bold"),command=G)
    B7.place(x=220, y=130, width=30, height=120)
    B8 = Button(win,text="H",bg="black",fg="white",font=("Helvetica",20, "bold"),command=H)
    B8.place(x=250, y=130, width=30, height=120)
    B9 = Button(win,text="I",font=("Helvetica",20, "bold"),command=I)
    B9.place(x=280, y=130, width=30, height=120)
    B10 = Button(win,text="J",bg="black",fg="white",font=("Helvetica",20, "bold"),command=J)
    B10.place(x=310, y=130, width=30, height=120)
    B11 = Button(win,text="K",font=("Helvetica",20, "bold"),command=L)
    B11.place(x=340, y=130, width=30, height=120)
    B12 = Button(win,text="M",bg="black",fg="white",font=("Helvetica",20, "bold"),command=M)
    B12.place(x=370, y=130, width=30, height=120)

    #about button
    about = Button(win,text="about!",font=("Helvetica",9, "bold"),command=about)
    about.place(x=200, y=300, width=70, height=30)

    #hello world
    label = Label(win,text="hello world",font=("tahoma",30, "bold"),fg="red",bg="#00FF00")
    label.place(x=80, y=330, width=300,height=50)
    t = threading.Thread(target=af_main)
    t.start()

    win.mainloop()

#run page
if __name__ == "__main__":
    main()
