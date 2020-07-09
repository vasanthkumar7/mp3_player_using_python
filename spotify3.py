from tkinter import *
import pygame
from tkinter import filedialog
from mutagen import File
from mutagen.mp3 import MP3
from PIL import ImageTk,Image
from tkinter import messagebox
import os
albumart=[]
def remove_extention(text):
    check=0
    for i in range(len(text)):
        if text[i]=="/":
            check=i
    text=text.replace(".mp3","")
    
    newname=text[check+1:len(text)]
    return newname
def pudualbum(text):
    try:
        file = File(text) # mutagen can automatically detect format and type of tags
        artwork = file.tags['APIC:'].data # access APIC frame and grab the image
        with open('image.jpg', 'wb') as img:
            img.write(artwork)
        img1=Image.open("image.jpg")
        p2=ImageTk.PhotoImage(img1.resize((250,250),Image.ANTIALIAS))
        albumart.append(p2)
    except:
        albumart.append(0)
alistofsongs=[]
albumarts=[]
currentdir="home"
root=Tk()
root.title("Spotify")
root.iconbitmap("spotifyi.ico")
root.configure(bg="green")
mymenu=Menu(root)
root.config(menu=mymenu)
songnames=[]
adds=Menu(mymenu)
playlist=Menu(mymenu)
dels=Menu(mymenu)

pygame.mixer.init()
topla=Frame(root)

planame=Label(topla,text="Playlistname: "+currentdir,bg="green",fg="white",font=("arial",12,"italic"))
planame.grid(row=0,column=0)

bottomdamapu=Frame(root)
myscroll=Scrollbar(bottomdamapu,orient=VERTICAL)
songbox=Listbox(bottomdamapu,width=60,borderwidth=0,bg="lightgreen",fg="black",yscrollcommand=myscroll.set)
myscroll.config(command=songbox.yview)





img1=Image.open("icons8-play-96.png")
img2=Image.open("icons8-pause-96.png")
img3=Image.open("icons8-stop-96.png")
img4=Image.open("icons8-skip-to-start-100.png")
img5=Image.open("icons8-end-100.png")
img6=Image.open("startimg.jpg")
img7=Image.open("5after.png")
img8=Image.open("5forward.png")
pl=ImageTk.PhotoImage(img1.resize((40,40),Image.ANTIALIAS))
pa=ImageTk.PhotoImage(img2.resize((40,40),Image.ANTIALIAS))
st=ImageTk.PhotoImage(img3.resize((40,40),Image.ANTIALIAS))
sf=ImageTk.PhotoImage(img4.resize((40,40),Image.ANTIALIAS))
sb=ImageTk.PhotoImage(img5.resize((40,40),Image.ANTIALIAS))
ff=ImageTk.PhotoImage(img7.resize((40,40),Image.ANTIALIAS))
fb=ImageTk.PhotoImage(img8.resize((40,40),Image.ANTIALIAS))
startimg=ImageTk.PhotoImage(img6.resize((250,250),Image.ANTIALIAS))
whatsong=Frame(root,bg="green")
randname="nothing"
currently=Label(whatsong,text="Currently playing:",bg="green")
currently.grid(row=0,column=0)

startingla=Label(whatsong,image=startimg,padx=5,pady=5)
startingla.grid(row=1,column=0,padx=5,pady=10)

lastahirrundasong=startimg

songname=Label(whatsong,text=randname,bg="green",fg="white",font=("arial",14))
songname.grid(row=2,column=0)
nowsong=""
pos=0
try:
    with open("home.txt","r") as f:
        for i in f:
            songbox.insert(END,i)
            i=i.replace("\n","")
            alistofsongs.append(i)
            pudualbum(i)
    
    f.close()

            

except:
    f=open("home.txt","a")
    f.close()

        
    


    

def stmu():
    global songname
    global whatsong
    global startingla
    global startimg
    global lastahirrundasong
    global curen
    curen=0
    pygame.mixer.music.stop()
    songname.grid_forget()
    songname=Label(whatsong,text="nothing",bg="green",fg="white",font=("arial",14))
    songname.grid(row=2,column=0)
    lastahirrundasong=startimg
    startingla=Label(whatsong,image=startimg,padx=5,pady=5)
    startingla.grid(row=1,column=0,padx=5,pady=10)
def hmm():
    nowsongs=songbox.get(ACTIVE)
    nowsongs=nowsong.replace("\n","")
    pygame.mixer.music.load(str(nowsongs))
    pygame.mixer.music.play()

    
