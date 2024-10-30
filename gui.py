# gui.py
import customtkinter as ctk
from tkinter import messagebox
from datetime import datetime
from auth import register_user, login_user
from transactions import add_transaction
from export import export_transactions_to_csv
from visualization import visualize_most_expenditure_item, visualize_monthly_surplus

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

class ExpenseTrackerApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Expense Tracker")
        self.geometry("800x600")
        self.configure(bg='white')
        self.user_id = None
        self.user_data = {}

        # Create frames
        self.create_login_frame()
        self.create_home_frame()

        # Start with the login frame
        self.show_frame(self.login_frame)

    def create_login_frame(self):
        self.login_frame = ctk.CTkFrame(self, fg_color='white')

        # Username Entry
        self.username_entry = ctk.CTkEntry(self.login_frame, placeholder_text="Username")
        self.username_entry.pack(pady=10)

        # Password Entry
        self.password_entry = ctk.CTkEntry(self.login_frame, placeholder_text="Password", show="*")
        self.password_entry.pack(pady=10)

        # Login Button
        self.login_button = ctk.CTkButton(self.login_frame, text="Login", command=self.login)
        self.login_button.pack(pady=10)

        # Register Button
        self.register_button = ctk.CTkButton(self.login_frame, text="Register", command=self.register)
        self.register_button.pack(pady=5)

    def create_home_frame(self):
        self.home_frame = ctk.CTkFrame(self, fg_color='white')

        # Time, date, and software name
        self.time_label = ctk.CTkLabel(self.home_frame, text="", text_color='black', font=('Helvetica', 20))
        self.time_label.pack(pady=20)
        self.update_time()

        self.software_name_label = ctk.CTkLabel(self.home_frame, text="Expense Tracker", text_color='black', font=('Helvetica', 24, 'bold'))
        self.software_name_label.pack(pady=10)

        # Display user info
        self.user_info_label = ctk.CTkLabel(self.home_frame, text="", text_color='black', font=('Helvetica', 16))
        self.user_info_label.pack(pady=5)

        # Buttons
        self.add_expense_button = ctk.CTkButton(self.home_frame, text="Add Expense", command=self.add_expense)
        self.add_expense_button.pack(pady=5)
        self.add_earning_button = ctk.CTkButton(self.home_frame, text="Add Earning", command=self.add_earning)
        self.add_earning_button.pack(pady=5)
        self.download_report_button = ctk.CTkButton(self.home_frame, text="Download Report", command=self.download_report)
        self.download_report_button.pack(pady=5)
        self.show_visualization_button = ctk.CTkButton(self.home_frame, text="Show Visualization", command=self.show_visualization)
        self.show_visualization_button.pack(pady=5)

    def show_frame(self, frame):
        frame.pack(fill="both", expand=True)

    def update_time(self):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.time_label.configure(text=now)
        self.after(1000, self.update_time)

    # Authentication Methods
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showwarning("Input Error", "Please enter both username and password.")
            return

        success, result = login_user(username, password)
        if success:
            self.user_data = result
            self.user_id = result['user_id']
            messagebox.showinfo("Login Successful", f"Welcome, {username}!")
            self.login_frame.pack_forget()
            self.show_frame(self.home_frame)
            self.display_user_info(username)
        else:
            messagebox.showerror("Login Failed", result)

    def register(self):
        # Open a new window for registration
        register_window = ctk.CTkToplevel(self)
        register_window.title("Register")
        register_window.geometry("400x500")
        register_window.configure(bg='white')

        # Username Entry
        username_entry = ctk.CTkEntry(register_window, placeholder_text="Username")
        username_entry.pack(pady=10)

        # Password Entry
        password_entry = ctk.CTkEntry(register_window, placeholder_text="Password", show="*")
        password_entry.pack(pady=10)

        # Confirm Password Entry
        confirm_password_entry = ctk.CTkEntry(register_window, placeholder_text="Confirm Password", show="*")
        confirm_password_entry.pack(pady=10)

        # Phone Number Entry
        phone_entry = ctk.CTkEntry(register_window, placeholder_text="Phone Number")
        phone_entry.pack(pady=10)

        # Job Title Entry
        job_entry = ctk.CTkEntry(register_window, placeholder_text="Job Title")
        job_entry.pack(pady=10)

        # Submit Button
        submit_button = ctk.CTkButton(register_window, text="Register", command=lambda: self.submit_registration(
            username_entry.get(),
            password_entry.get(),
            confirm_password_entry.get(),
            phone_entry.get(),
            job_entry.get(),
            register_window
        ))
        submit_button.pack(pady=20)

    def submit_registration(self, username, password, confirm_password, phone_number, job_title, window):
        if not username or not password or not confirm_password:
            messagebox.showwarning("Input Error", "Username and password fields cannot be empty.")
            return

        if password != confirm_password:
            messagebox.showwarning("Input Error", "Passwords do not match.")
            return

        # Optional: Validate phone number format
        if phone_number and not phone_number.isdigit():
            messagebox.showwarning("Input Error", "Phone number must contain only digits.")
            return

        success, message = register_user(username, password, confirm_password, phone_number, job_title)
        if success:
            messagebox.showinfo("Registration Successful", message)
            window.destroy()  # Close the registration window
        else:
            messagebox.showerror("Registration Failed", message)

    # User Information Display
    def display_user_info(self, username):
        job_title = self.user_data.get('job_title', '')
        phone_number = self.user_data.get('phone_number', '')
        info_text = f"Username: {username}\n"
        if job_title:
            info_text += f"Job Title: {job_title}\n"
        if phone_number:
            info_text += f"Phone Number: {phone_number}"
        self.user_info_label.configure(text=info_text)

    # Functionalities
    def add_expense(self):
        if not self.user_id:
            messagebox.showwarning("Authentication Required", "Please login to add expenses.")
            return

        def submit():
            name = name_entry.get()
            quantity = quantity_entry.get()
            price_per_unit = price_entry.get()

            if not name or not quantity or not price_per_unit:
                messagebox.showwarning("Input Error", "All fields are required.")
                return
            try:
                quantity = int(quantity)
                price_per_unit = float(price_per_unit)
            except ValueError:
                messagebox.showwarning("Input Error", "Please enter valid numeric values for quantity and price.")
                return

            add_transaction(self.user_id, 'expense', name, quantity, price_per_unit)
            messagebox.showinfo("Success", "Expense added successfully!")
            add_window.destroy()

        add_window = ctk.CTkToplevel(self)
        add_window.title("Add Expense")
        add_window.geometry("300x300")

        name_entry = ctk.CTkEntry(add_window, placeholder_text="Expense Name")
        name_entry.pack(pady=10)
        quantity_entry = ctk.CTkEntry(add_window, placeholder_text="Quantity")
        quantity_entry.pack(pady=10)
        price_entry = ctk.CTkEntry(add_window, placeholder_text="Price per Unit")
        price_entry.pack(pady=10)
        submit_button = ctk.CTkButton(add_window, text="Submit", command=submit)
        submit_button.pack(pady=10)

    def add_earning(self):
        if not self.user_id:
            messagebox.showwarning("Authentication Required", "Please login to add earnings.")
            return

        def submit():
            name = name_entry.get()
            quantity = quantity_entry.get()
            price_per_unit = price_entry.get()

            if not name or not quantity or not price_per_unit:
                messagebox.showwarning("Input Error", "All fields are required.")
                return
            try:
                quantity = int(quantity)
                price_per_unit = float(price_per_unit)
            except ValueError:
                messagebox.showwarning("Input Error", "Please enter valid numeric values for quantity and price.")
                return

            add_transaction(self.user_id, 'earning', name, quantity, price_per_unit)
            messagebox.showinfo("Success", "Earning added successfully!")
            add_window.destroy()

        add_window = ctk.CTkToplevel(self)
        add_window.title("Add Earning")
        add_window.geometry("300x300")

        name_entry = ctk.CTkEntry(add_window, placeholder_text="Earning Name")
        name_entry.pack(pady=10)
        quantity_entry = ctk.CTkEntry(add_window, placeholder_text="Quantity")
        quantity_entry.pack(pady=10)
        price_entry = ctk.CTkEntry(add_window, placeholder_text="Price per Unit")
        price_entry.pack(pady=10)
        submit_button = ctk.CTkButton(add_window, text="Submit", command=submit)
        submit_button.pack(pady=10)

    def download_report(self):
        if not self.user_id:
            messagebox.showwarning("Authentication Required", "Please login to download reports.")
            return
        from export import export_transactions_to_csv
        export_transactions_to_csv(self.user_id)
        messagebox.showinfo("Success", "Report downloaded successfully!")

    def show_visualization(self):
        if not self.user_id:
            messagebox.showwarning("Authentication Required", "Please login to view visualizations.")
            return

        def show_most_expenditure_item():
            visualize_most_expenditure_item(self.user_id)

        def show_monthly_surplus():
            visualize_monthly_surplus(self.user_id)

        viz_window = ctk.CTkToplevel(self)
        viz_window.title("Visualizations")
        viz_window.geometry("300x200")

        most_expenditure_button = ctk.CTkButton(viz_window, text="Most Expenditure Item", command=show_most_expenditure_item)
        most_expenditure_button.pack(pady=10)

        monthly_surplus_button = ctk.CTkButton(viz_window, text="Monthly Surplus", command=show_monthly_surplus)
        monthly_surplus_button.pack(pady=10)

if __name__ == "__main__":
    app = ExpenseTrackerApp()
    app.mainloop()
