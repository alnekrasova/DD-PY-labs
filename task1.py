if __name__ == "__main__":
    class Vehicle:
        """
        Базовый класс для всех транспортных средств.

        Атрибуты:
            make (str): Марка транспортного средства.
            model (str): Модель транспортного средства.
            year (int): Год выпуска.
            speed (float): Текущая скорость транспортного средства.
        """

        def __init__(self, make: str, model: str, year: int, speed: float = 0.0):
            """
            Конструктор базового класса.

            :param make: Марка транспортного средства.
            :param model: Модель транспортного средства.
            :param year: Год выпуска.
            :param speed: Текущая скорость (по умолчанию 0.0).
            """
            self.make = make
            self.model = model
            self.year = year
            self.speed = speed

        def __str__(self) -> str:
            """
            Возвращает строковое представление транспортного средства.

            :return: Строка с описанием транспортного средства.
            """
            return f"{self.year} {self.make} {self.model}, текущая скорость: {self.speed} км/ч"

        def __repr__(self) -> str:
            """
            Возвращает формальное строковое представление транспортного средства.

            :return: Формальное строковое представление.
            """
            return f"Vehicle(make={self.make}, model={self.model}, year={self.year}, speed={self.speed})"

        def accelerate(self, amount: float) -> None:
            """
            Увеличивает скорость транспортного средства на указанное значение.

            :param amount: На сколько увеличить скорость.
            """
            self.speed += amount

        def brake(self, amount: float) -> None:
            """
            Уменьшает скорость транспортного средства на указанное значение.

            :param amount: На сколько уменьшить скорость.
            """
            self.speed = max(0, self.speed - amount)


    class Car(Vehicle):
        """
        Дочерний класс для автомобилей.

        Атрибуты:
            make (str): Марка автомобиля.
            model (str): Модель автомобиля.
            year (int): Год выпуска.
            speed (float): Текущая скорость автомобиля.
            fuel_type (str): Тип топлива (бензин, дизель, электричество и т.д.).
        """

        def __init__(self, make: str, model: str, year: int, fuel_type: str, speed: float = 0.0):
            """
            Конструктор дочернего класса.

            :param make: Марка автомобиля.
            :param model: Модель автомобиля.
            :param year: Год выпуска.
            :param fuel_type: Тип топлива.
            :param speed: Текущая скорость (по умолчанию 0.0).
            """
            super().__init__(make, model, year, speed)
            self.fuel_type = fuel_type

        def __str__(self) -> str:
            """
            Возвращает строковое представление автомобиля.

            :return: Строка с описанием автомобиля.
            """
            return f"{self.year} {self.make} {self.model} ({self.fuel_type}), текущая скорость: {self.speed} км/ч"

        def __repr__(self) -> str:
            """
            Возвращает формальное строковое представление автомобиля.

            :return: Формальное строковое представление.
            """
            return f"Car(make={self.make}, model={self.model}, year={self.year}, fuel_type={self.fuel_type}, speed={self.speed})"

        def refuel(self, amount: float) -> None:
            """
            Заправка автомобиля.

            :param amount: Количество топлива для заправки.
            """
            # Логика заправки автомобиля
            pass

        def accelerate(self, amount: float) -> None:
            """
            Перегрузка метода accelerate для учета типа топлива.

            :param amount: На сколько увеличить скорость.
            """
            # Логика ускорения с учетом типа топлива
            super().accelerate(amount)
    pass
