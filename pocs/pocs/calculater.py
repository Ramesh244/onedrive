##Calculator GUI 
##
##It is GUI based calculator used to calculate any simple mathematical equation. 
##
#### Modules Used 
##
##- tkinter 
##
#### How it works 
##
##- It takes the mathematical equation by the User. 
##
## 
##
##- It returns the result of the mathematical equation 

##import Tkinter
##top = Tkinter.Tk()
##top.mainloop()


##from tkinter import *
##
##win = Tk() 
##win.geometry("300x400")  
##win.resizable(0, 0)
##win.title("Calculator")
##
##def btn_click(item):
##    global expression
##    expression = expression + str(item)
##    input_text.set(expression)
##
##def bt_clear(): 
##    global expression 
##    expression = "" 
##    input_text.set("")
## 
##def bt_equal():
##    global expression
##    result = str(eval(expression))
##    input_text.set(result)
##    expression = ""
## 
##expression = ""
## 
### 'StringVar()' :It is used to get the instance of input field
## 
##input_text = StringVar()
## 
### Let us creating a frame for the input field
## 
##input_frame = Frame(win, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
## 
##input_frame.pack(side=TOP)
## 
###Let us create a input field inside the 'Frame'
## 
##input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0, justify=RIGHT)
## 
##input_field.grid(row=0, column=0)
## 
##input_field.pack(ipady=10) # 'ipady' is internal padding to increase the height of input field
## 
###Let us creating another 'Frame' for the button below the 'input_frame'
## 
##btns_frame = Frame(win, width=312, height=272.5, bg="grey")
## 
##btns_frame.pack()
## 
### first row
## 
##clear = Button(btns_frame, text = "C", fg = "black", width = 32, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: bt_clear()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)
## 
##divide = Button(btns_frame, text = "/", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("/")).grid(row = 0, column = 3, padx = 1, pady = 1)
## 
### second row
## 
##seven = Button(btns_frame, text = "7", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(7)).grid(row = 1, column = 0, padx = 1, pady = 1)
## 
##eight = Button(btns_frame, text = "8", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
## 
##nine = Button(btns_frame, text = "9", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(9)).grid(row = 1, column = 2, padx = 1, pady = 1)
## 
##multiply = Button(btns_frame, text = "*", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("*")).grid(row = 1, column = 3, padx = 1, pady = 1)
## 
### third row
## 
##four = Button(btns_frame, text = "4", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
## 
##five = Button(btns_frame, text = "5", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
## 
##six = Button(btns_frame, text = "6", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
## 
##minus = Button(btns_frame, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("-")).grid(row = 2, column = 3, padx = 1, pady = 1)
## 
### fourth row
## 
##one = Button(btns_frame, text = "1", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
## 
##two = Button(btns_frame, text = "2", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
## 
##three = Button(btns_frame, text = "3", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(3)).grid(row = 3, column = 2, padx = 1, pady = 1)
## 
##plus = Button(btns_frame, text = "+", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("+")).grid(row = 3, column = 3, padx = 1, pady = 1)
## 
### fourth row
## 
##zero = Button(btns_frame, text = "0", fg = "black", width = 21, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(0)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
## 
##point = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click(".")).grid(row = 4, column = 2, padx = 1, pady = 1)
## 
##equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: bt_equal()).grid(row = 4, column = 3, padx = 1, pady = 1)
## 
##win.mainloop()
##


import tkinter as tk
from tkinter import *
app = tk.Tk()
app.geometry("170x230")
app.title("python-calculator")
app.maxsize(200,230)
app.minsize(200,230)
ent = Entry(app, width=16, borderwidth=4, relief=RIDGE)
ent.grid(pady=10,row=0,sticky="w",padx=15)
def delete():
        a = ent.get()
        ent.delete(first=len(a)-1,last="end")
def fresult():
        if ent.get() == "":
                pass
        elif ent.get()[0] == "0":
                ent.delete(0,"end")
        else:
                c_res = ent.get()
                c_res = eval(c_res)
                clearf()
                ent.insert("end",c_res)
