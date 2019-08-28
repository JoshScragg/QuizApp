from tkinter import *
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk
from utils import *
import json



class LogginWindow():
    def __init__(self):
        self.root = Tk()
        self.root.geometry("350x500")
        self.root.configure(bg="#1A1A1D")
        self.root.resizable(False, False)

        self.logo_img = Image.open("logo.png")
        self.logo_img = self.logo_img.resize((150, 150))
        self.logo_img = ImageTk.PhotoImage(self.logo_img)
        self.logo_img_label = Label(self.root, image = self.logo_img, bg="#1A1A1D")
        self.logo_img_label.place(x=104, y=30)

        self.username_entry = Entry(self.root, bg="#1A1A1D", width=150, highlightbackground="#C3073F", highlightthickness=2, 
                                    highlightcolor="#C3073F", insertbackground="white", fg= "white", font=("Corbel Light", 18, "normal"))
        self.username_entry.pack(fill="x", padx="80", pady=(220, 0))

        self.password_entry = Entry(self.root, bg="#1A1A1D", width=150, highlightbackground="#C3073F", highlightthickness=2, 
                                    highlightcolor="#C3073F", insertbackground="white", fg= "white", font=("Corbel Light", 18, "normal"))
        self.password_entry.pack(fill="x", padx="80", pady="25")

        self.login_button = Button(self.root, text="Login", width=15, height=2, bd=0, bg="#C3073F",
                                activebackground = "#FFF", activeforeground="#C3073F", command=self.loggedin)
        self.login_button.place(x=120, y=350)


    def render(self):
        self.root.mainloop()


    def loggedin(self):
        json_object = Json("JSON\\Users.json")
        users_json = json_object.read_json()
        login_fail = False
        for users in users_json['users']:
            if users['username'] == self.username_entry.get() and users['password'] == self.password_entry.get():
                self.root.destroy()
                setup_app = MainApplication()
                setup_quiz = Quizzes()
                setup_app.setup_objects()
                setup_app.render()
                return
            else:
                login_fail = True
        if login_fail == True:
            messagebox.showerror("Error", "Incorrect Username/Password")

class MainApplication():
    def __init__(self):
        self.root = Tk() 
        self.root.geometry("1000x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#1A1A1D")
        
        self.logo_img = Image.open("logo.png")
        self.logo_img = self.logo_img.resize((70, 70))
        self.logo_img = ImageTk.PhotoImage(self.logo_img)
        self.logo_img_label = Label(self.root, image = self.logo_img, bg="#1A1A1D")
        self.logo_img_label.grid(sticky="nw", column=0, row=1)

        self.home_button = Button(self.root, text="Home", width=12, height=3, bd=0, bg="#C3073F",
                                activebackground = "#FFF", activeforeground="#C3073F")
        self.home_button.grid(column= 1, row=1, padx=(15,0), pady=15)
        self.profile_button = Button(self.root, text="Profile", width=12, height=3, bd=0, bg="#C3073F",
                                activebackground = "#FFF", activeforeground="#C3073F", command=self.renderProfiles)
        self.profile_button.grid(column= 2, row=1, padx=15, pady=15)
        self.categories_button = Button(self.root, text="categories", width=12, height=3, bd=0, bg="#C3073F",
                                activebackground = "#FFF", activeforeground="#C3073F", command=self.rendercategories)
        self.categories_button.grid(column=3, row=1, padx=0, pady=15)


    def setup_objects(self):
        json_object = Json("JSON\\Quizzes.json")
        quiz_json = json_object.read_json()

        count = 1
        y_value = 100
        object_list = []

        for quizzes in quiz_json['quiz']:
            quiz_title = quizzes["Title"]
            quiz_category = quizzes["category"]
            image_location = quizzes["image_location"]
            description = quizzes["description"]
            questions = quizzes["questions"]
            quiz_name = "quiz{}".format(count)
            quiz_name = Quizzes(quiz_title, quiz_category, image_location, description, questions)
            object_list.append(quiz_name)
            y_value = self.render_quizzes(quiz_name, y_value)

    def render_quizzes(self, quiz_object, y_value):
        quiz_title = quiz_object.quiz_title
        quiz_image = quiz_object.image_location
        quiz_description = quiz_object.description
        quiz_question_list = quiz_object.questions

        self.quiz = Frame(self.root, bg="#1A1A1D", width=950, height=100, highlightbackground="#C3073F", highlightthickness=2)
        self.quiz.place(x=25, y=y_value)

        self.quiz_image = Image.open(quiz_image)
        self.quiz_image = self.quiz_image.resize((80,80))
        self.quiz_image = ImageTk.PhotoImage(self.quiz_image)
        self.quiz_image_label = Label(self.quiz, image = self.quiz_image)
        self.quiz_image_label.place(x=7, y=5)

        self.devider = Frame(self.quiz, bg="#4E4E50", width=2, height=85)
        self.devider.place(x=100, y=5)
        
        self.quiz_title = Label(self.quiz, text=quiz_title, font=("Arial", 18), bg="#1A1A1D", fg="white")
        self.quiz_title.place(x=105, y=3)

        self.quiz_description = Label(self.quiz, text=quiz_description, font=("Arial", 11), bg="#1A1A1D", fg="white")
        self.quiz_description.place(x=105, y=35)

        self.quiz_button = Button(self.quiz, text="Play Quiz", width=11, height=5, bd=0, bg="#C3073F",
                                activebackground = "#FFF", activeforeground="#C3073F", command=self.renderQuizWindow)
        self.quiz_button.place(x=854, y=7)
        y_value += 115
        return y_value

    def render(self):
        self.root.mainloop()

    def rendercategories(self):
        self.root.destroy()
        setup_categories = CategorysWindow()
        setup_categories.render()

    def renderProfiles(self):
        setup_profiles = ProfileWindow()

    def renderQuizWindow(self):
        self.root.destroy()
        setup_quiz = QuizWindow()
        setup_quiz.render()

