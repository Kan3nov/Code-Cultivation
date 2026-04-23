class Plant:
    class Tracker:
        _shows = 0
        _grows = 0
        _ages = 0

        def inc_ages(self):
            self._ages += 1

        def inc_grows(self):
            self._grows += 1

        def inc_shows(self):
            self._shows += 1

        def show(self):
            print(f"Stats : {self._grows} grow, {self._ages} age, " +
                  f"{self._shows} show")

    def __init__(
            self, name: str, height: float, age: int, growth_factor: float = 1
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
        self.tracker = self.Tracker()

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
        self.tracker.inc_shows()
        print(f"{self._name}: {self._height}cm, {self._age} days old")

    def age(self) -> None:
        self.tracker.inc_ages()
        self._age += 1
        self.grow()

    def grow(self) -> None:
        self.tracker.inc_grows()
        self._height += self.growth_factor
        self._height = round(self._height, 1)

    @staticmethod
    def check_year_old(days: int) -> bool:
        return days > 365

    @classmethod
    def make_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)


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


class Seed(Flower):
    seeds = 0

    def __init__(self, name: str, height: float, age: int,
                 growth_factor: float, color: str, seed_factor: int) -> None:
        super().__init__(name, height, age, growth_factor, color)
        self.seed_factor = seed_factor

    def bloom(self) -> None:
        super().bloom()
        self.seeds += self.seed_factor

    def show(self):
        super().show()
        print(f"Seeds: {self.seeds}")


class Tree(Plant):
    class Tracker(Plant.Tracker):
        _prod_shades = 0

        def inc_prod(self):
            self._prod_shades += 1

        def show(self):
            super().show()
            print(f"{self._prod_shades} shade")

    def __init__(self, name: str, height: float, age: int,
                 growth_factor: float, trunk_diameter: float) -> None:
        super().__init__(name, height, age, growth_factor)
        self.tracker = self.Tracker()
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        print(f"Tree {self._name} now produces a shade of" +
              f" {self._height}cm long and {self.trunk_diameter}cm wide.")
        self.tracker.inc_prod()

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


def main():
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print("Is 30 days more than a year? ->", Plant.check_year_old(30))
    print("Is 400 days more than a year? ->", Plant.check_year_old(400))

    print()
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, 0.2, "red")
    rose.show()
    print("Rose has not bloomed yet")
    print("[statistics for Rose]")
    rose.tracker.show()
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.show()
    rose.bloom()
    print("[statistics for Rose]")
    rose.tracker.show()

    print()
    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 0.8, 5.0)
    oak.show()
    print("[statistics for Oak]")
    oak.tracker.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("[statistics for Oak]")
    oak.tracker.show()

    print()
    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, 0.1, "yellow", 42)
    sunflower.show()
    print("Sunflower has not bloomed yet")
    print("[make sunflower grow, age and bloom]")
    sunflower.age()
    sunflower.bloom()
    sunflower.show()
    print("[statistics for Sunflower]")
    sunflower.tracker.show()

    print()
    print("=== Anonymous")
    unknown = Plant.make_anonymous()
    unknown.show()
    print("[statistics for Unknown plant]")
    unknown.tracker.show()


if __name__ == "__main__":
    main()
