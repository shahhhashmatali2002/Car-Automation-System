# Car Automation System
# Import library
from tkinter import*
from tkinter import messagebox
import pandas as pd
from PIL import Image, ImageTk
#All work in function
def comeback1():
    #window creating
    car = Tk()
    car.title('Car Automation System')
    car.geometry("1360x768")
#image for back ground
    toyota = ImageTk.PhotoImage(file="C:/images/toyta1.jpg")
    toyota1 = Label(car, image=toyota).pack()
    def open():
        #window destroying
        car.destroy()

        #New window creating
        def comeback2():
            cars= Tk()
            #window geometry and title creating
            cars.geometry('1360x768')
            cars.title('Car Automation System')
            # toyota = ImageTk.PhotoImage(file="C:/images/Corrola_Altis1.jpg")
            # toyota1 = Label(cars, image=toyota).place(x=750, y=50)
            label1=Label(cars,text="Selling A Car",font=("times new roman", 25),width=80,bg='lightseagreen').place(x=0,y=0)
            # label6
            label6 = Label(cars, text="Sell A Car", font=("bold", 13), width=16, fg="black", bg="indianred")
            label6.place(x=20, y=82)



            def open():
                Carss.get()
#___________________| Toyota Corolla Altis |___________________
                if Carss.get() == "Toyota Corrolla Altis":
                    print("Toyota Corrolla Altis")
                    CA_details = {
                        "Model": ["Corrolla Altis"],
                        "Year": [2020],
                        "Condition": ["New"],
                        "Fuel": ["Petrol"],
                        "KMs Driven": ["25,000 Km"],
                        "Registered in": ["Islamabad"],
                        "Price": [3485000]

                    }
                    print(CA_details)
                    # Creating Excel File All Data will be save in Excel sheet
                    df = pd.DataFrame(CA_details, columns=['Model', 'Year', 'Condition', 'Fuel', 'KMs Driven', 'Registered in',"Price"])

                    df.to_excel(r'C:\Users\Hashmat Ali\PycharmProjects\pythonProject23\Corrolla_Altis.xlsx', index=False,header=True)
                    #frame creating
                    frame1 = Frame(cars, bg='tomato').place(x=750, y=50, width=380, height=250)
                    # toyota = ImageTk.PhotoImage(file="C:/images/Corrola_Altis1.jpg")
                    # toyota1 = Label(frame1, image=toyota).place(x=750,y=50)
                    #data print on screen
                    details = "Details"
                    Label(cars,text=details,fg="black",font=("times new roman", 25)).place(x=750,y=300)
                    model1 = "Car Model: - " + str(CA_details['Model'])
                    year = "Car Year: - " + str(CA_details["Year"])
                    condition = "Car Condition: - " + str(CA_details["Condition"])
                    fuel = "Car Fuel: - " + str(CA_details["Fuel"])
                    kms_driven = "KMS Driven: - " + str(CA_details["KMs Driven"])
                    register = "Car Registration: - " + str(CA_details["Registered in"])
                    price = "RS: "+str(CA_details["Price"])
                    rupees = "Car Price"
                    description = "Description"
                    des = "Isld Reg Smart Card Book Sratchless Car Low Millege Family Use Car Full\n Mainatied Smooth Drive Orignal Keys Manaul Owner Books Avalible Only\n Serious Buyers Contact"
                    Label(cars, text=model1, width=25, bg="white").place(x=750, y=350)
                    Label(cars, text=year, width=20, bg="white").place(x=930, y=350)
                    Label(cars, text=condition, width=30, bg="white").place(x=1070, y=350)
                    Label(cars, text=fuel, width=22, bg="white").place(x=750, y=400)
                    Label(cars, text=kms_driven, width=22, bg="white").place(x=900, y=400)
                    Label(cars, text=register, width=30, bg="white").place(x=1050, y=400)
                    Label(cars, text=price).place(x=1200, y=250)
                    Label(cars,text=rupees,font=("times new roman", 25)).place(x=1180,y=200)
                    Label(cars,text=description,font=("times new roman", 25)).place(x=750,y=450)
                    Label(cars,text=des,width=70,bg='white').place(x=750,y=500)

                    #function for button
                    def opens():
                        cars.destroy()
                        carss=Tk()
                        carss.geometry("500x400")
                        # function for entry
                        def sub():
                            if name.get() == "" or agr.get() == 'Permoission':
                                messagebox.showerror("Error","Pleas Fill Form")
                            else:
                                print("Customer Name:- ", name.get())
                                print("Customer Permission:- ", agr.get())
                                # condition for permission drop down
                                if agr.get() == "Agree":
                                    carss.destroy()
                                    # LAst window here showing image
                                    img = Tk()
                                    img.geometry("500x600")
                                    img.title("Toyota Corolla")
                                    ################## HEADING ###################
                                    heading = Label(img, text="Toyota", fg='red', font=("times new roman", 28))
                                    heading.place(x=120, y=10)
                                    heading = Label(img, text="Corolla", fg='gray', font=("times new roman", 35))
                                    heading.place(x=240, y=5)
                                    toyota = ImageTk.PhotoImage(file="C:/images/Corrola_Altis1.jpg")
                                    toyota1 = Label(img, image=toyota).place(x=0, y=100)
                                    name1 = "Congratulations " + name.get() + "\n Keep Enjoying with Your Toyota Cor0lla Altis"
                                    Label(img, text=name1, font=("times new roman", 10)).place(x=120, y=520)
                                    #function for call again
                                    def op():
                                        img.destroy()
                                        comeback2()
                                    Button(img,text="More",width=20,bd=5,bg="gray",command=op).place(x=180,y=560)

                                    img.mainloop()
                                else:
                                    e = messagebox.askquestion("Question", "Do you want to take\n choose else Car")
                                    if e == "yes":
                                        carss.destroy()
                                        comeback2()
                                    else:
                                        messagebox.showinfo("Info", "Good Bye!")
                                        carss.destroy()




                        ################## HEADING ###################
                        heading = Label(carss,text="Toyota",  fg='red',font=("times new roman", 28))
                        heading.place(x=120, y=10)
                        heading = Label(carss,text="Corolla", fg='gray',font=("times new roman",35))
                        heading.place(x=240, y=5)
                        #entry and
                        name = StringVar()
                        carsss = StringVar()
                        Label(carss,text="Select").place(x=180,y=120)
                        Label(carss,text="Name").place(x=180,y=80)
                        Name = Entry(carss,textvariable=name, width="20").place(x=240, y=80)
                        #Drop down
                        list1 = ['Agree', 'Disagree']
                        agr = StringVar()
                        droplist = OptionMenu(carss, agr, *list1)
                        droplist.config(width=1, fg="Black", cursor="hand2")
                        agr.set('Permoission')
                        droplist.place(x=240, y=120, width=150)
                        # Button
                        Button(carss,text="Submit",command=sub,font=("times new roman", 10),bd=5).place(x=240,y=180)
                        carss.mainloop()

                    #Creating button for buy a car
                    Button(cars,text="Buy A Car",font=("times new roman", 10),bg="black",fg="red",width=20,bd=10,command=opens).place(x=750,y=600)
