import threading
from tkinter import Menu, IntVar, ttk, scrolledtext, messagebox
import tkinter as tk
import time
import random
import os
import datetime

coler = "#f3e6f5"
# coler = "#cfaf11"
# coler = "#fff678"
# ====================================================================================

def quit():
    def warning_Exit():
        global anw
        anw = messagebox.askyesno("Exit warning", "Are you sure you want to exit? \n All progress will be cleared.")
    warning_Exit()
    if anw == True:
        win.quit()
        win.destroy()
        exit()

# ====================================================================================

def New_win():
    def warning_Exit():
        global anw
        anw = messagebox.askyesno("Exit warning", "Are you sure you want to start a new window? \n All progress will be cleared.")
    warning_Exit()

    if anw == True:
        def restart():
            win.destroy()
            os.startfile("Game of life.py")
        restart()

        # def restart_program():
        #     new = sys.executable
        #     os.execl(new, new, * sys.argv)
        # restart_program()
        # win.mainloop()
        # win.quit()
        # win.destroy()
        # win = tk.Tk()
        # win.mainloop()
        # # exit()

# ====================================================================================

godrat = """
each of (x,y) is a location of one cell that i in Axis is x and j in Axis is y and the value of 0 or 1 that mean that cell is dead or live.


  ****      ***      ***    ***           ***********    *****         ***      ***        ****     ***                 ***     *****
 ******     ***      ***    *********     ***********    *******       ****     ***       ******     ***               ***     *** ***
***  ***    ***      ***    ****  ****    ***            ***  ****     *****    ***      ***  ***     ***             ***     ***   ***
 ***        ***      ***    ***     ***   ***            ***   ****    ******   ***     ***    ***     ***           ***     ***     ***
  ***       ***      ***    ****  ****    ***********    ***  ****     *** ***  ***    ***      ***     ***         ***     ***       ***
   ***      ***      ***    *********     ***********    *******       ***  *** ***    ***      ***      ***       ***     *************** 
    ***     ***      ***    ***           ***            **** ***      ***   ******     ***    ***        ***     ***     *****************
***  ***    ***      ***    ***           ***            ***   ***     ***    *****      ***  ***          ***   ***     ***             ***
 ******       ***  *** *    ***           ***********    ***    ***    ***     ****       ******            *** ***     ***               ***
  ****         ******  *    ***           ***********    ***     ***   ***      ***        ****              *****     ***                 ***
 \n \n \n \n"""

# ====================================================================================
def save():
    # try:
    #     f = open("locations.txt", "w")
    # except:
    #     f = open("locations.txt", "a")
    #     f.write(godrat)
    try:
        f = open("locations.txt", "x")
        f.write(godrat)
    except:
        f = open("locations.txt", "a")
    try:
        all1 = ["locations = { "]
        conuter5 = 1
        c_s = len(locations)
        for i in locations:
            demo = list(i)
            if conuter5 == c_s:
                te = "({}, {}) : {} ".format(demo[0], demo[1], locations[i][0])
            else:
                te = "({}, {}) : {} ,".format(demo[0], demo[1], locations[i][0])
            all1.append(te)
            conuter5 +=1
        all1.append("}\n")
        da = datetime.datetime.today()
        all1.append("\nDate and Time : {} \n \n \n".format(da))
        all_text = "".join(all1)
        f.write(all_text)
        f.close()
        moree = messagebox.askyesno("File Saved", "We save all location in locations.txt for you. \nAre you want to save more information in file? ")
        if moree == True:
            messagebox.showerror(" Really nigga ", " What do you want to save bro??! ")
    except:
        messagebox.showerror("so soon", "Please start the game then save it...")
# ====================================================================================

def about():
    messagebox.showinfo(" Info ", " GAME OF LIFE \n \n Made by supernova-313 \n Version: 1.0.4 (system setup) \n Date: 2022-1-1")

# ====================================================================================

def update():
    messagebox.showerror(" nop ", "become a enjoyer bro \U0001F4AA \ndon't be a updata fans")

