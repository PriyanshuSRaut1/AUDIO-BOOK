
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import pyttsx3
from pygame import mixer
from tkinter import messagebox
import os



engine = pyttsx3.init()
#----------------------------------------------play audio
def play_music(*args):
    running = listbox.get(ACTIVE)
    running_song['text'] = running
    mixer.music.load(running)
    mixer.music.play()

#--------------------------------open and read file
def OpenFile():
    textfile=filedialog.askopenfilename()
    textfile=open(textfile,'r')
    stuff=textfile.read()
    ftext.insert(END,stuff)
    textfile.close
#-----------------------------------------------previous button
def prev():
    playing = running_song['text']
    index = song.index(playing)
    new_index = index - 1
    print("index :", new_index)
    playing = song[new_index]
    mixer.music.load(playing)
    mixer.music.play()
    listbox.delete(0, END)

    show()
    listbox.select_set(new_index)
    running_song['text'] = playing
#--------------------------------------------------next Button
def next():
    playing = running_song['text']
    index = song.index(playing)
    try:
        new_index = index + 1
        print("index :", new_index)
        playing = song[new_index]
    except IndexError:
        new_index = 0
        print("index :", new_index)
        playing = song[new_index]
    mixer.music.load(playing)
    mixer.music.play()
    listbox.delete(0, END)

    show()
    listbox.select_set(new_index)
    running_song['text'] = playing

#--------------------------------------Convert text to speech
def speak():
    text1 = ftext.get(1.0, "end-1c")
    voices = engine.getProperty('voices')
    gender = gender_combo.get()
    speed = speed_combo.get()

    # --------------------------------speed  rate
    if speed == 'Slow':
        engine.setProperty('rate', 100)
    elif speed == 'Normal':
        engine.setProperty('rate', 180)
    else:
        engine.setProperty('rate', 250)

    if text1 == '':
        if (gender == 'Male'):
            engine.setProperty('voice', voices[0].id)
            engine.say('you does not enter any text')
            engine.runAndWait()

        else:
            engine.setProperty('voice', voices[1].id)
            engine.say('you does not enter any text')
            engine.runAndWait()
    else:
        # --------------------------------gender voice
        if (gender == 'Male'):
            engine.setProperty('voice', voices[0].id)
            engine.say(text1)
            engine.runAndWait()

        else:
            engine.setProperty('voice', voices[1].id)
            engine.say(text1)
            engine.runAndWait()

    # --------------------------------speed  rate

    if speed == 'Slow':
        engine.setProperty('rate', 100)
    elif speed == 'Normal':
        engine.setProperty('rate', 180)
    else:
        engine.setProperty('rate', 250)


# -----------------------------------------------------------save

def Save():
    text1 = ftext.get(1.0, "end-1c")
    voices = engine.getProperty('voices')
    gender = gender_combo.get()
    speed = speed_combo.get()

    # --------------------------------gender voice
    if (gender == 'Male'):
        engine.setProperty('voice', voices[0].id)

        # -------------------------------------------------------------
        path = 'C:\\Users\\HP\\Music'
        os.chdir(path)
        newfolder = 'AudioBookFinal'
        if not os.path.exists(newfolder):
            os.makedirs(newfolder)
        path2 = path + '//' + newfolder + '//'
        os.chdir(path2)
        filename = text1[0:10] + ' M_voice' + '  mp3'
        engine.save_to_file(text1, filename)
        messagebox.showinfo('Save ','Save Successfully')
        # ------------------------------------------------------------
        engine.runAndWait()
        top.update_idletasks()
    else:
        engine.setProperty('voice', voices[1].id)

        # ------------------------------------------------------
        path = 'C:\\Users\\Hp\\Music'  #
        os.chdir(path)  #
        newfolder = 'AudioBookFinal'
        if not os.path.exists(newfolder):  #
            os.makedirs(newfolder)
        path2 = path + '//' + newfolder + '//'  #
        os.chdir(path2)
        engine.save_to_file(text1, text1[0:10]+ '  F_Voice' + '  mp3')  #
        messagebox.showinfo('Save ', 'Save Successfully')
        # ------------------------------------------------------
        engine.runAndWait()
        top.update_idletasks()
    show1()
    # =========================================================


# --------------------------------heading of frame
top = Tk()
top.title("Audio Book ")
top.config(bg='#000428')
top.geometry("995x650")
top.resizable(False, False)


if __name__=="__main__":
    import audiobookp1


# --------------------------------Top frame
frame = Frame(top, bg='white', width=1000, height=100)
frame.place(x=0, y=0)

logofront = PhotoImage(file='./images/output-onlinepngtools (5).png')
logo = Label(frame, image=logofront, bg='white')
logo.place(x=10, y=0)
l2 = Label(frame, text="Audio Book", font=('Algerian', 35, 'bold'), bg='white')
l2.place(x=120, y=20)

# --------------------------------text field
text_frame = Frame(top, bg='white', width=400, height=400)
text_frame.place(x=10, y=120)
logofront = PhotoImage(file='./images/output-onlinepngtools (5).png')
logo = Label(frame, image=logofront, bg='white')
logo.place(x=10, y=0)

def on_enter(e):
    if ftext.get(1.0, "end-1c")=="Enter Text Here :":
        ftext.delete(-1.0,'end')
def on_leave(e): 
    if (ftext.get(1.0, "end-1c")==""):
        ftext.insert(1.0,'Enter Text Here :')

ftext = Text(text_frame, width=35, height=15, border=2, font=("arial", 15),fg='#434343')
ftext.place(x=5, y=5)

