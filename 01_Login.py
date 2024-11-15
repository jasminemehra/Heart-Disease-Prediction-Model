#!/usr/bin/env python
# coding: utf-8

# In[4]:


import mysql.connector
from tkinter import*
from PIL import ImageTk,Image
from tkinter import messagebox
import joblib

def main():
    win = Tk()
    app = Login_Window(win)
    win.mainloop()
class Login_Window:
    def __init__(self,master):
        self.master= master
        self.master.title("Login")
        master.geometry('1200x600')
        master.iconbitmap('Images\heartIcon.ico')
        master_width = 1200
        master_height= 600
        master.geometry(f"{master_width}x{master_height}+{30}+{20}")

        #--------------Image---------------
        self.my_pic = Image.open("Images/img7.jpg")

        # Resize Image
        self.resized = self.my_pic.resize((1300,800),Image.ANTIALIAS)
        self.new_pic = ImageTk.PhotoImage(self.resized)
        self.bg_image=Label(self.master,image=self.new_pic).place(x=0,y=0,relwidth=1,relheight=1)

        #---------------Login-----------------
        Frame_login=Frame(self.master,bg="white").place(x=100,y=120,height=340,width=450)

        title = Label(Frame_login,text="Login Here",font=("Impact",35,"bold"),fg="#d77337",
                      bg="white").place(x=110,y=120)

        lbl_user = Label(Frame_login,text="Email",font=("times new roman",20),fg="black",
                                bg="white").place(x=115,y=220)

        self.txt_user=Entry(Frame_login,font=("times new roman",15,"bold"),bg="lightgray")
        self.txt_user.place(x=115,y=260,width=390,height=30)

        #----------------Password----------------
        lbl_pass = Label(Frame_login,text="Password",font=("times new roman",20),fg="black",
                         bg="white").place(x=115,y=300)
        self.txt_pass=Entry(Frame_login,font=("times new roman",15,"bold"),
                            bg="lightgray",show="*")
        self.txt_pass.place(x=115,y=340,width=390,height=30)

        #--------------Forgot Password Button-----------
        forget_btn=Button(Frame_login,text="Forget Password?",cursor="hand2",
                          bg="white",fg="#d77337",bd=0,font=("times new roman",12),
                          activeforeground="green",activebackground="white",).place(x=112,y=380)

        #-----------------Login Button-------------------
        Login_btn=Button(self.master,command=self.login_fun,cursor="hand2",text="Login",fg="white",
                         bg="#d77337",font=("times new roman",20),activebackground="green4",
                           activeforeground="black").place(x=290,y=430)

        #----------------Sign Up Button-----------------
        Register_btn = Button(Frame_login, text="Sign up", cursor="hand2",command=self.register_window,
                            bg="white", fg="#d77337", bd=0, font=("times new roman", 12),
                            activeforeground="green", activebackground="white", ).place(x=450, y=380)
    def register_window(self):
        self.new_window=Toplevel(self.master)
        self.app=Register(self.new_window)

    def login_fun(self):

        if self.txt_pass.get()=="" or self.txt_user.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.master)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="Jarus@2k0", database="sys")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where email=%s and pass =%s ",(
                                                                    self.txt_user.get(),
                                                                    self.txt_pass.get(),
            ))

            row = my_cursor.fetchone()

            if row == None:
                messagebox.showerror("Error","Invalid User Name & Password")
            else:
                open_main= messagebox.askyesno("YesNo","Do you wnat to Log in")
                if open_main>0:
                    self.new_window= Toplevel(self.master)
                    self.app = Heart(self.new_window)

                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()



# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    REGISTER    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
class Register:
    def __init__ (self,root):
        self.root = root
        self.root.title("Register")
        root.iconbitmap('Images\heartIcon.ico')
        master_width = 840
        master_height = 500
        root.geometry(f"{master_width}x{master_height}+{200}+{85}")
        #root.resizable(False,False)

        #======================Variables====================
        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_pass = StringVar()
        self.var_con_pass = StringVar()


        # --------------Image---------------
        self.my_pic = Image.open("Images/img8.jpg")

        # Resize Image
        self.resized = self.my_pic.resize((1300,800), Image.ANTIALIAS)
        self.new_pic = ImageTk.PhotoImage(self.resized)
        self.bg_image = Label(self.root, image=self.new_pic).place(x=0, y=0, relwidth=1, relheight=1)


        # ---------------Login-----------------
        Frame_Register = Frame(self.root, bg="white").place(x=100,y=120, height=300, width=655)

        #---------------Frame(Register)---------------
        title = Label(self.root, text="Register Here", font=("Impact", 30, "bold"), fg="#d77337",
                      bg="white").place(x=110,y=120)

        #----------------Name------------------
        lbl_name = Label(self.root,text="Full Name", font=("times new roman", 20), fg="black",
                         bg="white").place(x=115,y=220)
        self.txt_name = Entry(self.root , textvariable=self.var_name,
                              font=("times new roman", 15, "bold"), bg="lightgray")
        self.txt_name.place(x=115,y=260,width=300,height=30)

        #----------------Email------------------
        lbl_email = Label(self.root, text="Email",font=("times new roman", 20), fg="black",
                         bg="white").place(x=440,y=220)
        self.email_name = Entry(self.root, textvariable=self.var_email,
                                font=("times new roman", 15, "bold"), bg="lightgray")
        self.email_name.place(x=440,y=260,width=300,height=30)

        # ----------------Password------------------
        lbl_pass = Label(self.root, text="Password", font=("times new roman", 20), fg="black",
                          bg="white").place(x=115,y=300)

        self.pass_name = Entry(self.root,textvariable=self.var_pass,
                               font=("times new roman", 15, "bold"), bg="lightgray")
        self.pass_name.place(x=115,y=340,width=300,height=30)

        # ----------------Confirm Password------------------
        lbl_Con_pass = Label(self.root, text="Confirm Password", font=("times new roman", 20), fg="black",
                         bg="white").place(x=440,y=300)

        self.Con_pass = Entry(self.root, textvariable=self.var_con_pass,
                               font=("times new roman", 15, "bold"), bg="lightgray")
        self.Con_pass .place(x=440,y=340,width=300,height=30)

        # -----------------Register Button-------------------
        Register_btn = Button(self.root, cursor="hand2",command=self.register_data, text="Register", fg="white",
                           bg="#d77337", font=("times new roman", 20), activebackground="red3",
                           activeforeground="black").place(x=440, y=395)

        # -----------------LoginButton-------------------
        Login_btn = Button(self.root, cursor="hand2", command=self.return_login, text="Login Now", fg="white",
                              bg="cyan4", font=("times new roman", 20), activebackground="green4",
                              activeforeground="black").place(x=570, y=395)



    #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxFunction declarationxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

    def register_data(self):
        if self.var_name.get()=="" or self.var_email.get()=="" or self.var_pass.get()=="" or self.var_con_pass.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.var_pass.get()!= self.var_con_pass.get():
            messagebox.showerror("Error","Password & Confirm Password must be same",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost",user="root",password="Jarus@2k0",database="sys")
            my_cursor=conn.cursor()
            query = ("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row = my_cursor.fetchone()
            if row!= None:
                messagebox.showerror("Error","already exist",parent=self.root)
            else:
                my_cursor.execute("insert into register values(%s,%s,%s)",(
                                                                            self.var_name.get(),
                                                                            self.var_email.get(),
                                                                            self.var_pass.get(),
                                                                            ))
                messagebox.showinfo("Success", "Succesfully Registered", parent=self.root)
            conn.commit()
            conn.close()

    def return_login(self):
        self.root.destroy()

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx     HEART     xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

class Heart:
    def __init__ (self, suraj):
        self.suraj = suraj
        suraj_width = 1200
        suraj_height = 600
        suraj.geometry(f"{suraj_width}x{suraj_height}+{30}+{20}")
        #suraj.config(bg="#0096DC")
        suraj.title("Signature Verification")
        suraj.iconbitmap('Images/heartIcon.ico')

        self.my_pic = Image.open("Images/img3.jpg")

        # Resize Image
        self.resized = self.my_pic.resize((1300, 800), Image.ANTIALIAS)
        self.new_pic = ImageTk.PhotoImage(self.resized)
        self.bg_image = Label(suraj, image=self.new_pic).place(x=0, y=0, relwidth=1, relheight=1)

        self.label = Label(self.suraj, text="S I G N A T U R E  V E R I F I C A T I O N", font=("Impact", 35, "bold"), fg="#d77337",
              bg="white").place(x=180, y=20)

        # ----------------Frame-----------------------

        Frame_login = Frame(self.suraj, bg="#7F7FFF").place(x=70, y=110, height=495, width=970)

        # ----------------Age-----------------------
        Label(self.suraj, text="1. Enter Your Age", font=("times new roman", 20, "bold"), fg="black",
             bg="#F0F0F8", borderwidth=1, relief="solid").place(x=85, y=120)
        self.e1 = Entry(self.suraj, cursor="hand2", borderwidth=1, relief="solid")
        self.e1.place(x=400, y=130, height=23)

        # ----------------Gender-----------------------
        Label(self.suraj, text="2. Male Or Female [1/0]", font=("times new roman", 20, "bold"), fg="black",
            bg="#F0F0F8", borderwidth=1, relief="solid").place(x=85, y=175)
        self.e2 = Entry(self.suraj, cursor="hand2", borderwidth=1, relief="solid")
        self.e2.place(x=400, y=185, height=23)

        #------------------CP---------------------
        Label(self.suraj, text="3. Enter Value of CP", font=("times new roman", 20, "bold"), fg="black",
            bg="#F0F0F8", borderwidth=1, relief="solid").place(x=85, y=230)
        self.e3 = Entry(self.suraj, cursor="hand2", borderwidth=1, relief="solid")
        self.e3.place(x=400, y=240, height=23)

        # ------------------trestbps---------------------
        Label(self.suraj, text="4. Enter Value of trestbps", font=("times new roman", 20, "bold"), fg="black",
            bg="#F0F0F8", borderwidth=1, relief="solid").place(x=85, y=285)
        self.e4 = Entry(self.suraj, cursor="hand2", borderwidth=1, relief="solid")
        self.e4.place(x=400, y=295, height=23)

        # ------------------chol---------------------
        Label(self.suraj, text="5. Enter Value of chol", font=("times new roman", 20, "bold"), fg="black",
            bg="#F0F0F8", borderwidth=1, relief="solid").place(x=85, y=340)
        self.e5 = Entry(self.suraj, cursor="hand2", borderwidth=1, relief="solid")
        self.e5.place(x=400, y=350, height=23)

        # ------------------fbs---------------------
        Label(self.suraj, text="6. Enter Value of fbs", font=("times new roman", 20, "bold"), fg="black",
             bg="#F0F0F8", borderwidth=1, relief="solid").place(x=85, y=395)
        self.e6 = Entry(self.suraj, cursor="hand2", borderwidth=1, relief="solid")
        self.e6.place(x=400, y=405, height=23)

        # ------------------restecg---------------------
        Label(self.suraj, text="7. Enter Value of restecg", font=("times new roman", 20, "bold"), fg="black",
            bg="#F0F0F8", borderwidth=1, relief="solid").place(x=85, y=450)
        self.e7 = Entry(self.suraj, cursor="hand2", borderwidth=1, relief="solid")
        self.e7.place(x=400, y=460, height=23)

        # -------------------thalach--------------------
        Label(self.suraj, text="8. Enter Value of thalach", font=("times new roman", 20, "bold"), fg="black",
            bg="#F0F0F8", borderwidth=1, relief="solid").place(x=85, y=505)
        self.e8 = Entry(self.suraj, cursor="hand2", borderwidth=1, relief="solid")
        self.e8.place(x=400, y=515, height=23)

        # -------------------exang--------------------
        Label(self.suraj, text="9. Enter Value of exang", font=("times new roman", 20, "bold"), fg="black",
             bg="#F0F0F8", borderwidth=1, relief="solid").place(x=85, y=560)
        self.e9 = Entry(self.suraj, cursor="hand2", borderwidth=1, relief="solid")
        self.e9.place(x=400, y=570, height=23)

        # -------------------oldpeak--------------------
        Label(self.suraj, text="10. Enter Value of oldpeak", font=("times new roman", 20, "bold"), fg="black",
            bg="#F0F0F8", borderwidth=1, relief="solid").place(x=570, y=120)
        self.e10 = Entry(self.suraj, cursor="hand2", borderwidth=1, relief="solid")
        self.e10.place(x=900, y=130, height=23)

        # -------------------slope--------------------
        Label(self.suraj, text="11. Enter Value of slope", font=("times new roman", 20, "bold"), fg="black",
            bg="#F0F0F8", borderwidth=1, relief="solid").place(x=570, y=175)
        self.e11 = Entry(self.suraj, cursor="hand2", borderwidth=1, relief="solid")
        self.e11.place(x=900, y=185, height=23)

        # -------------------ca--------------------
        Label(self.suraj, text="12. Enter Value of ca", font=("times new roman", 20, "bold"), fg="black",
            bg="#F0F0F8", borderwidth=1, relief="solid").place(x=570, y=230)
        self.e12 = Entry(self.suraj, cursor="hand2", borderwidth=1, relief="solid")
        self.e12.place(x=900, y=240, height=23)

        # -------------------thal--------------------
        Label(self.suraj, text="13. Enter Value of thal", font=("times new roman", 20, "bold"), fg="black",
            bg="#F0F0F8", borderwidth=1, relief="solid").place(x=570, y=285)
        self.e13 = Entry(self.suraj, cursor="hand2", borderwidth=1, relief="solid")
        self.e13.place(x=900, y=295, height=23)

        # -------------------RESULT-----------------------


        Label(self.suraj, text="Result: ", font=("times new roman", 25, "bold"), fg="black",
            bg="#7F7FFF").place(x=640, y=440)
        self.But1 = Button(self.suraj, text='Submit', command=self.entry, bd='7', activebackground='green', fg="green", bg="white",
            font=("Arial", 12), cursor="hand2").place(x=800, y=540)

        self.exit_button = Button(self.suraj, text="EXIT", fg="red", bd='7', bg="white",
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


main()


# In[ ]:




