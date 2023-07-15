"""
Переписать код в соответствии с Interface Segregation Principle:

public interface Shape {
    double area();
    double volume();
}
public class Circle implements Shape {
    private double radius;
    public Circle(double radius) {
        this.radius = radius;
    }
    @Override
    public double area() {
        return 2 * 3.14 * radius;
    }
    @Override
    public double volume() {
        throw new UnsupportedOperationException();
    }
}
public class Cube implements Shape {
    private int edge;
    public Cube(int edge) {
        this.edge = edge;
    }
    @Override
    public double area() {
        return 6 * edge * edge;
    }
    @Override
    public double volume() {
        return edge * edge * edge;
    }
}

Подсказка: круг не объемная фигура и этому классу не нужен метод volume().
"""

from abc import ABC, abstractmethod
from math import pi


# Разделены интерфейсы и каждый содержит только те методы, которые относятся
# к необходимой функциональности. В то же время, классы реализуют только
# те интерфейсы, которые они используют.
class FlatShape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass


class VolumeShape(ABC):
    @abstractmethod
    def volume(self) -> float:
        pass


class Circle(FlatShape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return 2 * pi * self.radius

    def __str__(self):
        return f"Circle area: {self.area()}"


class Cube(FlatShape, VolumeShape):
    def __init__(self, edge: int):
        self.edge = edge

    def area(self) -> float:
        return 6 * self.edge * self.edge

    def volume(self) -> float:
        return self.edge * self.edge * self.edge

    def __str__(self):
        return f'Cube area: {self.area()}, volume: {self.volume()}'


circle = Circle(radius=5.0)
cube = Cube(edge=3)

print(circle)
print(cube)