#___________________| Toyota Corolla XLI |______________________
                elif Carss.get() == "Toyota Corrolla XLI":
                    print("Toyota Corrolla XLI")
                    CXLI_details = {
                        "Model": ["Corrolla XLI"],
                        "Year": [2012],
                        "Condition": ["Used"],
                        "Fuel": ["Petrol"],
                        "KMs Driven": ["10,000 Km"],
                        "Registered in": ["Rawalpindi"],
                        "Price": ["1,600,000"],

                    }
                    print(CXLI_details)
                    # Creating Excel File All Data will be save in Excel sheet
                    df = pd.DataFrame(CXLI_details,columns=['Model', 'Year', 'Condition', 'Fuel', 'KMs Driven', 'Registered in',"Price"])

                    df.to_excel(r'C:\Users\Hashmat Ali\PycharmProjects\pythonProject23\Corrolla_XLI.xlsx',index=False, header=True)
                    # frame creating
                    frame1 = Frame(cars, bg='tomato').place(x=750, y=50, width=380, height=250)
                    # data print on screen
                    details = "Details"
                    Label(cars, text=details, fg="black", font=("times new roman", 25)).place(x=750, y=300)
                    model1 = "Car Model: - " + str(CXLI_details['Model'])
                    year = "Car Year: - " + str(CXLI_details["Year"])
                    condition = "Car Condition: - " + str(CXLI_details["Condition"])
                    fuel = "Car Fuel: - " + str(CXLI_details["Fuel"])
                    kms_driven = "KMS Driven: - " + str(CXLI_details["KMs Driven"])
                    register = "Car Registration: - " + str(CXLI_details["Registered in"])
                    price = "RS: " + str(CXLI_details["Price"])
                    rupees = "Car Price"
                    description = "Description"
                    des = "1.Toyota corolla 2012.\n2.Outer showered.\n3.Inner genuine."
                    Label(cars, text=model1,width=25,bg="white").place(x=750, y=350)
                    Label(cars, text=year,width=20,bg="white").place(x=930, y=350)
                    Label(cars, text=condition,width=30,bg="white").place(x=1070, y=350)
                    Label(cars, text=fuel,width=22,bg="white").place(x=750, y=400)
                    Label(cars, text=kms_driven,width=22,bg="white").place(x=900, y=400)
                    Label(cars, text=register,width=30,bg="white").place(x=1050, y=400)
                    Label(cars, text=price).place(x=1200, y=250)
                    Label(cars, text=rupees, font=("times new roman", 25)).place(x=1180, y=200)
                    Label(cars, text=description, font=("times new roman", 25)).place(x=750, y=450)
                    Label(cars, text=des,width=70,bg='white').place(x=750, y=500)

                    # function for button
                    def opens():
                        cars.destroy()
                        carss = Tk()
                        carss.geometry("500x400")

                        # function for entry
                        def sub():
                            if name.get() == "" or agr.get() == 'Permoission':
                                messagebox.showerror("Error", "Pleas Fill Form")
                            else:
                                print("Customer Name:- ", name.get())
                                print("Customer Permission:- ", agr.get())
                                # condition for permission drop down
                                if agr.get() == "Agree":
                                    carss.destroy()
                                    # LAst window here showing image
                                    img = Tk()
                                    img.geometry("500x600")
                                    img.title("Toyota Corolla")
                                    ################## HEADING ###################
                                    heading = Label(img, text="Toyota", fg='red', font=("times new roman", 28))
                                    heading.place(x=120, y=10)
                                    heading = Label(img, text="Corolla", fg='gray', font=("times new roman", 35))
                                    heading.place(x=240, y=5)
                                    toyota = ImageTk.PhotoImage(file="C:/images/XLI.jpg")
                                    toyota1 = Label(img, image=toyota).place(x=0, y=100)
                                    name1 = "Congratulations " + name.get() + "\n Keep Enjoying with Your Toyota Corlla XLI"
                                    Label(img, text=name1, font=("times new roman", 10)).place(x=120, y=520)
                                    def op():
                                        img.destroy()
                                        comeback2()
                                    Button(img,text="More",width=20,bd=5,bg="gray",command=op).place(x=180,y=560)

                                    img.mainloop()
                                else:
                                    e = messagebox.askquestion("Question", "Do you want to take\n choose else Car")
                                    if e == "yes":
                                        carss.destroy()
                                        comeback2()
                                    else:
                                        messagebox.showinfo("Info", "Good Bye!")
                                        carss.destroy()

                        ################## HEADING ###################
                        heading = Label(carss, text="Toyota", fg='red', font=("times new roman", 28))
                        heading.place(x=120, y=10)
                        heading = Label(carss, text="Corolla", fg='gray', font=("times new roman", 35))
                        heading.place(x=240, y=5)
                        # entry and
                        name = StringVar()
                        carsss = StringVar()
                        Label(carss, text="Select").place(x=180, y=120)
                        Label(carss, text="Name").place(x=180, y=80)
                        Name = Entry(carss, textvariable=name, width="20").place(x=240, y=80)
                        # Drop down
                        list1 = ['Agree', 'Disagree']
                        agr = StringVar()
                        droplist = OptionMenu(carss, agr, *list1)
                        droplist.config(width=1, fg="Black", cursor="hand2")
                        agr.set('Permoission')
                        droplist.place(x=240, y=120, width=150)
                        # Button
                        Button(carss, text="Submit", command=sub, font=("times new roman", 10), bd=5).place(x=240,
                                                                                                            y=180)
                        carss.mainloop()

                    # Creating button for buy a car
                    Button(cars, text="Buy A Car", font=("times new roman", 10), bg="black", fg="red", width=20, bd=10,
                           command=opens).place(x=750, y=600)

