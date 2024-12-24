class Human:
    def __init__(self):
        self.name = ""
        self.age = ""

    def print_info(self, name, age):
        self.name = name
        self.age = age
        print(f"{self.name}の年齢は{self.age}歳です")

print_age = Human()

print_age.print_info("侍太郎", "21")