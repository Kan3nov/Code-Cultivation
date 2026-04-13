class Plant :
    def __init__(self : Plant, name : str, height : float, age : int, growth_factor : int = 1) -> None :
        self.name = name
        self.height = height
        self.age = age
        self.growth_factor = growth_factor
    def show(self : Plant) -> None:
        print(f"{self.name}, {self.height}cm, {self.age} days old")
    def age(self : Plant) -> None:
        self.age+=1
        self.grow()
    def grow(self : Plant) -> None:
        self.height += self.growth_factor
        self.height = round(self.height, 1)
        
if (__name__ == "__main__"):
    rose = Plant("Rose", 25.0, 30)
    oak = Plant("Oak", 200.0, 365)
    cactus = Plant("Cactus", 5.0, 90)
    sunflower = Plant("Sunflower", 80.0, 45)
    fern = Plant("Fern", 15.0, 120)
    print("=== Plant Factory Output ===")
    print("created : ", end = "")
    rose.show()
    print("created : ", end = "")
    oak.show()
    print("created : ", end = "")
    cactus.show()
    print("created : ", end = "")
    sunflower.show()
    print("created : ", end = "")
    fern.show()