#_____________________| Toyota Fortuner |__________________
                elif Carss.get() == "Toyota Fortuner":
                    print("Toyota Fortuner")
                    TF_details = {
                        "Model": ["Fortuner"],
                        "Year": [2018],
                        "Condition": ["New"],
                        "Fuel": ["Diesel"],
                        "KMs Driven": ["14,000 Km"],
                        "Registered in": ["Lahore"],
                        "Price": ["9,700,000"],

                    }
                    print(TF_details)
                    # Creating Excel File All Data will be save in Excel sheet
                    df = pd.DataFrame(TF_details,columns=['Model', 'Year', 'Condition', 'Fuel', 'KMs Driven', 'Registered in',"Price"])

                    df.to_excel(r'C:\Users\Hashmat Ali\PycharmProjects\pythonProject23\Toyota_Fortuner.xlsx',index=False, header=True)

                    frame1 = Frame(cars, bg='tomato').place(x=750, y=50, width=380, height=250)
                    # data print on screen
                    details = "Details"
                    Label(cars, text=details, fg="black", font=("times new roman", 25)).place(x=750, y=300)
                    model1 = "Car Model: - " + str(TF_details['Model'])
                    year = "Car Year: - " + str(TF_details["Year"])
                    condition = "Car Condition: - " + str(TF_details["Condition"])
                    fuel = "Car Fuel: - " + str(TF_details["Fuel"])
                    kms_driven = "KMS Driven: - " + str(TF_details["KMs Driven"])
                    register = "Car Registration: - " + str(TF_details["Registered in"])
                    price = "RS: " + str(TF_details["Price"])
                    rupees = "Car Price"
                    description = "Description"
                    des = "Toyota Fortuner sigma 2.8 Diesel.\nBumper to Bumet Total Geniune.\nJust driven in 14000 km.Look like new car"
                    Label(cars, text=model1, width=25, bg="white").place(x=750, y=350)
                    Label(cars, text=year, width=20, bg="white").place(x=930, y=350)
                    Label(cars, text=condition, width=30, bg="white").place(x=1070, y=350)
                    Label(cars, text=fuel, width=22, bg="white").place(x=750, y=400)
                    Label(cars, text=kms_driven, width=22, bg="white").place(x=900, y=400)
                    Label(cars, text=register, width=30, bg="white").place(x=1050, y=400)
                    Label(cars, text=price).place(x=1200, y=250)
                    Label(cars, text=rupees, font=("times new roman", 25)).place(x=1180, y=200)
                    Label(cars, text=description, font=("times new roman", 25)).place(x=750, y=450)
                    Label(cars, text=des,width=70,bg='white').place(x=750, y=500)

                    # function for button
                    def opens():
                        cars.destroy()
                        carss = Tk()
                        carss.geometry("500x400")

                        # function for entry
                        def sub():
                            if name.get() == "" or agr.get() == 'Permoission':
                                messagebox.showerror("Error", "Pleas Fill Form")
                            else:
                                print("Customer Name:- ", name.get())
                                print("Customer Permission:- ", agr.get())
                                # condition for permission drop down
                                if agr.get() == "Agree":
                                    carss.destroy()
                                    # LAst window here showing image
                                    img = Tk()
                                    img.geometry("500x600")
                                    img.title("Toyota Corolla")
                                    ################## HEADING ###################
                                    heading = Label(img, text="Toyota", fg='red', font=("times new roman", 28))
                                    heading.place(x=120, y=10)
                                    heading = Label(img, text="Corolla", fg='gray', font=("times new roman", 35))
                                    heading.place(x=240, y=5)
