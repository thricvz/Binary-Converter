from tkinter import *

#fundamental function
def decimal_to_binary(entry,output):
    #condition checks if entry is not empty
    if len(entry.get()) > 0:
        decimal = int(entry.get())
        byte = list()
        rest = None
        while decimal != 0:
            rest = decimal % 2
            decimal //= 2
            byte.append(rest)
        #turning list in the right sense and completing
        byte.extend([0]*(8-len(byte)))
        byte.reverse()
        #turning the list into a string
        output.set(''.join(str(bit) for bit in byte))

def binary_to_decimal(entry,output):
    byte = entry.get()
    if len(byte) > 0:
        sum = 0
        #sum of every bit multiplied its corresponding power of 2
        for index,bit in enumerate(byte): 
            sum += int(bit) * 2 ** (len(byte)-(index+1))
        output.set(sum)

#setting window up

ROOT = Tk(className="Bit transformer")
ROOT.geometry("400x400")

FRAME =  Frame(ROOT)
FRAME.place(relx = 0.5, rely = 0.5,anchor = CENTER)

ENTRY_BOX = Entry(FRAME,width = 18)
ENTRY_BOX.pack()
OUTPUT = StringVar()

BUTTON_1 = Button(FRAME,text = "Turn into decimal",width = 15,command = lambda : binary_to_decimal(ENTRY_BOX,OUTPUT),bg = "green").pack()
BUTTON_2 = Button(FRAME,text = "Turn into binary",width = 15,command = lambda : decimal_to_binary(ENTRY_BOX,OUTPUT),bg = "red").pack()
TEXT_BOX = Label(FRAME,textvariable = OUTPUT,width = 18).pack()

ROOT.mainloop()