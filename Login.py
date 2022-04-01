from tkinter import *
import tkinter.font as font
from tkinter import messagebox as mb
from pygame import mixer
import json
import webbrowser

global quit_button, quit_button2

mixer.init()

root = Tk()
root.title("Login")
img = PhotoImage(file="C:\\Users\\edu27\\OneDrive\\Escritorio\\GROUP PROJECT\\Login\\image.png")
root.iconphoto(False, img)
root.geometry("700x500")
root.config(bg="#3062C7")
root.resizable(False, False)

def login():
    global user_entry, pass_entry, password, user

    for line in open("users and passwords.txt", "r").readlines():
        login_info = line.split()
        #print(login_info)
        if user_entry.get() == login_info[0] and pass_entry.get() == login_info[1]:
            mixer.music.load("got item.mp3")
            mixer.music.play()
            menu()
            return True
        else:
            mixer.music.load("error.mp3")
            mixer.music.play()
    return False


def menu():
    global menu_l, unit1, unit2, logout_b

    user_l.place_forget()
    user_entry.place_forget()
    pass_entry.place_forget()
    pass_l.place_forget()
    # fail_l.place_forget()
    login_button.place_forget()

    root.geometry("700x500")
    bg_1 = Canvas(root, bg="#3062C7", width=700, height=500)
    bg_1.place(x=0, y=0)

    menu_l = Label(
        root,
        text="Select unit to revise",
        font=("Cambria", 24, "bold", "italic", "underline"),
        bg="#3062C7",)
    menu_l.place(x=210, y=50)

    unit1 = Button(
        root,
        text="Unit 1",
        font=("Cambria", 18, "bold"),
        activebackground="#00FF00",
        padx=20,
        pady=20,
        command=unit1_menu,)
    unit1.place(x=100, y=150)

    unit2 = Button(
        root,
        text="Unit 2",
        font=("Cambria", 18, "bold"),
        activebackground="#00FF00",
        padx=20,
        pady=20,
        command=unit2_menu,)
    unit2.place(x=300, y=150)

    logout_b = Button(
        root,
        text="Logout",
        font=("Cambria", 16, "bold", "italic"),
        activebackground="red",
        padx=20,
        command=lambda: [start(), sound()])
    logout_b.place(x=540, y=420)


def sound():
    mixer.music.load("logout.mp3")
    mixer.music.play()


def unit1_menu():
    global flash_1, test_1, back_b1, menu1_l, links1

    mixer.music.load("click.mp3")
    mixer.music.play()

    root.geometry("700x500")
    bg_1 = Canvas(root, bg="#3062C7", width=700, height=500)
    bg_1.place(x=0, y=0)

    menu_l.place_forget()
    unit1.place_forget()
    unit2.place_forget()

    menu1_l = Label(
        root,
        text="Unit 1 menu",
        font=("Cambria", 24, "bold", "italic", "underline"),
        bg="#3062C7")
    menu1_l.place(x=260, y=50)

    flash_1 = Button(
        root,
        text="Flashcard",
        font=("Arial", 16, "bold", "italic"),
        pady=10,
        activebackground="#18CD84",
        command=flashcard_1,)
    flash_1.place(x=100, y=200)

    test_1 = Button(
        root,
        text="Quiz",
        font=("Arial", 16, "bold", "italic"),
        pady=10,
        activebackground="#18CD84",
        command=quiz_1,)
    test_1.place(x=325, y=200)

    links1 = Button(
        root,
        text="Revision\nVideos",
        font=("Arial", 16, "bold", "italic"),
        activebackground="#18CD84",
        command=vids_unit1,)
    links1.place(x=500, y=200)

    back_b1 = Button(
        root,
        text="Back",
        font=("Cambria", 16, "bold", "italic"),
        activebackground="red",
        command=lambda:[menu(), xd()])
    back_b1.place(x=580, y=420)


