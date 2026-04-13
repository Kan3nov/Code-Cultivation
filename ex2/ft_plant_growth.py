class Plant:
    def __init__(self, name: str, height: float, age: int,
                 growth_factor: float) -> None:
        self.name = name
        self.height = height
        self._age = age
        self.growth_factor = growth_factor

    def show(self) -> None:
        print(f"{self.name}, {self.height}cm, {self._age} days old")

    def age(self) -> None:
        self._age += 1
        self.grow()

    def grow(self) -> None:
        self.height += self.growth_factor
        self.height = round(self.height, 2)


if (__name__ == "__main__"):
    rose = Plant("Rose", 25.0, 30, 0.8)
    print("=== Garden Plant Growth ===")
    rose.show()
    init_height = rose.height
    for x in range(1, 8):
        Plant.age(rose)
        print(f"=== Day {x}===")
        rose.show()
    fin_height = rose.height
    growth = round(fin_height - init_height, 2)
    print(f"Growth this week: {growth}cm")
