from gui import *
from tkinter import *


class Logic:
    def __init__(self, window) -> None:
        """
        Declares the color variable then opens the main window
        """
        self.color = 'green'
        self.window = window
        self.main_window = MainWindow(window, self)

    def open_window_rectangle(self) -> None:
        """
        Opens the rectangle drawing window
        """
        window_rectangle = WindowRectangle(Toplevel(self.window), self)
        window_rectangle.window.geometry('300x300')

    def draw_rectangle(self, window) -> None:
        """
        Draws a rectangle on the main canvas using data from the toplevel then closes the toplevel
        """
        self.main_window.canvas.create_rectangle(*self.get_relative_coordinates(self.main_window.window, window),
                                                 fill=self.color, outline=self.color)
        window.destroy()

    def open_window_oval(self) -> None:
        """
        Opens the oval drawing window
        """
        window_oval = WindowOval(Toplevel(self.window), self)
        window_oval.window.geometry('300x300')

    def draw_oval(self, window) -> None:
        """
        Draws an oval on the main canvas of using data from toplevel then closes toplevel
        """
        self.main_window.canvas.create_oval(*self.get_relative_coordinates(self.main_window.window, window),
                                            fill=self.color, outline=self.color)
        window.destroy()

    def open_window_text(self) -> None:
        """
        Opens the text window
        """
        window_text = WindowText(Toplevel(self.window), self)
        window_text.window.geometry('300x300')

    def draw_text(self, window, text, fontsize) -> None:
        """
        Draws text on the main window with font matching that of the toplevel window then closes toplevel
        """
        self.main_window.canvas.create_text(self.get_relative_coordinates(self.main_window.window, window)[0],
                                            fill=self.color, text=text, font=('Arial', fontsize), anchor='nw')
        window.destroy()

    def open_window_triangle(self) -> None:
        """
        Opens the triangle drawing window
        """
        window_triangle = WindowTriangle(Toplevel(self.window), self)
        window_triangle.window.geometry('300x300')

    def draw_triangle(self, window) -> None:
        """
        Draws a triangle on the main window using data from the closing toplevel window then deletes toplevel
        """
        point1, point2 = self.get_relative_coordinates(self.main_window.window, window)
        self.main_window.canvas.create_polygon(point1[0], point2[1], (point1[0] + point2[0]) / 2, point1[1], *point2,
                                               fill=self.color)
        window.destroy()

    def change_color(self, color) -> None:
        """
        Updates color variable and changes color of color indicator on main window
        """
        self.color = color
        self.main_window.label_color.config(bg=self.color)

    def get_relative_coordinates(self, main_window, second_window) -> tuple[tuple[int, int], tuple[int, int]]:
        """
        Return relative coordinates between two windows
        """
        offset_x = -self.main_window.canvas.winfo_x()
        offset_y = -self.main_window.canvas.winfo_y()
        top_left = (second_window.winfo_x() - main_window.winfo_x() + offset_x,
                    second_window.winfo_y() - main_window.winfo_y() + offset_y)
        bottom_right = (second_window.winfo_x() - main_window.winfo_x() + second_window.winfo_width() + offset_x,
                        second_window.winfo_y() - main_window.winfo_y() + second_window.winfo_height() + offset_y)
        return top_left, bottom_right
