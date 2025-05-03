from lab_python_oop.figure import GeometricFigure
from lab_python_oop.color import Color

class Rectangle(GeometricFigure):

    type = "Прямоуголник"

    @classmethod
    def get_type(arg):
        return arg.type

    def __init__(self, width_param, height_param, color_param):
        self.width = width_param
        self.height = height_param
        self.color = Color()
        self.color.colorproperty = color_param
    
    def area(self):
        return self.height*self.width

    def __repr__(self):
        return '{} {} цвета шириной {} и высотой {} площадью {}.'.format(
            Rectangle.get_type(),
            self.color.colorproperty,
            self.width,
            self.height,
            self.area()
        )