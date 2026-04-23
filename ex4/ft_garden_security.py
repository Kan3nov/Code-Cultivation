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
        print("Plant created : ", end="")
        self.show()

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
        print(f"{self._name}, {self._height}cm, {self._age} days old")

    def age(self) -> None:
        self._age += 1
        self.grow()

    def grow(self) -> None:
        self._height += self.growth_factor
        self._height = round(self._height, 1)


if (__name__ == "__main__"):
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 10)
    print()
    rose.set_height(25.0)
    rose.set_age(30)
    rose.set_height(-25.0)
    print()
    rose.set_age(-30)
    print()
    print("Current state : ", end="")
    rose.show()
