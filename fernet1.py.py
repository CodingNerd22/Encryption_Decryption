import tkinter as tk
from cryptography.fernet import Fernet
root= tk.Tk()
root.geometry("2600x2600")
root.title(" Encryption and Decryption Project")
frame = tk.Canvas(root, width = 800, height = 600)
frame.pack()
DataEntry = tk.Entry(root, width=50, font=('calibri', 26),
               bd=2, insertwidth=4,
               bg="powder blue") 
frame.create_window(100, 40, window=DataEntry)

#===============================================
key = Fernet.generate_key()
fernet = Fernet(key)
#===============================================
def encryptMsg ():  
    EncryptedMsg = tk.Entry (root, width=100) 
    frame.create_window(100, 80, window=EncryptedMsg)
    DecryptedMsg = tk.Entry (root, width=100) 
    frame.create_window(100, 120, window=DecryptedMsg)

    originalmessage = str(DataEntry.get())
    encMessage = fernet.encrypt(originalmessage.encode())
    EncryptedMsg.delete(0,"end")
    EncryptedMsg.insert(1, encMessage)
    
    decMessage = fernet.decrypt(encMessage).decode()
    DecryptedMsg.delete(0,"end")
    DecryptedMsg.insert(1, decMessage)
       
button1 = tk.Button(text='Encrypt & Decrypt', command=lambda:encryptMsg())
frame.create_window(100, 220, window=button1)

root.mainloop()