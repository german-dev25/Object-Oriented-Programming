"""Переписать код в соответствии с Dependency Inversion Principle:
public class Car {
    private PetrolEngine engine;
    public Car(PetrolEngine engine) {
        this.engine = engine;
    }
    public void start() {
        this.engine.start();
    }
}

public class PetrolEngine {
    public void start() {
    }
}
Разорвать зависимость классов Car и PetrolEngine.
У машины же может быть DieselEngine.
"""
from abc import ABC, abstractmethod


# Разорвана связь между конкретным типом PetrolEngine и классом Car. Создан
# родительский класс Engine, имеющий абстрактный метод start(), который
# обязательно реализуется в наследниках. Класс Car получает ту реализацию
# метода start, которая соответствует PetrolEngine/DieselEngine
class Engine(ABC):
    @abstractmethod
    def start(self) -> None: pass


class PetrolEngine(Engine):
    def start(self) -> None:
        print("Petrol engine started.")


class DieselEngine(Engine):
    def start(self) -> None:
        print("Diesel engine started.")


class Car:
    def __init__(self, engine: Engine):
        self.engine = engine

    def start(self):
        self.engine.start()


car_with_petrol = Car(PetrolEngine())
car_with_diesel = Car(DieselEngine())

car_with_petrol.start()
car_with_diesel.start()
