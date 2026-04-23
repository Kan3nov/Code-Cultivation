class Plant:
    def __init__(
            self, name: str, height: float, age: int,
            growth_factor: float = 1.0
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

    def get_height(self) -> float:
        return self._height

    def get_name(self) -> str:
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


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, 0.1, "red")
    rose.show()
    print(rose.get_name() + " has not bloomed yet")
    print("[asking the rose to bloom]")
    rose.show()
    rose.bloom()
    print()
    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 0.5, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print()
    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, 0.2, "April")
    tomato.show()
    print("[make tomato grown and age for 20 days]")
    for x in range(20):
        tomato.age()
    tomato.show()
