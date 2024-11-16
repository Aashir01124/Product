import tkinter as tk

def calculate_product():
    try:
        num1 = int(entry1.get())  # Changed to int()
        num2 = int(entry2.get())  # Changed to int()
        result_label.config(text=f"{num1}x{num2} = {num1 * num2}")
    except ValueError:
        result_label.config(text="Invalid input!")

root = tk.Tk()
root.title("Product Calculator")
root.geometry("400x300")

tk.Label(root, text="Number 1:").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Number 2:").pack()
entry2 = tk.Entry(root)
entry2.pack()

tk.Button(root, text="Calculate", command=calculate_product).pack()
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()