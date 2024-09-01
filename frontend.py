# Theatre Ticket Booking System 

# Importing necessary module(s)
from tkinter import *
from PIL import ImageTk, Image
import backend


# Defining the Frontend of the Customer
def frontend():


    def user_input():
        # Defining an instance of a GUI window using TKinter
        child1 = Tk()
        child1.title("CreateAcct")
        child1.geometry('400x200')

        # Labels are the text that appears on the GUI window
        # Entries are the places where we input the data
        """ .place() is a method associated with TKinter to display the object (here: Label, Entry or Radiobutton) 
            on the GUI using coordinates"""

        head_label = Label(child1, text = "Login or Register", font = ("Times New Roman", 20)).place(x=100, y=10)

        gmail_label = Label(child1, text = "Enter Gmail: ", font = ("Calibri", 15)).place(x = 20, y = 50)
        gmail_entry = Entry(child1, width = 40)
        gmail_entry.place(x = 140, y = 55)

        pass_label = Label(child1, text="Enter Password: ", font=("Calibri", 15)).place(x = 20, y = 90)
        pass_entry = Entry(child1, show="*", width=30)
        pass_entry.place(x=185, y=97)

        """This function will be called only when the button "create_button" 
        (defined below) is clicked on, or when the function is called"""


        def create():
            # .get() method is associated with TKinter to get the value from the entry field
            gmail = gmail_entry.get()       
            password = pass_entry.get()

            backend.input_userData(gmail, password)
            if gmail == "":

                child1_1 = Tk()
                child1_1.title("GmailEmptyException")
                child1_1.geometry("300x100")

                gmail_er = Label(child1_1, text="Please Check if Entered Gmail").place(x=50, y=30)
                ok_button = Button(child1_1, text="OK", command=child1_1.destroy).place(x=135, y=50)

            elif password == "" or len(password) < 6:

                child1_2 = Tk()
                child1_2.title("PasswordInvalidException")
                child1_2.geometry("300x100")

                gmail_er = Label(child1_2, text="Please Enter Valid Password").place(x=50, y=30)
                ok_button = Button(child1_2, text="OK", command=child1_2.destroy).place(x=135, y=50)

                child1_2.mainloop()

            else:

                child1.destroy()


        create_button = Button(child1, text="Create Account", command=create)
        create_button.place(x=150, y=140)

        child1.mainloop()

    user_input()


    def book_ticket():

        parent1  = Tk()
        parent1.title("MyTheatreApp")
        parent1.geometry('1920x1080')
        parent1.iconbitmap(r'icon/minecraft-icon-24.ico')

        bg = ImageTk.PhotoImage(Image.open(r".\theatre\movie-theater.png"))
        bg_label = Label(image=bg).pack()

        """Radiobuttons are where we select and highlight the predefined choices available for the user.
        It is just the same "circle" buttons in a Google Form"""

        head_label = Label(parent1, text ="Book Your Show", font = ("ROG Fonts", 40),bg="#FFFFFF").place(relx=0.5,y=50,anchor=CENTER)

        name_label = Label(parent1, text="Enter Name: ", font = ("Tenorite", 15)).place(x=725, y=150)
        name_entry = Entry(parent1, width=40)
        name_entry.place(x=960, y=150)

        age_label = Label(parent1, text ="Enter Age: ", font = ("Tenorite", 15)).place(x = 725, y = 250)
        age_entry = Entry(parent1, width = 10)
        age_entry.place(x = 960, y = 250 )

        seat_nos_label = Label(parent1, text ="Enter Number of Seats: ", font = ("Tenorite", 15)).place(x = 725, y = 350)
        seat_nos_entry = Entry(parent1, width = 10)
        seat_nos_entry.place(x = 960, y = 350)

        #Assigning a Boolean Variable to "prem" to store a true or false value
        prem = BooleanVar()

        prem_label = Label(parent1, text ="Select Premium: ", font = ("Tenorite", 15)).place(x = 725, y = 450)
        prem_radbtn_true = Radiobutton(parent1, text ="YES", variable = prem, value = True, font = ("Tenorite", 15)).place(x = 960, y = 450)
        prem_radbtn_false = Radiobutton(parent1, text ="NO", variable = prem, value = False, font = ("Tenorite", 15)).place(x = 1110, y = 450)


        def submit():
            name = name_entry.get()
            age = age_entry.get()
            seat_nos = seat_nos_entry.get()
            premium = prem.get()

            """ Some conditions to check whether an entry field is empty and open a new child instance 
            of a GUI window to show error messages"""

            if name == "":
                tk1 = Tk()
                tk1.title("NameEmptyException")
                tk1.geometry("300x100")

                name_er = Label(tk1, text = "Please Check if Entered Name").place(relx=0.5 , y = 30,anchor=CENTER)
                ok_button = Button(tk1, text = "OK", command = tk1.destroy).place(x = 135, y = 50)

                tk1.mainloop()

            elif age == "":
                tk2 = Tk()
                tk2.title("AgeEmptyException")
                tk2.geometry("300x100")

                age_er = Label(tk2, text = "Please Check if Entered Valid Age").place(relx = 0.5, y = 30,anchor=CENTER)
                ok_button = Button(tk2, text = "OK", command = tk2.destroy).place(x = 135, y = 50)

                tk2.mainloop()

            elif seat_nos == "":
                tk3 = Tk()
                tk3.title("SeatsEmptyException")
                tk3.geometry("300x100")

                seat_nos_er = Label(tk3, text = "Please Check if Entered Valid Number Of Seats").place(relx = 0.5, y = 30, anchor=CENTER)
                ok_button = Button(tk3, text = "OK", command = tk3.destroy).place(x = 135, y = 50)

                tk3.mainloop()

            else:
                ''' "backend" is another python file which we have imported earlier which is in 
                the same directory as this program. Here ".input_data" is a method associated with "backend" but it is a 
                function in that file. To summarise, we are just calling a function which is in another python file'''

                backend.input_data(name, age, seat_nos, premium)
                parent1.destroy()
                select_movie()
                

        submit_button = Button(parent1, text ="Submit", command = submit, font = ("Tenorite", 15))
        submit_button.place(x = 855, y = 600)

        quit_button = Button(parent1, text ="Quit", command = parent1.destroy, font = ("Tenorite", 15))
        quit_button.place(x = 1005, y = 600)


        def select_movie():

            parent2  = Tk()
            parent2.title("MyTheatreApp")
            parent2.geometry("1920x1080")
            parent2.iconbitmap(r".\icon\minecraft-icon-24.ico")

            movie_theater = ImageTk.PhotoImage(Image.open(r".\theatre\movie-theater.png"))

            my_canvas = Canvas(parent2, width=1920, height=1080)
            my_canvas.pack(fill="both", expand=True)
            my_canvas.create_image(0, 0, image=movie_theater, anchor="nw")
            my_canvas.create_text(750, 100, text="Select Your Movie", font=("Times New Roman", 30), fill="White")


            def movie1():

                parent2.destroy()
                movie = "Avatar: The Way of Water"
                genre = "Fantasy"
                movie_language = "English"
                cast = ("Sam Worthington", "Zoey Saldana")
                select_seating()

                backend.write_newData(movie, genre, movie_language, cast)


            def movie2():

                parent2.destroy()
                movie = "Oppenheimer"
                genre = "Thriller"
                movie_language = "English"
                cast = ("Cillian Murphy","Robert Downey Jr.")
                select_seating()

                backend.write_newData(movie, genre, movie_language, cast)


            def movie3():

                parent2.destroy()
                movie = "Jailer"
                genre = "Action"
                movie_language = "Tamil"
                cast = ("Rajinikanth","Vinayakan")
                select_seating()

                backend.write_newData(movie, genre, movie_language, cast)


            def movie4():

                parent2.destroy()
                movie = "Love Today"
                genre = "Comedy"
                movie_language = "Tamil"
                cast = ("Pradeep Ranganadhan","Nikita")
                select_seating()

                backend.write_newData(movie, genre, movie_language, cast)


            def movie5():

                parent2.destroy()
                movie = "Ponniyin Selvan: Part II"
                genre = "Historical Drama"
                movie_language = "Tamil"
                cast = ("Jayam Ravi","Karthi","Vikram",
                "Aishwarya Rai","Trisha Krishnan")
                select_seating()


                backend.write_newData(movie, genre, movie_language, cast)


            def movie6():

                parent2.destroy()
                movie = "Don"
                genre = "Romance"
                movie_language = "Tamil"
                cast = ("Sivakarthikeyan","Priyanka Mohan")
                select_seating()

                backend.write_newData(movie, genre, movie_language, cast)


            def movie7():

                parent2.destroy()
                movie = "Kaathuvaakula Rendu Kaadhal"
                genre = "Romantic Comedy"
                movie_language = "Tamil"
                cast = ("Vijay Sethupathi","Nayanthara", "Samantha Ruth Prabhu")
                select_seating()

                backend.write_newData(movie, genre, movie_language, cast)


            def movie8():

                parent2.destroy()
                movie = "KGF Chapter:2"
                genre = "Historical Drama"
                movie_language = "Tamil"
                cast = ("Yash", "Srinidhi Shetty")
                select_seating()
                
                backend.write_newData(movie, genre, movie_language, cast)


            def movie9():

                parent2.destroy()
                movie = "Vikram"
                genre = "Action Thriller"
                movie_language = "Tamil"
                cast = ("Kamal Haasan", "Vijay Sethupathi")
                select_seating()

                backend.write_newData(movie, genre, movie_language, cast)


            def movie10():

                parent2.destroy()
                movie = "Leo"
                genre = "Action Thriller"
                movie_language = "Tamil"
                cast = ("Vijay", "Trisha")
                select_seating()

                backend.write_newData(movie, genre, movie_language, cast)


            def movie11():

                parent2.destroy()
                movie = "Kalki 2898 AD"
                genre = "Sci-fi"
                movie_language = "Tamil"
                cast = ("Prabhas","Kamal Haasan","Amitabh Bachchan")
                select_seating()

                backend.write_newData(movie, genre, movie_language, cast)


            def movie12():

                parent2.destroy()
                movie = "Captain Miller"
                genre = "Action"
                movie_language = "Tamil"
                cast = ("Dhanush", "Priyanka Mohan")
                select_seating()

                backend.write_newData(movie, genre, movie_language, cast)


            def movie13():

                parent2.destroy()
                movie = "Master"
                genre = "Mystery"
                movie_language = "Tamil"
                cast = ("Vijay","Vijay Sethupathi")
                select_seating()

                backend.write_newData(movie, genre, movie_language, cast)


            def movie14():
                parent2.destroy()
                movie = "Jai Bhim"
                genre = "Legal Drama"
                movie_language = "Tamil"
                cast = ("Suriya", "Lijmol Jose")
                select_seating()

                backend.write_newData(movie, genre, movie_language, cast)
                

            movie1_poster = ImageTk.PhotoImage(Image.open(r".\movies\avatar_the_way_of_water.png"))
            my_canvas.create_image(100, 150, image=movie1_poster, anchor="nw")
            movie1_button = Button(parent2, text="Avatar: The Way of Water", fg='Blue', command=movie1)
            movie1_buttonWindow = my_canvas.create_window(100, 400, anchor="nw", window=movie1_button)


            movie2_poster = ImageTk.PhotoImage(Image.open(r".\movies\oppenheimer.png"))
            my_canvas.create_image(300, 150, image=movie2_poster, anchor="nw")
            movie2_button = Button(parent2, text="Oppenheimer", fg='Blue', command=movie2)
            movie2_buttonWindow = my_canvas.create_window(300, 400, anchor="nw", window=movie2_button)


            movie3_poster = ImageTk.PhotoImage(Image.open(r".\movies\jailer.png"))
            my_canvas.create_image(500, 150, image=movie3_poster, anchor="nw")
            movie3_button = Button(parent2, text="Jailer", fg='Blue', command=movie3)
            movie3_buttonWindow = my_canvas.create_window(525, 400, anchor="nw", window=movie3_button)


            movie4_poster = ImageTk.PhotoImage(Image.open(r".\movies\love_today.png"))
            my_canvas.create_image(700, 150, image=movie4_poster, anchor="nw")
            movie4_button = Button(parent2, text="Love Today", fg='Blue', command=movie4)
            movie4_buttonWindow = my_canvas.create_window(725, 400, anchor="nw", window=movie4_button)


            movie5_poster = ImageTk.PhotoImage(Image.open(r".\movies\ponniyin_selvan_part2.png"))
            my_canvas.create_image(900, 150, image=movie5_poster, anchor="nw")
            movie5_button = Button(parent2, text="Ponniyin Selvan: Part II", fg='Blue', command=movie5)
            movie5_buttonWindow = my_canvas.create_window(900, 400, anchor="nw", window=movie5_button)


            movie6_poster = ImageTk.PhotoImage(Image.open(r".\movies\don.png"))
            my_canvas.create_image(1100, 150, image=movie6_poster, anchor="nw")
            movie6_button = Button(parent2, text="Don", fg='Blue', command=movie6)
            movie6_buttonWindow = my_canvas.create_window(1100, 400, anchor="nw", window=movie6_button)


            movie7_poster = ImageTk.PhotoImage(Image.open(r".\movies\kaathuvaakula_rendu_kaadhal.png"))
            my_canvas.create_image(1300, 150, image=movie7_poster, anchor="nw")
            movie7_button = Button(parent2, text="Kaathuvaakula Rendu Kaadhal", fg='Blue', command=movie7)
            movie7_buttonWindow = my_canvas.create_window(1300, 400, anchor="nw", window=movie7_button)


            movie8_poster = ImageTk.PhotoImage(Image.open(r".\movies\KGF.png"))
            my_canvas.create_image(100, 475, image=movie8_poster, anchor="nw")
            movie8_button = Button(parent2, text="KGF Chapter:2", fg='Blue', command=movie8)
            movie8_buttonWindow = my_canvas.create_window(100, 725, anchor="nw", window=movie8_button)


            movie9_poster = ImageTk.PhotoImage(Image.open(r".\movies\vikram.png"))
            my_canvas.create_image(300, 475, image=movie9_poster, anchor="nw")
            movie9_button = Button(parent2, text="Vikram", fg='Blue', command=movie9)
            movie9_buttonWindow = my_canvas.create_window(300, 725, anchor="nw", window=movie9_button)


            movie10_poster = ImageTk.PhotoImage(Image.open(r".\movies\leo.png"))
            my_canvas.create_image(500, 475, image=movie10_poster, anchor="nw")
            movie10_button = Button(parent2, text="Leo", fg='Blue', command=movie10)
            movie10_buttonWindow = my_canvas.create_window(500, 725, anchor="nw", window=movie10_button)


            movie11_poster = ImageTk.PhotoImage(Image.open(r".\movies\kalki.png"))
            my_canvas.create_image(700, 475, image=movie11_poster, anchor="nw")
            movie11_button = Button(parent2, text="Kalki 2898 AD", fg='Blue', command=movie11)
            movie11_buttonWindow = my_canvas.create_window(700, 725, anchor="nw", window=movie11_button)


            movie12_poster = ImageTk.PhotoImage(Image.open(r".\movies\annaatthe.png"))
            my_canvas.create_image(900, 475, image=movie12_poster, anchor="nw")
            movie12_button = Button(parent2, text="Captain Miller", fg='Blue', command=movie12)
            movie3_buttonWindow = my_canvas.create_window(900, 725, anchor="nw", window=movie12_button)


            movie13_poster = ImageTk.PhotoImage(Image.open(r".\movies\master.png"))
            my_canvas.create_image(1100, 475, image=movie13_poster, anchor="nw")
            movie13_button = Button(parent2, text="Master", fg='Blue', command=movie13)
            movie13_buttonWindow = my_canvas.create_window(1100, 725, anchor="nw", window=movie13_button)


            movie14_poster = ImageTk.PhotoImage(Image.open(r".\movies\jai_bhim.png"))
            my_canvas.create_image(1300, 475, image=movie14_poster, anchor="nw")
            movie14_button = Button(parent2, text="Jai Bhim", fg='Blue', command=movie14)
            movie14_buttonWindow = my_canvas.create_window(1300, 725, anchor="nw", window=movie14_button)

            parent2.mainloop()


        def select_seating():

            selected_seats = []

            parent3 = Tk()
            parent3.title("MyTheatreApp")
            parent3.geometry("1920x1080")
            parent3.iconbitmap(r".\icon\minecraft-icon-24.ico")

            theater_seats = ImageTk.PhotoImage(Image.open(r".\theatre\theater_seatings.png"))

            my_canvas = Canvas(parent3, width=1920, height=1080)
            my_canvas.pack(fill="both", expand=True)
            my_canvas.create_image(0, 0, image=theater_seats, anchor='nw')
            my_canvas.create_text(750, 100, text="Select Your Seats", font=("Times New Roman", 30))


            def button_clicked(seat):
                selected_seats.append(seat)


            def submit_seats():
                backend.write_seatData(selected_seats)


                def payment():

                    pay = Tk()
                    pay.title("ThankYou")
                    pay.geometry("300x100")
                    pay.iconbitmap(r".\icon\minecraft-icon-24.ico")
                    amt = 250 * len(selected_seats)


                    def ok_command():
                        pay.destroy()
                        thank_you()


                    thankYou_label = Label(pay, text=f"Your Amount is: {amt}").pack()
                    ok_button = Button(pay, text="Proceed to Pay", command=ok_command).pack()

                payment()


                def thank_you():

                    thanks = Tk()
                    thanks.title("ThankYou")
                    thanks.geometry("300x100")
                    thanks.iconbitmap(r".\icon\minecraft-icon-24.ico")


                    def ok_command():

                        thanks.destroy()
                        parent3.destroy()


                    thankYou_label = Label(thanks, text="Your Tickets have been booked Successfully!").pack()
                    reciept_label = Label(thanks, text="Your reciept has been sent to your mail").pack()
                    ok_button = Button(thanks, text="OK", command=ok_command).pack()


            def buttons():

                A1_button = Button(parent3, text="A1", command=lambda: button_clicked("A1"))
                A1_buttonWindow = my_canvas.create_window(190, 675, anchor="nw", window=A1_button)

                A2_button = Button(parent3, text="A2", command=lambda: button_clicked("A2"))
                A2_buttonWindow = my_canvas.create_window(323, 675, anchor="nw", window=A2_button)

                A3_button = Button(parent3, text="A3", command=lambda: button_clicked("A3"))
                A3_buttonWindow = my_canvas.create_window(456, 675, anchor="nw", window=A3_button)

                A4_button = Button(parent3, text="A4", command=lambda: button_clicked("A4"))
                A4_buttonWindow = my_canvas.create_window(589, 675, anchor="nw", window=A4_button)

                A5_button = Button(parent3, text="A5", command=lambda: button_clicked("A5"))
                A5_buttonWindow = my_canvas.create_window(722, 675, anchor="nw", window=A5_button)

                A6_button = Button(parent3, text="A6", command=lambda: button_clicked("A6"))
                A6_buttonWindow = my_canvas.create_window(855, 675, anchor="nw", window=A6_button)

                A7_button = Button(parent3, text="A7", command=lambda: button_clicked("A7"))
                A7_buttonWindow = my_canvas.create_window(988, 675, anchor="nw", window=A7_button)

                A8_button = Button(parent3, text="A8", command=lambda: button_clicked("A8"))
                A8_buttonWindow = my_canvas.create_window(1120, 675, anchor="nw", window=A8_button)

                B1_button = Button(parent3, text="B1", command=lambda: button_clicked("B1"))
                B1_buttonWindow = my_canvas.create_window(190, 564, anchor="nw", window=B1_button)

                B2_button = Button(parent3, text="B2", command=lambda: button_clicked("B2"))
                B2_buttonWindow = my_canvas.create_window(323, 564, anchor="nw", window=B2_button)

                B3_button = Button(parent3, text="B3", command=lambda: button_clicked("B3"))
                B3_buttonWindow = my_canvas.create_window(456, 564, anchor="nw", window=B3_button)

                B4_button = Button(parent3, text="B4", command=lambda: button_clicked("B4"))
                B4_buttonWindow = my_canvas.create_window(589, 564, anchor="nw", window=B4_button)

                B5_button = Button(parent3, text="B5", command=lambda: button_clicked("B5"))
                B5_buttonWindow = my_canvas.create_window(722, 564, anchor="nw", window=B5_button)

                B6_button = Button(parent3, text="B6", command=lambda: button_clicked("B6"))
                B6_buttonWindow = my_canvas.create_window(855, 564, anchor="nw", window=B6_button)

                B7_button = Button(parent3, text="B7", command=lambda: button_clicked("B7"))
                B7_buttonWindow = my_canvas.create_window(988, 564, anchor="nw", window=B7_button)

                B8_button = Button(parent3, text="B8", command=lambda: button_clicked("B8"))
                B8_buttonWindow = my_canvas.create_window(1120, 564, anchor="nw", window=B8_button)

                C1_button = Button(parent3, text="C1", command=lambda: button_clicked("C1"))
                C1_buttonWindow = my_canvas.create_window(190, 451, anchor="nw", window=C1_button)

                C2_button = Button(parent3, text="C2", command=lambda: button_clicked("C2"))
                C2_buttonWindow = my_canvas.create_window(323, 451, anchor="nw", window=C2_button)

                C3_button = Button(parent3, text="C3", command=lambda: button_clicked("C3"))
                C3_buttonWindow = my_canvas.create_window(456, 451, anchor="nw", window=C3_button)

                C4_button = Button(parent3, text="C4", command=lambda: button_clicked("C4"))
                C4_buttonWindow = my_canvas.create_window(589, 451, anchor="nw", window=C4_button)

                C5_button = Button(parent3, text="C5", command=lambda: button_clicked("C5"))
                C5_buttonWindow = my_canvas.create_window(722, 451, anchor="nw", window=C5_button)

                C6_button = Button(parent3, text="C6", command=lambda: button_clicked("C6"))
                C6_buttonWindow = my_canvas.create_window(855, 451, anchor="nw", window=C6_button)

                C7_button = Button(parent3, text="C7", command=lambda: button_clicked("C7"))
                C7_buttonWindow = my_canvas.create_window(988, 451, anchor="nw", window=C7_button)

                C8_button = Button(parent3, text="C8", command=lambda: button_clicked("C8"))
                C8_buttonWindow = my_canvas.create_window(1120, 451, anchor="nw", window=C8_button)

                D1_button = Button(parent3, text="D1", command=lambda: button_clicked("D1"))
                D1_buttonWindow = my_canvas.create_window(190, 338, anchor="nw", window=D1_button)

                D2_button = Button(parent3, text="D2", command=lambda: button_clicked("D2"))
                D2_buttonWindow = my_canvas.create_window(323, 338, anchor="nw", window=D2_button)

                D3_button = Button(parent3, text="D3", command=lambda: button_clicked("D3"))
                D3_buttonWindow = my_canvas.create_window(456, 338, anchor="nw", window=D3_button)

                D4_button = Button(parent3, text="D4", command=lambda: button_clicked("D4"))
                D4_buttonWindow = my_canvas.create_window(589, 338, anchor="nw", window=D4_button)

                D5_button = Button(parent3, text="D5", command=lambda: button_clicked("D5"))
                D5_buttonWindow = my_canvas.create_window(722, 338, anchor="nw", window=D5_button)

                D6_button = Button(parent3, text="D6", command=lambda: button_clicked("D6"))
                D6_buttonWindow = my_canvas.create_window(855, 338, anchor="nw", window=D6_button)

                D7_button = Button(parent3, text="D7", command=lambda: button_clicked("D7"))
                D7_buttonWindow = my_canvas.create_window(988, 338, anchor="nw", window=D7_button)

                D8_button = Button(parent3, text="D8", command=lambda: button_clicked("D8"))
                D8_buttonWindow = my_canvas.create_window(1120, 338, anchor="nw", window=D8_button)

                E1_button = Button(parent3, text="E1", command=lambda: button_clicked("E1"))
                E1_buttonWindow = my_canvas.create_window(190, 225, anchor="nw", window=E1_button)

                E2_button = Button(parent3, text="E2", command=lambda: button_clicked("E2"))
                E2_buttonWindow = my_canvas.create_window(323, 225, anchor="nw", window=E2_button)

                E3_button = Button(parent3, text="E3", command=lambda: button_clicked("E3"))
                E3_buttonWindow = my_canvas.create_window(456, 225, anchor="nw", window=E3_button)

                E4_button = Button(parent3, text="E4", command=lambda: button_clicked("E4"))
                E4_buttonWindow = my_canvas.create_window(589, 225, anchor="nw", window=E4_button)

                E5_button = Button(parent3, text="E5", command=lambda: button_clicked("E5"))
                E5_buttonWindow = my_canvas.create_window(722, 225, anchor="nw", window=E5_button)

                E6_button = Button(parent3, text="E6", command=lambda: button_clicked("E6"))
                E6_buttonWindow = my_canvas.create_window(855, 225, anchor="nw", window=E6_button)

                E7_button = Button(parent3, text="E7", command=lambda: button_clicked("E7"))
                E7_buttonWindow = my_canvas.create_window(988, 225, anchor="nw", window=E7_button)

                E8_button = Button(parent3, text="E8", command=lambda: button_clicked("E8"))
                E8_buttonWindow = my_canvas.create_window(1120, 225, anchor="nw", window=E8_button)

                submit_button = Button(parent3, text="Submit", command=submit_seats)
                submit_buttonWindow = my_canvas.create_window(655, 725, anchor="nw", window=submit_button)

            buttons()


            parent3.mainloop()

        parent1.mainloop()
    
    book_ticket()
    
frontend()


