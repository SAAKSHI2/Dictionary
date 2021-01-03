import tkinter
window = tkinter.Tk()
window.title("window")

import json
data = json.load(open("data.json"))

def search():
    t3.delete(1.0,tkinter.END)
    word=t2.get()
    word = word.lower()
    if word in data:
        t3.insert(tkinter.END,data[word])
    else:
        t3.insert(tkinter.END,"No such word found......You can add the word")

def add():
    word = t2.get()
    if word in data:
        t3.insert(tkinter.END, "\nword already exists in dictionary")
    else:
       meaning=t3.get(1.0,'end-1c')
       data[word]=meaning
       with open('data.json','w') as jso:
           json.dump(data,jso)

def edit():
    word=t2.get()
    meaning=t3.get(1.0,'end-1c')
    data[word]=meaning
    with open("data.json", 'w') as jso:
        json.dump(data,jso)



left_frame = tkinter.Frame(window)
left_frame.grid(row=0,column=0)

t1 = tkinter.Label(left_frame,text="Word",font='10')
t1.grid(row=0,column=0)
t2 = tkinter.Entry(left_frame,width=70)
t2.grid(row=0,column=1)
t3 = tkinter.Text(left_frame,height=25,width=60)
t3.grid(row=1,column=0,columnspan=2)

right_frame = tkinter.Frame(window)
right_frame.grid(row=0,column=1)

btn1 = tkinter.Button(right_frame,text="search",bg="#ecf4f3",height=5,width=20,command=search)
btn1.grid(row=0,column=1)
btn2 = tkinter.Button(right_frame,text="add",bg="#ecf4f3",height=5,width=20,command=add)
btn2.grid(row=1,column=1)
btn3 = tkinter.Button(right_frame,text="Edit",bg="#ecf4f3",height=5,width=20,command=edit)
btn3.grid(row=3,column=1)

window.mainloop()