def flashcard_1():
    global f_text, my_text, f, q_lines, i, k

    mixer.music.load("click.mp3")
    mixer.music.play()

    flash_1.place_forget()
    test_1.place_forget()
    links1.place_forget()
    back_b1.place_forget()
    menu1_l.place_forget()
    i = 0
    k = -1

    def question():
        clear()
        global my_text, f, q_lines, i, k

        with open("Unit1 questions.txt") as f:
            q_lines = f.readlines()
            my_text.insert(1.0, q_lines[i] + "\n\n")
            k = k + 1
            i = i + 1

    def clear():
        my_text.delete(1.0, END)

    def answer():
        global my_text, f, a_lines, k
        g = open("Unit1 answers.txt")
        a_lines = g.readlines()
        my_text.insert(3.0, a_lines[k])
        if k == 35:
            final_1 = Label(
                root,
                text="End of Unit 1 :)",
                font=("Arial", 20, "bold", "italic"),
                bg="#3062C7",
            ).place(x=250, y=340)
            f.close()

    f_text = font.Font(family="Arial", size=14)
    q_button = Button(
        root, text="Question", bg="white", activebackground="green", command=question
    )
    q_button["font"] = f_text
    q_button.place(x=245, y=280)

    a_button = Button(
        root, text="Answer", bg="white", activebackground="green", command=answer
    )
    a_button["font"] = f_text
    a_button.place(x=365, y=280)

    back_button = Button(
        root, text="Back", bg="white", activebackground="red", command=unit1_menu
    )
    back_button["font"] = f_text
    back_button.place(x=320, y=400)

    my_text = Text(root, width=40, height=10, font=("Helvetica", 16))
    my_text.place(x=120, y=20)


def quiz_1():
    global quit_button

    mixer.music.load("click.mp3")
    mixer.music.play()

    flash_1.place_forget()
    test_1.place_forget()
    links1.place_forget()
    back_b1.place_forget()
    menu1_l.place_forget()

    class Quiz:
        # root.config(bg="SystemButtonFace")
        bg_1 = Canvas(root, bg="SystemButtonFace", width=800, height=450)
        bg_1.place(x=0, y=0)

        def __init__(self):
            self.q_no = 0
            self.display_title()
            self.display_question()
            self.opt_selected = IntVar()
            self.opts = self.radio_buttons()
            self.display_options()
            self.buttons()
            self.data_size = len(question)
            self.correct = 0

        def display_result(self):
            wrong_count = self.data_size - self.correct
            correct = f"Correct: {self.correct}"
            wrong = f"Wrong: {wrong_count}"
            score = int(self.correct / self.data_size * 100)
            result = f"Score: {score}%"
            mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")

        def check_ans(self, q_no):
            if self.opt_selected.get() == answer[q_no]:
                return True

        def next_btn(self):
            if self.check_ans(self.q_no):
                self.correct += 1

            self.q_no += 1

            if self.q_no == self.data_size:
                self.display_result()
                # root.destroy()
            else:
                self.display_question()
                self.display_options()

        def buttons(self):
            next_button = Button(
                root,
                text="Next",
                command=self.next_btn,
                width=10,
                bg="blue",
                activebackground="yellow",
                fg="white",
                font=("ariel", 16, "bold"),
            )
            next_button.place(x=350, y=380)

            quit_button = Button(
                root,
                text="Quit",
                command=unit1_menu,
                width=5,
                bg="black",
                activebackground="red",
                fg="white",
                font=("ariel", 16, " bold"),
            )

            quit_button.place(x=700, y=50)

        def display_options(self):
            val = 0

            self.opt_selected.set(0)

            for option in options[self.q_no]:
                self.opts[val]["text"] = option
                val += 1

        def display_question(self):
            q_no = Label(
                root,
                text=question[self.q_no],
                width=50,
                font=("ariel", 16, "bold"),
                anchor="w",
            )
            q_no.place(x=70, y=100)

        def display_title(self):
            title = Label(
                root,
                text="Unit 1 QUIZ",
                width=47,
                bg="green",
                fg="white",
                font=("ariel", 20, "italic", "bold"),
            )
            title.place(x=0, y=2)

        def radio_buttons(self):
            q_list = []
            y_pos = 150

            while len(q_list) < 4:
                radio_btn = Radiobutton(
                    root,
                    text=" ",
                    variable=self.opt_selected,
                    value=len(q_list) + 1,
                    font=("ariel", 14),
                )
                q_list.append(radio_btn)
                radio_btn.place(x=100, y=y_pos)
                y_pos += 40
            return q_list

    root.geometry("800x450")

    with open("data.json") as f:
        data = json.load(f)

    question = data["question"]
    options = data["options"]
    answer = data["answer"]
    quiz = Quiz()


def vids_unit1():
    mixer.music.load("click.mp3")
    mixer.music.play()

    bg_v1 = Canvas(root, bg="#3062C7", width=700, height=500)
    bg_v1.place(x=0, y=0)

    v1_u1 = Button(
        root,
        text="Virtual memory",
        command=lambda: webbrowser.open("https://youtu.be/AMj4A1EBTTY"),
    )
    v1_u1.place(x=10, y=10)

    v2_u1 = Button(
        root,
        text="Lossy, lossless",
        command=lambda: webbrowser.open("https://youtu.be/v1u-vY6NEmM"),
    )
    v2_u1.place(x=120, y=10)

    v3_u1 = Button(
        root,
        text="Opertaing System",
        command=lambda: webbrowser.open("https://youtu.be/7vbRGDgHukA"),
    )
    v3_u1.place(x=220, y=10)

    v4_u1 = Button(
        root,
        text="Utilities",
        command=lambda: webbrowser.open("https://youtu.be/Z0uVNcNKags"),
    )
    v4_u1.place(x=280, y=10)

    back_button = Button(
        root,
        text="Back",
        font=("Arial", 16, "italic", "bold"),
        activebackground="red",
        command=unit1_menu,
    )
    back_button.place(x=320, y=400)