# ====================================================================================

def connect():
    win2 = tk.Tk()
    win2.title(" Contact us ")
    win2.resizable(False, False)
    win2.geometry("300x250")
    win2.configure(background=coler)

    about_me = ttk.Label(win2, text=" Telegram ID : @A_R_nasa \n Discord : supernova_1#0689 ", border = 1)
    about_me.grid(column = 0, row = 0)
    about_me.configure(background=coler)

    frame1 = tk.Frame(win2, border = 3)
    frame1.grid(column = 0, row = 2, padx = 9 , pady = 2)
    frame1.configure(background=coler)

    helping = ttk.Label(frame1, text = " You can also write your feedback in this section \n so that we can send it now.")
    helping.grid(column = 0, row = 0)
    helping.configure(background=coler)

    texts = scrolledtext.ScrolledText(frame1, width = 30, height = 7, wrap = tk.WORD)
    texts.grid(column= 0, row = 1, padx= 7)

    def click_s():
        text_r = texts.get("1.0", tk.END)

        if "fuck" in text_r:
            messagebox.showerror(" ara ara ", "Your text contains inappropriate words.\n Please try again.")
            win2.destroy()
        elif text_r == "\n":
            texts.configure(state = "disabled")
            messagebox.showinfo(" Tnx ", "Have a great day")
            win2.destroy()
        else:
            texts.configure(state = "disabled")
            messagebox.showinfo(" Tnx ", "Thank you for sending your feedback.\n We save it and send it as soon as possible.")
            win2.destroy()

    send_b = ttk.Button(win2, text = "Send", command = click_s)
    send_b.grid(column = 0, row = 4)
    
    win2.mainloop()

# ====================================================================================

def game_earth(x):
    first_location = {}
    for item in range(1, x+1):
        for item2 in range(1, x+1):
            first_location[(item, item2)] = [0]
    return first_location

# ====================================================================================

def live_block(z, loc):
    f_list = list(loc.keys())
    s_list = []
    ran = random.randrange(len(f_list))
    
    first_random_block = random.choices(f_list, weights= None, k = z)
    for v in first_random_block:
        s_list.append(v)
    
    test = set(s_list)
    for i in test:
        f_list.remove(i)
    while(len(test) != z):
        mn = random.choice(f_list)
        f_list.remove(mn)
        s_list.append(mn)
        test = set(s_list)
    
    s_list = list(test)
    
    other_block = random.choices(f_list,weights=None, k= ran)
    for v in other_block:
        s_list.append(v)
    
    for i in loc:
        if i in s_list:
            loc[i] = [1]

    return loc

# ====================================================================================

def erea(x, n):
    list_hamsaye = []
    z = list(n)
    for i in range(1, 4):
        for cc in range(1, 4):
            f = [z[0]+(i-2), z[1]+(cc-2)]
            if tuple(f) in x:
                list_hamsaye.append(tuple(f))
    list_hamsaye.remove(n)
    return list_hamsaye

# ====================================================================================

def sabet_erea(x):
    dict_sabet = {}
    for i in x:
        z = erea(x, i)
        dict_sabet[i] = z
    return dict_sabet

# ====================================================================================

def tagirat():
    # global save_locations
    global dict_sabet, save_locations, locations
    new_locations = save_locations.copy()
    for i in locations:
        vb = dict_sabet[i]
        live = 0
        dead = 0
        for z in vb:
            if locations[z] == [1]:
                live += 1
            else:
                dead += 1
        if (live == 2) or (live == 3):
            new_locations[i] = [1]
        else:
            new_locations[i] = [0]
    locations = new_locations.copy()
    # return new_locations

# ====================================================================================

win = tk.Tk()
win.title(" Game Of Life ")
win.resizable(True, True)
win.configure(background=coler)
menus = Menu(win, background=coler)
win.config(menu=menus,background=coler)

