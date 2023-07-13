class calculator:
    """Calculator class"""
    def __init__(self, list) -> None:
        """Constructor"""
        self.list = list

    def __add__(self, object) -> None:
        """Addition"""
        for index, _ in enumerate(self.list):
            self.list[index] += object
        print(self.list)

    def __mul__(self, object) -> None:
        """"Multiplication"""
        for index, _ in enumerate(self.list):
            self.list[index] *= object
        print(self.list)

    def __sub__(self, object) -> None:
        """Subtraction"""
        for index, _ in enumerate(self.list):
            self.list[index] -= object
        print(self.list)

    def __truediv__(self, object) -> None:
        """Division"""
        if (object == 0):
            print("Error: Division by 0 is not possible")
            return
        for index, _ in enumerate(self.list):
            self.list[index] /= object
        print(self.list)
