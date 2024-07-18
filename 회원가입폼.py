#사용자의 이름, 나이, 연락처를 입력받아서 화면에 '입력하신 이름은 000이며, 나이는 000
#그리고 연락처는 00-000입니다.'를 출력하는 클래스를 작성하시오


class sign:
        def __init__(self, a, b, c):
            self.name = a
            self.age = b
            self.phone = c

            def print_info(self):
                print(self.name, self.age, self.phone)
print(sign("최미선","22", "010-1234-5678"))


class person :
    def __init__(self, n, a, p):
        self.name =n
        self.age = a
        self.phone = p

        def print_info(self):
            print("사람 이름 :"self.name)
my_person = person("최미선", "25","010-1234-5678")
my_person.print_info()