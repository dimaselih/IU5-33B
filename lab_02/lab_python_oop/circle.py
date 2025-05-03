from lab_python_oop.figure import GeometricFigure
from lab_python_oop.color import Color
import math

class Circle(GeometricFigure):

    type = "Круг"

    @classmethod
    def get_type(arg):
        return arg.type

    def __init__(self, Rad_param, color_param):
        self.radius = Rad_param
        self.color = Color()
        self.color.colorproperty = color_param
    
    def area(self):
        return math.pi*(self.radius**2)
    
    def __repr__(self):
        return '{} {} цвета радиусом {} площадью {}.'.format(
            Circle.get_type(),
            self.color.colorproperty,
            self.radius,
            self.area()
        )