def clearf():
        ent.delete(0,"end")
clean = Button(app,text="C",width=2,command=clearf,bg="green",fg="white",relief=RIDGE)
clean.grid(row=0,sticky="w",padx=125)
Char_nine = Button(text="9",width=2,command=lambda : ent.insert("end","9"),borderwidth=3,relief=RIDGE)
Char_nine.grid(row=1,sticky="w",padx=15)
Char_eight = Button(text="8",width=2,command=lambda : ent.insert("end","8"),borderwidth=3,relief=RIDGE)
Char_eight.grid(row=1,sticky="w",padx=45)
Char_seven = Button(app,text="7",width=2,command=lambda : ent.insert("end","7"),borderwidth=3,relief=RIDGE)
Char_seven.grid(row=1,sticky="w",padx=75)
Char_plus = Button(app,text="+",width=2,command=lambda : ent.insert("end","+"),borderwidth=3,relief=RIDGE)
Char_plus.grid(row=1,sticky="e",padx=125)
Char_six = Button(text="6",width=2,command=lambda : ent.insert("end","6"),borderwidth=3,relief=RIDGE)
Char_six.grid(row=2,sticky="w",padx=15,pady=5)
Char_five = Button(text="5",width=2,command=lambda : ent.insert("end","5"),borderwidth=3,relief=RIDGE)
Char_five.grid(row=2,sticky="w",padx=45,pady=5)
Char_four = Button(app,text="4",width=2,command=lambda : ent.insert("end","4"),borderwidth=3,relief=RIDGE)
Char_four.grid(row=2,sticky="w",padx=75,pady=5)
Char_minus = Button(app,text="-",width=2,command=lambda : ent.insert("end","-"),borderwidth=3,relief=RIDGE)
Char_minus.grid(row=2,sticky="e",padx=125,pady=5)
Char_three = Button(text="3",width=2,command=lambda : ent.insert("end","3"),borderwidth=3,relief=RIDGE)
Char_three.grid(row=3,sticky="w",padx=15,pady=5)
Char_two = Button(text="2",width=2,command=lambda : ent.insert("end","2"),borderwidth=3,relief=RIDGE)
Char_two.grid(row=3,sticky="w",padx=45,pady=5)
Char_one = Button(app,text="1",width=2,command=lambda : ent.insert("end","1"),borderwidth=3,relief=RIDGE)
Char_one.grid(row=3,sticky="w",padx=75,pady=5)
Char_multiply = Button(app,text="*",width=2,command=lambda : ent.insert("end","*"),borderwidth=3,relief=RIDGE)
Char_multiply.grid(row=3,sticky="e",padx=125,pady=5)
Char_zero = Button(text="0",width=2,command=lambda : ent.insert("end","0"),borderwidth=3,relief=RIDGE)
Char_zero.grid(row=4,sticky="w",padx=15,pady=5)
Char_double_zero = Button(text="00",width=2,command=lambda : ent.insert("end","00"),borderwidth=3,relief=RIDGE)
Char_double_zero.grid(row=4,sticky="w",padx=45,pady=5)
Char_dot = Button(app,text=".",width=2,command=lambda : ent.insert("end","."),borderwidth=3,relief=RIDGE)
Char_dot.grid(row=4,sticky="w",padx=75,pady=5)
Char_divide = Button(app,text="/",width=2,command=lambda : ent.insert("end","/"),borderwidth=3,relief=RIDGE)
Char_divide.grid(row=4,sticky="e",padx=125,pady=5)
result = Button(app,text="=",width=10,command=fresult,bg="green",fg="white",borderwidth=3,relief=RIDGE)
result.grid(row=5,sticky="w",padx=15,pady=5)
Char_modulus = Button(app,text="%",width=2,command=lambda : ent.insert("end","%"),borderwidth=3,relief=RIDGE)
Char_modulus.grid(row=5,sticky="e",padx=125,pady=5)
delete = Button(app,text="del",width=2,command=delete,borderwidth=3,relief=RIDGE)
delete.grid(row=5,sticky="w",padx=80,pady=5)
app.mainloop()






































