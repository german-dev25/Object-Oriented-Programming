"""
Переписать код в соответствии с Liskov Substitution Principle:
public class Rectangle {
    private int width;
    private int height;
    public void setWidth(int width) {
        this.width = width;
    }
    public void setHeight(int height) {
        this.height = height;
    }
    public int area() {
        return this.width * this.height;
    }
}

public class Square extends Rectangle {
    @Override
    public void setWidth(int width) {
        super.width = width;
        super.height = width;
    }
    @Override
    public void setHeight(int height) {
        super.width = height;
        super.height = height;
    }
}
"""
from abc import abstractmethod, ABC


# Создал интерфейс, содержащий метод обязательный для реализации
# Каждый класс-наследник реализует его по своему и при этом не будет
# необходимости изменять что-либо в коде при появлении новых классов в самом
# абстрактном классе Quadrilateral, равно и в уже созданных наследниках
class Quadrilateral(ABC):
    @abstractmethod
    def area(self) -> float: pass

    def __str__(self):
        return f'{self.__class__.__name__} area: {self.area}'


class Rectangle(Quadrilateral):
    def __init__(self, width: float, length: float):
        self.width = width
        self.length = length

    @property
    def area(self) -> float:
        return self.width * self.length


class Square(Quadrilateral):
    def __init__(self, width: float):
        self.width = width

    @property
    def area(self) -> float:
        return self.width * self.width


rectangle = Rectangle(width=5, length=10)
square = Square(width=7)

print(rectangle)
print(square)
