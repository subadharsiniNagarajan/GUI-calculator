import tkinter as tk
#create window
root = tk.Tk()
root.title("calculator")
root.geometry("300x400")
#entry box
entry=tk.Entry(root,width=16,font=("Arial",24),
bd=5,relief="ridge",justify="right")
entry.grid(row=0,column=0,columnspan=4)
#function to click button
def click(num):
    entry.insert(tk.END,num)
#clear function
def clear():
    entry.delete(0,tk.END)
#calculateresult
def equal():
    try:
        result=eval(entry.get())
        entry.delete(0,tk.END)
        entry.insert(tk.END,result)
    except:
        entry.delete(0,tk.END)
        entry.insert(tk.END,"Error")
#button layout
button=[
    ('7',1,0),('8',1,1),('9',1,2),('/',1,3),
    ('4',2,0),('5',2,1),('6',2,2),('*',2,3),
    ('1',3,0),('2',3,1),('3',3,2),('-',3,3),
    ('0',4,0),('.',4,1),('=',4,2),('+',4,3),
    ]
#creartew button
for(text,row,col)in button:
    if text == '=':
        tk.Button(root,text=text,width=5,height=2,font=("Arial",20),
                  command=equal).grid(row=row,column=col)
    else:
        tk.Button(root,text=text,width=5,height=2,font=("Arial",20),
                  command=lambda t=text:
                  click(t)).grid(row=row,column=col)
        #clear button
tk.Button(root,text="C",width=22,height=2,font=("Arial",20),
          command=clear).grid(row=5,column=0,columnspan=4)
root.mainloop()

                  
                  
        