#______________________________| Image TF |____________________________
                                    toyota = ImageTk.PhotoImage(file="C:/images/TF.jpg")
                                    toyota1 = Label(img, image=toyota).place(x=0, y=100)
                                    name1 = "Congratulations " + name.get() + "\n Keep Enjoying with Your Toyota Fortuner"
                                    Label(img, text=name1, font=("times new roman", 10)).place(x=120, y=520)
                                    def op():
                                        img.destroy()
                                        comeback2()
                                    Button(img,text="More",width=20,bd=5,bg="gray",command=op).place(x=180,y=560)
                                    img.mainloop()
                                else:
                                    e = messagebox.askquestion("Question", "Do you want to take\n choose else Car")
                                    if e == "yes":
                                        carss.destroy()
                                        comeback2()
                                    else:
                                        messagebox.showinfo("Info", "Good Bye!")
                                        carss.destroy()

                        ################## HEADING ###################
                        heading = Label(carss, text="Toyota", fg='red', font=("times new roman", 28))
                        heading.place(x=120, y=10)
                        heading = Label(carss, text="Corolla", fg='gray', font=("times new roman", 35))
                        heading.place(x=240, y=5)
                        # entry and
                        name = StringVar()
                        carsss = StringVar()
                        Label(carss, text="Select").place(x=180, y=120)
                        Label(carss, text="Name").place(x=180, y=80)
                        Name = Entry(carss, textvariable=name, width="20").place(x=240, y=80)
                        # Drop down
                        list1 = ['Agree', 'Disagree']
                        agr = StringVar()
                        droplist = OptionMenu(carss, agr, *list1)
                        droplist.config(width=1, fg="Black", cursor="hand2")
                        agr.set('Permoission')
                        droplist.place(x=240, y=120, width=150)
                        # Button
                        Button(carss, text="Submit", command=sub, font=("times new roman", 10), bd=5).place(x=240,
                                                                                                            y=180)
                        carss.mainloop()

                    # Creating button for buy a car
                    Button(cars, text="Buy A Car", font=("times new roman", 10), bg="black", fg="red", width=20, bd=10,
                           command=opens).place(x=750, y=600)


