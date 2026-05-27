import tkinter as tk
from tkinter import messagebox, scrolledtext

students = []

def add_student():
    data = [e.get().strip() for e in entries]

    if not all(data):
        messagebox.showerror("Error", "All fields are required!")
        return

    try:
        gpa = float(data[6])
        if not (0.0 <= gpa <= 4.0):
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "GPA must be between 0.0 and 4.0")
        return

    student = {
        "name": data[0],
        "id": data[1],
        "email": data[2],
        "phone": data[3],
        "course": data[4],
        "year": data[5],
        "gpa": gpa,
        "status": data[7]
    }

    students.append(student)
    update_display()
    clear_fields()


def update_display():
    text_area.delete(1.0, tk.END)

    display_order = [
        "name",
        "id",
        "email",
        "phone",
        "course",
        "year",
        "gpa",
        "status",
    ]

    display_labels = {
        "name": "Student Name",
        "id": "Student ID",
        "email": "Email",
        "phone": "Phone Number",
        "course": "Course/Program",
        "year": "Year Level",
        "gpa": "GPA",
        "status": "Enrollment Status",
    }

    for i, s in enumerate(students, 1):
        text_area.insert(tk.END, f"{'='*60}\n")
        text_area.insert(tk.END, f"Student #{i}\n")
        text_area.insert(tk.END, f"{'-'*60}\n")
        for key in display_order:
            text_area.insert(tk.END, f"{display_labels[key]:18}: {s[key]}\n")
        text_area.insert(tk.END, "\n")

    status_bar.config(text=f"Total Students: {len(students)}")


def clear_fields():
    for e in entries:
        e.delete(0, tk.END)

root = tk.Tk()
root.title("Student Management System")
root.geometry("750x650")
root.resizable(True, True)
root.configure(bg="#ffe6f2")

# Title
tk.Label(root, text="Student Management System",
         font=("Arial", 18, "bold"), fg="green", bg="#ffe6f2").pack(pady=10)

form_frame = tk.Frame(root, bg="#cce7ff")
form_frame.pack(pady=10, padx=10, fill="x")

labels = [
    "Student Name",
    "Student ID",
    "Email",
    "Phone Number",
    "Course/Program",
    "Year Level",
    "GPA",
    "Enrollment Status",
]

entries = []

for i, label in enumerate(labels):
    tk.Label(form_frame, text=label + ":", width=15, anchor="w", bg="#cce7ff").grid(
        row=i, column=0, padx=10, pady=5)

    entry = tk.Entry(form_frame, width=35)
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries.append(entry)

button_frame = tk.Frame(root, bg="#ffe6f2")
button_frame.pack(pady=15)

tk.Button(button_frame, text="Add Student",
          bg="#0077cc", fg="white", width=15,
          command=add_student).grid(row=0, column=0, padx=10)

tk.Button(button_frame, text="Clear Fields",
          bg="#ff66b2", fg="white", width=15,
          command=clear_fields).grid(row=0, column=1, padx=10)

tk.Label(root, text="Student List",
         font=("Arial", 12, "bold"), bg="#ffe6f2").pack(pady=5)
display_frame = tk.Frame(root, bg="#ffe6f2")
display_frame.pack(pady=10, fill="both", expand=True)

inner_frame = tk.Frame(display_frame, bg="#ffe6f2")
inner_frame.pack(expand=True, fill="both", padx=10, pady=5)

text_area = scrolledtext.ScrolledText(inner_frame, wrap=tk.WORD, width=100, height=20,
                                     bg="#f8f0ff", fg="#000000")
text_area.pack(fill="both", expand=True)

status_bar = tk.Label(root, text="Total Students: 0",
                      bd=1, relief=tk.SUNKEN, anchor="w",
                      bg="#ffd6e8")
status_bar.pack(fill="x", side="bottom")

root.mainloop()