file_menu = Menu(menus, tearoff = 0,background=coler)
file_menu.add_command(label="New", command = New_win)
file_menu.add_separator()
file_menu.add_command(label="Save", command = save)
file_menu.add_separator()
file_menu.add_command(label="Exit", command = quit)

file_menu2 = Menu(menus, tearoff = 0, background=coler)

file_menu2.add_command(label="Check for update", command= update)
file_menu2.add_separator()
file_menu2.add_command(label="connect us", command= connect)
file_menu2.add_command(label="About", command= about)

menus.add_cascade(label="File", menu=file_menu,background=coler)
menus.add_cascade(label="Help", menu=file_menu2,background=coler)

tabControl = ttk.Notebook(win)
tab1 = tk.Frame(tabControl,background=coler)
tab2 = tk.Frame(tabControl,background=coler)
tab3 = tk.Frame(tabControl,background="#9b9ef2")# "#d5d6f0"
tabControl.add(tab1, text=' game ')# main section 
# tabControl.pack(expand=1, fill="both")
tabControl.add(tab2, text=' settings ')
tabControl.add(tab3, text=' story ')
tabControl.pack(expand=1, fill="both")

# ====================================================================================
# tab3
storyy = tk.Frame(tab3, border=5, relief="ridge",highlightthickness=4)
storyy.grid(column=0, row=0, padx= 7, pady= 7)
storyy.configure(background=coler)
big_text = "In this game we have M*M cell that they dead or live.(Gold=live,White=dead)\nAt each stage they can be changed according to the following rules.\n\n 1.Any live cell with fewer than two live neighbors dies due to under-population. \n 2.Any live cell with two or three live neighbors lives on to the next generation. \n 3.Any live cell with more than three live neighbors dies due to overpopulation. \n 4.Any dead cell with three or tow live neighbors becomes a live cell by reproduction. \n\nHere, the neighbor of a cell includes its adjacent cells as well as diagonal ones, \nso for each cell, a total of 8 neighbors are there. \n\nYou can find interesting patterns and events during this process by computer."
big_text_h = ttk.Label(storyy, text=big_text, font=("Courier", 10))# , width= 75
big_text_h.grid(column=0, row=0,padx=7, pady= 7, sticky= tk.E)
big_text_h.configure(background=coler)
# ====================================================================================
# tab2
mode = tk.Frame(tab2, border=7,relief="sunken", highlightthickness=2)
mode.grid(column=0, row=0, padx= 7, pady= 7)
mode.configure(background=coler)

mode_text = ttk.Label(mode, text="Mode:", font=("Courier", 10))
mode_text.grid(column=0,row=0, padx=7,pady=7, sticky= tk.W)
mode_text.configure(background=coler)