#_____________________| Toyota Aqua |_________________________
                elif Carss.get() == "Toyota Aqua":
                    print("Toyota Aqua")
                    TAQUA_details = {
                        "Model": ["Aqua"],
                        "Year": [2018],
                        "Condition": ["Used"],
                        "Fuel": ["Hybrid"],
                        "KMs Driven": ["33,000 Km"],
                        "Registered in": ["Unregistered"],
                        "Price": ["3,650,000"],
                    }
                    print(TAQUA_details)
                    # Creating Excel File All Data will be save in Excel sheet
                    df = pd.DataFrame(TAQUA_details,columns=['Model', 'Year', 'Condition', 'Fuel', 'KMs Driven', 'Registered in',"Price"])

                    df.to_excel(r'C:\Users\Hashmat Ali\PycharmProjects\pythonProject23\Toyota_Aqua.xlsx',index=False, header=True)

                    # frame creating
                    frame1 = Frame(cars, bg='tomato').place(x=750, y=50, width=380, height=250)
                    # data print on screen
                    details = "Details"
                    Label(cars, text=details, fg="black", font=("times new roman", 25)).place(x=750, y=300)
                    model1 = "Car Model: - " + str(TAQUA_details['Model'])
                    year = "Car Year: - " + str(TAQUA_details["Year"])
                    condition = "Car Condition: - " + str(TAQUA_details["Condition"])
                    fuel = "Car Fuel: - " + str(TAQUA_details["Fuel"])
                    kms_driven = "KMS Driven: - " + str(TAQUA_details["KMs Driven"])
                    register = "Car Registration: - " + str(TAQUA_details["Registered in"])
                    price = "RS: " + str(TAQUA_details["Price"])
                    rupees = "Car Price"
                    description = "Description"
                    des = "• Pearl White Color. • 2020 October Fresh Import. • 2020 Alloy Rims.\n• Push Start. Full Options. • Intelligent Clearance System. • Fuel Avg 31.5 km/l\n• Dash Camera & Back Camera. • Height adjustable Seats. • Traction Control."
                    Label(cars, text=model1, width=25, bg="white").place(x=750, y=350)
                    Label(cars, text=year, width=20, bg="white").place(x=930, y=350)
                    Label(cars, text=condition, width=30, bg="white").place(x=1070, y=350)
                    Label(cars, text=fuel, width=22, bg="white").place(x=750, y=400)
                    Label(cars, text=kms_driven, width=22, bg="white").place(x=900, y=400)
                    Label(cars, text=register, width=30, bg="white").place(x=1050, y=400)
                    Label(cars, text=price).place(x=1200, y=250)
                    Label(cars, text=rupees, font=("times new roman", 25)).place(x=1180, y=200)
                    Label(cars, text=description, font=("times new roman", 25)).place(x=750, y=450)
                    Label(cars, text=des,width=70,bg='white').place(x=750, y=500)

                    # function for button
                    def opens():
                        cars.destroy()
                        carss = Tk()
                        carss.geometry("500x400")

                        # function for entry
                        def sub():
                            if name.get() == "" or agr.get() == 'Permoission':
                                messagebox.showerror("Error", "Pleas Fill Form")
                            else:
                                print("Customer Name:- ", name.get())
                                print("Customer Permission:- ", agr.get())
                                # condition for permission drop down
                                if agr.get() == "Agree":
                                    carss.destroy()
                                    # LAst window here showing image
                                    img = Tk()
                                    img.geometry("500x600")
                                    img.title("Toyota Corolla")
                                    ################## HEADING ###################
                                    heading = Label(img, text="Toyota", fg='red', font=("times new roman", 28))
                                    heading.place(x=120, y=10)
                                    heading = Label(img, text="Corolla", fg='gray', font=("times new roman", 35))
                                    heading.place(x=240, y=5)
