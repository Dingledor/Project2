from logic import *
from tkinter import *


class MainWindow:
    def __init__(self, window, logic) -> None:
        """
        Generates all the widgets for the main drawing window
        """
        self.window = window

        # Top Menu
        self.top_menu = Frame(self.window, bd=2, relief=GROOVE)
        self.top_menu.pack(fill=BOTH)
        self.button_oval = Button(self.top_menu, text="Oval", command=logic.open_window_oval)
        self.button_oval.pack(side=LEFT)
        self.button_rectangle = Button(self.top_menu, text="Rectangle", command=logic.open_window_rectangle)
        self.button_rectangle.pack(side=LEFT)
        self.button_triangle = Button(self.top_menu, text="Triangle", command=logic.open_window_triangle)
        self.button_triangle.pack(side=LEFT)
        self.button_text = Button(self.top_menu, text="Text", command=logic.open_window_text)
        self.button_text.pack(side=LEFT)
        self.label_color = Label(self.top_menu, text='    ', bg=logic.color, bd=2, relief=GROOVE)
        self.label_color.pack(side=LEFT, padx=2)

        # Color Menu
        self.frame_color_menu = Frame(self.window)
        self.frame_color_menu.pack(side=LEFT, anchor='nw', pady=2)
        self.button_red = Button(self.frame_color_menu, text="   ", bg="red", fg="red",
                                 activebackground="red", activeforeground="red",
                                 command=lambda: logic.change_color('red'))
        self.button_red.pack(side=TOP)
        self.button_orange = Button(self.frame_color_menu, text="   ", bg="orange", fg="orange",
                                    activebackground="orange", activeforeground="orange",
                                    command=lambda: logic.change_color('orange'))
        self.button_orange.pack(side=TOP)
        self.button_yellow = Button(self.frame_color_menu, text="   ", bg="yellow", fg="yellow",
                                    activebackground="yellow", activeforeground="yellow",
                                    command=lambda: logic.change_color('yellow'))
        self.button_yellow.pack(side=TOP)
        self.button_green = Button(self.frame_color_menu, text="   ", bg="green", fg="green",
                                   activebackground="green", activeforeground="green",
                                   command=lambda: logic.change_color('green'))
        self.button_green.pack(side=TOP)
        self.button_blue = Button(self.frame_color_menu, text="   ", bg="blue", fg="blue",
                                  activebackground="blue", activeforeground="blue",
                                  command=lambda: logic.change_color('blue'))
        self.button_blue.pack(side=TOP)
        self.button_purple = Button(self.frame_color_menu, text="   ", bg="purple", fg="purple",
                                    activebackground="purple", activeforeground="purple",
                                    command=lambda: logic.change_color('purple'))
        self.button_purple.pack(side=TOP)
        self.button_brown = Button(self.frame_color_menu, text="   ", bg="brown", fg="brown",
                                   activebackground="brown", activeforeground="brown",
                                   command=lambda: logic.change_color('brown'))
        self.button_brown.pack(side=TOP)
        self.button_white = Button(self.frame_color_menu, text="   ", bg="white", fg="white",
                                   activebackground="white", activeforeground="white",
                                   command=lambda: logic.change_color('white'))
        self.button_white.pack(side=TOP)
        self.button_black = Button(self.frame_color_menu, text="   ", bg="black", fg="black",
                                   activebackground="black", activeforeground="black",
                                   command=lambda: logic.change_color('black'))
        self.button_black.pack(side=TOP)
        # Canvas
        self.canvas = Canvas(self.window, bg="black", bd=2, relief=GROOVE)
        self.canvas.pack(expand=True, fill=BOTH)


class WindowRectangle:
    def __init__(self, window, logic) -> None:
        """
        Creates the widgets for the rectangle drawing window and binds delete and focus out to functions
        """
        self.window = window
        self.window.focus_force()
        self.window.protocol("WM_DELETE_WINDOW", lambda: logic.draw_rectangle(self.window))
        self.window.bind("<FocusOut>", self.focus_out)
        self.window.title('Rectangle')
        self.frame_background = Frame(self.window, bg=logic.color)
        self.frame_background.pack(fill=BOTH, expand=True)

    def focus_out(self, event) -> None:
        """
        Destroy window
        """
        self.window.destroy()


