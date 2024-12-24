class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(f"{self.name}の年齢は{self.age}歳です")

print_age = Human("侍太郎", "21")

print_age.print_info()