#__________________________________| image for TA |____________________________
                                    toyota = ImageTk.PhotoImage(file="C:/images/TA.jpg")
                                    toyota1 = Label(img, image=toyota).place(x=0, y=100)
                                    name1 = "Congratulations " + name.get() + "\n Keep Enjoying with Your Toyota Aqua"
                                    Label(img, text=name1, font=("times new roman", 10)).place(x=120, y=520)
                                    def op():
                                        img.destroy()
                                        comeback2()
                                    Button(img,text="More",width=20,bd=5,bg="gray",command=op).place(x=180,y=560)
                                    img.mainloop()
                                else:
                                    e = messagebox.askquestion("Question", "Do you want to take\n choose else Car")
                                    if e == "yes":
                                        carss.destroy()
                                        comeback2()
                                    else:
                                        messagebox.showinfo("Info", "Good Bye!")
                                        carss.destroy()

                        ################## HEADING ###################
                        heading = Label(carss, text="Toyota", fg='red', font=("times new roman", 28))
                        heading.place(x=120, y=10)
                        heading = Label(carss, text="Corolla", fg='gray', font=("times new roman", 35))
                        heading.place(x=240, y=5)
                        # entry and
                        name = StringVar()
                        carsss = StringVar()
                        Label(carss, text="Select").place(x=180, y=120)
                        Label(carss, text="Name").place(x=180, y=80)
                        Name = Entry(carss, textvariable=name, width="20").place(x=240, y=80)
                        # Drop down
                        list1 = ['Agree', 'Disagree']
                        agr = StringVar()
                        droplist = OptionMenu(carss, agr, *list1)
                        droplist.config(width=1, fg="Black", cursor="hand2")
                        agr.set('Permoission')
                        droplist.place(x=240, y=120, width=150)
                        # Button
                        Button(carss, text="Submit", command=sub, font=("times new roman", 10), bd=5).place(x=240,
                                                                                                            y=180)
                        carss.mainloop()

                    # Creating button for buy a car
                    Button(cars, text="Buy A Car", font=("times new roman", 10), bg="black", fg="red", width=20, bd=10,
                           command=opens).place(x=750, y=600)


