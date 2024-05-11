from tkinter import *
from logic import *


def main() -> None:
    root = Tk()
    root.title("Window Paint")
    root.geometry("600x600")
    root.resizable(False, False)
    Logic(root)
    root.mainloop()


if __name__ == "__main__":
    main()
