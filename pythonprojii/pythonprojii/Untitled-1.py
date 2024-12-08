from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
import mysql.connector

class Hospital:
    def __init__(self, root):  
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1350x750+0+0")
        self.root.config(bg="#f4f4f9")  # Light gray background for the root window

        # Database connection
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="your_username",  # replace with your MySQL username
                password="your_password",  # replace with your MySQL password
                database="hospital_db"
            )
            self.cursor = self.conn.cursor()
        except mysql.connector.Error as err:
            messagebox.showerror("Database Connection Error", f"Error: {err}")
            self.conn = None

        # Define variables to hold data
        self.NameTablet = StringVar()
        self.ReferenceNo = StringVar()
        self.Dose = StringVar()
        self.NoOfTablets = StringVar()
        self.Lot = StringVar()
        self.IssueDate = StringVar()
        self.ExpDate = StringVar()
        self.DailyDose = StringVar()
        self.SideEffect = StringVar()
        self.FurtherInfo = StringVar()
        self.BloodPressure = StringVar()
        self.PatientName = StringVar()
        self.PatientID = StringVar()
        self.PatientAddress = StringVar()
        self.PatientInformation = StringVar()
        self.PatientMobile = StringVar()

        # Main Frame
        MainFrame = Frame(self.root, bg="#f4f4f9")
        MainFrame.grid()

        # Title Frame
        TitleFrame = Frame(MainFrame, bd=20, width=1350, padx=20, relief=RIDGE, bg="#4a90e2")
        TitleFrame.pack(side=TOP)

        self.lblTitle = Label(TitleFrame, width=39, font=("Helvetica", 40, "bold"), text="Hospital Management System", bg="#4a90e2", fg="white")
        self.lblTitle.grid()

        # Data Frame for input fields and prescription details
        DataFrame = Frame(MainFrame, bd=20, width=1350, height=500, padx=20, relief=RIDGE, bg="#f4f4f9")
        DataFrame.pack(side=BOTTOM)

        DataFrameLeft = LabelFrame(DataFrame, bd=10, width=800, height=300, padx=20, relief=RIDGE, font=("Helvetica", 12, "bold"), text="Prescription", bg="#f4f4f9")
        DataFrameLeft.pack(side=LEFT)

        DataFrameRight = LabelFrame(DataFrame, bd=10, width=450, height=400, padx=20, relief=RIDGE, font=("Helvetica", 12, "bold"), text="Prescription Details", bg="#f4f4f9")
        DataFrameRight.pack(side=RIGHT)

        # Widgets for Data Entry
        lblNameTablet = Label(DataFrameLeft, font=("Helvetica", 12, "bold"), text="Name of Tablets:", padx=2, pady=6, bg="#f4f4f9")
        lblNameTablet.grid(row=0, column=0, sticky=W)
        cboNameTablet = Combobox(DataFrameLeft, font=("Helvetica", 13, "bold"), width=35, textvariable=self.NameTablet, state='readonly')
        cboNameTablet['values'] = ('Ascazin', 'Paracetamol', 'Combiflame', 'JIFI 500')
        cboNameTablet.grid(row=0, column=1)

        lblReferenceNo = Label(DataFrameLeft, font=("Helvetica", 12, "bold"), text="Reference No:", padx=2, pady=6, bg="#f4f4f9")
        lblReferenceNo.grid(row=1, column=0, sticky=W)
        txtReferenceNo = Entry(DataFrameLeft, font=("Helvetica", 13, "bold"), width=35, textvariable=self.ReferenceNo)
        txtReferenceNo.grid(row=1, column=1)

        lblDose = Label(DataFrameLeft, font=("Helvetica", 12, "bold"), text="Dose:", padx=2, pady=6, bg="#f4f4f9")
        lblDose.grid(row=2, column=0, sticky=W)
        txtDose = Entry(DataFrameLeft, font=("Helvetica", 13, "bold"), width=35, textvariable=self.Dose)
        txtDose.grid(row=2, column=1)

        lblNoOfTablets = Label(DataFrameLeft, font=("Helvetica", 12, "bold"), text="Number of Tablets:", padx=2, pady=6, bg="#f4f4f9")
        lblNoOfTablets.grid(row=3, column=0, sticky=W)
        txtNoOfTablets = Entry(DataFrameLeft, font=("Helvetica", 13, "bold"), width=35, textvariable=self.NoOfTablets)
        txtNoOfTablets.grid(row=3, column=1)

        # Other input fields here...

        lblPatientMobile = Label(DataFrameLeft, font=("Helvetica", 12, "bold"), text="Patient Mobile:", padx=2, pady=6, bg="#f4f4f9")
        lblPatientMobile.grid(row=15, column=0, sticky=W)
        txtPatientMobile = Entry(DataFrameLeft, font=("Helvetica", 13, "bold"), width=35, textvariable=self.PatientMobile)
        txtPatientMobile.grid(row=15, column=1)

        # Prescription Details Text Box
        self.txtPrescriptionDetails = Text(DataFrameRight, font=("Helvetica", 12, "bold"), width=45, height=15, padx=10, pady=10)
        self.txtPrescriptionDetails.grid(row=0, column=0)

        # Buttons
        buttonFrame = Frame(DataFrameRight, bg="#f4f4f9")
        buttonFrame.grid(row=1, column=0, pady=10)

        btnAddPrescription = Button(buttonFrame, text="Add Prescription", bg="#5cb85c", fg="white", width=15, font=("Helvetica", 12, "bold"), command=self.add_prescription)
        btnAddPrescription.grid(row=0, column=0, padx=5)

        btnClear = Button(buttonFrame, text="Clear", bg="#f0ad4e", fg="white", width=15, font=("Helvetica", 12, "bold"), command=self.clear_fields)
        btnClear.grid(row=0, column=1, padx=5)

        btnExit = Button(buttonFrame, text="Exit", bg="#d9534f", fg="white", width=15, font=("Helvetica", 12, "bold"), command=self.exit_application)
        btnExit.grid(row=0, column=2, padx=5)

    def add_prescription(self):
        if self.conn:
            try:
                # Collect data from input fields
                data = (
                    self.NameTablet.get(),
                    self.ReferenceNo.get(),
                    self.Dose.get(),
                    self.NoOfTablets.get(),
                    self.Lot.get(),
                    self.IssueDate.get(),
                    self.ExpDate.get(),
                    self.DailyDose.get(),
                    self.SideEffect.get(),
                    self.FurtherInfo.get(),
                    self.BloodPressure.get(),
                    self.PatientName.get(),
                    self.PatientID.get(),
                    self.PatientAddress.get(),
                    self.PatientInformation.get(),
                    self.PatientMobile.get()
                )
                # Insert the data into the database (adjust the SQL query as necessary)
                query = """INSERT INTO prescriptions (NameTablet, ReferenceNo, Dose, NoOfTablets, Lot, IssueDate, ExpDate, DailyDose,
                           SideEffect, FurtherInfo, BloodPressure, PatientName, PatientID, PatientAddress, PatientInformation, PatientMobile)
                           VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                self.cursor.execute(query, data)
                self.conn.commit()
                messagebox.showinfo("Success", "Prescription added successfully.")
                self.clear_fields()  # Clear fields after successful insertion
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error: {err}")

    def clear_fields(self):
        # Clear all input fields
        self.NameTablet.set("")
        self.ReferenceNo.set("")
        self.Dose.set("")
        self.NoOfTablets.set("")
        self.Lot.set("")
        self.IssueDate.set("")
        self.ExpDate.set("")
        self.DailyDose.set("")
        self.SideEffect.set("")
        self.FurtherInfo.set("")
        self.BloodPressure.set("")
        self.PatientName.set("")
        self.PatientID.set("")
        self.PatientAddress.set("")
