import tkinter as tk

def btn_on_click():
    # label_num["text"] = float(entry_mile.get()) * 1.609
    label_num.configure(text=f"{float(entry_mile.get())* 1.609}")

window = tk.Tk()
window.title("Mile to Kilometer Converter")
window.minsize(300, 100)
window.configure(padx=30, pady=30)

# # label
label_miles = tk.Label( text=f"Miles", font=("Arial", 10, "bold"))
label_miles.grid(column=2, row=0)
label_miles.configure(padx=10, pady=10)

label_km = tk.Label(text=f"Km", font=("Arial", 10, "bold"))
label_km.grid(column=2, row=1)
label_km.configure(padx=10, pady=10)

label_equal = tk.Label( text=f"is equal to", font=("Arial", 10, "bold"))
label_equal.grid(column=0, row=1)
label_equal.configure(padx=10, pady=10)

label_num = tk.Label(text=f"0", font=("Arial", 10, "bold"))
label_num.grid(column=1, row=1)
label_num.configure(padx=10, pady=10)

# # button
btn_cal = tk.Button(text="Calculate", command=btn_on_click)
btn_cal.grid(column=1, row=3)

# #  entry - one line inpput
entry_mile = tk.Entry(width=14)
entry_mile.grid(column=1, row=0)

# keep the window open
window.mainloop()