#_______________________| Toyota Corrlla GLI |______________________
                elif Carss.get() == "Toyota Corolla GLI":
                    # log = ImageTk.PhotoImage(file="C:/images/login3.png")
                    # log = Label(cars, image=log).place(x=152, y=120, width=451, height=450)
                    print("Toyota Corrolla GLI")
                    CGLI_details = {
                        "Model": ["Corrolla GLI"],
                        "Year": [2020],
                        "Condition": ["New"],
                        "Fuel": ["Petrol"],
                        "KMs Driven": ["6,700 km"],
                        "Registered in": ["Karachi"],
                        "Price": ["3,065,000"],

                    }
                    print(CGLI_details)
                    # Creating Excel File All Data will be save in Excel sheet
                    df = pd.DataFrame(CGLI_details,columns=['Model', 'Year', 'Condition', 'Fuel', 'KMs Driven', 'Registered in',"Price"])

                    df.to_excel(r'C:\Users\Hashmat Ali\PycharmProjects\pythonProject23\Corrolla_GLI.xlsx',index=False, header=True)
                    # frame creating
                    frame1 = Frame(cars, bg='tomato').place(x=750, y=50, width=380, height=250)
                    # data print on screen
                    details = "Details"
                    Label(cars, text=details, fg="black", font=("times new roman", 25)).place(x=750, y=300)
                    model1 = "Car Model: - " + str(CGLI_details['Model'])
                    year = "Car Year: - " + str(CGLI_details["Year"])
                    condition = "Car Condition: - " + str(CGLI_details["Condition"])
                    fuel = "Car Fuel: - " + str(CGLI_details["Fuel"])
                    kms_driven = "KMS Driven: - " + str(CGLI_details["KMs Driven"])
                    register = "Car Registration: - " + str(CGLI_details["Registered in"])
                    price = "RS: " + str(CGLI_details["Price"])
                    rupees = "Car Price"
                    description = "Description"
                    des = "Brand new GLi Manufacture 2019  Reg.2020, 100% original scratchless \nfirst owner,plastic on seats, Floor Matting,Sunvoisers,Sparewheel unused,only\n new GLi buyers can contact me."
                    Label(cars, text=model1, width=25, bg="white").place(x=750, y=350)
                    Label(cars, text=year, width=20, bg="white").place(x=930, y=350)
                    Label(cars, text=condition, width=30, bg="white").place(x=1070, y=350)
                    Label(cars, text=fuel, width=22, bg="white").place(x=750, y=400)
                    Label(cars, text=kms_driven, width=22, bg="white").place(x=900, y=400)
                    Label(cars, text=register, width=30, bg="white").place(x=1050, y=400)
                    Label(cars, text=price).place(x=1200, y=250)
                    Label(cars, text=rupees, font=("times new roman", 25)).place(x=1180, y=200)
                    Label(cars, text=description, font=("times new roman", 25)).place(x=750, y=450)
                    Label(cars, text=des,width=70,bg='white').place(x=750, y=500)

                    # function for button
                    def opens():
                        cars.destroy()
                        carss = Tk()
                        carss.geometry("500x400")

                        # function for entry
                        def sub():
                            if name.get() == "" or agr.get() == 'Permoission':
                                messagebox.showerror("Error", "Pleas Fill Form")
                            else:
                                print("Customer Name:- ", name.get())
                                print("Customer Permission:- ", agr.get())
                                # condition for permission drop down
                                if agr.get() == "Agree":
                                    carss.destroy()
                                    # LAst window here showing image
                                    img = Tk()
                                    img.geometry("500x600")
                                    img.title("Toyota Corolla")
                                    ################## HEADING ###################
                                    heading = Label(img, text="Toyota", fg='red', font=("times new roman", 28))
                                    heading.place(x=120, y=10)
                                    heading = Label(img, text="Corolla", fg='gray', font=("times new roman", 35))
                                    heading.place(x=240, y=5)
