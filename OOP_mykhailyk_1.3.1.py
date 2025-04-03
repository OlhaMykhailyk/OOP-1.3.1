import math

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def perimeter(self):
        return self.a + self.b + self.c
    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))

class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h
    def perimeter(self):
        return 2*(self.h+self.w)
    def area(self):
        return self.h*self.w

class Trapeze:
    def __init__(self, base1, base2, side1, side2, height):
        self.base1 = base1
        self.base2 = base2
        self.side1 = side1
        self.side2 = side2
        self.height = height

    def perimeter(self):
        return self.base1 + self.base2 + self.side1 + self.side2

    def area(self):
        return (self.base1 + self.base2) * self.height / 2

class Parallelogram:
    def __init__(self, base, side, height):
        self.base = base
        self.side = side
        self.height = height

    def perimeter(self):
        return 2 * (self.base + self.side)

    def area(self):
        return self.base * self.height


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius ** 2

def read_figures_from_files(filenames):
    figures = []

    for filename in filenames:
        try:
            with open(filename, 'r') as file:
                for line in file:
                    parts = line.split()
                    if not parts:
                        continue
                    name = parts[0]  # Назва фігури
                    params = list(map(float, parts[1:]))  # Числові параметри

                    if name == "Triangle" and len(params) == 3:
                        figures.append(Triangle(*params))
                    elif name == "Rectangle" and len(params) == 2:
                        figures.append(Rectangle(*params))
                    elif name == "Trapeze" and len(params) == 5:
                        figures.append(Trapeze(*params))
                    elif name == "Parallelogram" and len(params) == 3:
                        figures.append(Parallelogram(*params))
                    elif name == "Circle" and len(params) == 1:
                        figures.append(Circle(*params))
        except FileNotFoundError:
            print(f"Файл {filename} не знайдено!")
    return figures

input_files = ["input01.txt", "input02.txt", "input03.txt"]

figures = read_figures_from_files(input_files)

max_area_shape = max(figures, key=lambda shape: shape.area())
max_perimeter_shape = max(figures, key=lambda shape: shape.perimeter())

result = (
    f"Фігура з найбільшою площею: {max_area_shape.__class__.__name__}, Площа: {max_area_shape.area():.2f}\n"
    f"Фігура з найбільшим периметром: {max_perimeter_shape.__class__.__name__}, Периметр: {max_perimeter_shape.perimeter():.2f}\n"
)

with open("output.txt", "w") as output_file:
    output_file.write(result)