from Tkinter import *
from PIL import Image, ImageTk
import pyglet

master = Tk()
master.title("Are you ready?")

def revolution():
	master.quit()
	
def starovia():
	music = pyglet.resource.media('USSR.mp3')
	music.play()
	pyglet.app.run()
	master.quit()

im = Image.open('Karl.png')
tkimage = ImageTk.PhotoImage(im)
img = Label(master, image=tkimage).pack(side = LEFT) 

f = Frame(master)
f.pack_propagate(0)
f.pack()

t = Label(master, height = 1, font = (None, 12),
	text = "Are you ready for a Communist revolution?")
t.pack(fill = X)

rev1 = Button(master, text = "Yes", bg = "black", 
	fg = "white", height = 4, command = revolution, font = (None, 12))
rev1.pack(fill = X)

rev2 = Button(master, text = "Hell Yes", bg = "red",
	fg = "yellow", height = 4, command = starovia, font = (None, 12))
rev2.pack(fill = X, side = BOTTOM)

mainloop()
