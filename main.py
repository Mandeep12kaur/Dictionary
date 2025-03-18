from tkinter import *
import json
from difflib import get_close_matches
from tkinter import messagebox
import pyttsx3

engine=pyttsx3.init()##creating instance of engine class

voice=engine.getProperty('voices')
engine.setProperty('voices',voice[0].id)




##funtionpart
def search():
    data=json.load(open('data.json'))
    word=enterwordenrty.get()
    word=word.lower()
    
    if word in data:
        meaning=data[word]
        textarea.delete(1.0,END)
        for item in meaning:
            textarea.insert(END,u'\u2022'+item+'\n\n')
            
    
    elif   len(get_close_matches(word,data.keys()))>0:
        close_match=get_close_matches(word,data.keys())[0]
        res=messagebox.askyesno('Confirm',f'Did you mean {close_match} instead?')
        if res==TRUE:
            enterwordenrty.delete(0,END)
            enterwordenrty.insert(END,close_match)
            
            meaning=data[close_match]
            textarea.delete(1.0,END)
            
            for item in meaning:
              textarea.insert(END,u'\u2022'+item+'\n\n')
       
        
        else:
            messagebox.showerror('Error','The word doesnt exist,Please recheck')
            enterwordenrty.delete(0,END)
            textarea.delete(1.0,END)
                  

def clear():
    enterwordenrty.delete(0,END)        
    textarea.delete(1.0,END)

def iexit():
    res=messagebox.askyesno('Confirm','Do you want to exit?') 
    if res==True:
        root.destroy()
    else:
        pass

def wordaudio():
    engine.say(enterwordenrty.get())
    engine.runAndWait()
    
def meaningaudio():
    engine.say(textarea.get(1.0,END))
    engine.runAndWait()












## gui part
root=Tk()
root.geometry('1000x626+100+30')
root.title('Talking Dictionary')
root.resizable(0,0)

bgImage=PhotoImage(file='bg.png')
bgLabel=Label(root,image=bgImage)
bgLabel.place(x=0,y=0)

enterwordlabel=Label(root,text='ENTER WORD',font=('castellar',35,'bold'),fg='red3',bg='whitesmoke')
enterwordlabel.place(x=530,y=20)

enterwordenrty=Entry(root,font=('arial',23,'bold'),justify=CENTER,bd=5,relief=GROOVE)
enterwordenrty.place(x=510,y=80)

searchimage=PhotoImage(file='search.png')
searchbutton=Button(root,image=searchimage,bd=0,bg='whitesmoke',cursor='hand2',activebackground='whitesmoke',command=search)
searchbutton.place(x=620,y=150)

micimage=PhotoImage(file='mic.png')
micbutton=Button(root,image=micimage,bd=0,bg='whitesmoke',activebackground='whitesmoke',cursor='hand2',command=wordaudio)
micbutton.place(x=710,y=153)

meaninglabel=Label(root,text='MEANING',font=('castellar',35,'bold'),fg='red3',bg='whitesmoke')
meaninglabel.place(x=580,y=240)

textarea=Text(root,width=34,height=8,font=('arial',18,'bold'),bd=5,relief=GROOVE)
textarea.place(x=460,y=300)

audioimage=PhotoImage(file='microphone.png')
audioButton=Button(root,image=audioimage,bd=0,bg='whitesmoke',activebackground='whitesmoke',cursor='hand2',command=meaningaudio)
audioButton.place(x=530,y=555)

clearimage=PhotoImage(file='clear.png')
clearButton=Button(root,image=clearimage,bd=0,bg='whitesmoke',activebackground='whitesmoke',cursor='hand2',command=clear)
clearButton.place(x=660,y=555)


exitimage=PhotoImage(file='exit.png')
exitButton=Button(root,image=exitimage,bd=0,bg='whitesmoke',activebackground='whitesmoke',cursor='hand2',command=iexit)
exitButton.place(x=790,y=555)



def enter_function(event):
    searchbutton.invoke()
    


root.bind('<Return>',enter_function)





root.mainloop()