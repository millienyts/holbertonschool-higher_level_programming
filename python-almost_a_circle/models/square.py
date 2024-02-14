#!/usr/bin/python3
"""comment"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """comment"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def update(self, *args, **kwargs):
        """comment"""
        my_list = ["id", "size", "x", "y"]
        if args:
            for name, value in zip(my_list, args):
                setattr(self, name, value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """comment"""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
            }

    def __repr__(self):
        return str(self.to_dictionary())