#_________________________________| GLI Image |_________________________________________
                                    toyota = ImageTk.PhotoImage(file="C:/images/GLI.jpg")
                                    toyota1 = Label(img, image=toyota).place(x=0, y=100)
                                    name1 = "Congratulations " + name.get() + "\n Keep Enjoying with Your Toyota Corolla GLI"
                                    Label(img, text=name1, font=("times new roman", 10)).place(x=120, y=520)
                                    def op():
                                        img.destroy()
                                        comeback2()
                                    Button(img,text="More",width=20,bd=5,bg="gray",command=op).place(x=180,y=560)
                                    img.mainloop()
                                else:
                                    e = messagebox.askquestion("Question", "Do you want to take\n choose else Car")
                                    if e == "yes":
                                        carss.destroy()
                                        comeback2()
                                    else:
                                        messagebox.showinfo("Info", "Good Bye!")
                                        carss.destroy()

                        ################## HEADING ###################
                        heading = Label(carss, text="Toyota", fg='red', font=("times new roman", 28))
                        heading.place(x=120, y=10)
                        heading = Label(carss, text="Corolla", fg='gray', font=("times new roman", 35))
                        heading.place(x=240, y=5)
                        # entry and
                        name = StringVar()
                        carsss = StringVar()
                        Label(carss, text="Select").place(x=180, y=120)
                        Label(carss, text="Name").place(x=180, y=80)
                        Name = Entry(carss, textvariable=name, width="20").place(x=240, y=80)
                        # Drop down
                        list1 = ['Agree', 'Disagree']
                        agr = StringVar()
                        droplist = OptionMenu(carss, agr, *list1)
                        droplist.config(width=1, fg="Black", cursor="hand2")
                        agr.set('Permoission')
                        droplist.place(x=240, y=120, width=150)
                        # Button
                        Button(carss, text="Submit", command=sub, font=("times new roman", 10), bd=5).place(x=240,
                                                                                                            y=180)
                        carss.mainloop()

                    # Creating button for buy a car
                    Button(cars, text="Buy A Car", font=("times new roman", 10), bg="black", fg="red", width=20, bd=10,
                           command=opens).place(x=750, y=600)


                else:
                    messagebox.showerror("Error","Please Select Any Car!")

            # entry6
            list1 = ['Toyota Corrolla Altis', 'Toyota Corrolla XLI', 'Toyota Fortuner', 'Toyota Aqua', 'Toyota Corolla GLI']
            Carss= StringVar()
            droplist = OptionMenu(cars, Carss, *list1)
            droplist.config(width=1, fg="Black", cursor="hand2")
            Carss.set('Select Your Cars')
            droplist.place(x=200, y=80, width=220)

            button= Button(cars,text="Insert", width="20", font=("times new roman", 15),activebackground="red",bg='dimgray',command=open,bd=10).place(x=70, y=150)

            cars.mainloop()
        comeback2()

    button=Button(car, text="Welcome", width="20", font=("times new roman", 15),activebackground="red",bg='royalblue',command=open,pady=1,padx=1,bd=10).place(x=1050, y=620)


    car.mainloop()
comeback1()
