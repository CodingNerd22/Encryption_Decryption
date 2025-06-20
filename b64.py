from tkinter import *

import random

import base64
from tkinter import font


root = Tk()


root.geometry("1600x800")


root.title(" Encryption and Decryption Project")

Tops = Frame(root, width=1600, relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width=800, relief=SUNKEN)
f1.pack(side=LEFT)

# ==============================================


lblInfo = Label(Tops, font=('times', 50, ),
                text="Encryption And Decryption ",
                fg="black", bd=5, anchor='e')

lblInfo.grid(row=100, column=0)



Msg = StringVar()
key = StringVar()
mode = StringVar()
Result = StringVar()



lblMsg = Label(f1, font=('Constantia', 16, ),
               text="Message", bd=16, anchor="e")

lblMsg.grid(row=0, column=0)

# Entry box- message
txtMsg = Entry(f1, font=('Constantia', 16, ),
               textvariable=Msg, bd=2, insertwidth=4,
               bg="powder blue", justify='left')


txtMsg.grid(row=0, column=1)

# labels - key
lblkey = Label(f1, font=('Constantia', 16, ),
               text="KEY ", bd=16, anchor="e")

lblkey.grid(row=2, column=0)



# Entry box - key
txtkey = Entry(f1, font=('Constantia', 16, ),
               textvariable=key, bd=2, insertwidth=4,
               bg="powder blue", justify='left')

txtkey.grid(row=2, column=1)
txtkey.insert(0,"Only integer")

# labels -mode
lblmode = Label(f1, font=('Constantia', 16, ),
                text="MODE",
                bd=16, anchor="e")

lblmode.grid(row=3, column=0)
# Entry box - mode
txtmode = Entry(f1, font=('Constantia', 16 ),
                textvariable=mode, bd=2, insertwidth=8,
                bg="powder blue", justify='left')

txtmode.grid(row=3, column=1)

txtmode.insert(0,"e for encrypt,d for decrypt")

# labels - result
lblResult = Label(f1, font=('Constantia', 16, ),
                  text="The Result-", bd=16, anchor="e")

lblResult.grid(row=2, column=2)

# Entry box - result
txtResult = Entry(f1, font=('Constantia', 16, ),
                  textvariable=Result, bd=2, insertwidth=4,
                  bg="powder blue", justify='left')

txtResult.grid(row=2, column=3)

# Function to encode


def encode(key, msg):
    enc = []
    for i in range(len(msg)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(msg[i]) +
                     ord(key_c)) % 256)
        enc.append(enc_c)
        print("enc:", enc)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

# Function to decode


def decode(key, enc):
    dec = []

    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) -
                     ord(key_c)) % 256)

        dec.append(dec_c)
        print("dec:", dec)
    return "".join(dec)


def Results():


    msg = Msg.get()
    k = key.get()
    m = mode.get()

    if (m == 'e'):
        Result.set(encode(k, msg))
    else:
        Result.set(decode(k, msg))

# exit function


def qExit():
    root.destroy()

# Function to reset the window


def Reset():

    Msg.set("")
    key.set("")
    mode.set("")
    Result.set("")


# Show message button
btnTotal = Button(f1, padx=16, pady=8, bd=10, fg="black",
                  font=('Constantia', 26, ), width=10,
                  text="Show Message", bg="black",
                  command=Results).grid(row=30, column=0, pady=50)

# Reset button
btnReset = Button(f1, padx=16, pady=8, bd=10,
                  fg="black", font=('Constantia', 26, ),
                  width=10, text="Reset", bg="#FFFFFF",
                  command=Reset).grid(row=30, column=2)

# Exit button
btnExit = Button(f1, padx=16, pady=8, bd=10,
                 fg="black", font=('Constantia', 26, ),
                 width=10, text="Exit", bg="#FFFFFF",
                 command=qExit).grid(row=30, column=4)


root.mainloop()
