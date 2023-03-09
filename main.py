import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *
from PIL import Image,ImageTk


class Face_detection_system:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1500x710+0+0")
        self.root.title("Smart Attendence")

# background image 
        img1 = Image.open("D:/Bca/Smart_Attendance/Images/backg.jpg")
        img1=img1.resize((1400,710),Image.ADAPTIVE)
        self.photoimg = ImageTk.PhotoImage(img1)

        bg_img =Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,width=1400 ,height=710)

        # title
        title_label = Label(bg_img,text="Smart Attendence System",bg="white",font=("times new roman",35,"bold"),fg="green")
        title_label.place(x=0,y=0,width=1500,height=45)

        #  button1 stusent
        img2 = Image.open("D:/Bca/Smart_Attendance/Images/student.jpg")
        img2=img2.resize((220,220),Image.ADAPTIVE)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        b1 =Button(bg_img,image=self.photoimg2,cursor="hand2")
        b1.place(x=100,y=80,width=220,height=220)

        
        b1 =Button(bg_img,text="Student Details",cursor="hand2",bg="black",font=("times new roman",15,"bold"),fg="green")
        b1.place(x=100,y=280,width=220,height=40)

         #  button2 face
        img3 = Image.open("D:/Bca/Smart_Attendance/Images/face.jpg")
        img3=img3.resize((220,220),Image.ADAPTIVE)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        b2 =Button(bg_img,image=self.photoimg3,cursor="hand2")
        b2.place(x=400,y=80,width=220,height=220)

        
        b2 =Button(bg_img,text="Face Detector",cursor="hand2",bg="black",font=("times new roman",15,"bold"),fg="green")
        b2.place(x=400,y=280,width=220,height=40)

         #  button4 Attentence
        img4 = Image.open("D:/Bca/Smart_Attendance/Images/attentence.jpg")
        img4=img4.resize((220,220),Image.ADAPTIVE)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b3 =Button(bg_img,image=self.photoimg4,cursor="hand2")
        b3.place(x=700,y=80,width=220,height=220)

        
        b3 =Button(bg_img,text="Attendance",cursor="hand2",bg="black",font=("times new roman",15,"bold"),fg="green")
        b3.place(x=700,y=280,width=220,height=40)


        
         #  button5 Train Image
        img5 = Image.open("D:/Bca/Smart_Attendance/Images/download.jpg")
        img5=img5.resize((220,220),Image.ADAPTIVE)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b4 =Button(bg_img,image=self.photoimg5,cursor="hand2")
        b4.place(x=1000,y=80,width=220,height=220)

        
        b4 =Button(bg_img,text="Train Image",cursor="hand2",bg="black",font=("times new roman",15,"bold"),fg="green")
        b4.place(x=1000,y=280,width=220,height=40)

        
         #  button6 Exit
        img6 = Image.open("D:/Bca/Smart_Attendance/Images/view.jpg")
        img6=img6.resize((220,220),Image.ADAPTIVE)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b5 =Button(bg_img,image=self.photoimg6,cursor="hand2")
        b5.place(x=100,y=360,width=220,height=220)

        
        b5 =Button(bg_img,text="View Attendence",cursor="hand2",bg="black",font=("times new roman",15,"bold"),fg="green")
        b5.place(x=100,y=560,width=220,height=40)

           #  button7 
        img7 = Image.open("D:/Bca/Smart_Attendance/Images/exit.jpg")
        img7=img7.resize((220,220),Image.ADAPTIVE)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b6 =Button(bg_img,image=self.photoimg7,cursor="hand2")
        b6.place(x=400,y=360,width=220,height=220)

        
        b6 =Button(bg_img,text="Exit",cursor="hand2",bg="black",font=("times new roman",15,"bold"),fg="green")
        b6.place(x=400,y=560,width=220,height=40)


if __name__  == "__main__" :
    root = Tk()
    obj = Face_detection_system(root)
    root.mainloop()
 