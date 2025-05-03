from lab_python_oop.rectangle import Rectangle

class Square(Rectangle):

    type = "Квадрат"

    @classmethod
    def get_type(arg):
        return arg.type

    def __init__(self, side_param, color_param):    
        self.side = side_param

        super().__init__(self.side, self.side, color_param)

    def __repr__(self):
            return '{} {} цвета со стороной {} площадью {}.'.format(
                Square.get_type(),
                self.color.colorproperty,
                self.side,
                self.area()
            )