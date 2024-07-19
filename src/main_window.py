import customtkinter as ctk
import tkinter.messagebox
from gui.room import RoomManagement
from gui.reservation import ReservationManagement
from gui.customer import CustomerManagement
from gui.bill import BillManagement

class MainWindow:
    def __init__(self, master):
        self.master = master
        
        # Create a notebook (tabbed interface)
        self.notebook = ctk.CTkTabview(self.master)
        self.notebook.pack(expand=True, fill="both", padx=10, pady=10)

        # Create tabs
        self.customer_tab = self.notebook.add("Customers")
        self.reservation_tab = self.notebook.add("Reservations")
        self.billing_tab = self.notebook.add("Billing")
        self.room_tab = self.notebook.add("Room Management")

        # Initialize tab contents
        self.customer_management = CustomerManagement(self.customer_tab)
        self.reservation_management = ReservationManagement(self.reservation_tab)
        self.billing = BillManagement(self.billing_tab)
        self.room_management = RoomManagement(self.room_tab)
        
        # Add a logout button
        self.logout_button = ctk.CTkButton(self.master, text="Logout", command=self.logout)
        self.logout_button.pack(pady=10)

    def logout(self):
        if tkinter.messagebox.askyesno("Logout", "Are you sure you want to logout?"):
            self.master.quit()