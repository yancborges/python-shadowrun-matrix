class Matrix:

    def __init__(self, rows, cols):

        self.__rows = rows
        self.__cols = cols
        self.__matrix = [[1] * cols for r in range(rows)]

    def __str__(self):
        return str(self.__matrix)

    def __add__(self, n):
        if isinstance(n, int) or isinstance(n, float):
            self.add(n)

    def __mul__(self, n):
        if isinstance(n, int) or isinstance(n, float):
            self.multiply(n)

    def multiply(self, n):
        for row in range(self.__rows):
            for col in range(self.__cols):
                self.__matrix[row][col] *= n

    def add(self, n):
        for row in range(self.__rows):
            for col in range(self.__cols):
                self.__matrix[row][col] += n


m = Matrix(2, 6)
m.multiply(3)
m.multiply(2)
m + 4
print(m)
