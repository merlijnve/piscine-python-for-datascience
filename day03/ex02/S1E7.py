from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""

    def __init__(self, first_name, is_alive=True):
        """Your docstring for Constructor"""
        super().__init__(first_name)
        self.is_alive = is_alive
        self.family_name = "Baratheon"
        self.eyes = 'brown'
        self.hairs = 'dark'

    def die(self):
        """Your docstring for Method"""
        self.is_alive = False

    def __str__(self):
        """Your docstring for Method"""
        return f"Vector: {(self.family_name, self.eyes, self.hairs)}"

    def __repr__(self):
        """Your docstring for Method"""
        return self.__str__()


class Lannister(Character):
    """Representing the Lannister family."""

    def __init__(self, first_name, is_alive=True):
        """Your docstring for Constructor"""
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = "Lannister"
        self.eyes = 'blue'
        self.hairs = 'light'

    @classmethod
    def create_lannister(self, first_name, is_alive=True):
        """Your docstring for Constructor"""
        return Lannister(first_name, is_alive)

    def die(self):
        """Your docstring for Method"""
        self.is_alive = False

    def __str__(self):
        """Your docstring for Method"""
        return f"Vector: {(self.family_name, self.eyes, self.hairs)}"

    def __repr__(self):
        """Your docstring for Method"""
        return self.__str__()
