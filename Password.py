import tkinter as tk
from tkinter import ttk, messagebox
from decimal import Decimal, getcontext
import pyperclip

getcontext().prec = 100


def generate_password():
    try:
        n = entry_name.get().upper()
        n = ''.join(n.split())
        l = len(n)
        k = 0
        if ord(n[0]) >= 65 and ord(n[0]) <= 90:
            k = 1
            for i in n:
                n = n + str(ord(i))
            n = n[l:]
            l = len(n)

        try:  # Check for valid numeric input
            int(n)  # will raise error for names which also contains non digits
        except ValueError:
            pass

        n = Decimal('0.' + n)

        company_name = entry_company.get()
        company_name = ''.join(company_name.split())
        if not company_name:
            messagebox.showerror("Error", "Pnemonic cannot be empty")  # raise error if no pnemonic input
            return  # added so the program does not break if nothing given in name

        iterations = l + len(company_name)
        res = ""

        for i in range(iterations):
            n = n * 16
            integer_part = int(n)
            st = hex(integer_part)[2:]
            res = res + st
            n -= integer_part

        password = res
        output_text.delete(1.0, tk.END)  # added this as you mentioned that u needed only current passsword
        output_text.insert(tk.END, password)
        pyperclip.copy(password)


    except Exception as e:
        messagebox.showerror("Error",
                             "Invalid Input Please make sure input text  contains either only integers or only alpha characters")
        print(f"Error: {e}")


root = tk.Tk()
root.title("Password Generator")

label_name = ttk.Label(root, text="Enter a name or number:")
label_name.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
entry_name = ttk.Entry(root)
entry_name.grid(row=0, column=1, padx=5, pady=5)

label_company = ttk.Label(root, text="Enter pnemonic:")
label_company.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
entry_company = ttk.Entry(root)
entry_company.grid(row=1, column=1, padx=5, pady=5)

generate_button = ttk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=2, column=0, columnspan=2, pady=10)

output_text = tk.Text(root, wrap=tk.WORD, height=2)
output_text.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
