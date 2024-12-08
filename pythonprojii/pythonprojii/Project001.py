from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
import mysql.connector

class Hospital:
    def __init__(self, root):  # Corrected constructor
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1350x750+0+0")

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
        self.PatientMobile = StringVar()  # New variable for mobile number

        # Main Frame
        MainFrame = Frame(self.root)
        MainFrame.grid()

        # Title
        TitleFrame = Frame(MainFrame, bd=20, width=1350, padx=20, relief=RIDGE)
        TitleFrame.pack(side=TOP)

        self.lblTitle = Label(TitleFrame, width=39, font=("arial", 40, "bold"), text="Hospital Management System")
        self.lblTitle.grid()

        # Frame for data entry and display
        DataFrame = Frame(MainFrame, bd=20, width=1350, height=500, padx=20, relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLeft = LabelFrame(DataFrame, bd=10, width=800, height=300, padx=20, relief=RIDGE,
                                   font=("arial", 12, "bold"), text="Prescription")
        DataFrameLeft.pack(side=LEFT)

        DataFrameRight = LabelFrame(DataFrame, bd=10, width=450, height=400, padx=20, relief=RIDGE,
                                    font=("arial", 12, "bold"), text="Prescription Details")
        DataFrameRight.pack(side=RIGHT)

        # Widgets for data entry
        lblNameTablet = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Name of Tablets:", padx=2, pady=6)
        lblNameTablet.grid(row=0, column=0, sticky=W)
        cboNameTablet = Combobox(DataFrameLeft, font=("arial", 13, "bold"), width=35, textvariable=self.NameTablet, state='readonly')
        cboNameTablet['values'] = ('Ascazin', 'Paracetamol', 'Combiflame', 'JIFI 500')
        cboNameTablet.grid(row=0, column=1)

        lblReferenceNo = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Reference No:", padx=2, pady=6)
        lblReferenceNo.grid(row=1, column=0, sticky=W)
        txtReferenceNo = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=35, textvariable=self.ReferenceNo)
        txtReferenceNo.grid(row=1, column=1)

        lblDose = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Dose:", padx=2, pady=6)
        lblDose.grid(row=2, column=0, sticky=W)
        txtDose = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=35, textvariable=self.Dose)
        txtDose.grid(row=2, column=1)

        lblNoOfTablets = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Number of Tablets:", padx=2, pady=6)
        lblNoOfTablets.grid(row=3, column=0, sticky=W)
        txtNoOfTablets = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=35, textvariable=self.NoOfTablets)
        txtNoOfTablets.grid(row=3, column=1)

        lblLot = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Lot:", padx=2, pady=6)
        lblLot.grid(row=4, column=0, sticky=W)
        txtLot = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=35, textvariable=self.Lot)
        txtLot.grid(row=4, column=1)

        lblIssueDate = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Issue Date:", padx=2, pady=6)
        lblIssueDate.grid(row=5, column=0, sticky=W)
        txtIssueDate = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=35, textvariable=self.IssueDate)
        txtIssueDate.grid(row=5, column=1)

        lblExpDate = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Expiry Date:", padx=2, pady=6)
        lblExpDate.grid(row=6, column=0, sticky=W)
        txtExpDate = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=35, textvariable=self.ExpDate)
        txtExpDate.grid(row=6, column=1)

        lblDailyDose = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Daily Dose:", padx=2, pady=6)
        lblDailyDose.grid(row=7, column=0, sticky=W)
        txtDailyDose = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=35, textvariable=self.DailyDose)
        txtDailyDose.grid(row=7, column=1)

        lblSideEffect = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Side Effect:", padx=2, pady=6)
        lblSideEffect.grid(row=8, column=0, sticky=W)
        txtSideEffect = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=35, textvariable=self.SideEffect)
        txtSideEffect.grid(row=8, column=1)

        lblFurtherInfo = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Further Information:", padx=2, pady=6)
        lblFurtherInfo.grid(row=9, column=0, sticky=W)
        txtFurtherInfo = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=35, textvariable=self.FurtherInfo)
        txtFurtherInfo.grid(row=9, column=1)

        lblBloodPressure = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Blood Pressure:", padx=2, pady=6)
        lblBloodPressure.grid(row=10, column=0, sticky=W)
        txtBloodPressure = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=35, textvariable=self.BloodPressure)
        txtBloodPressure.grid(row=10, column=1)

        lblPatientName = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Patient Name:", padx=2, pady=6)
        lblPatientName.grid(row=11, column=0, sticky=W)
        txtPatientName = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=35, textvariable=self.PatientName)
        txtPatientName.grid(row=11, column=1)

        lblPatientID = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Patient ID:", padx=2, pady=6)
        lblPatientID.grid(row=12, column=0, sticky=W)
        txtPatientID = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=35, textvariable=self.PatientID)
        txtPatientID.grid(row=12, column=1)

        lblPatientAddress = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Patient Address:", padx=2, pady=6)
        lblPatientAddress.grid(row=13, column=0, sticky=W)
        txtPatientAddress = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=35, textvariable=self.PatientAddress)
        txtPatientAddress.grid(row=13, column=1)

        lblPatientInformation = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Patient Information:", padx=2, pady=6)
        lblPatientInformation.grid(row=14, column=0, sticky=W)
        txtPatientInformation = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=35, textvariable=self.PatientInformation)
        txtPatientInformation.grid(row=14, column=1)

        lblPatientMobile = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Patient Mobile:", padx=2, pady=6)  # New label for mobile number
        lblPatientMobile.grid(row=15, column=0, sticky=W)
        txtPatientMobile = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=35, textvariable=self.PatientMobile)  # Entry for mobile number
        txtPatientMobile.grid(row=15, column=1)

        # Prescription Details Text Box
        self.txtPrescriptionDetails = Text(DataFrameRight, font=("arial", 12, "bold"), width=45, height=15, padx=10, pady=10)
        self.txtPrescriptionDetails.grid(row=0, column=0)

        # Buttons for actions
        buttonFrame = Frame(DataFrameRight)
        buttonFrame.grid(row=1, column=0, pady=10)

        btnAddPrescription = Button(buttonFrame, text="Add Prescription", bg="lightblue", width=15, command=self.add_prescription)
        btnAddPrescription.grid(row=0, column=0, padx=5)

        btnClear = Button(buttonFrame, text="Clear", bg="orange", width=15, command=self.clear_fields)
        btnClear.grid(row=0, column=1, padx=5)

        btnExit = Button(buttonFrame, text="Exit", bg="red", width=15, command=self.exit_application)
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
        self.PatientInformation.set("")
        self.PatientMobile.set("")
        self.txtPrescriptionDetails.delete(1.0, END)  # Clear prescription details text box

    def exit_application(self):
        if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            self.root.destroy()  # Close the application

if __name__ == "__main__":  # Corrected main check
    root = Tk()
    application = Hospital(root)
    root.mainloop()