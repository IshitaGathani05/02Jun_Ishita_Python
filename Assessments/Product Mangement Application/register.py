import tkinter as tk
from tkinter import ttk, messagebox
from db import Database

def register_window(role):
    def register():
        name = entry_name.get().strip()
        contact = entry_contact.get().strip()
        email = entry_email.get().strip()
        gender = gender_var.get()
        city = combo_city.get()
        state = combo_state.get()

        can_manage_stock = can_view_stock = None
        if role == 'product_manager':
            can_manage_stock = int(manage_var.get())
            can_view_stock = int(view_var.get())

        if not all([name, contact, email, gender, city, state]):
            messagebox.showerror("Error", "All fields are required!")
            return

        db = Database()
        balance = 1000.0 if role == 'customer' else None

        query = """
        INSERT INTO users (name, contact, email, gender, city, state, role, balance, can_manage_stock, can_view_stock)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (name, contact, email, gender, city, state, role, balance, can_manage_stock, can_view_stock)
        result = db.execute(query, values)

        if result:
            messagebox.showinfo("Success", f"{role.capitalize()} registered successfully!")
            window.destroy()

    window = tk.Tk()
    window.title("Registration Form")
    window.geometry("400x500")
    window.configure(bg="white")

    tk.Label(window, text="Please enter details below", bg="orange", fg="white",
             font=('Arial', 12, 'bold')).pack(fill=tk.X)

    form = tk.Frame(window, bg="white")
    form.pack(pady=10)

    tk.Label(form, text="Name *", bg="white").grid(row=0, column=0, sticky="w")
    entry_name = tk.Entry(form)
    entry_name.grid(row=0, column=1)

    tk.Label(form, text="Contact *", bg="white").grid(row=1, column=0, sticky="w")
    entry_contact = tk.Entry(form)
    entry_contact.grid(row=1, column=1)

    tk.Label(form, text="Email *", bg="white").grid(row=2, column=0, sticky="w")
    entry_email = tk.Entry(form)
    entry_email.grid(row=2, column=1)

    tk.Label(form, text="Gender *", bg="white").grid(row=3, column=0, sticky="w")
    gender_var = tk.StringVar()
    tk.Radiobutton(form, text="Male", variable=gender_var, value="Male", bg="white").grid(row=3, column=1, sticky="w")
    tk.Radiobutton(form, text="Female", variable=gender_var, value="Female", bg="white").grid(row=3, column=1, sticky="e")

    tk.Label(form, text="City *", bg="white").grid(row=4, column=0, sticky="w")
    combo_city = ttk.Combobox(form, values=["Surat", "Ahmedabad", "Vadodara"])
    combo_city.grid(row=4, column=1)

    tk.Label(form, text="State *", bg="white").grid(row=5, column=0, sticky="w")
    combo_state = ttk.Combobox(form, values=["Gujarat", "Maharashtra", "Rajasthan"])
    combo_state.grid(row=5, column=1)

    # Additional Options for Product Manager
    if role == 'product_manager':
        tk.Label(form, text="Permissions", bg="white", font=('Arial', 10, 'bold')).grid(row=6, column=0, sticky="w", pady=(10, 0))

        manage_var = tk.IntVar()
        view_var = tk.IntVar()
        tk.Checkbutton(form, text="Can manage all product stocks", variable=manage_var, bg="white").grid(row=7, column=0, columnspan=2, sticky="w")
        tk.Checkbutton(form, text="Can view all stocks", variable=view_var, bg="white").grid(row=8, column=0, columnspan=2, sticky="w")

    tk.Button(window, text="Register", bg="orange", fg="black", command=register).pack(pady=20)

    window.mainloop()