def play():
    global randname
    global songname
    global whatsong
    global nowsong
    global paused
    global pos
    global startingla
    global albumart
    global lastahirrundasong
    global startimg
    global curenspos
    global curen
    curenspos=0
    curen=0
        
    paused=True
    
    if(len(alistofsongs)!=0):
        nowsong=songbox.get(ACTIVE)
        nowsong=nowsong.replace("\n","")
        song=songbox.get(ACTIVE)
        song=song.replace("\n","")
        for i in range(len(alistofsongs)):
            if(alistofsongs[i]==nowsong):
                pos=i
                break
        try:
            lastahirrundasong=albumart[pos]
            startingla=Label(whatsong,image=albumart[pos],padx=5,pady=5)
            startingla.grid(row=1,column=0,padx=5,pady=10)
        except:
            lastahirrundasong=startimg
            startingla=Label(whatsong,image=startimg,padx=5,pady=5)
            startingla.grid(row=1,column=0,padx=5,pady=10)
        randname=remove_extention(song)
        songname.grid_forget()
        songname=Label(whatsong,text=randname,bg="green",fg="white",font=("arial",14))
        songname.grid(row=2,column=0)
        pygame.mixer.music.load(song)
        pygame.mixer.music.play(-1)
        
    else:
        messagebox.showinfo("spotify","Add some somgs")
        
    

  
    
    #song=f'C:/Users/New/Desktop/python codes/{song}.mp3'


curen=0
curenspos=0
iduprev=0
def musicforward():
    global curen
    global curenspos
    global iduprev
    global pos
    global alistofsongs
    try:
        idu=int(pygame.mixer.music.get_pos()/1000)
        curen+=int(pygame.mixer.music.get_pos()/1000)+5
        so=MP3(alistofsongs[pos])
        totallen=int(so.info.length/60)*60+int(so.info.length%60)
        curen=curen-idu
        if(curen<=0 or curen>=totallen):
            curen=0
        pygame.mixer.music.set_pos(curen)
    except:
        pass
   
    

def musicbackward():
    global curen
    global curenspos
    global iduprev
    global pos
    global alistofsongs
    try:
        idu=int(pygame.mixer.music.get_pos()/1000)
        curen+=int(pygame.mixer.music.get_pos()/1000)-5
        so=MP3(alistofsongs[pos])
        totallen=int(so.info.length/60)*60+int(so.info.length%60)
        curen=curen-idu
        if(curen<=0 or curen>=totallen):
            curen=0
        pygame.mixer.music.set_pos(curen)
    except:
        pass
    
    
    
        
def skiptrackf():
    global nowsong
    global curen
    global alistofsongs
    global songname
    global lastahirrundasong
    global pos
    global paused
    curen=0
    paused=True
    
    if pos==len(alistofsongs)-1:
        pos=-1

    if(len(alistofsongs)!=0):
        randname=remove_extention(alistofsongs[pos+1])
        realname=alistofsongs[pos+1]
        pos=pos+1
        try:
            lastahirrundasong=albumart[pos]
            startingla=Label(whatsong,image=albumart[pos],padx=5,pady=5)
            startingla.grid(row=1,column=0,padx=5,pady=10)
        except:
            lastahirrundasong=startimg
            startingla=Label(whatsong,image=startimg,padx=5,pady=5)
            startingla.grid(row=1,column=0,padx=5,pady=10)
        songname.grid_forget()
        songname=Label(whatsong,text=randname,bg="green",fg="white",font=("arial",14))
        songname.grid(row=2,column=0)
        pygame.mixer.music.load(realname)
        pygame.mixer.music.play(-1)
    else:
        messagebox.showinfo("spotify","Add some somgs")
    


def skiptrackb():
    global nowsong
    global songname
    global alistofsongs
    global lastahirrundasong
    global pos
    global paused
    global curen
    curen=0
    paused=True

    if pos==0:
        pos=len(alistofsongs)
    

    if(len(alistofsongs)!=0):
        randname=remove_extention(alistofsongs[pos-1])
        realname=alistofsongs[pos-1]
        pos=pos-1
        try:
            lastahirrundasong=albumart[pos]
            startingla=Label(whatsong,image=albumart[pos],padx=5,pady=5)
            startingla.grid(row=1,column=0,padx=5,pady=10)
        except:
            lastahirrundasong=startimg
            startingla=Label(whatsong,image=startimg,padx=5,pady=5)
            startingla.grid(row=1,column=0,padx=5,pady=10)
        songname.grid_forget()
        songname=Label(whatsong,text=randname,bg="green",fg="white",font=("arial",14))
        songname.grid(row=2,column=0)
        pygame.mixer.music.load(realname)
        pygame.mixer.music.play(-1)
    else:
        messagebox.showinfo("spotify","Add some somgs")


paused=False
def pause(ispaused):
    global paused
    paused=ispaused
    
    if(ispaused):
        pygame.mixer.music.pause()
        paused=False
    else:
        pygame.mixer.music.unpause()
        paused=True

def addsongs():
    global alistofsongs
    global currentdir
    songs=filedialog.askopenfilenames(initialdir="/Desktop/python codes",title="open songs",filetypes=(("mp3 files","*.mp3"),("jpg files","*.jpg"),))
    for so in songs:
        songbox.insert(END,so)
        alistofsongs.append(so)
        pudualbum(so)
        with open(currentdir+".txt","a") as f:
            print(so,file=f)
    f.close()


