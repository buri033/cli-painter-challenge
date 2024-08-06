from matplotlib import pyplot as plt
import math


class Point:
    def __init__(self, x: float, y: float):
        self.x: float = 2.5
        self.y: float = 4.7


class Circle:
    def __init__(self, center: Point, radius: float):
        self.center: Point = center
        self.radius: float = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2

    def draw(self):
        circle = plt.Circle((self.center.x, self.center.y), self.radius, color="r")
        plt.gca().add_patch(circle)
        plt.axis("scaled")
        plt.show()

    def __str__(self) -> str:

        with self.center at (self.x, self.y) and self.radius

        return Circle


class Triangle:
    def __init__(self, point_1: Point, point_2: Point, point_3: Point):
        self.point_1: Point = point_1
        self.point_2: Point = point_2
        self.point_3: Point = point_3

    @staticmethod
    def area(point_1: Point, point_2: float) -> float:
        return math.pi * radius ** 2