def colcall():
    global frame3, selected, v_color, frame4, stage, stage_t, time_sh
    v_color = color_b.get()
    # ssss.configure('TNotebook.Tab', background=coler)

    if v_color == 1:
        col1.configure(background="#343645",fg="#5c59ff")
        col2.configure(background="#343645",fg="#e09538")# #ffff40
        mode_text.configure(background="#343645",foreground="#b84040")
        mode.configure(background="#343645")
        tab1.configure(background="#121340")
        tab2.configure(background="#121340")
        tab3.configure(background="#121340")
        storyy.configure(background="#343645")
        big_text_h.configure(background="#343645",foreground="#ccde54")
        file_menu.configure(background="#121340",foreground="#dfdfed")
        file_menu2.configure(background="#121340",foreground="#dfdfed")
        mode2.configure(background="#343645")
        time_text.configure(background="#343645",foreground="#b84040")
        try:
            selected.configure(background="#343645",foreground="#dfdfed")
            frame3.configure(background="#121340")
            time_sh.configure(background="#343645",foreground="#dfdfed")
            stage.configure(background="#343645",foreground="#dfdfed")
            stage_t.configure(background="#343645",foreground="#b84040")
            frame4.configure(background="#343645")
        except:
            pass
        try:
            war.configure(background="#343645",foreground="#dfdfed")
        except:
            pass
        check1.configure(background="#343645",foreground="#73bf69")
        s_q.configure(background="#343645",foreground="#dfdfed")
        f_q.configure(background="#343645",foreground="#dfdfed")
        titr.configure(background="#343645",foreground="#b84040")
        frame2.configure(background="#343645")
        # win.configure(background="#121340")
        ssss.configure('TNotebook.Tab', background="#121340",foreground="#dfdfed")

        
    else:
        col1.configure(background="#dfdfed",fg="#5c59ff")
        col2.configure(background="#dfdfed",fg="#e09538")
        mode_text.configure(background="#dfdfed",foreground="#b84040")
        mode.configure(background="#dfdfed")
        tab1.configure(background="#f0f0f0")
        tab2.configure(background="#f0f0f0")
        tab3.configure(background="#edcee0")
        storyy.configure(background="#dfdfed")
        big_text_h.configure(background="#dfdfed",foreground="#248c04")
        file_menu.configure(background="#dfdfed",foreground="#171717")
        file_menu2.configure(background="#dfdfed",foreground="#171717")
        mode2.configure(background="#dfdfed")
        time_text.configure(background="#dfdfed",foreground="#b84040")
        try:
            selected.configure(background="#f0f0f0",foreground="#171717")
            frame3.configure(background="#f0f0f0")
            time_sh.configure(background="#dfdfed",foreground="#171717")
            stage.configure(background="#dfdfed",foreground="#171717")
            stage_t.configure(background="#dfdfed",foreground="#b84040")
            frame4.configure(background="#dfdfed")
        except:
            pass
        try:
            war.configure(background="#dfdfed",foreground="#171717")
        except:
            pass
        check1.configure(background="#dfdfed",foreground="#171717")
        s_q.configure(background="#dfdfed",foreground="#171717")
        f_q.configure(background="#dfdfed",foreground="#171717")
        titr.configure(background="#dfdfed",foreground="#b84040")
        frame2.configure(background="#dfdfed")
        # win.configure(background="#121340")
        ssss.configure('TNotebook.Tab', background="#f0f0f0",foreground="#171717")
        
color_b = IntVar()
col1 = tk.Radiobutton(mode, text = 'Dark_Blue', variable = color_b, value = 1,fg="#5c59ff", command= colcall)#  , command = colcall
col1.grid(column = 0, row = 1,padx= 4 , pady= 4, sticky = tk.W)
col1.configure(background=coler)
col2 = tk.Radiobutton(mode, text="Light", variable= color_b, value= 2,fg="#e09538", command= colcall)
col2.grid(column = 1, row = 1,padx= 4 , pady= 4, sticky = tk.W)
col2.configure(background=coler)

mode2 = tk.Frame(tab2, border=7,relief="sunken", highlightthickness=2)
mode2.grid(column=0, row=1, padx= 7, pady= 7)
mode2.configure(background=coler)

time_text = ttk.Label(mode2, text=" Auto slide timesleep:", font=("Courier", 10))
time_text.grid(column=0,row=0, padx=7,pady=7, sticky= tk.W)
time_text.configure(background=coler)

number_t = tk.StringVar()
listim = list(range(1, 121))
number_chosen_t = ttk.Combobox(mode2, width=12, textvariable=number_t, values=listim, state='readonly')# , values= lis , state='readonly'
number_chosen_t.grid(column = 1, row = 0)
number_chosen_t.current(9)

# ====================================================================================
# tab1

frame2 = tk.Frame(tab1, border = 3,relief="groove", highlightthickness=2)
frame2.grid(column = 0, row = 0, padx= 7 , pady= 3, sticky=tk.N)
frame2.configure(background=coler)

titr = ttk.Label(frame2, text="Information: ",background=coler)
titr.grid(column=0, row=0, sticky= tk.W, pady=5, padx=1)

f_q = ttk.Label(frame2, text="Select the game size(between 3 & 150): ")
f_q.grid(column = 0, row = 1,padx=6, sticky= tk.W)
f_q.configure(background=coler)

