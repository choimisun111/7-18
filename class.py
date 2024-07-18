class Dog:
    def __init__(self, name, breed):
        self.dog_name = name
        self.dog_breed = breed
        self.dog_sex = "남"
    def bark(self):
        print(self.dog_breed, "가 짖습니다.")


(Dog("뽀삐", "말티즈")).bark()


my_dog = Dog("뽀삐", "말티즈")
my_dog.bark()
my_dog.bark()
my_dog.bark()
my_dog.bark()
my_dog.bark()


