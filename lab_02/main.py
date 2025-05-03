from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
from colorama import init, Fore, Back, Style


def main():
    init()
    r = Rectangle(3, 2, "синего")
    c = Circle(5, "зеленого")
    s = Square(5, "красного")
    print(Fore.BLUE)
    print(r)
    print(Fore.GREEN)
    print(c)
    print(Fore.RED)
    print(s)
    print(Style.RESET_ALL)

if __name__ == "__main__":
    main()