s_q = ttk.Label(frame2, text="Enter the minimum number of living homes(>0): ")
s_q.grid(column=0, row = 2, padx=6, sticky= tk.W)
s_q.configure(background=coler)

map_si = tk.StringVar()
between_n = list(range(3, 151))
map_entered = ttk.Combobox(frame2, width=8, textvariable=map_si, values=between_n, state='readonly')
map_entered.grid(column=1, row=1)
map_entered.current(0)

s_numb = tk.StringVar()
number_chosen = ttk.Entry(frame2, width=11, textvariable=s_numb)
number_chosen.grid(column = 1, row = 2, pady= 5, padx=3)
number_chosen.focus()

slide_ch = tk.IntVar()
check1 = tk.Checkbutton(frame2, text = "Auto slide", variable = slide_ch)
# check1.select()
check1.grid(column = 0, row = 3,padx=6, sticky = tk.W)
check1.configure(background=coler)

war = ttk.Label(frame2, text="Recommended \nfor weak systems\nM <= 70")
war.grid(column = 2, row = 1,rowspan=2,padx=4,pady=4, sticky= tk.E)
war.configure(background=coler)

counter10 = 1
pause_ch = 1

def main_def():
    global dict_sabet , save_locations, locations, counter10, frame3, selected, v_color, frame4, stage, stage_t, time_sh

    size = int(map_si.get())
    slide = int(slide_ch.get())
    s = size**2
    fs = 9
    bd1 = 2

    if 20 <= size:
        fs = 7
    if 29 <= size:
        fs = 5
        bd1 = 1
    if 43 <= size:
        fs = 3
    if 63 <= size:
        fs = 1

    try:
        testing_live = s_numb.get()
        fuck = 0
        if "-" in testing_live:
            fuck = 1
        live = int(testing_live)
        if not(live>=0 and live<=(size**2)):
            fuck = 1
    except:
        fuck = 1
    if fuck == 1:
        messagebox.showerror(" Incorrect input ", "Your input is incorrect. \nThe input must be a number in the range 0 to {}. \nPlease try again.".format(s))
    else:
        check1.configure(state="disabled")
        number_chosen.configure(state="disabled")
        map_entered.configure(state="disabled")
        number_chosen_t.configure(state="disabled")
        info_b.destroy()
        war.destroy()
        
        selected = tk.Label(frame2, text="there is {} cell".format(s), relief = "raised", width= (len(str(s))+10), height=2, bd=5)
        selected.grid(column=1, row=3, padx=3, pady=5)
        selected.configure(background=coler)

        st = time.process_time()

        # ====================================================================================

        frame3 = tk.Frame(tab1, border=3)
        frame3.grid(column = 1, row = 0, rowspan=2, padx= 7 , pady= 2)
        frame3.configure(background=coler)

        locations = game_earth(size)
        save_locations = locations.copy()
        dict_sabet = sabet_erea(locations)
        locations = live_block(live, locations)
    
        for i in locations:
            list_Tup = list(i)
            if locations[i] == [1]:
                celcolor = "Gold"
            else:
                celcolor = "White"
            cells = tk.Label(frame3, background = celcolor, height = 1, width = 2, relief = "solid", bd= bd1)
            cells.grid(column=((list_Tup[1])-1),row=((list_Tup[0])-1))
            cells.configure(font=("Courier", fs))
        
        fi = time.process_time()
        # ====================================================================================

        frame4 = tk.Frame(tab1, border=3, relief="groove", highlightthickness=2)
        frame4.grid(column=0, row=1 ,padx=7, pady=3, sticky=tk.N)
        frame4.configure(background=coler)
        
        stage_t = ttk.Label(frame4, text="stages: ", background=coler)
        stage_t.grid(column= 0, row=0 ,sticky= tk.W, pady=5, padx=1)
        
        stage = ttk.Label(frame4, text="this is the first case, click the button to continue ",background=coler)# +" "*((len(str(s))-1)*3)
        stage.grid(column = 0, row = 1,padx=3,pady=5, sticky= tk.W)

        strtime = str((fi-st))
        time_sh = tk.Label(frame4, text="Process time : {}".format(strtime), relief= "groove",background=coler,width=(len(strtime)+14),height=2,border=2)
        time_sh.grid(column=0, row=2,pady= 18,padx= 5, columnspan=1)
        
        
        def startgame():
            global counter10, x

            if slide == 1:
                stage_b.destroy()
                setting_t = int(number_t.get())*1000
                x = 0

                def atuomat():
                    global counter10, x, pas_b
                    
                    
                    def pas():
                        global x, pas_b
                        if x == 0:
                            x = 1
                            pas_b.configure(text=" unpause ")
                              
                        else:
                            x = 0
                            pas_b.configure(text=" pause ")

                    if counter10 == 1:
                        pas_b = ttk.Button(frame4, text="pause", command=pas)
                        pas_b.grid(column=1, row=1, rowspan=1, padx=8, pady=4) 
                        
                    if x == 0:
                        
                        st = time.process_time()
                        
                        for item in frame3.winfo_children():
                            item.destroy()

                        tagirat()

                        for j in locations:
                            list_Tupp = list(j)
                            if locations[j] == [1]:
                                celcolor = "Gold"
                            else:
                                celcolor = "White"
                            cells = tk.Label(frame3, background = celcolor, height = 1, width = 2, relief = "solid", bd= bd1)
                            cells.grid(column=((list_Tupp[1])-1),row=((list_Tupp[0])-1))
                            cells.configure(font=("Courier", fs))
                        
                        fi = time.process_time()
                        strtime = float(fi-st)
                        time_sh.configure(text="Process time : %3.4f"%strtime)
                        stage.configure(text="in step {}".format(counter10))
                        counter10 +=1
                        

                    else:
                        pass

                    win.after(setting_t,atuomat)

                atuomat()
                    

            else:
                if counter10 == 1:
                    stage_b.configure(text=" next ")
                st = time.process_time()

                for xc in frame3.winfo_children():
                        xc.destroy()

                tagirat()
                
                for j in locations:
                    list_Tupp = list(j)
                    if locations[j] == [1]:
                        celcolor = "Gold"
                    else:
                        celcolor = "White"
                    cells = tk.Label(frame3, background = celcolor, height = 1, width = 2, relief = "solid", bd= bd1)
                    cells.grid(column=((list_Tupp[1])-1),row=((list_Tupp[0])-1))
                    cells.configure(font=("Courier", fs))
                
                fi = time.process_time()
                strtime = float(fi-st)
                time_sh.configure(text="Process time : %3.4f"%strtime)

                stage.configure(text="in step {}".format(counter10))
                counter10 +=1

        
        v_color = color_b.get()
        if v_color == 1:
            selected.configure(background="#343645",foreground="#dfdfed")
            frame3.configure(background="#121340")
            time_sh.configure(background="#343645",foreground="#dfdfed")
            stage.configure(background="#343645",foreground="#dfdfed")
            stage_t.configure(background="#343645",foreground="#b84040")
            frame4.configure(background="#343645")
        if v_color == 2:
            selected.configure(background="#f0f0f0",foreground="#222424")
            frame3.configure(background="#f0f0f0")
            time_sh.configure(background="#dfdfed",foreground="#171717")
            stage.configure(background="#dfdfed",foreground="#171717")
            stage_t.configure(background="#dfdfed",foreground="#b84040")
            frame4.configure(background="#dfdfed")

        stage_b = ttk.Button(frame4, text=" start ",command=startgame)
        stage_b.grid(column=1, row=1, rowspan=1, padx=8, pady=4)


info_b = ttk.Button(frame2, text="next", command= main_def)
info_b.grid(column=1, row=3)
# ====================================================================================

ssss = ttk.Style()
ssss.theme_use('winnative')
ssss.configure('TNotebook.Tab', background=coler)
win.update()

win.mainloop()