def unit2_menu():
    global menu_l, unit1, unit2, flash_2, test_2, back_b2, menu2_l, links2

    mixer.music.load("click.mp3")
    mixer.music.play()

    root.geometry("700x500")
    bg_1 = Canvas(root, bg="#3062C7", width=700, height=500)
    bg_1.place(x=0, y=0)

    menu_l.place_forget()
    unit1.place_forget()
    unit2.place_forget()

    menu2_l = Label(
        root,
        text="Unit 2 menu",
        font=("Cambria", 24, "bold", "italic", "underline"),
        bg="#3062C7",)
    menu2_l.place(x=260, y=50)

    flash_2 = Button(
        root,
        text="Flashcard",
        font=("Arial", 16, "bold", "italic"),
        pady=10,
        activebackground="#18CD84",
        command=flashcard_2,)
    flash_2.place(x=100, y=200)

    test_2 = Button(
        root,
        text="Quiz",
        font=("Arial", 16, "bold", "italic"),
        pady=10,
        activebackground="#18CD84",
        command=quiz_2,)
    test_2.place(x=325, y=200)

    links2 = Button(
        root,
        text="Revision\nVideos",
        font=("Arial", 16, "bold", "italic"),
        activebackground="#18CD84",
        command=vids_unit2,)
    links2.place(x=500, y=200)

    back_b2 = Button(
        root,
        text="Back",
        font=("Cambria", 16, "bold", "italic"),
        activebackground="red",
        command=lambda:[menu(),xd()])
    back_b2.place(x=580, y=420)


def flashcard_2():
    global f_text_2, my_text2, f2, q2_lines, i2, k2

    mixer.music.load("click.mp3")
    mixer.music.play()

    flash_2.place_forget()
    test_2.place_forget()
    links2.place_forget()
    back_b2.place_forget()
    menu2_l.place_forget()
    i2 = 0
    k2 = -1

    def question():
        clear()
        global my_text2, f2, q2_lines, i2, k2

        with open("Unit2 questions.txt") as f2:
            q2_lines = f2.readlines()
            my_text2.insert(1.0, q2_lines[i2] + "\n\n")
            k2 = k2 + 1
            i2 = i2 + 1

    def clear():
        my_text2.delete(1.0, END)

    def answer():
        global my_text2, f2, a2_lines, k2
        g2 = open("Unit2 answers.txt")
        a2_lines = g2.readlines()
        my_text2.insert(3.0, a2_lines[k2])
        if k2 == 43:
            final_12 = Label(
                root,
                text="End of Unit 2 :)",
                font=("Arial", 20, "bold", "italic"),
                bg="#3062C7",
            ).place(x=250, y=340)
            f2.close()

    f_text_2 = font.Font(family="Arial", size=14)
    q2_button = Button(
        root, text="Question", bg="white", activebackground="green", command=question
    )
    q2_button["font"] = f_text_2
    q2_button.place(x=245, y=280)

    a2_button = Button(
        root, text="Answer", bg="white", activebackground="green", command=answer
    )
    a2_button["font"] = f_text_2
    a2_button.place(x=365, y=280)

    back2_button = Button(
        root, text="Back", bg="white", activebackground="red", command=unit2_menu
    )
    back2_button["font"] = f_text_2
    back2_button.place(x=320, y=400)

    my_text2 = Text(root, width=40, height=10, font=("Helvetica", 16))
    my_text2.place(x=120, y=20)


