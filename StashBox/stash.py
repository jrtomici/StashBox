from tkinter import *

def view_balance_clicked():
    #display current balance in new window
    box = open('box.txt', 'r')
    balance = int(box.readline())
    box.close()
    vbw = Tk()
    vbw.title("View balance")
    Label(vbw, text="Current balance: $").grid(row=0, column=2)
    Label(vbw, text=balance).grid(row=1, column=2)

def view_history_clicked():
    #display history in new window
    file = open('history.txt', 'r')
    history = file.read()
    file.close()
    vhw = Tk()
    vhw.title("View history")
    Label(vhw, text="History:").grid(row=0, column=2)
    Label(vhw, text=history).grid(row=1, column=2)
   
def deposit_clicked():
    #retrieve balance
    box = open('box.txt', 'r')
    balance = int(box.readline())
    box.close()
    dw = Tk()
    dw.title("Deposit")
    #take input
    Label(dw, text="Amount: $").grid(row=0, column=0)
    e1 = Entry(dw)
    e1.grid(row=0, column = 1)
    e1.insert(0,0)
    e2 = Entry(dw)
    e2.grid(row=1, column = 1)
    e2.insert(0,"Enter memo")
    Button(dw, text='Save', command=lambda: save_deposit(e1, e2, balance, dw)).grid(row=1, column=2, padx = 4, pady=4)

def save_deposit(e1, e2, balance, dw):
    box = open('box.txt', 'w')
    history = open('history.txt', 'a')
    #update balance
    newBalance = balance + int(e1.get())
    box.write(str(newBalance))
    memo = str(e2.get())
    #append history
    history.write("\nDeposited $" + str(int(e1.get())) + " -- " + memo)
    box.close()
    history.close()
    dw.destroy()

def withdraw_clicked():
    #retrieve balance
    box = open('box.txt', 'r')
    balance = int(box.readline())
    box.close()
    ww = Tk()
    ww.title("Withdraw")
    #take input
    Label(ww, text="Amount: $").grid(row=0, column=0)
    e1 = Entry(ww)
    e1.grid(row=0, column = 1)
    e1.insert(0,0)
    e2 = Entry(ww)
    e2.grid(row=1, column = 1)
    e2.insert(0,"Enter memo")
    Button(ww, text='Save', command=lambda: save_withdraw(e1, e2, balance, ww)).grid(row=1, column=2, padx = 4, pady=4)

def save_withdraw(e1, e2, balance, ww):
    #check if enough cash in box
    if int(e1.get()) <= balance:
        box = open('box.txt', 'w')
        history = open('history.txt', 'a')
        #update balance
        newBalance = balance - int(e1.get())
        box.write(str(newBalance))
        memo = str(e2.get())
        #append history
        history.write("\nWithdrew $" + str(int(e1.get())) + " -- " + memo)
        box.close()
        history.close()
        ww.destroy()
    #display error
    else:
        ww.destroy()
        messagebox.showinfo("Error", "Not enough cash in box.")

def login_clicked(e1,e2,login):
    users = open('users.txt', 'r')
    #loop through user list
    for line in users:
        #admin
        if str(e1.get()) + " " + str(e2.get()) == line.rstrip() and str(e1.get()) == "admin":
            user = str(e1.get())
            pw = str(e2.get())
            login.destroy()
            admin_menu(user, pw)
        #if matched credentials, open menu
        if str(e1.get()) + " " + str(e2.get()) == line.rstrip():
            user = str(e1.get())
            pw = str(e2.get())
            login.destroy()
            menu(user, pw)
    #display error
    messagebox.showinfo("Error", "Wrong credentials.")

def main():
    #display login menu
    login = Tk()
    login.title("Login")
    Label(login, text="Username").grid(row=0, column=0)
    Label(login, text="Password").grid(row=1, column=0)
    e1 = Entry(login)
    e1.grid(row=0, column=1)
    e2 = Entry(login, show="*")
    e2.grid(row=1, column=1)
    Button(login, text="Login", command=lambda: login_clicked(e1, e2,login)).grid(columnspan=2)

