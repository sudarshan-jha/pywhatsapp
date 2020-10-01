import pywhatkit as kit
from tkinter import*


def changeOption(*args):
    global data
    print('    args', args)
    print('name.get', name.get())

    data = choices[name.get()]
    data = choices[args[0]]
    var1 = data[0:15]
    print('var1=', var1)


def go():
    kit.sendwhatmsg(data[0:15],
                    var.get(), int1.get(), int2.get())


# tkinter root window with tittle
root = Tk()
root.title("whatsapp msg")

# creating a frame and Grid to hold the content
frame = Frame(root)
frame.grid(column=0, row=0, sticky=(N, W, E, S))
frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)
frame.pack(pady=100, padx=100)

# variable to store message
var = StringVar()

# textbox to take user message
Label(frame, text='',
      ).grid(row=1, column=0)

Label(frame, text="WHATSAPP ",
      font=('Aerial 20 italic'), fg="sea green").grid(row=0, column=1)

Label(frame, text="Enter text to send : ",
      font='none 10 bold').grid(row=4, column=0)

textbox = Entry(frame, textvariable=var, width=40, font='none 10 bold',
                bd=3).grid(row=4, column=1)


# label for Time
Label(frame, text="Enter time in 24hr format : ",
      font='none 10 bold').grid(row=3, column=1)

# setting time of message
int1 = IntVar()
int1.set('20')
hourbox = Entry(frame, textvariable=int1, width=4, font='none 10 bold',
                bd=3).place(x=365, y=56)
int2 = IntVar()
int2.set("0")
minutebox = Entry(frame, textvariable=int2, width=4, font='none 10 bold',
                  bd=3).place(x=405, y=56)

# button to send message
btn = Button(frame, text='>',  width=2, height=1, font='none 10 bold',
             bd=2, bg="sea green", fg="white", command=go).grid(row=4, column=2)

# choices to select from contact
choices = {'Bitu': "+91908129632",
           'kamlesh': '"+919922728886"', 'Rajesh': '"+9175999007881"'}
keys = sorted(choices)  # don't over write option even sorted returns key

# variables for drop down list
name = StringVar(root)
name.set('Contact List')



root.mainloop()
