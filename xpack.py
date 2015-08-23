from Tkinter import *
from tkMessageBox import *
import o

def terminal(command, place):
     wid = place.winfo_id()
     os.system('xterm -into '+str(wid)+' -geometry 90x30 -sb -rightbar -fa \'Monospace\' -hold -bg black -fg aqua -e "'+command+'" &') 
def upgrade():
     if askyesno('Verify', 'Do you really want to start an upgrade?'):
          os.system('sudo killall pacman')
          os.system('sudo killall packer')
          terminal('sudo pacman -Syu', termf)
     else:
          showinfo('No', 'Upgrade has been cancelled!')
def search():
     if askyesno('Verify', 'Do you really want to search(it can cancel other running processes)?'):
          os.system('sudo killall pacman')
          os.system('sudo killall packer')
          terminal('packer -Ss '+searchbox.get(), termf)
     else:
          showinfo('No', 'Search has been cancelled!')
def install():
     if askyesno('Verify', 'Do you really want to start an install '+installbox.get()+'?'):
          os.system('sudo killall pacman')
          os.system('sudo killall packer')
          terminal('packer -S '+installbox.get(), termf)
     else:
          showinfo('No', 'Installation has been cancelled!')
def remove():
     if askyesno('Verify', 'Do you really want to start an remove '+removebox.get()+'?'):
          os.system('sudo killall pacman')
          os.system('sudo killall packer')
          terminal('sudo pacman -Rs '+removebox.get(), termf)
     else:
          showinfo('No', 'Removal has been cancelled!')
def home():
     if askyesno('Verify', 'Do you really want to terminate the currently running process?'):
          os.system('sudo killall pacman')
          os.system('sudo killall packer')
          terminal('python home.py', termf)
     else:
          showinfo('No', 'Close all has been cancelled!')

root = Tk(className=" XPack package manager")
root.config(bg="white")

Label(root, text="XPack package manager", font = "Helvetica 18 bold", bg="white").pack()

termf = Frame(root, height=400, width=564)
termf.config(bg="white")
termf.pack(fill=BOTH, expand=YES)

button = Button(root, bg="white", text='Close all', width=67, command=home)
button.pack()
button = Button(root, bg="white", text='Upgrade', width=67, command=upgrade)
button.pack()

frame = Frame(root)
frame.config(bg="white")
frame.pack()

searchbox = Entry(frame, width=61)
searchbox.pack(side=LEFT)
button = Button(frame, bg="white", text='Search', command=search)
button.pack(side=LEFT)

frame2 = Frame(root)
frame2.config(bg="white")
frame2.pack()

installbox = Entry(frame2, width=62)
installbox.pack(side=LEFT)
button = Button(frame2, bg="white", text='Install', command=install)
button.pack(side=LEFT)

frame3 = Frame(root)
frame3.config(bg="white")
frame3.pack()

removebox = Entry(frame3, width=60)
removebox.pack(side=LEFT)
button = Button(frame3, bg="white", text='Remove', command=remove)
button.pack(side=LEFT)

terminal('python home.py', termf)
root.mainloop()
