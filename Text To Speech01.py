import tkinter as tk
from tkinter import *
import pyttsx3
engine=pyttsx3.init()




voices = engine.getProperty("voices")

#print("Male Voice :{0}".format(voices[0].id))
#print("Female Voice :{0}".format(voices[1].id))
#engine.setProperty("voice", voices[0].id)
#engine.setProperty("voice", voices[1].id)
root=Tk()

textv=StringVar()

obj=LabelFrame(root,text="Text to speech",font=20,bd=3,fg="black")
obj.pack(fill="both",expand="yes",padx=10,pady=10)

lbl=Label(obj,text="Text",font=25,fg="black")
lbl.pack(side=tk.LEFT,padx=20)

text=Entry(obj,textvariable=textv,font=25,width=20,bd=5)
text.pack(side=tk.LEFT,padx=10)

def speaknow():
    engine.say(textv.get())
    engine.setProperty("voice", voices[1].id)
    engine.runAndWait()
    engine.stop()
btn=Button(obj,text="Male voice",font=20,bg="black",fg="white",command=speaknow)
btn.pack(side=tk.LEFT,padx=5)

def speak1now():
    engine.say(textv.get())
    engine.setProperty("voice", voices[0].id)
    engine.runAndWait()
    engine.stop()
    
btn=Button(obj,text="Female voice",font=20,bg="black",fg="white",command=speak1now)
btn.pack(side=tk.LEFT,padx=5)

root.title("Text to speech")
root.geometry("700x200")
root.resizable(False,False)
root.mainloop()
