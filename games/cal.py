from tkinter import Tk, Label, Entry, Button


def add_numbers():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result_label.config(text=f"Result{num1 + num2}")
        
    except ValueError:
        result_label.config(text="Please enter valid number")
        
        
def sub_numbers():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result_label.config(text=f"Result{num1 - num2}")
        
    except ValueError:
        result_label.config(text="Please enter valid number")
        
        
def multiply_numbers():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result_label.config(text=f"Result{num1 * num2}")
    
    except ValueError:
        result_label.config(text="Please enter valid number")
        
        

def divide_numbers():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if num2 == 0:
            result_label.config(text="Cannot divide by zero")
        else:
            result_label.config(text=f"Result: {num1 / num2}")
    except ValueError:
        result_label.config(text="Please enter valid numbers")

    
root = Tk()
root.title("My Calculator")
root.geometry("400x400")



mylabel1 = Label(root, text="Enter the first number: ")
mylabel1.pack(pady=5)

entry1 = Entry(root)
entry1.pack(pady=5)


mylabel2 = Label(root, text="Enter the second number: ")
mylabel2.pack(pady=5)

entry2 = Entry(root)
entry2.pack(pady=5)


button = Button(root,text="Add",command=add_numbers)
button.pack(pady=10)
button = Button(root,text="Subtract",command=sub_numbers)
button.pack(pady=10)
button = Button(root,text="Multiply",command=multiply_numbers)
button.pack(pady=10)
button = Button(root,text="Divide",command=divide_numbers)
button.pack(pady=10)



#result label
result_label = Label(root, text="Result: ")
result_label.pack(pady=5)

root.mainloop()
      