import simpleback as sbk
import tkinter
from tkinter.ttk import *
import os.path
from os import path
from tkinter import Text, messagebox
from IPython.terminal.pt_inputhooks import tk

window=tkinter.Tk()
window.geometry('970x1050')
window.title("Simple")

 
label1=tkinter.Label(window,text="Welcome to simple Program",foreground='Blue',font=("Times", 20, "bold"))
label1.grid(row=0,column=1)
style=Style()

style.configure('TButton',font= ('calibri', 10, 'bold'), foreground = 'green', borderwidth=10)
 

 # After selecting the items
def avg_length():
    text=sbk.average()
    text=str(text)

    avg_info=Text(window,width=24, height=1)
     
    avg_info.grid(row=6,column=2)
    avg_info.insert("end",text)
def lon_name():
    name=sbk.longhest_name()
     
    name=str(name)

    longname=Text(window,width=29, height=2)
    longname.grid(row=8,column=2,pady=5)
    longname.insert("end", name)
     
def display_a():
    allitem=sbk.display_all()
    display_all=Text(window,width=42, height=28)
    display_all.grid(row=11,column=2)
    for i in range(len(allitem)):
        
        display_all.insert("end",allitem[i]+'\n')
 

def clickme(event):
    if combo.get()==combo["values"][0]:
         
        # create a entry box that can accept string
        # the string should be the name of the file present in the current directory 
        # if file not found raise FileNotFound execption
        label3=Label(window, text="Enter a name of file")
        label3.grid(row=3, column=0)

        file_entry= Entry(window, width=15)
        file_entry.grid(row=3,column=1)
        
        def enter_execute():
            #if file_entry.get()==path.exists("guru99.txt")
            try:
                if path.exists(file_entry.get()):
                    def functions():
                         
                        l_zero=Label(window, text=" Enter name to know status")
                        l_zero.grid(row=5, column=0)
                        name_entry=Entry(window, width=10)
                        name_entry.grid(row=5,column=1)
                        def chk_status():
                            infor=sbk.check_present(name_entry.get())
                            status_info=Text(window,width=16, height=2)
    
                            status_info.grid(row=5,column=3)
                            status_info.insert("end",infor)
                        

                        b_zero=Button(window, text="go", command=chk_status)
                        b_zero.grid(row=5,column=2)
        


                        l1=Label(window,text="Know average Length of your class")
                        l1.grid(row=6, column=0)
                        b1=Button(window,text="go",command=avg_length)
                        b1.grid(row=6,column=1)
                         
                        # mode part display
                        lmode=Label(window, text="Know mode of our class")
                        lmode.grid(row=7,column=0)
                        def know_mode():
                            mode_info=sbk.calc_mode()
                            mode_box=Text(window, width=27, height=2)
                            mode_box.grid(row=7, column=2)
                            mode_box.insert("end",mode_info)
                        bmode=Button(window, text="go", command=know_mode)
                        bmode.grid(row=7,column=1)

                        # 

                        l2=Label(window,text="Know name with length of all")
                        l2.grid(row=10, column=0)
                        b2=Button(window,text="go",command=display_a)
                        b2.grid(row=10,column=1)

                        l3=Label(window,text="Know the longhest name with character")
                        l3.grid(row=8, column=0)
                        b3=Button(window,text="go",command=lon_name)
                        b3.grid(row=8,column=1)

                        minl=Label(window,text="Names with lowest charcter length ")
                        minl.grid(row=9, column=0)
                        

                        def min_char():
                            min_info=sbk.lowest_character_length_with_names()
                            min_info_box=Text(window, width=26, height=2)
                            min_info_box.grid(row=9,column=2)
                            min_info_box.insert("end",min_info)
                        minb=Button(window,text="go",command=min_char)
                        minb.grid(row=9,column=1)
                         
                        
        
                    
                    option_button=Button(window,command=functions,text="click me to know what I could help you with", style='TButton')
                    option_button.grid(row= 4,column=0,pady=17)
                    
                    
                     
                else:
                    messagebox.showinfo("Not found", "file not found, , please enter file name as'SEclassnames.txt'")
                    
            except FileNotFoundError:
                print("file does not exist")


        enter_bottom=Button(text="Enter", width=5, command=enter_execute)
        enter_bottom.grid(row=3, column=2)
    else:
         
        messagebox.showerror(title="Error !", message=" Not available now")

#create a text box  with scroll option
label2=tkinter.Label(window,text="Select a file")
label2.grid(row=1, column=0,pady=15)
 

combo=Combobox(window,width=15)
combo['values']=(".txt",".xls",".html")
combo.current(0)
combo.grid(column=1, row =1)
combo.bind('<<ComboboxSelected>>',clickme)  


  
 
window.mainloop()