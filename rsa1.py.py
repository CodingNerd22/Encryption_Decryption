import tkinter as tk
import rsa 
root= tk.Tk()
root.geometry("1000x1000")
root.title(" Encryption and Decryption Project")
frame = tk.Canvas(root, width = 800, height = 600)
frame.pack()
DataEntry = tk.Entry(root, width=25, font=('calibri', 26),
               bd=2, insertwidth=4,
               bg="powder blue") 
frame.create_window(100, 40, window=DataEntry)

#===============================================
publicKey, privateKey = rsa.newkeys(512)
#===============================================
def encryptMsg ():  
    EncryptedMsg = tk.Entry (root, width=100) 
    frame.create_window(100, 80, window=EncryptedMsg)
    DecryptedMsg = tk.Entry (root, width=100) 
    frame.create_window(100, 120, window=DecryptedMsg)

    originalmessage = str(DataEntry.get())
    encMessage = rsa.encrypt(originalmessage.encode(),publicKey)
    EncryptedMsg.delete(0,"end")
    EncryptedMsg.insert(1, encMessage)
    
    decMessage = str(DataEntry.get())
    DecryptedMsg.delete(0,"end")
    DecryptedMsg.insert(1, decMessage)
       
button1 = tk.Button(text='Encrypt & Decrypt', command=lambda:encryptMsg())
frame.create_window(100, 220, window=button1)


root.mainloop()