class WindowOval:
    def __init__(self, window, logic) -> None:
        """
        Creates the widgets for the oval drawing window then binds configure, delete, and focus out to functions
        """
        self.window = window
        self.window.focus_force()
        self.window.bind("<Configure>", self.resize)
        self.window.bind("<FocusOut>", self.focus_out)
        self.window.title('Oval')
        self.window.protocol("WM_DELETE_WINDOW", lambda: logic.draw_oval(self.window))
        self.canvas = Canvas(self.window, bg=('white' if logic.color != 'white' else 'black'), bd=0)
        self.canvas.pack(fill=BOTH, expand=True)
        self.canvas.update_idletasks()
        self.oval = self.canvas.create_oval(0, 0, 300, 300, fill=logic.color)

    def resize(self, event) -> None:
        """
        Resize the oval to fit canvas
        """
        self.window.update_idletasks()
        self.canvas.coords(self.oval, 0, 0, self.window.winfo_width(), self.window.winfo_height())

    def focus_out(self, event) -> None:
        """
        Destroy window
        """
        self.window.destroy()


class WindowText:
    def __init__(self, window, logic) -> None:
        """
        Creates all the widgets for the text window then binds configure, delete, and focus out to functions
        """
        self.fontsize = 30
        self.length_limit = 5
        self.text = StringVar(value='')
        self.window = window
        self.window.focus_force()
        self.window.bind("<Configure>", self.resize)
        self.window.bind("<FocusOut>", self.focus_out)
        self.label_validate = Label(self.window, textvariable=self.text, font='Arial')
        self.window.title('Text')
        self.window.protocol("WM_DELETE_WINDOW", lambda: logic.draw_text(self.window, self.text.get(), self.fontsize))
        self.entry = Entry(self.window, bg=('white' if logic.color != 'white' else 'black'), fg=logic.color,
                           font=('Arial', self.fontsize), bd=0, textvariable=self.text)
        self.entry.place(x=0, y=0, anchor='nw')

    def resize(self, event) -> None:
        """
        Change the font size to fit the window vertically and remove end of text string to fit window horizontally
        """
        self.window.update_idletasks()
        self.fontsize = int(self.window.winfo_height() * (3 / 4))
        self.entry.config(font=('Arial', self.fontsize))
        self.label_validate.config(font=('Arial', self.fontsize))
        while self.label_validate.winfo_width() > self.window.winfo_width():
            self.text.set(self.text.get()[0:-1])
            self.window.update_idletasks()

    def focus_out(self, event) -> None:
        """
        Destroy window
        """
        self.window.destroy()


class WindowTriangle:
    def __init__(self, window, logic) -> None:
        """
        Creates all the widgets for the triangle drawing window then binds configure, delete, and focus out to functions
        """
        self.window = window
        self.window.focus_force()
        self.window.title('Triangle')
        self.window.bind("<FocusOut>", self.focus_out)
        self.window.bind("<Configure>", self.resize)
        self.window.protocol("WM_DELETE_WINDOW", lambda: logic.draw_triangle(self.window))
        self.canvas = Canvas(self.window, bg=('white' if logic.color != 'white' else 'black'), bd=0)
        self.canvas.pack(fill=BOTH, expand=True)
        self.canvas.update_idletasks()
        self.triangle = self.canvas.create_polygon(0, 300, 150, 0, 300, 300, fill=logic.color)

    def resize(self, event) -> None:
        """
        Resize triangle to fit canvas
        """
        self.window.update_idletasks()
        self.canvas.coords(self.triangle, 0, self.window.winfo_height(), self.window.winfo_width() / 2, 0,
                           self.window.winfo_width(), self.window.winfo_height())

    def focus_out(self, event) -> None:
        """
        Destroy window
        """
        self.window.destroy()