def quiz_2():
    global quit_button2

    mixer.music.load("click.mp3")
    mixer.music.play()

    flash_2.place_forget()
    test_2.place_forget()
    links2.place_forget()
    back_b2.place_forget()
    menu2_l.place_forget()

    class Quiz:
        root.geometry("900x450")
        # root.config(bg="SystemButtonFace")
        bg_1 = Canvas(root, bg="SystemButtonFace", width=900, height=450)
        bg_1.place(x=0, y=0)

        def __init__(self):
            self.q_no = 0
            self.display_title()
            self.display_question()
            self.opt_selected = IntVar()
            self.opts = self.radio_buttons()
            self.display_options()
            self.buttons()
            self.data_size = len(question)
            self.correct = 0

        def display_result(self):
            wrong_count = self.data_size - self.correct
            correct = f"Correct: {self.correct}"
            wrong = f"Wrong: {wrong_count}"
            score = int(self.correct / self.data_size * 100)
            result = f"Score: {score}%"
            mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")

        def check_ans(self, q_no):
            if self.opt_selected.get() == answer[q_no]:
                return True

        def next_btn(self):
            if self.check_ans(self.q_no):
                self.correct += 1

            self.q_no += 1

            if self.q_no == self.data_size:
                self.display_result()
                # root.destroy()
            else:
                self.display_question()
                self.display_options()

        def buttons(self):
            next_button = Button(
                root,
                text="Next",
                command=self.next_btn,
                width=10,
                bg="blue",
                activebackground="yellow",
                fg="white",
                font=("ariel", 16, "bold"),
            )
            next_button.place(x=400, y=380)

            quit_button = Button(
                root,
                text="Quit",
                command=unit2_menu,
                width=5,
                bg="black",
                activebackground="red",
                fg="white",
                font=("ariel", 16, " bold"),
            )

            quit_button.place(x=800, y=50)

        def display_options(self):
            val = 0

            self.opt_selected.set(0)

            for option in options[self.q_no]:
                self.opts[val]["text"] = option
                val += 1

        def display_question(self):
            q_no = Label(
                root,
                text=question[self.q_no],
                width=50,
                font=("ariel", 16, "bold"),
                anchor="w",
            )
            q_no.place(x=70, y=100)

        def display_title(self):
            title = Label(
                root,
                text="Unit 2 QUIZ",
                width=53,
                bg="green",
                fg="white",
                font=("ariel", 20, "italic", "bold"),
            )
            title.place(x=0, y=2)

        def radio_buttons(self):
            q_list = []
            y_pos = 150

            while len(q_list) < 4:
                radio_btn = Radiobutton(
                    root,
                    text=" ",
                    variable=self.opt_selected,
                    value=len(q_list) + 1,
                    font=("ariel", 14),
                )
                q_list.append(radio_btn)
                radio_btn.place(x=100, y=y_pos)
                y_pos += 40
            return q_list

    with open("data2.json") as f:
        data2 = json.load(f)

    question = data2["question"]
    options = data2["options"]
    answer = data2["answer"]
    quiz = Quiz()


def vids_unit2():
    mixer.music.load("click.mp3")
    mixer.music.play()

    bg_v1 = Canvas(root, bg="#3062C7", width=700, height=500)
    bg_v1.place(x=0, y=0)

    v1_u2 = Button(
        root,
        text="Virtual\nmemory",
        font=("Arial", 16),
        command=lambda: webbrowser.open("https://youtu.be/AMj4A1EBTTY"),
    )
    v1_u2.place(x=10, y=50)

    v2_u2 = Button(
        root,
        text="Lossy,\nlossless",
        font=("Arial", 16),
        command=lambda: webbrowser.open("https://youtu.be/v1u-vY6NEmM"),
    )
    v2_u2.place(x=110, y=50)

    v3_u2 = Button(
        root,
        text="Opertaing System",
        font=("Arial", 16),
        command=lambda: webbrowser.open("https://youtu.be/7vbRGDgHukA"),
    )
    v3_u2.place(x=320, y=50)

    v4_u2 = Button(
        root,
        text="Utilities",
        font=("Arial", 16),
        command=lambda: webbrowser.open("https://youtu.be/Z0uVNcNKags"),
    )
    v4_u2.place(x=10, y=120)

    back2_button = Button(
        root,
        text="Back",
        font=("Arial", 16, "italic"),
        activebackground="red",
        command=unit2_menu,
    )
    back2_button.place(x=320, y=400)

def xd():
    mixer.music.load("click.mp3")
    mixer.music.play()

def start():
    global user_l, user_entry, pass_l, pass_entry, login_button, logout_b

    bg_1 = Canvas(root, bg="#3062C7", width=700, height=500)
    bg_1.place(x=0, y=0)

    program = True
    while program:

        user_l = Label(
            root, text="Username", font=("Arial", 20, "italic", "bold"), bg="#3062C7"
        )
        user_l.place(x=115, y=200)

        user_entry = Entry(root, font="Arial 20", width=20)
        user_entry.place(x=260, y=200)

        pass_l = Label(
            root, text="Password", font=("Arial", 20, "italic", "bold"), bg="#3062C7"
        )
        pass_l.place(x=115, y=280)

        pass_entry = Entry(root, font="Arial 20", width=20)
        pass_entry.place(x=260, y=280)

        login_button = Button(
            root,
            text="Login",
            padx=20,
            font=("Cambria", 16, "italic", "bold"),
            command=login)
        login_button.place(x=300, y=350)

        root.mainloop()
        program = False


start()
