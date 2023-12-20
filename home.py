import tkinter as tk

def on_entry_click(event):
    if entry.get() == 'Password':
        entry.delete(0, "end")
        entry.config(fg='black')

def on_focus_out(event):
    if entry.get() == '':
        entry.insert(0, 'Password')
        entry.config(fg='grey')

root = tk.Tk()

def get_input():
    value = entry.get()
    if value != 'Password':
        print(value)
    else:
        print("Please enter a password.")

entry = tk.Entry(root, width=25, fg='grey', border=0, bg='white', font=("HOUSECLEANING, PLUMBING, ELECTRICITY SERVICE & MAINTENANCE SYSTEM", 11))
entry.insert(0, 'Password')
entry.bind('<FocusIn>', on_entry_click)
entry.bind('<FocusOut>', on_focus_out)
entry.place(x=30, y=150)

button = tk.Button(root, text="Get Input", command=get_input)
button.place(x=30, y=180)

root.mainloop()
