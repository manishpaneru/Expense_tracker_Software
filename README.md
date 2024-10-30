Introduction
Welcome to the Simple Expense Tracker! This is a straightforward Python application designed to help users track their expenses and earnings. It features a clean and minimalistic graphical user interface (GUI) inspired by Pinterest's white and blue accent scheme.

Features
User Authentication

Secure registration with username, password, phone number, and job title.
Login functionality with password hashing for security.
Expense and Earning Management

Add expenses and earnings with details like name, quantity, and price per unit.
Automatic calculation of the total amount spent or earned.
Data Export

Download your transaction history as a CSV file for personal records or further analysis.
Data Visualization

Visual representations of your financial data using Matplotlib.
View your most significant expenses and monthly surplus.
User-Friendly GUI

Clean design with a focus on simplicity and ease of use.
Real-time display of current time and date.
Accessible buttons for all main functionalities.
Prerequisites
Python 3.x

Required Python Libraries:


pip install bcrypt customtkinter pandas matplotlib
Installation
Clone the Repository


git clone https://github.com/yourusername/expense-tracker.git
cd expense-tracker
Install Required Libraries


pip install bcrypt customtkinter pandas matplotlib
Initialize the Database

Run the database setup script to create the necessary SQLite database and tables.


python db_setup.py
Usage
Run the Application


python gui.py
Register a New User

Click on the "Register" button.
Fill in the required fields:
Username
Password
Confirm Password
Phone Number (optional)
Job Title (optional)
Click "Register" to create your account.
Login

Enter your registered username and password.
Click "Login" to access the main application.
Add Expenses and Earnings

Use the "Add Expense" and "Add Earning" buttons to input your financial data.
Fill in the details:
Name
Quantity
Price per Unit
Download Reports

Click on "Download Report" to export your transactions to a CSV file.
View Visualizations

Use the "Show Visualization" button to access graphical representations of your data.
Options include:
Most significant expenditure item.
Monthly surplus analysis.
Project Structure
arduino
Copy code
expense-tracker/
├── auth.py
├── db_setup.py
├── export.py
├── gui.py
├── transactions.py
├── visualization.py
├── README.md
auth.py: Handles user authentication.
db_setup.py: Initializes the database and creates tables.
export.py: Manages data export to CSV files.
gui.py: The main GUI application.
transactions.py: Functions for adding expenses and earnings.
visualization.py: Generates data visualizations.
README.md: Project documentation.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
This project was created as a fun exploration into combining data analysis skills with basic software development. It serves as a simple tool for personal finance management and is open for further enhancements.

