import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        m1 = int(e1.get())
        m2 = int(e2.get())
        m3 = int(e3.get())

        total = m1 + m2 + m3
        avg = total / 3

        if avg >= 75:
            grade = "A"
        elif avg >= 60:
            grade = "B"
        elif avg >= 50:
            grade = "C"
        elif avg >= 35:
            grade = "D"
        else:
            grade = "Fail"

        result.config(text=f"Total: {total}\nAverage: {avg:.2f}\nGrade: {grade}")

    except:
        messagebox.showerror("Error", "Enter valid marks")

# Root window
root = tk.Tk()
root.title("Student Grade Calculator")
root.geometry("350x380")

# Main Heading
tk.Label(
    root,
    text="Student Grade Calculator",
    font=("Arial", 16, "bold")
).pack(pady=10)

# Frame
frame = tk.Frame(root)
frame.pack(pady=10)

# Input Fields
tk.Label(frame, text="Subject 1").grid(row=0, column=0, pady=5)
e1 = tk.Entry(frame)
e1.grid(row=0, column=1)

tk.Label(frame, text="Subject 2").grid(row=1, column=0, pady=5)
e2 = tk.Entry(frame)
e2.grid(row=1, column=1)

tk.Label(frame, text="Subject 3").grid(row=2, column=0, pady=5)
e3 = tk.Entry(frame)
e3.grid(row=2, column=1)

# Button
tk.Button(frame, text="Calculate", command=calculate).grid(
    row=3, columnspan=2, pady=10
)

# Output Heading
tk.Label(frame, text="Result", font=("Arial", 12, "bold")).grid(
    row=4, columnspan=2, pady=5
)

# Output
result = tk.Label(frame, text="")
result.grid(row=5, columnspan=2)

root.mainloop()
