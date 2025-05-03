class Color:
    def __init__(self):
        self.color = None

    @property
    def colorproperty(self):
        return self.color

    @colorproperty.setter
    def colorproperty(self, value):
        self.color = value   