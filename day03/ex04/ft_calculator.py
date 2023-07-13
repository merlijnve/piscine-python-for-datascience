class calculator:
    """Vector calculator class"""
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Dot product"""
        total = 0
        for index, _ in enumerate(V1):
            total += V1[index] * V2[index]
        print(total)

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Addition"""
        new = []
        for index, _ in enumerate(V1):
            new.append(float(V1[index] + V2[index]))
        print(new)

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Subtraction"""
        new = []
        for index, _ in enumerate(V1):
            new.append(float(V1[index] - V2[index]))
        print(new)
