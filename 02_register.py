from tkinter import*
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector

class Register:
    def __init__ (self,root):
        self.root = root
        self.root.title("Register")
        root.iconbitmap('Images\heartIcon.ico')
        root_width = 840
        root_height = 500
        root.geometry(f"{root_width}x{root_height}+{200}+{120}")
        #root.resizable(False,False)

        #======================Variables====================
        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_pass = StringVar()
        self.var_con_pass = StringVar()


        # --------------Image---------------
        self.my_pic = Image.open("Images/img6.jpg")

        # Resize Image
        self.resized = self.my_pic.resize((1300,800), Image.ANTIALIAS)
        self.new_pic = ImageTk.PhotoImage(self.resized)
        self.bg_image = Label(self.root, image=self.new_pic).place(x=0, y=0, relwidth=1, relheight=1)


        # ---------------Login-----------------
        Frame_Register = Frame(self.root, bg="white").place(x=100,y=120, height=300, width=655)

        #---------------Frame(Register)---------------
        title = Label(Frame_Register , text="Register Here", font=("Impact", 30, "bold"), fg="#d77337",
                      bg="white").place(x=110,y=120)

        #----------------Name------------------
        lbl_name = Label(Frame_Register ,text="Full Name", font=("times new roman", 20), fg="black",
                         bg="white").place(x=115,y=220)
        self.txt_name = Entry(Frame_Register , textvariable=self.var_name,
                              font=("times new roman", 15, "bold"), bg="lightgray")
        self.txt_name.place(x=115,y=260,width=300,height=30)

        #----------------Email------------------
        lbl_email = Label(Frame_Register, text="Email",font=("times new roman", 20), fg="black",
                         bg="white").place(x=440,y=220)
        self.email_name = Entry(Frame_Register, textvariable=self.var_email,
                                font=("times new roman", 15, "bold"), bg="lightgray")
        self.email_name.place(x=440,y=260,width=300,height=30)

        # ----------------Password------------------
        lbl_pass = Label(Frame_Register, text="Password", font=("times new roman", 20), fg="black",
                          bg="white").place(x=115,y=300)

        self.pass_name = Entry(Frame_Register,textvariable=self.var_pass,
                               font=("times new roman", 15, "bold"), bg="lightgray")
        self.pass_name.place(x=115,y=340,width=300,height=30)

        # ----------------Confirm Password------------------
        lbl_Con_pass = Label(Frame_Register, text="Confirm Password", font=("times new roman", 20), fg="black",
                         bg="white").place(x=440,y=300)

        self.Con_pass = Entry(Frame_Register, textvariable=self.var_con_pass,
                               font=("times new roman", 15, "bold"), bg="lightgray")
        self.Con_pass .place(x=440,y=340,width=300,height=30)

        # -----------------Register Button-------------------
        Register_btn = Button(self.root, cursor="hand2",command=self.register_data, text="Register", fg="white",
                           bg="#d77337", font=("times new roman", 20), activebackground="red3",
                           activeforeground="black").place(x=440, y=395)

        # -----------------Login Button-------------------
        Login_btn = Button(self.root, cursor="hand2", text="Login Now", fg="white",
                           bg="cyan4", font=("times new roman", 20), activebackground="green4",
                           activeforeground="black").place(x=570, y=395)

    #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxFunction declarationxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

    def register_data(self):
        if self.var_name.get()=="" or self.var_email.get()=="" or self.var_pass.get()=="" or \
                self.var_con_pass.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.var_pass.get()!= self.var_con_pass.get():
            messagebox.showerror("Error","Password & Confirm Password must be same")
        else:
            conn = mysql.connector.connect(host="localhost",user="root",password="Jarus@2k0",database="sys")
            my_cursor=conn.cursor()
            query = ("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row = my_cursor.fetchone()
            if row!= None:
                messagebox.showerror("Error","already exist")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s)",(
                                                                            self.var_name.get(),
                                                                            self.var_email.get(),
                                                                            self.var_pass.get(),
                                                                            ))
                messagebox.showinfo("Welcome", "Register Scuccesfully")
            conn.commit()
            conn.close()


root = Tk()
app = Register(root)
root.mainloop()
