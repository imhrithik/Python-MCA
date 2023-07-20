import tkinter as tk

def calculate():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    operation = entry3.get()
    
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        result = num1 / num2
    else:
        result = 'Invalid Operation'
    
    label_result.config(text=f'Result: {result}')

window = tk.Tk()
window.title('Calculator')

label1 = tk.Label(window, text='Enter number 1:')
label1.pack()
entry1 = tk.Entry(window)
entry1.pack()

label2 = tk.Label(window, text='Enter number 2:')
label2.pack()
entry2 = tk.Entry(window)
entry2.pack()

label3 = tk.Label(window, text='Enter operation (+, -, *, /):')
label3.pack()
entry3 = tk.Entry(window)
entry3.pack()

button = tk.Button(window, text='Calculate', command=calculate)
button.pack()

label_result = tk.Label(window, text='Result: ')
label_result.pack()

window.mainloop()
