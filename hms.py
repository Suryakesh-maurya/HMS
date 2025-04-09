import random
import time 
import datetime
from tkinter import messagebox
import mysql.connector

from tkinter import *
from tkinter import ttk 

class Hospital:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")

        # Database variables
        self.Nameoftablets = StringVar()
        self.ref = StringVar()
        self.Dose = StringVar()
        self.NumberofTablets = StringVar()
        self.Lot = StringVar()
        self.Issuedate = StringVar()
        self.ExpDate = StringVar()
        self.DailyDose = StringVar()
        self.sideEfect = StringVar()
        self.FurtherInformation = StringVar()
        self.StorageAdvice = StringVar()
        self.BloodPressur = StringVar()
        self.HowToUseMedication = StringVar()
        self.PatientId = StringVar()
        self.nhsNumber = StringVar()
        self.PatientName = StringVar()
        self.DateOfBirth = StringVar()
        self.PatientAddress = StringVar()






        lbltitle = Label(self.root, bd=20, relief=RIDGE, text="HOSPITAL MANAGEMENT SYSTEM", 
                         fg="red", bg="white", font=("times new roman", 50, "bold"))
        lbltitle.pack(side=TOP, fill=X)
      # ---------- data Frame------------------
        DataFrame = Frame(self.root, bd=20, relief=RIDGE)
        DataFrame.place(x=0, y=130, width=1530, height=400)

        DataFrameLeft = LabelFrame(DataFrame, bd=10, padx=20, relief=RIDGE,
                                   font=("arial", 12, "bold"), text="Patient Information")
        DataFrameLeft.place(x=0, y=5, width=980, height=350)

        DataFrameRight = LabelFrame(DataFrame, bd=10, padx=20, relief=RIDGE,
                                    font=("arial", 12, "bold"), text="Prescription")
        DataFrameRight.place(x=990, y=5, width=460, height=350)

        # ------------------- Button Frames ----------------------
        Buttonframe = Frame(self.root, bd=20, relief=RIDGE)
        Buttonframe.place(x=0, y=530, width=1530, height=70)


        # ------------------- Details Frame-----------------------
        DetailFrame = Frame(self.root, bd=20, relief=RIDGE)
        DetailFrame.place(x=0, y=600, width=1530, height=190)

        # -------------------- DataFramesLeft ------------------------
        lblNameTablet =Label(DataFrameLeft,font=("arial",12,"bold"),text="Name of Tablet",padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0,sticky=W)

        comNameTablet=ttk.Combobox(DataFrameLeft, textvariable=self.Nameoftablets,state="readonly",
                                    font=("arial",12,"bold"),width=33)
        comNameTablet['value']=("Nice","Corona Vaccine","Acetaminophen","Adderall","Amlodipin","Ativan")
        comNameTablet.current(0)
        comNameTablet.grid(row=0,column=1)

        lblref=Label(DataFrameLeft, font=("arial",12, "bold"),text="Refrence No:", padx=2,)
        lblref.grid(row=1,column=0,sticky=W)
        txtref=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.ref,width=35)
        txtref.grid(row=1,column=1)


        lblDose=Label(DataFrameLeft, font=("arial",12, "bold"),text="Dose :", padx=2,pady=6)
        lblDose.grid(row=2,column=0,sticky=W)
        txtDose=Entry(DataFrameLeft,font=("arial",13,"bold"), textvariable=self.Dose, width=35)
        txtDose.grid(row=2,column=1)

        lblNoOfTablet=Label(DataFrameLeft, font=("arial",12, "bold"),text="No of Tablets :", padx=2,pady=6)
        lblNoOfTablet.grid(row=3,column=0,sticky=W)
        txtNoOfTablet=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.NumberofTablets,width=35)
        txtNoOfTablet.grid(row=3,column=1)

        lblLot=Label(DataFrameLeft, font=("arial",12, "bold"),text="Lot :", padx=2,pady=6)
        lblLot.grid(row=4,column=0,sticky=W)
        txtLot=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.Lot, width=35)
        txtLot.grid(row=4,column=1)

        lblIssueDate=Label(DataFrameLeft, font=("arial",12, "bold"),text="Issue Date :", padx=2,pady=6)
        lblIssueDate.grid(row=5,column=0,sticky=W)
        txtIssueDate=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.Issuedate, width=35)
        txtIssueDate.grid(row=5,column=1)

        lblExpDate=Label(DataFrameLeft, font=("arial",12, "bold"),text="Exp Date :", padx=2,pady=6)
        lblExpDate.grid(row=6,column=0,sticky=W)
        txtExpDate=Entry(DataFrameLeft,font=("arial",13,"bold"), textvariable=self.ExpDate, width=35)
        txtExpDate.grid(row=6,column=1)

        lblDailyDose=Label(DataFrameLeft, font=("arial",12, "bold"),text="Daily Dose :", padx=2,pady=6)
        lblDailyDose.grid(row=7,column=0,sticky=W)
        txtDailyDose=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.DailyDose, width=35)
        txtDailyDose.grid(row=7,column=1)

        lblSideEffect=Label(DataFrameLeft, font=("arial",12, "bold"),text="Side Effect :", padx=2,pady=6)
        lblSideEffect.grid(row=8,column=0,sticky=W)
        txtSideEffect=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.sideEfect,width=35)
        txtSideEffect.grid(row=8,column=1)


        # --------------- second Portion right  left --------------------

        
        lblFurtheInfo=Label(DataFrameLeft, font=("arial",12, "bold"),text="Further Information:", padx=2,)
        lblFurtheInfo.grid(row=0,column=2,sticky=W)
        txtFurtherInfo=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.FurtherInformation, width=35)
        txtFurtherInfo.grid(row=0,column=3)


        lblBloodPressor=Label(DataFrameLeft, font=("arial",12, "bold"),text="Blood Pressur :", padx=2,pady=6)
        lblBloodPressor.grid(row=1,column=2,sticky=W)
        txtBloodPressor=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.BloodPressur, width=35)
        txtBloodPressor.grid(row=1,column=3)

        lblStorage=Label(DataFrameLeft, font=("arial",12, "bold"),text="Storage Advice :", padx=2,pady=6)
        lblStorage.grid(row=2,column=2,sticky=W)
        txtStorage=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.StorageAdvice, width=35)
        txtStorage.grid(row=2,column=3)

        lblMedicine=Label(DataFrameLeft, font=("arial",12, "bold"),text="Medication :", padx=2,pady=6)
        lblMedicine.grid(row=3,column=2,sticky=W)
        txtMedicine=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.HowToUseMedication, width=35)
        txtMedicine.grid(row=3,column=3)

        lblPatientId=Label(DataFrameLeft, font=("arial",12, "bold"),text="Patient Id :", padx=2,pady=6)
        lblPatientId.grid(row=4,column=2,sticky=W)
        txtPatientId=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.PatientId, width=35)
        txtPatientId.grid(row=4,column=3)

        lblNhsNumber=Label(DataFrameLeft, font=("arial",12, "bold"),text="Nhs Number :", padx=2,pady=6)
        lblNhsNumber.grid(row=5,column=2,sticky=W)
        txtNhsNumber=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.nhsNumber, width=35)
        txtNhsNumber.grid(row=5,column=3)

        lblPatientName=Label(DataFrameLeft, font=("arial",12, "bold"),text="Patient Name :", padx=2,pady=6)
        lblPatientName.grid(row=6,column=2,sticky=W)
        txtPatientName=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.PatientName, width=35)
        txtPatientName.grid(row=6,column=3)

        lblDateofBirth=Label(DataFrameLeft, font=("arial",12, "bold"),text="Date Of Birth :", padx=2,pady=6)
        lblDateofBirth.grid(row=7,column=2,sticky=W)
        txtDateofBirth=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.DateOfBirth, width=35)
        txtDateofBirth.grid(row=7,column=3)

        lblPatientAddress=Label(DataFrameLeft, font=("arial",12, "bold"),text="Patient Address :", padx=2,pady=6)
        lblPatientAddress.grid(row=8,column=2,sticky=W)
        txtPatientAddress=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.PatientAddress, width=35)
        txtPatientAddress.grid(row=8,column=3)

        # -------------------- Data Frame Right -------------------------------------

        self.txtPrescription = Text(DataFrameRight, font=("arial", 12, "bold"), width=44, height=16, padx=2, pady=6) 
        self.txtPrescription.grid(row=0, column=0)

        # --------------------------- Button -----------------------------------------
        btnPrescription = Button(Buttonframe, command=self.iPrescription, text="Prescription", bg="green", fg="white", font=("arial",12,"bold"), width=23,  padx=2, pady=6)
        btnPrescription.grid(row=0,column=0)

        btnPrescriptionData = Button(Buttonframe, text="Prescription Data", bg="green", fg="white",
                                     font=("arial", 12, "bold"), width=23, padx=2, pady=6,
                                     command=self.iPrescriptionData)
        btnPrescriptionData.grid(row=0, column=1)


        btnUpdate = Button(Buttonframe,command=self.update_data,text="Update", bg="green", fg="white", font=("arial",12,"bold"), width=23,  padx=2, pady=6)
        btnUpdate.grid(row=0,column=2)
         
        btnDelete = Button(Buttonframe,command=self.idelete, text="Delete",bg="green", fg="white", font=("arial",12,"bold"), width=23,  padx=2, pady=6 )
        btnDelete.grid(row=0,column=3)

        btnClear = Button(Buttonframe,command=self.clear, text="Clear", bg="green", fg="white" ,font=("arial",12,"bold"), width=23,  padx=2, pady=6 )
        btnClear.grid(row=0, column=4)

        btnExit = Button(Buttonframe,command=self.exit_app, text="Exit",bg="green", fg="white" ,font=("arial",12,"bold"), width=23,  padx=2, pady=6 )
        btnExit.grid(row=0,column=5)

        # --------------------- Table ----------------------------------------------
        # ======================= SCROLL==============================================
        
        scroll_x = ttk.Scrollbar(DetailFrame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(DetailFrame, orient=VERTICAL)

        self.hospital_table = ttk.Treeview(DetailFrame,
                                           columns=("nameoftablets", "ref", "dose", "nooftablets", "lot", "issuedate",
                                                    "expdate", "dailydose","sideEfect","furtherInformation", "storage", "bloodPressur", "medication","patientId", "nhsnumber", "pname", "dob", "address"),
                                           xscrollcommand=scroll_x.set,
                                           yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.hospital_table.xview)
        scroll_y.config(command=self.hospital_table.yview)

        self.hospital_table.heading("nameoftablets", text="Name of Tablets")
        self.hospital_table.heading("ref", text="Reference No.")
        self.hospital_table.heading("dose", text="Dose")
        self.hospital_table.heading("nooftablets", text="No of Tablets")
        self.hospital_table.heading("lot", text="Lot")
        self.hospital_table.heading("issuedate", text="Issue Date")
        self.hospital_table.heading("expdate", text="Exp Date")
        self.hospital_table.heading("dailydose", text="Daily Dose")
        self.hospital_table.heading("sideEfect", text="SideEfect")
        self.hospital_table.heading("furtherInformation",text="Further information")
        self.hospital_table.heading("storage", text="Storage")
        self.hospital_table.heading("bloodPressur",text="BloodPressur")
        self.hospital_table.heading("medication", text="Medication")
        self.hospital_table.heading("patientId", text="PatientId")
        self.hospital_table.heading("nhsnumber", text="NHS Number")
        self.hospital_table.heading("pname", text="Patient Name")
        self.hospital_table.heading("dob", text="DOB")
        self.hospital_table.heading("address", text="Address")

        self.hospital_table["show"] = "headings"

        self.hospital_table.column("nameoftablets", width=100)
        self.hospital_table.column("ref", width=100)
        self.hospital_table.column("dose", width=100)
        self.hospital_table.column("nooftablets", width=100)
        self.hospital_table.column("lot", width=100)
        self.hospital_table.column("issuedate", width=100)
        self.hospital_table.column("expdate", width=100)
        self.hospital_table.column("dailydose", width=100)
        self.hospital_table.column("sideEfect", width=100)
        self.hospital_table.column("furtherInformation", width=100)
        self.hospital_table.column("storage", width=100)
        self.hospital_table.column("bloodPressur", width=100)
        self.hospital_table.column("medication", width=100)
        self.hospital_table.column("patientId", width=100)
        self.hospital_table.column("nhsnumber", width=100)
        self.hospital_table.column("pname", width=100)
        self.hospital_table.column("dob", width=100)
        self.hospital_table.column("address", width=100)

        self.hospital_table.pack(fill=BOTH, expand=1)
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cusrsor)

        self.fetch_data()

    #  Function to insert data into MySQL
    def iPrescriptionData(self):
        if self.Nameoftablets.get() == "" or self.ref.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="Maurya@123",  # Replace with your actual password
                    database="hospitaldb"
                )
                my_cursor = conn.cursor()
                query = """
                    INSERT INTO hospital (
                        Nameoftablets, ref, Dose, NumberofTablets, Lot,
                        Issuedate, ExpDate, DailyDose, sideEfect,
                        FurtherInformation, StorageAdvice, BloodPressur,
                        HowToUseMedication, PatientId, nhsNumber,
                        PatientName, DateOfBirth, PatientAddress
                    )
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                values = (
                    self.Nameoftablets.get(), 
                    self.ref.get(), 
                    self.Dose.get(),
                    self.NumberofTablets.get(),
                    self.Lot.get(),
                    self.Issuedate.get(), 
                    self.ExpDate.get(), 
                    self.DailyDose.get(),
                    self.sideEfect.get(), 
                    self.FurtherInformation.get(), 
                    self.StorageAdvice.get(),
                    self.BloodPressur.get(), 
                    self.HowToUseMedication.get(), 
                    self.PatientId.get(),
                    self.nhsNumber.get(), 
                    self.PatientName.get(), 
                    self.DateOfBirth.get(), 
                    self.PatientAddress.get()
                )
                my_cursor.execute(query, values)
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Record has been inserted successfully")

            except Exception as e:
                messagebox.showerror("Database Error", f"An error occurred: {str(e)}")
        
        # ------------------- Update ------------------def update_data(self):
    def update_data(self):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Maurya@123",
                database="hospitaldb"
            )
            my_cursor = conn.cursor()
            query = """UPDATE hospital SET 
                Nameoftablets=%s, Dose=%s, NumberofTablets=%s, Lot=%s,
                Issuedate=%s, ExpDate=%s, DailyDose=%s, sideEfect=%s, 
                FurtherInformation=%s, StorageAdvice=%s, BloodPressur=%s,
                HowToUseMedication=%s, PatientId=%s, nhsNumber=%s, 
                PatientName=%s, DateOfBirth=%s, PatientAddress=%s 
                WHERE ref=%s"""
            values = (
                self.Nameoftablets.get(),
                self.Dose.get(),
                self.NumberofTablets.get(),
                self.Lot.get(),
                self.Issuedate.get(),
                self.ExpDate.get(),
                self.DailyDose.get(),
                self.sideEfect.get(),
                self.FurtherInformation.get(),
                self.StorageAdvice.get(),
                self.BloodPressur.get(),
                self.HowToUseMedication.get(),
                self.PatientId.get(),
                self.nhsNumber.get(),
                self.PatientName.get(),
                self.DateOfBirth.get(),
                self.PatientAddress.get(),
                self.ref.get()
            )
            my_cursor.execute(query, values)
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update", "Record has been updated successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Update failed: {str(e)}")

        # -------------------------- Prescription------------------
    def iPrescription(self):
        self.txtPrescription.insert(END,"name of Tablest:\t\t\t"+self.Nameoftablets.get()+"\n")
        self.txtPrescription.insert(END,"Refrence No:\t\t\t"+self.ref.get()+"\n")
        self.txtPrescription.insert(END,"Number of Tablets:\t\t\t"+self.NumberofTablets.get()+"\n")
        self.txtPrescription.insert(END,"Lot:\t\t\t"+self.Lot.get()+"\n")
        self.txtPrescription.insert(END,"Issue Date: \t\t\t"+self.Issuedate.get()+"\n")
        self.txtPrescription.insert(END, "EXP Date:\t\t\t"+self.ExpDate.get()+"\n")
        self.txtPrescription.insert(END,"Daily Dose:\t\t\t"+self.DailyDose.get()+"\n")
        self.txtPrescription.insert(END,"Side Efect:\t\t\t"+self.sideEfect.get()+"\n")
        self.txtPrescription.insert(END,"Furter Information:\t\t\t"+self.FurtherInformation.get()+"\n")
        self.txtPrescription.insert(END, "Storage Advice:\t\t\t"+self.StorageAdvice.get()+"\n")
        self.txtPrescription.insert(END,"Blood Pressure:\t\t\t"+self.BloodPressur.get()+"\n")
        self.txtPrescription.insert(END,"How To Medication:\t\t\t"+self.HowToUseMedication.get()+"\n")
        self.txtPrescription.insert(END,"Patient Id:\t\t\t"+self.PatientId.get()+"\n")
        self.txtPrescription.insert(END,"NHS Number:\t\t\t"+self.nhsNumber.get()+"\n")
        self.txtPrescription.insert(END,"Patient Nmae:\t\t\t"+self.PatientName.get()+"\n")
        self.txtPrescription.insert(END,"Date Of Birth:\t\t\t"+self.DateOfBirth.get()+"\n")
        self.txtPrescription.insert(END,"Patient Address:\t\t\t"+self.PatientAddress.get()+"\n")

        # ---------------------------------------Delete------------------------------------
    def idelete(self):
        # if self.ref.get() == "":
        #     messagebox.showerror("Error", "Please select a patient to delete")
        #     return

        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Maurya@123",
            database="hospitaldb"
        )
        my_cursor = conn.cursor()
        query = "delete from hospital where ref = %s"
        value = (self.ref.get(),)
        my_cursor.execute(query, value)

        conn.commit()
        conn.close()
        self.fetch_data()  # Refresh the screen
        messagebox.showinfo("Delete", "Patient has been deleted successfully")

        # ============================== Clear=====================================

    def clear(self):
        self.Nameoftablets.set("")
        self.ref.set("")
        self.Dose.set("")
        self.NumberofTablets.set("")
        self.Lot.set("")
        self.Issuedate.set("")
        self.ExpDate.set("")
        self.DailyDose.set("")
        self.sideEfect.set("")
        self.FurtherInformation.set("")
        self.StorageAdvice.set("")
        self.BloodPressur.set("")
        self.HowToUseMedication.set("")
        self.PatientId.set("")
        self.nhsNumber.set("")
        self.PatientName.set("")
        self.DateOfBirth.set("")
        self.PatientAddress.set("")
        self.txtPrescription.delete("1.0", END)


    # ============================= Exit ==============================
    def exit_app(self):
        confirm = messagebox.askyesno("Exit", "Are you sure you want to exit?")
        if confirm:
            self.root.destroy()



    def fetch_data(self):
        conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="Maurya@123",  # Replace with your actual password
                    database="hospitaldb"
                )
        my_cursor = conn.cursor()
        my_cursor.execute("select * from hospital")
        rows = my_cursor.fetchall()
        if len(rows)!=0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("", END,values=i)
                # conn.commit()
            conn.close()

    def get_cusrsor(self,event = ""):
        cursor_row = self.hospital_table.focus()
        content = self.hospital_table.item(cursor_row)
        row = content["values"]
        self.Nameoftablets.set(row[0])
        self.ref.set(row[1])
        self.Dose.set(row[2])
        self.NumberofTablets.set(row[3])
        self.Lot.set(row[4])
        self.Issuedate.set(row[5])
        self.ExpDate.set(row[6])
        self.DailyDose.set(row[7])
        self.sideEfect.set(row[8])
        self.FurtherInformation.set(row[9])
        self.StorageAdvice.set(row[10])
        self.BloodPressur.set(row[11])
        self.HowToUseMedication.set(row[12])
        self.PatientId.set(row[13])
        self.nhsNumber.set(row[14])
        self.PatientName.set(row[15])
        self.DateOfBirth.set(row[16])
        self.PatientAddress.set(row[17])



if __name__ == "__main__":
    root = Tk()
    app = Hospital(root)  # Creates an instance of the Hospital class
    root.mainloop()

