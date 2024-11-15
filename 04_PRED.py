#!/usr/bin/env python
# coding: utf-8

# In[11]:


from tkinter import *
import joblib
from PIL import ImageTk, Image
import numpy as np
from sklearn import *
from tkinter import messagebox


class Heart:
    def __init__ (self,suraj):
        self.suraj = suraj
        suraj_width = 1200
        suraj_height = 650
        suraj.geometry(f"{suraj_width}x{suraj_height}+{30}+{0}")
        #suraj.config(bg="#0096DC")
        suraj.title("Heart Disease Prediction")
        suraj.iconbitmap('Images/heartIcon.ico')

        self.my_pic = Image.open("Images/img3.jpg")

        # Resize Image
        self.resized = self.my_pic.resize((1300, 800))
        self.new_pic = ImageTk.PhotoImage(self.resized)
        bg_image = Label(suraj, image=self.new_pic).place(x=0, y=0, relwidth=1, relheight=1)

        label = Label(suraj, text="H E A R T   D I S E A S E   P R E D I C T I O N", font=("Impact", 35, "bold"), fg="#d77337",
              bg="white").place(x=180, y=20)

        # ----------------Frame-----------------------

        Frame_login = Frame(suraj, bg="#7F7FFF").place(x=70, y=110, height=495, width=970)

        # ----------------Age-----------------------
        Label(suraj, text="1. Enter Your Age", font=("times new roman", 20, "bold"), fg="black",
             bg="#F0F0F8", borderwidth=1, relief="solid").place(x=85, y=120)
        self.e1 = Entry(suraj, cursor="hand2", borderwidth=1, relief="solid")
        self.e1.place(x=400, y=130, height=23)

        # ----------------Gender-----------------------
        Label(suraj, text="2. Male Or Female [1/0]", font=("times new roman", 20, "bold"), fg="black",
            bg="#F0F0F8", borderwidth=1, relief="solid").place(x=85, y=175)
        self.e2 = Entry(suraj, cursor="hand2", borderwidth=1, relief="solid")
        self.e2.place(x=400, y=185, height=23)

        #------------------CP---------------------
        Label(suraj, text="3. Enter Value of CP", font=("times new roman", 20, "bold"), fg="black",
            bg="#F0F0F8", borderwidth=1, relief="solid").place(x=85, y=230)
        self.e3 = Entry(suraj, cursor="hand2", borderwidth=1, relief="solid")
        self.e3.place(x=400, y=240, height=23)

        # ------------------trestbps---------------------
        Label(suraj, text="4. Enter Value of trestbps", font=("times new roman", 20, "bold"), fg="black",
            bg="#F0F0F8", borderwidth=1, relief="solid").place(x=85, y=285)
        self.e4 = Entry(suraj, cursor="hand2", borderwidth=1, relief="solid")
        self.e4.place(x=400, y=295, height=23)

        # ------------------chol---------------------
        Label(suraj, text="5. Enter Value of chol", font=("times new roman", 20, "bold"), fg="black",
            bg="#F0F0F8", borderwidth=1, relief="solid").place(x=85, y=340)
        self.e5 = Entry(suraj, cursor="hand2", borderwidth=1, relief="solid")
        self.e5.place(x=400, y=350, height=23)

        # ------------------fbs---------------------
        Label(suraj, text="6. Enter Value of fbs", font=("times new roman", 20, "bold"), fg="black",
             bg="#F0F0F8", borderwidth=1, relief="solid").place(x=85, y=395)
        self.e6 = Entry(suraj, cursor="hand2", borderwidth=1, relief="solid")
        self.e6.place(x=400, y=405, height=23)

        # ------------------restecg---------------------
        Label(suraj, text="7. Enter Value of restecg", font=("times new roman", 20, "bold"), fg="black",
            bg="#F0F0F8", borderwidth=1, relief="solid").place(x=85, y=450)
        self.e7 = Entry(suraj, cursor="hand2", borderwidth=1, relief="solid")
        self.e7.place(x=400, y=460, height=23)

        # -------------------thalach--------------------
        Label(suraj, text="8. Enter Value of thalach", font=("times new roman", 20, "bold"), fg="black",
            bg="#F0F0F8", borderwidth=1, relief="solid").place(x=85, y=505)
        self.e8 = Entry(suraj, cursor="hand2", borderwidth=1, relief="solid")
        self.e8.place(x=400, y=515, height=23)

        # -------------------exang--------------------
        Label(suraj, text="9. Enter Value of exang", font=("times new roman", 20, "bold"), fg="black",
             bg="#F0F0F8", borderwidth=1, relief="solid").place(x=85, y=560)
        self.e9 = Entry(suraj, cursor="hand2", borderwidth=1, relief="solid")
        self.e9.place(x=400, y=570, height=23)

        # -------------------oldpeak--------------------
        Label(suraj, text="10. Enter Value of oldpeak", font=("times new roman", 20, "bold"), fg="black",
            bg="#F0F0F8", borderwidth=1, relief="solid").place(x=570, y=120)
        self.e10 = Entry(suraj, cursor="hand2", borderwidth=1, relief="solid")
        self.e10.place(x=900, y=130, height=23)

        # -------------------slope--------------------
        Label(suraj, text="11. Enter Value of slope", font=("times new roman", 20, "bold"), fg="black",
            bg="#F0F0F8", borderwidth=1, relief="solid").place(x=570, y=175)
        self.e11 = Entry(suraj, cursor="hand2", borderwidth=1, relief="solid")
        self.e11.place(x=900, y=185, height=23)

        # -------------------ca--------------------
        Label(suraj, text="12. Enter Value of ca", font=("times new roman", 20, "bold"), fg="black",
            bg="#F0F0F8", borderwidth=1, relief="solid").place(x=570, y=230)
        self.e12 = Entry(suraj, cursor="hand2", borderwidth=1, relief="solid")
        self.e12.place(x=900, y=240, height=23)

        # -------------------thal--------------------
        Label(suraj, text="13. Enter Value of thal", font=("times new roman", 20, "bold"), fg="black",
            bg="#F0F0F8", borderwidth=1, relief="solid").place(x=570, y=285)
        self.e13 = Entry(suraj, cursor="hand2", borderwidth=1, relief="solid")
        self.e13.place(x=900, y=295, height=23)

        # -------------------RESULT-----------------------


        Label(suraj, text="Result: ", font=("times new roman", 25, "bold"), fg="black",
            bg="#7F7FFF").place(x=640, y=440)
        self.But1 = Button(suraj, text='Submit', command=self.entry, bd='7', activebackground='green', fg="green", bg="white",
            font=("Arial", 12), cursor="hand2").place(x=800, y=540)

        self.exit_button = Button(suraj, text="EXIT", fg="red", bd='7', bg="white",
                     activebackground="red", font=("Classy Button", 14), cursor="hand2", command=self.ExitApplication)
        self.exit_button.place(x=1100, y=580)

    def ExitApplication(self):
        self.box = messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application ?',
                                 icon='warning')

        if self.box == 'yes':
            self.suraj.destroy()

    def entry(self):
        try:
            p1 = int(self.e1.get())
            p2 = int(self.e2.get())
            p3 = int(self.e3.get())
            p4 = int(self.e4.get())
            p5 = int(self.e5.get())
            p6 = int(self.e6.get())
            p7 = int(self.e7.get())
            p8 = int(self.e8.get())
            p9 = int(self.e9.get())
            p10 = float(self.e10.get())
            p11 = int(self.e11.get())
            p12 = int(self.e12.get())
            p13 = int(self.e13.get())

        except:
            messagebox.showerror("Empty Fields", 'All Fields Are Mandatory !', icon='warning')

        self.model = joblib.load('model_joblib_heart')
        self.result = self.model.predict([[p1, p2, p3, p4, p5, p6, p7, p8, p8, p10, p11, p12, p13]])

        if self.result == 0:
            Label(self.suraj, text="No Heart Disease", font=("times new roman", 25, "bold"), fg="black",
                  bg="#7F7FFF", foreground="green").place(x=750, y=440)
        else:
            Label(self.suraj, text="Possibility \nof Heart Disease", font=("times new roman", 25, "bold"), fg="black",
                  bg="#7F7FFF", foreground="red").place(x=750, y=440)


suraj = Tk()
app = Heart(suraj)
mainloop()

# In[ ]:


# In[ ]:
