from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):

    def __init__(self, first_name, is_alive=True):
        """Your docstring for Constructor"""
        super().__init__(first_name, is_alive)

    def set_eyes(self, color):
        """Your docstring for set_eyes"""
        self.eyes = color

    def get_eyes(self):
        """Your docstring for get_eyes"""
        return self.eyes

    def set_hairs(self, color):
        """Your docstring for set_hairs"""
        self.hairs = color

    def get_hairs(self):
        """Your docstring for get_hairs"""
        return self.hairs