class QuizWindow():
    def __init__(self):
        self.root = Tk() 
        self.root.geometry("1000x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#1A1A1D")

        self.logo_img = Image.open("logo.png")
        self.logo_img = self.logo_img.resize((70, 70))
        self.logo_img = ImageTk.PhotoImage(self.logo_img)
        self.logo_img_label = Label(self.root, image = self.logo_img, bg="#1A1A1D")
        self.logo_img_label.grid(sticky="nw", column=0, row=1)

        self.home_button = Button(self.root, text="Home", width=12, height=3, bd=0, bg="#C3073F",
                                activebackground = "#FFF", activeforeground="#C3073F")
        self.home_button.grid(column= 1, row=1, padx=(15,0), pady=15)
        self.profile_button = Button(self.root, text="Profile", width=12, height=3, bd=0, bg="#C3073F",
                                activebackground = "#FFF", activeforeground="#C3073F", command=self.renderProfiles)
        self.profile_button.grid(column= 2, row=1, padx=15, pady=15)
        self.categories_button = Button(self.root, text="categories", width=12, height=3, bd=0, bg="#C3073F",
                                activebackground = "#FFF", activeforeground="#C3073F", command=self.rendercategories)
        self.categories_button.grid(column=3, row=1, padx=0, pady=15)

        self.count = 0

        self.quiz_header = Label(self.root, text='swag', font=("Arial", 18), bg="#1A1A1D", fg="#C3073F")
        self.quiz_header.place(x=25, y=90)

        self.frame_list = []

        for i in range(3):
            quiz_list = self.createQuizObjects()

            count = 0

            self.question_header = Label(self.root, text=quiz_list[0].questions[count]['question'], font=("Arial", 18), bg="#1A1A1D", fg="#C3073F")
            self.question_header.place(x=25, y=125)

            frame_name = "question{}".format(i)

            self.frame_name = Frame(self.root, bg="#1A1A1D", width=950, height=350, highlightbackground="#C3073F", highlightthickness=2)
            self.frame_name.place(x=25, y=170)

            self.a1_button = Button(self.frame_name, text="1.", width=12, height=6, bd=0, bg="#C3073F",
                                    activebackground = "#FFF", activeforeground="#C3073F")
            self.a1_button.place(x=10, y=10)

            self.a1_label = Label(self.frame_name, text=quiz_list[0].questions[count]['answers'][0], font=("Arial", 18), bg="#1A1A1D", fg="#C3073F")
            self.a1_label.place(x=110, y=40)

            self.devider = Frame(self.frame_name, bg="#C3073F", width=950, height=2)
            self.devider.place(x=0, y=116)

            self.a2_button = Button(self.frame_name, text="2.", width=12, height=6, bd=0, bg="#C3073F",
                                    activebackground = "#FFF", activeforeground="#C3073F")
            self.a2_button.place(x=10, y=127)

            self.a1_label = Label(self.frame_name, text=quiz_list[0].questions[count]['answers'][1], font=("Arial", 18), bg="#1A1A1D", fg="#C3073F")
            self.a1_label.place(x=110, y=160)
                
            self.devider = Frame(self.frame_name, bg="#C3073F", width=950, height=2)
            self.devider.place(x=0, y=232)

            self.a3_button = Button(self.frame_name, text="3.", width=12, height=6, bd=0, bg="#C3073F",
                                    activebackground = "#FFF", activeforeground="#C3073F")
            self.a3_button.place(x=10, y=242)

            self.a1_label = Label(self.frame_name, text=quiz_list[0].questions[count]['answers'][2], font=("Arial", 18), bg="#1A1A1D", fg="#C3073F")
            self.a1_label.place(x=110, y=270)

            self.count += 1

            self.frame_list.append(self.frame_name)
            print(self.frame_list)

        self.test_count = 0

        self.next_button = Button(self.root, text="Next", width=12, height=2, bd=0, bg="#C3073F",
                                activebackground = "#FFF", activeforeground="#C3073F", command=lambda: self.renderQuestion(self.frame_list, self.test_count))
        self.next_button.place(x=885, y= 540)

    def renderQuestion(self, frame_list, count):
        print(count)
        print(frame_list)
        frame_list[count].tkraise()
        self.test_count += 1


    def createQuizObjects(self):
        json_object = Json("JSON\\Quizzes.json")
        quiz_json = json_object.read_json()

        count = 1
        y_value = 100
        object_list = []

        for quizzes in quiz_json['quiz']:
            quiz_title = quizzes["Title"]
            quiz_category = quizzes["category"]
            image_location = quizzes["image_location"]
            description = quizzes["description"]
            questions = quizzes["questions"]
            quiz_name = "quiz{}".format(count)
            quiz_name = Quizzes(quiz_title, quiz_category, image_location, description, questions)
            object_list.append(quiz_name)
        return object_list

    def rendercategories(self):
        self.root.destroy()
        setup_categories = CategorysWindow()
        setup_categories.render()

    def renderProfiles(self):
        setup_profiles = ProfileWindow()

    def render(self):
        self.root.mainloop()
        