def deletesong():
    global pos
    global alistofsongs
    global currentdir
    
    song=songbox.get(ACTIVE)
    song=song.replace("\n","")
    
    for i in range(len(alistofsongs)):
        if(alistofsongs[i]==song):
            pos=i
            break

    if(song!=""):
        f=open(currentdir+".txt","r")
        an=open("copypanna.txt","a")
        for i in f:
            i=i.replace("\n","")
            if(i!=song):
                print(i,file=an)
        songbox.delete(ANCHOR)
        f.close()
        an.close()
        os.remove(currentdir+".txt")
        os.rename("copypanna.txt",currentdir+".txt")
        albumart.pop(pos)
        alistofsongs.pop(pos)
    else:
         messagebox.showinfo("spotify","no songs in this playlist")
        
    
    





    
def playersname(texts):
    songbox.delete(0,END)
    global alistofsongs
    global planame
    global pos
    global albumart
    global lastahirrundasong
    pos=0
    alistofsongs=[]
    albumart=[]
    global currentdir
    currentdir=texts
    planame.grid_forget()
    planame=Label(topla,text="Playlistname: "+currentdir,bg="green",fg="white",font=("arial",12,"italic"))
    planame.grid(row=0,column=0)
    startingla=Label(whatsong,image=lastahirrundasong,padx=5,pady=5)
    startingla.grid(row=1,column=0)
    with open(texts+".txt","r") as f:
        for i in f:
            songbox.insert(END,i)
            i=i.replace("\n","")
            alistofsongs.append(i)
            pudualbum(i)
    f.close()
    


    
def collec():
    songnames.append(playlistname.get())
    
    a=""
    for i in songnames:
        a=i
    with open("playersname.txt","a") as fa:
        print(a,file=fa)
    fa.close()
    playlist.add_command(label=playlistname.get(),command=lambda: playersname(a))
    f=open(str(a)+".txt","a")
    f.close()

def addplay():
    global playlistname
    top=Toplevel()
    top.title("Spotify")
    top.iconbitmap("spotifyi.ico")
    head=Label(top,text="enter playlist name")
    head.pack()
    playlistname=Entry(top,width=40)
    playlistname.pack()
    
        
    submit=Button(top,text="add",command=collec)
    submit.pack()

def cuscollec(text):
    songnames.append(text)
    playlist.add_command(label=text,command=lambda: playersname(text))
    f=open(str(text)+".txt","a")
    f.close()

try:
    with open("playersname.txt","r") as f:
        for i in f:
            i=i.replace("\n","")
            cuscollec(i)
    f.close()
except:
    f=open("playersname.txt","a")
    f.close()

def deletema():
    songbox.delete(0,END)

mymenu.add_cascade(label="Add", menu=adds)
adds.add_command(label="Add songs to playlist",command=addsongs)
adds.add_command(label="Add a playlist",command=addplay)

mymenu.add_cascade(label="playlists", menu=playlist)
playlist.add_command(label="Home",command=lambda:playersname("home"))


mymenu.add_cascade(label="Remove", menu=dels)
dels.add_command(label="remove this song",command=deletesong)

whatsong.pack(padx=10)
butfr=Frame(root)
butfr.pack(padx=10,pady=5)

stbtn=Button(butfr,image=st,command=stmu,borderwidth=0,bg="green")
playbutton=Button(butfr,image=pl,command= play,borderwidth=0,bg="green")
pausebtn=Button(butfr,image=pa,command=lambda:pause(paused),borderwidth=0,bg="green")
skipfront=Button(butfr,image=sf,command=skiptrackb,borderwidth=0,bg="green")
skipback=Button(butfr,image=sb,command=skiptrackf,borderwidth=0,bg="green")
fastforward=Button(butfr,image=ff,command=musicforward,borderwidth=0,bg="green")
fastback=Button(butfr,image=fb,command=musicbackward,borderwidth=0,bg="green")

skipback.grid(row=0,column=6)
fastforward.grid(row=0,column=5)
fastback.grid(row=0,column=1)
stbtn.grid(row=0,column=2)
playbutton.grid(row=0,column=3)
pausebtn.grid(row=0,column=4)
skipfront.grid(row=0,column=0)

def set_vol(val):
    volume=int(val)/100
    pygame.mixer.music.set_volume(volume)
    

scalename=Label(root,text="Volume:",bg="green",fg="white")
scalename.pack(pady=5)
scale=Scale(root,from_=0,to=100,orient=HORIZONTAL,command=set_vol,bg="green",borderwidth=0)
scale.set(70)
scale.pack()
topla.pack()

myscroll.pack(side=RIGHT,fill=Y)

songbox.pack()
bottomdamapu.pack()

root.mainloop()

