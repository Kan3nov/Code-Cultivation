class Plant:
    def __init__(
            self, name: str, height: float, age: int, growth_factor: int = 1
            ) -> None:
        if (name == ""):
            print("Error, no empty strings are permitted")
        else:
            self._name = name
        if (height < 0):
            print("Error, no negative values are permitted")
        else:
            self._height = height
        if (age < 0):
            print("Error, no negative values are permitted")
        else:
            self._age = age
        self.growth_factor = growth_factor

    def get_age(self) -> int:
        return self._age

    def get_height(self) -> int:
        return self._height

    def get_name(self) -> int:
        return self._name

    def set_age(self, age: int) -> None:
        if (age < 0):
            print("Error, no negative values are permitted")
        else:
            self._age = age
            print("Age updated :", age, "days")

    def set_height(self, height: float) -> None:
        if (height < 0):
            print("Error, no negative values are permitted")
        else:
            self._height = height
            print("Height updated : ", height, "cm\n", end="")

    def set_name(self, name: str) -> None:
        if (name == ""):
            print("Error, no empty strings are permitted")
        else:
            self._name = name
            print("Name updated :", name)

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._age} days old")

    def age(self) -> None:
        self._age += 1
        self.grow()

    def grow(self) -> None:
        self._height += self.growth_factor
        self._height = round(self._height, 1)

    @staticmethod
    def check_year_old(days: int) -> bool:
        return days > 365

    @classmethod
    def make_anonymous(cls) -> "Plant":
        return cls("Anonymous", 0.0, 0)


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int,
                 growth_factor: float, color: str) -> None:
        super().__init__(name, height, age, growth_factor)
        self.color = color

    def bloom(self) -> None:
        print(f"{self._name} is blooming beautifully!")

    def show(self):
        super().show()
        print(f"Color : {self.color}")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int,
                 growth_factor: float, trunk_diameter: float) -> None:
        super().__init__(name, height, age, growth_factor)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        print(f"Tree {self._name} now produces a shade of" +
              f" {self._height}cm long and {self.trunk_diameter}cm wide.")

    def show(self):
        super().show()
        print(f"Trunk Diameter: {self.trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 growth_factor: float,
                 harvest_season: str) -> None:
        super().__init__(name, height, age, growth_factor)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def age(self) -> None:
        super().age()
        self.nutritional_value += 1

    def show(self):
        super().show()
        print(f"Harvest season: {self.harvest_season}\n" +
              f"Nutritional value: {self.nutritional_value}")