class CategoryWindow():
    def __init__(self):
        self.root = Toplevel()
        self.root.geometry("400x500")
        self.root.configure(bg="#1A1A1D")
        self.root.resizable(False, False)

        self.profile_header = Label(self.root, text="Category: Swag", font=("Arial", 18), bg="#1A1A1D", fg="#C3073F")
        self.profile_header.place(x=10, y=8)

        self.devider = Frame(self.root, bg="#4E4E50", width=500, height=2)
        self.devider.place(x=0, y=45)

        y_value = 60
        top_count = 1
        for i in range(3):
            self.top_frame = Frame(self.root, bg="#222226", width=380, height=40, highlightbackground="#C3073F", highlightthickness=2)
            self.top_frame.place(x=11,y=y_value)
            self.first_label = Label(self.top_frame, text="Quiz {}".format(top_count), font=("Arial", 12), bg="#222226", fg="white")
            self.first_label.place(x=0, y=6)
            top_count += 1
            y_value += 50

class ProfileWindow():
    def __init__(self):
        self.root = Toplevel()
        self.root.geometry("350x500")
        self.root.configure(bg="#1A1A1D")
        self.root.resizable(False, False)

        username = self.grabUserInfo()
        self.profile_header = Label(self.root, text="{}'s Profile".format(username), font=("Arial", 18), bg="#1A1A1D", fg="#C3073F")
        self.profile_header.place(x=10, y=8)

        self.devider = Frame(self.root, bg="#4E4E50", width=350, height=2)
        self.devider.place(x=0, y=45)

        self.users_points = Label(self.root, text="Points: 350", font=("Arial", 16), bg="#1A1A1D", fg="white")
        self.users_points.place(x=10, y=55)

        self.top_quizzes = Frame(self.root, bg="#1A1A1D", width=350, height=163, highlightbackground="#C3073F", highlightthickness=2)
        self.top_quizzes.place(x=0, y=100)
        
        y_value = 10
        top_count = 1
        for i in range(3):
            self.top_frame = Frame(self.top_quizzes, bg="#222226", width=340, height=40, highlightbackground="#C3073F", highlightthickness=2)
            self.top_frame.place(x=3,y=y_value)
            self.first_label = Label(self.top_frame, text="{}. 2018 Movies: 9/10".format(top_count), font=("Arial", 12), bg="#222226", fg="white")
            self.first_label.place(x=0, y=6)
            top_count += 1
            y_value += 50

    def grabUserInfo(self):
        json_object = Json("JSON\\Users.json")
        user_info_json = json_object.read_json()
        
        for users in user_info_json['users']:
            if users['loggedin'] == True:
                return users['username']