def logout(master):
    #close menu and return to login
    master.destroy()
    main()

def change_pass_clicked(user, pw):
    #display change password screen
    cpw = Tk()
    cpw.title("Change password")
    Label(cpw, text="New password: ").grid(row=0, column=0)
    e1 = Entry(cpw, show="*")
    e1.grid(row=0,column=1)
    Button(cpw, text="Enter", command=lambda: save_changed_pass(e1, user, pw, cpw)).grid(columnspan=2)

def save_changed_pass(e1, user, pw, cpw):
    users = open("users.txt", "r")
    temp = open("temp_users.txt.", "w+")
    new_pw = str(e1.get())
    for line in users:
        if user + " " + pw + '\n' == line:
            temp.write(user + " " + new_pw + '\n')
        else:
            temp.write(line)
    users = open("users.txt", "w")
    temp = open("temp_users.txt.", "r")
    for line in temp:
        print('whyyy')
        users.write(line)
    users.close()
    temp.close()
    cpw.destroy()
            
    

def create_user():
    #display registration
    reg = Tk()
    reg.title("Register")
    Label(reg, text="Username").grid(row=0, column=0)
    Label(reg, text="Password").grid(row=1, column=0)
    e1 = Entry(reg)
    e1.grid(row=0, column=1)
    e2 = Entry(reg, show="*")
    e2.grid(row=1, column=1)
    Button(reg, text="Register", command=lambda: reg_clicked(e1, e2, reg)).grid(columnspan=2)

def reg_clicked(e1,e2,reg):
    #append user list
    users = open('users.txt', 'a')
    user = str(e1.get())
    pw = str(e2.get())
    users.write("\n" + user + " " + pw)
    reg.destroy()

def admin_menu(user, pw):
    #display admin menu
    master = Tk()
    master.title("Cash Stash Manager")
    Label(master, text='Welcome, ' + user).grid(row=0, column=1)
    Button(master, text='View balance', command=view_balance_clicked).grid(row=1, column=0, sticky=W, padx = 4, pady=4)
    Button(master, text='View history', command=view_history_clicked).grid(row=2, column=0, sticky=W, padx = 4, pady=4)
    Button(master, text='Desposit', command=deposit_clicked).grid(row=1, column=1, sticky=W, padx = 4, pady=4)
    Button(master, text='Withdraw', command=withdraw_clicked).grid(row=2, column=1, sticky=W, padx = 4, pady=4)
    Button(master, text='Change password', command=lambda: change_pass_clicked(user, pw)).grid(row=1, column=2, sticky=W, padx = 4, pady=4)
    Button(master, text='Logout', command=lambda: logout(master)).grid(row=2, column=2, sticky=W, padx = 4, pady=4)
    Button(master, text='Create new user', command=create_user).grid(row=3, column=2, sticky=W, padx = 4, pady=4)

    mainloop( )

def menu(user, pw):
    #display menu
    master = Tk()
    master.title("Cash Stash Manager")
    Label(master, text='Welcome, ' + user).grid(row=0, column=1)
    Button(master, text='View balance', command=view_balance_clicked).grid(row=1, column=0, sticky=W, padx = 4, pady=4)
    Button(master, text='View history', command=view_history_clicked).grid(row=2, column=0, sticky=W, padx = 4, pady=4)
    Button(master, text='Desposit', command=deposit_clicked).grid(row=1, column=1, sticky=W, padx = 4, pady=4)
    Button(master, text='Withdraw', command=withdraw_clicked).grid(row=2, column=1, sticky=W, padx = 4, pady=4)
    Button(master, text='Change password', command=lambda: change_pass_clicked(user,pw)).grid(row=1, column=2, sticky=W, padx = 4, pady=4)
    Button(master, text='Logout', command=lambda: logout(master)).grid(row=2, column=2, sticky=W, padx = 4, pady=4)

    mainloop( )

main()
