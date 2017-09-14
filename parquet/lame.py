
class Lame(object):

    def __init__(self, length, width, color, y=None):
        self.length = length
        self.width = width
        self.color = color
        self._y = y
        self._end_y = None

    @property
    def end_y(self):
        return self._end_y

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value
        self._end_y = value + self.length

    def __repr__(self):
        return "<lame: l={} w={} {} y={} end_y={}>".format(self.length, self.width, self.color, self.y, self._end_y)