ftext.insert(END,"Enter Text Here :")
ftext.bind("<FocusIn>",on_enter)
ftext.bind("<FocusOut>",on_leave)

# --------------------------------gender
l = Label(top, text="VOICE", font=('Arial', 15, 'bold'), bg='#000428', fg='white')
l.place(x=500, y=235)
gender_combo = ttk.Combobox(top, values=['Male', 'Female'], state='r')
gender_combo.set('Male')
gender_combo.place(x=470, y=270)

# -------------------------------- voice SPEED
sl1 = Label(top, text="SPEED", font=('Arial', 15, 'bold'), bg='#000428', fg='white')
sl1.place(x=750, y=235)
speed_combo = ttk.Combobox(top, values=['Fast', 'Normal', 'Slow'], state='r')
speed_combo.set('Normal')
speed_combo.place(x=713, y=270)

# --------------------------------speech button,
img = PhotoImage(file='./images/output-onlinepngtools.png')
btn1 = Button(top, text='Play', image=img, bg='white', compound=LEFT, font=('Times New Roman', 15, 'bold'),
              command=speak, border=0, width=100)
btn1.place(x=150, y=550)

# --------------------------------privious button
prev_img = PhotoImage(file='./images/output-onlinepngtools (3).png')

privious = Button(top, text='Previous', image=prev_img, font=('Times New Roman', 15, 'bold'), width=120, command=prev,
                  compound=LEFT, bg='white')
privious.place(x=10, y=550)


nextimg=PhotoImage(file='./images/output-onlinepngtools.png')#user another image
nextbtn=Button(top, text='Next', image=nextimg,font=('Times New Roman', 15, 'bold'), width=120,height=32,command=next, compound=RIGHT, bg='white')
nextbtn.place(x=280,y=550)


# --------------------------------Exit Button
exitimg = PhotoImage(file='./images/output-onlinepngtools (2).png')
exit1 = Button(top, text='Exit', bg='White', image=exitimg, compound=LEFT, width=80, border=0, command=top.destroy)
exit1.place(x=900, y=30)


#--------------------------------------------clear 
def Clear1():
    ftext.delete(-1.0,'end')

clear=Button(top,command=Clear1,text="Clear",compound=LEFT,height=0,width=4)
clear.place(x=370,y=522)
# ---------------------------------Save
saveimg= PhotoImage(file='./images/output-onlinepngtools.png')#user another image
Savebtn = Button(top, text=' Save  ',command=Save,compound=LEFT, image=saveimg,width=80)
Savebtn.place(x=490, y=370)

# ===================================================================================== Play list
playlist= PhotoImage(file='./images/output-onlinepngtools.png')#user another image
pl=Label(top,image=playlist)
pl.place(x=2000,y=100)
 
l1 = Label(top, text="Play List ", font=('Arial', 15, 'bold'), bg='#000428', fg='white')
l1.place(x=2000, y=100)
listbox = Listbox(top, selectmode=SINGLE,font=('Arial 9 bold'), width=25, height=28, fg='black',bg='white')
listbox.place(x=2000, y=130)
listbox.bind('<Double-Button-1>', play_music)


#-------------------------------------------------choose audio
running_song = Label(top, text='choose a Audio', width=56,bg='#E8CBC0',height=2,fg='black')
running_song.place(x=11, y=480)

os.chdir(r'C:\\Users\\Hp\\Music\\AudioBookFinal')
song = os.listdir()


#===================================================list box 
def show():

    for i in song:
        listbox.insert(END, i)
listbox.update_idletasks()
show()
def show1():
        os.chdir(r'C:\\Users\\Hp\\Music\\AudioBookFinal')
        song = os.listdir()
        for i in song:
            listbox.delete(0,END)
        listbox.update_idletasks()
        
        for i in song:
            listbox.insert(END, i)
        listbox.update_idletasks()
show1()

OpenFolderimg= PhotoImage(file='D:\AUDIO BOOK\images\output-onlinepngtools (17).png')
OpenFolder = Button(top, text='Open Folder', bg='White', image=OpenFolderimg,command=OpenFile,compound=LEFT, width=100)
OpenFolder.place(x=730, y=370)


pc=1
def plist():
    global pc
    if pc%2==0:
        listbox.place(x=2000, y=130)
        l1.place(x=2000, y=100)
        pl.place(x=2000,y=100)
        #speed
        sl1.place(x=750, y=235)
        speed_combo.place(x=713, y=270)
        #gender
        l.place(x=500, y=235)
        gender_combo.place(x=470, y=270)
        #save
        Savebtn.place(x=490, y=370)
        #openfolder
        OpenFolder.place(x=730, y=370)

        pc+=1
    else:
        listbox.place(x=810, y=130)
        l1.place(x=850, y=100)
        pl.place(x=810,y=100)
        #speed
        sl1.place(x=650, y=235)
        speed_combo.place(x=613, y=270)
        #gender
        l.place(x=460, y=235)
        gender_combo.place(x=430, y=270)
        #save
        Savebtn.place(x=450, y=370)

        #openfolder
        OpenFolder.place(x=630, y=370)

        pc+=1

list33= PhotoImage(file='D:\AUDIO BOOK\images\output-onlinepngtools.png')#user another image
clear=Button(top,command=plist,text="list",compound=LEFT,height=0,width=4)
clear.place(x=320,y=522)

mixer.init()
music_state = StringVar()
music_state.set('choose one!')
top.mainloop()

