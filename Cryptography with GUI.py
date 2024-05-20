from tkinter import *
from tkinter import messagebox

class Crypto(Frame):

    def __init__(self):

        Frame.__init__(self)
        self.master.title("Encrypt/Decrypt")
        self.pack()
       
        self.my_lbl = Label(self, text = "Cryptography ", font = ("Century", 27))
        self.my_lbl.pack(pady = 35)
        
        self.my_entryVar = StringVar()
        self.my_entry = Entry(self, font = ("Century", 15), textvariable = self.my_entryVar)    
        self.my_entry.pack(pady = 35)
                
        self.my_entryNum = IntVar()
        self.my_entrynum = Entry(self, font = ("Century", 15), textvariable = self.my_entryNum)       
        self.my_entrynum.pack(pady = 35)

        self.Btn = Button(self, text = "Encrypt", font = ("Century", 15), command = self.encrypt)
        self.Btn.pack(side = LEFT)

        self.Btn1 = Button(self, text = "Decrypt", font = ("Century", 15), command = self.decrypt)
        self.Btn1.pack(side = RIGHT)
    
    def encrypt(self):

      try:
        txt = (self.my_entryVar.get())
        num = int(self.my_entryNum.get())
        num = num%26
        enc=""
        for a in txt:
         if(ord(a))>=65 and (ord(a)<=90):
             con =(ord(a)+num)
             if con >90:
                 con = con%90+64
             enc=enc+chr(con)
         elif(ord(a))>=97 and (ord(a)<=122):
             con =(ord(a)+num)
             if con >122:
                 con = con%122+96
             enc=enc+chr(con)
         else:
             enc=enc+chr(ord(a)+num)
        
        messagebox.showinfo("Result", f"Encrpyted : {enc}")
      except ValueError:
             messagebox.showerror("Error", "Invalid format")
      Crypto.result1 = enc
    def decrypt(self):

        try:
            code = (self.my_entryVar.get())
            num = int(self.my_entryNum.get())
            num = num%26
            code = Crypto.result1
            dec=""
            for a in code:
             if((ord(a))>=65) and (ord(a))<=90:
              dec=dec+chr((ord(a) - num -65) % 26 + 65)
             elif((ord(a))>=97) and (ord(a))<=122:
              dec=dec+chr((ord(a) - num - 97) % 26 + 97)
             else:
              dec=dec+chr(ord(a)-num)

            messagebox.showinfo("Result", f"Decrypted : {dec}")

        except ValueError:
          messagebox.showerror("Error", "Invalid format")


def main():

    Crypto().mainloop()

main()
