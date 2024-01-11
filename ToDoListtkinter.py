import tkinter
from tkinter import *

root = Tk()
root.title("To-Do-List")
root.geometry("400x620+400+100")

task_list = []


def TaskAdd():
    task = addtask.get()
    addtask.delete(0, END)

    if task:
        with open("tasklist.txt", "a") as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END, task)


def openTaskFile():
    try:
        global task_list
        with open("tasklist.txt", "r") as taskfile:
            tasks = taskfile.readlines()
        for task in tasks:
            if task != "\n":
                task_list.append(task)
                listbox.insert(END, task)
    except:
        file = open("tasklist.txt", "w")
        file.close()


def deleteTask():
    global task_list
    task = str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt", "w") as taskfie:
            for task in task_list:
                taskfie.write(task + "\n")

        listbox.delete(ANCHOR)


# icon
Image_icon = PhotoImage(file="task.png")
root.iconphoto(False, Image_icon)

# topbar
topimg = PhotoImage(file="bar.png")
Label(root, image=topimg).pack()


heading = Label(root, text="ALL TASK", font="arial 15 bold", fg="white", bg="#FC6C85")
heading.place(x=150, y=5)

# main
frame = Frame(root, width=400, height=40, bg="white")
frame.place(x=0, y=50)

task = StringVar()
addtask = Entry(frame, width=15, font="arial 15", bd=0)
addtask.place(x=5, y=7)
addtask.focus()

btn = Button(
    frame,
    text="ADD",
    font="arial 15 bold",
    width=10,
    bg="#5a95ff",
    fg="#fff",
    bd=0,
    command=TaskAdd,
)
btn.place(x=300, y=0)

# listbox
frame1 = Frame(root, bd=1, width=400, height=300, bg="#32405b")
frame1.pack(pady=(160, 0))
frame1.place(x=0, y=110)

listbox = Listbox(
    frame1,
    font=("arial,12"),
    width=34,
    height=18,
    bg="#32405b",
    fg="white",
    cursor="hand2",
    selectbackground="#5a95ff",
)
listbox.pack(side=LEFT, fill=BOTH, padx=2)
scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# delete
dele = PhotoImage(file="del.png")
Button(root, image=dele, bd=0, command=deleteTask).pack(side=BOTTOM, pady=13)

root.mainloop()
