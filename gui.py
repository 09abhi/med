from tkinter import *
import sys
#Medicine Menu
def mclickedbtn1():
    print("Allegra")
def mclickedbtn2():
    print("Crocin")
def mclickedbtn3():
    print("Uprise")
def mclickedbtn4():
    print("Calpol")
def clickedbtn1():
    medicine_menu_window = Tk()
    medicine_menu_window.geometry('350x200')
    medicine_menu_window.title("Pharmacy Management Software")
    lbl = Label(medicine_menu_window, text="Medicine Menu!")
    lbl.grid(column=0, row=0)
    lbl2 = Label(medicine_menu_window, text="What would you like to do!")
    lbl2.grid(column=0, row=1)
    btn1 = Button(medicine_menu_window, text="Add New Medicine",fg="red", command=mclickedbtn1)
    btn1.grid(column=0, row=2)
    btn2 = Button(medicine_menu_window, text="Search Medicine",fg="red", command=mclickedbtn2)
    btn2.grid(column=0, row=3)
    btn3 = Button(medicine_menu_window, text="Update Medicine",fg="red", command=mclickedbtn3)
    btn3.grid(column=0, row=4)
    btn4 = Button(medicine_menu_window, text="Medicines to be purchased",fg="red", command=mclickedbtn4)
    btn4.grid(column=0, row=5)
    btn4 = Button(medicine_menu_window, text="Return to main menu",fg="red", command=mclickedbtn4)
    btn4.grid(column=0, row=6)
    medicine_menu_window.mainloop()
#Customer Menu
def mclickedbtn1():
    print("Harsh")
def mclickedbtn2():
    print("Shaurya")
def mclickedbtn3():
    print("Abhishek")
def mclickedbtn4():
    print("Saurabh")
def clickedbtn2():
    c_menu_window = Tk()
    c_menu_window.geometry('350x200')
    c_menu_window.title("Pharmacy Management Software")
    lbl = Label(c_menu_window, text="Customer Menu!")
    lbl.grid(column=0, row=0)
    lbl2 = Label(c_menu_window, text="What would you like to do!")
    lbl2.grid(column=0, row=1)
    btn1 = Button(c_menu_window, text="Search Customer",fg="red", command=mclickedbtn1)
    btn1.grid(column=0, row=2)
    btn2 = Button(c_menu_window, text="New Customer",fg="red", command=mclickedbtn2)
    btn2.grid(column=0, row=3)
    btn3 = Button(c_menu_window, text="Update Customer Info",fg="red", command=mclickedbtn3)
    btn3.grid(column=0, row=4)
    btn4 = Button(c_menu_window, text="Return to main menu",fg="red", command=mclickedbtn4)
    btn4.grid(column=0, row=5)
    c_menu_window.mainloop()
#Supplier Menu
def mclickedbtn1():
    print("Medtech")
def mclickedbtn2():
    print("First Choice Health")
def mclickedbtn3():
    print("Gold Medical Testing")
def mclickedbtn4():
    print("CrossPoint Medical Supplier")
def clickedbtn3():
    s_menu_window = Tk()
    s_menu_window.geometry('350x200')
    s_menu_window.title("Pharmacy Management Software")
    lbl = Label(s_menu_window, text="Supplier Menu!")
    lbl.grid(column=0, row=0)
    lbl2 = Label(s_menu_window, text="What would you like to do!")
    lbl2.grid(column=0, row=1)
    btn1 = Button(s_menu_window, text="Search Supplier",fg="red", command=mclickedbtn1)
    btn1.grid(column=0, row=2)
    btn2 = Button(s_menu_window, text="New Supplier",fg="red", command=mclickedbtn2)
    btn2.grid(column=0, row=3)
    btn3 = Button(s_menu_window, text="Update Supplier Info",fg="red", command=mclickedbtn3)
    btn3.grid(column=0, row=4)
    btn4 = Button(s_menu_window, text="Return to main menu",fg="red", command=mclickedbtn4)
    btn4.grid(column=0, row=5)
    s_menu_window.mainloop()
#Report Menu
def mclickedbtn1():
    print("100")
def mclickedbtn2():
    print("3000")
def mclickedbtn3():
    print("5000")
def mclickedbtn4():
    print("50000")
def clickedbtn4():
    r_menu_window = Tk()
    r_menu_window.geometry('350x200')
    r_menu_window.title("Pharmacy Management Software")
    lbl = Label(r_menu_window, text="Supplier Menu!")
    lbl.grid(column=0, row=0)
    lbl2 = Label(r_menu_window, text="What would you like to do!")
    lbl2.grid(column=0, row=1)
    btn1 = Button(r_menu_window, text="Day Sales",fg="red", command=mclickedbtn1)
    btn1.grid(column=0, row=2)
    btn2 = Button(r_menu_window, text="Month Sales",fg="red", command=mclickedbtn2)
    btn2.grid(column=0, row=3)
    btn3 = Button(r_menu_window, text="Day Purchase",fg="red", command=mclickedbtn3)
    btn3.grid(column=0, row=4)
    btn3 = Button(r_menu_window, text="Month Purchase",fg="red", command=mclickedbtn3)
    btn3.grid(column=0, row=5)
    btn3 = Button(r_menu_window, text="Profit Report",fg="red", command=mclickedbtn3)
    btn3.grid(column=0, row=6)
    btn4 = Button(r_menu_window, text="Return to main menu",fg="red", command=mclickedbtn4)
    btn4.grid(column=0, row=7)
    r_menu_window.mainloop()
#Invoicing Menu
def clickedbtn5():
    r_menu_window = Tk()
    r_menu_window.geometry('350x200')
    r_menu_window.title("Pharmacy Management Software")
    lbl = Label(r_menu_window, text="Invoice Menu!")
    lbl.grid(column=0, row=0)
    lbl2 = Label(r_menu_window, text="What would you like to do!")
    lbl2.grid(column=0, row=1)
    btn1 = Button(r_menu_window, text="Supplier Invoice",fg="red", command=mclickedbtn1)
    btn1.grid(column=0, row=2)
    btn2 = Button(r_menu_window, text="Customer Invoice",fg="red", command=mclickedbtn2)
    btn2.grid(column=0, row=3)
    btn4 = Button(r_menu_window, text="Return to main menu",fg="red", command=mclickedbtn4)
    btn4.grid(column=0, row=4)
    r_menu_window.mainloop()

#Main Menu
window = Tk()
window.geometry('350x200')
window.title("Pharmacy Management Software")
lbl = Label(window, text="Welcome to Pharmacy Management Software!")
lbl.grid(column=0, row=0)
lbl2 = Label(window, text="What would you like to do!")
lbl2.grid(column=0, row=1)
btn1 = Button(window, text="Medicine Menu",fg="red", command=clickedbtn1)
btn1.grid(column=0, row=2)
btn2 = Button(window, text="Customer Menu",fg="red", command=clickedbtn2)
btn2.grid(column=0, row=3)
btn3 = Button(window, text="Supplier Menu",fg="red", command=clickedbtn3)
btn3.grid(column=0, row=4)
btn4 = Button(window, text="Report Menu",fg="red", command=clickedbtn4)
btn4.grid(column=0, row=5)
btn5 = Button(window, text="Invoicing Menu",fg="red", command=clickedbtn5)
btn5.grid(column=0, row=6)
window.mainloop()
