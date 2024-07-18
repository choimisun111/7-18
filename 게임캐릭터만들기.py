#게임캐릭터 생성 클래스는 아이디, 성별, 직업정보를 가지며 기본 공격 함수를 갖는다.
#기본 공격 함수는 사용시 "공격" 문자열을 화면에 출력한다.


# class game:
#
#     def __init__(self, name, sex, job, 공격):
#         self.game_id = name
#         self.game_sex = sex
#         self.game_job = job
#         self.game_공격 = 공격
#
#
# most = game("닉네임", "남","직업","공격")
# print(most)


class game_char:
    def __init__(self,n,s,j):
        self.game_id =n
        self.game_sex =s
        self.game_job = j
    def attack(self, 상대방_id):
        print(self.game_id, "(이)가", 상대방_id, "공격했다!")




my_char=game_char("관훈짱짱", "여", "전사")
my_char.attack("짱짱보스")
my_char.attack("짱짱보스")
my_char2 = game_char("뉴비입니다", "여", "전사")
my_char2.attack()

def add(a, b):
    result = a+ b + b**b + a ** a
    return result
print(add(125, 200))