class CategorysWindow():
    def __init__(self):
        self.root = Tk() 
        self.root.geometry("1000x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#1A1A1D")

        self.logo_img = Image.open("logo.png")
        self.logo_img = self.logo_img.resize((70, 70))
        self.logo_img = ImageTk.PhotoImage(self.logo_img)
        self.logo_img_label = Label(self.root, image = self.logo_img, bg="#1A1A1D")
        self.logo_img_label.grid(sticky="nw", column=0, row=1)

        self.home_button = Button(self.root, text="Home", width=12, height=3, bd=0, bg="#C3073F",
                                activebackground = "#FFF", activeforeground="#C3073F", command=self.renderMain)
        self.home_button.grid(column= 1, row=1, padx=(15,0), pady=15)
        self.profile_button = Button(self.root, text="Profile", width=12, height=3, bd=0, bg="#C3073F",
                                activebackground = "#FFF", activeforeground="#C3073F")
        self.profile_button.grid(column= 2, row=1, padx=15, pady=15)

        parent_frame = 100
        categories = ["Gaming", "Geography", "Music", "Movies", "General", "TV", "History", "Science", "Misc"]
        cat_count = 0
        for i in range(3):
            child_frame = 25
            self.row = Frame(self.root, bg="#1A1A1D", width=950, height=152, highlightbackground="#1A1A1D", highlightthickness=2)
            self.row.place(x=25, y=parent_frame)

            self.quiz_image = Image.open("300.png")
            self.quiz_image = self.quiz_image.resize((80,80))
            self.quiz_image = ImageTk.PhotoImage(self.quiz_image)
            for i in range(3):
                self.category1 = Frame(self.row, bg="#1A1A1D", width=250, height=110, highlightbackground="#C3073F", highlightthickness=2)
                self.category1.place(x=child_frame, y=0)
                self.image_label = Label(self.category1, image = self.quiz_image)
                self.image_label.place(x=10, y=10)
                self.cat_title = Label(self.category1, text=categories[cat_count], font=("Arial", 18), bg="#1A1A1D", fg="white")
                self.cat_title.place(x=100, y=5)
                self.devider = Frame(self.category1, bg="#4E4E50", width=120, height=2)
                self.devider.place(x=100, y=42)
                self.cat_button = Button(self.category1, text="Open", width=16, height=2, bd=0, bg="#C3073F",
                                activebackground = "#FFF", activeforeground="#C3073F", command=self.renderCategoryWindow)
                self.cat_button.place(x=102, y=55)
                cat_count += 1
                child_frame += 320
            parent_frame += 170


    def render(self):
        self.root.mainloop()

    def renderMain(self):
        self.root.destroy()
        setup_app = MainApplication()
        setup_quiz = Quizzes()
        setup_app.setup_objects()
        setup_app.render()
    
    def renderCategoryWindow(self):
        setup_catagory = CategoryWindow()