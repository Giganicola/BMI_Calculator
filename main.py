"""
BMI App

Author: Nicola Simioni
Email:  info@nicolasimioni.com
"""

from tkinter import *
import datetime
import webbrowser
from errors_handler import ErrorsHandler
from converter import Converter

# Creating the main window from the Frame class.
class Window(Frame):

    # Initializing class and setting up main variables
    def __init__(self, master=None):

        Frame.__init__(self, master)

        # Create frames
        self.user_name_frame = Frame(bd=1, relief=SUNKEN, background="#CCCCCC")
        self.weight_frame = Frame(bd=1, relief=SUNKEN)
        self.height_frame = Frame(bd=1, relief=SUNKEN)
        self.error_messages_frame = Frame(bd=1, relief=SUNKEN, background="#CCCCCC")
        self.result_frame = Frame(bd=1, relief=SUNKEN, background="#CCCCCC")

        # Pack frames
        self.user_name_frame.pack(expand=1, fill=BOTH)
        self.weight_frame.pack(expand=1, fill=BOTH)
        self.height_frame.pack(expand=1, fill=BOTH)
        self.error_messages_frame.pack(expand=1, fill=BOTH)
        self.result_frame.pack(expand=1, fill=BOTH)

        # Reference to the master tk window
        self.master = master

        # Get the Year
        self.year = datetime.date.today().year

        # Weight variables
        self.w_pounds = 0
        self.w_stones = 0
        self.w_kgs = 0

        # Height variables
        self.h_feet = 0
        self.h_inches = 0
        self.h_cms = 0

        # Initialize the window
        self.init_window()


    # Creation of main window
    def init_window(self):

        # Set up main window settings
        self.master.title("BMI - Nicola Simioni")
        self.master.iconbitmap('icons/bmi.ico')
        self.master.geometry('400x400')

        # Setting up Menu
        self.init_menu()

        # Frame1: Username
        Label(self.user_name_frame, text="Enter Your Name", background="#CCCCCC").pack(pady=5)

        self.user_name = Entry(self.user_name_frame, width=15)
        self.user_name.pack(pady=5)
        self.user_name.focus_set()
        self.user_name.bind("<KeyRelease>", (lambda event: ErrorsHandler.reset_username(self)))

        # Frame2: Weight
        Label(self.weight_frame, text="Enter Your Weight").pack(pady=5)

        Label(self.weight_frame, text="Stones ").pack(padx=10, pady=5, side=LEFT)
        self.w_stones = Entry(self.weight_frame, width=6)
        self.w_stones.insert(0, 0)
        self.w_stones.pack(padx=10, pady=5, side=LEFT)
        self.w_stones.bind("<KeyRelease>", (lambda event: Converter.weight_conversion(self,'stones')))

        Label(self.weight_frame, text="Pounds ").pack(padx=(8, 6), pady=5, side=LEFT)
        self.w_pounds = Entry(self.weight_frame, width=6)
        self.w_pounds.insert(0, 0)
        self.w_pounds.pack(padx=(10, 10), pady=5, side=LEFT)
        self.w_pounds.bind("<KeyRelease>", (lambda event: Converter.weight_conversion(self,'pounds')))

        Label(self.weight_frame, text="or KGs ").pack(padx=(10, 12), pady=5, side=LEFT)
        self.w_kgs = Entry(self.weight_frame, width=6)
        self.w_kgs.insert(0, 0)
        self.w_kgs.pack(padx=10, pady=5, side=LEFT)
        self.w_kgs.bind("<KeyRelease>", (lambda event: Converter.weight_conversion(self,'kgs')))

        # Frame3: Height
        Label(self.height_frame, text="Enter Your Height").pack(pady=5)

        Label(self.height_frame, text="Feet ").pack(padx=10, pady=5, side=LEFT)
        self.h_feet = Entry(self.height_frame, width=6)
        self.h_feet.insert(0, 0)
        self.h_feet.pack(padx=(22, 10), pady=5, side=LEFT)
        self.h_feet.bind("<KeyRelease>", (lambda event: Converter.height_conversion(self,'feet')))

        Label(self.height_frame, text="Inches ").pack(padx=10, pady=5, side=LEFT)
        self.h_inches = Entry(self.height_frame, width=6)
        self.h_inches.insert(0, 0)
        self.h_inches.pack(padx=10, pady=5, side=LEFT)
        self.h_inches.bind("<KeyRelease>", (lambda event: Converter.height_conversion(self,'inches')))

        Label(self.height_frame, text="or CMs ").pack(padx=10, pady=5, side=LEFT)
        self.h_cms = Entry(self.height_frame, width=6)
        self.h_cms.insert(0, 0)
        self.h_cms.pack(padx=10, pady=5, side=LEFT)
        self.h_cms.bind("<KeyRelease>", (lambda event: Converter.height_conversion(self,'cms')))

        # Frame4: Error messages
        self.errors = Label(self.error_messages_frame, text="", background="#CCCCCC")
        self.errors.pack(pady=5)

        # Frame5: Results
        self.calculate_button = Button(self.result_frame, text="Calculate BMI", command=self.calculate_bmi)
        self.calculate_button.pack(pady=10)
        self.bmi_result = Label(self.result_frame, text="", font="bold", background="#CCCCCC")
        self.bmi_result.pack(pady=5)
        self.bmi_message = Label(self.result_frame, text="", background="#CCCCCC")
        self.bmi_message.pack(pady=5)
        self.bmi_kgs = 0
        self.bmi_cms = 0


    # Initialize menu
    def init_menu(self):

        # Creating a menu instance
        menu = Menu(self.master)
        self.master.config(menu=menu)

        # Create the File object
        file = Menu(menu, tearoff=False)

        # Adding command to exit the app to menu option
        file.add_command(label="Exit", command=self.exit_app)

        # Adding "file" item to our menu
        menu.add_cascade(label="File", menu=file)

        # Create the Edit object)
        edit = Menu(menu)

        # added "About" item to the menu
        menu.add_cascade(label="About", command=self.show_about)


    # Calculate BMI
    def calculate_bmi(self):

        # First, check for the username
        username = self.user_name.get()

        if len(username) == 0:
            self.user_name.config(background='#ffb3b3')
            self.errors.config(text='Please insert a valid username')
            self.error_messages_frame.config(background='#ffb3b3')
            self.errors.config(background='#ffb3b3')
        else:
            self.user_name.config(background='#FFFFFF')

            # Check if we have in values for weight
            try:
                weight1 = int(self.w_stones.get())
                weight2 = int(self.w_pounds.get())
                weight3 = int(self.w_kgs.get())

                # Check if we have in values for height
                try:
                    height1 = int(self.h_feet.get())
                    height2 = int(self.h_inches.get())
                    height3 = int(self.h_cms.get())

                    # Values range checks
                    if weight1 >= 0 and weight2 >= 0 and weight3 >= 0:
                        if height1 >= 0 and height2 >= 0 and height3 >= 0:
                            if self.bmi_kgs >= 0 and self.bmi_kgs >= 30 and self.bmi_kgs <= 350:
                                if self.bmi_cms >= 0 and self.bmi_cms >= 50 and self.bmi_cms <= 250:

                                    # Calculate BMI
                                    self.errors.config(text='')
                                    self.error_messages_frame.config(background='#CCCCCC')
                                    self.errors.config(background='#CCCCCC')

                                    meters = float(self.bmi_cms / 100)
                                    bmi = self.bmi_kgs / (meters * meters)
                                    bmi = round(bmi, 1)

                                    # Print result
                                    self.bmi_result.config(text='Your BMI value is: ' + str(bmi))

                                    # Print BMI message
                                    if bmi < 18.5:
                                        self.bmi_message.config(text='You are Underweight (go to eat somehting)')
                                    elif bmi >= 18.5 and bmi <= 24.9:
                                        self.bmi_message.config(text='You are Normal (healthy weight)')
                                    elif bmi >= 25 and bmi < 29.9:
                                        self.bmi_message.config(text='You are Overweight (stop eating!)')
                                    elif bmi >= 30:
                                        self.bmi_message.config(text='You are Obese (time to run my friend)')

                                    # Save data
                                    try:
                                        now = datetime.datetime.now()
                                        date_string = now.strftime("%d-%b-%Y (%H:%M:%S)")
                                        fo = open("bmi_data.csv", "a")
                                        fo.write("%s, %s, %s, %s, %s, %s, %s, %s\n" % (
                                                'User name: '+username,
                                                'Stones: '+str(weight1),
                                                'Pounds: '+str(weight2),
                                                'Kgs: '+str(weight3),
                                                'Feet:'+ str(height1),
                                                'Inches: '+str(height2),
                                                'Cms: '+str(height3),
                                                date_string))
                                        fo.close()

                                        self.errors.config(text='Data has been saved in bmi_data.csv. Try again with '
                                                                'different values!')
                                        self.error_messages_frame.config(background='#84fa84')
                                        self.errors.config(background='#84fa84')

                                    except PermissionError:
                                        self.errors.config(text='Data cannot be saved. Close bmi_data.csv first and '
                                                                'then try again')
                                        self.error_messages_frame.config(background='#ffb3b3')
                                        self.errors.config(background='#ffb3b3')

                                    except ValueError:
                                        self.errors.config(text='Data has not been saved, please retry')
                                        self.error_messages_frame.config(background='#ffb3b3')
                                        self.errors.config(background='#ffb3b3')
                                else:
                                    self.h_cms.config(background='#ffb3b3')
                                    self.errors.config(text='Please insert a valid height between 50 and 250 cms')
                                    self.error_messages_frame.config(background='#ffb3b3')
                                    self.errors.config(background='#ffb3b3')
                            else:
                                self.w_kgs.config(background='#ffb3b3')
                                self.errors.config(text='Please insert a valid weight between 30 and 350 kgs')
                                self.error_messages_frame.config(background='#ffb3b3')
                                self.errors.config(background='#ffb3b3')
                        else:
                            ErrorsHandler.highlight_height_errors(self)
                    else:
                        ErrorsHandler.highlight_weight_errors(self)

                except ValueError:
                    self.h_feet.config(background='#ffb3b3')
                    self.h_inches.config(background='#ffb3b3')
                    self.h_cms.config(background='#ffb3b3')
                    ErrorsHandler.invalid_input(self)

            except ValueError:
                self.w_stones.config(background='#ffb3b3')
                self.w_pounds.config(background='#ffb3b3')
                self.w_kgs.config(background='#ffb3b3')
                ErrorsHandler.invalid_input(self)


    # Save data
    def save_data(self):
        print("yeee")


    # Closing app
    def exit_app(self):
        exit()


    # Show About Popup
    def show_about(self):

        # Create new window
        about = Toplevel(self.master)
        about.title('About')
        about.iconbitmap('icons/bmi.ico')
        about.geometry('300x200')
        about.focus_set()

        # Show about info
        Label(about, text="BMI App").pack(side="top", pady=40)
        Label(about, text="Nicola Simioni - " + str(self.year)).pack(side="top")

        # Show website link
        link = Label(about, text="http://nicolasimioni.com", fg="blue", cursor="hand2")
        link.pack()
        link.bind("<Button-1>", lambda event: webbrowser.open(link.cget("text")))


# Start
root = Tk()

# Creation main window
app = Window(root)

# Mainloop
root.mainloop()
