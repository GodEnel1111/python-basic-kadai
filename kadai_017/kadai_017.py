class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def check_adult(self):
        if self.age >= 20:
            print(f"{self.name}は大人です")
        else:
            print(f"{self.name}は大人ではありません")

ages_dict = {"侍太郎":19, "侍一郎":20, "侍次郎":21}
human_list = []

for name, age in ages_dict.items():
    human = Human(name, age)
    human_list.append(human)

for human in human_list:
    human.check_adult()