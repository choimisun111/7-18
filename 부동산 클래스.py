#부동산 정보 클래스는 위치, 평수, 건물의 종류, 가격, 건물이 지어진 년도 정보를 갖는다.
#또한, 정보 확인 함수를 사용하면 부동산 객체에 포함된 속성 정보를 화면에 출력한다.

#
# 건물이름 : "힐스테이트"
# 건물연식 : "2008년"
# 건물위치 : 서울 구로구
# 건물평수 : 33평
# 건물가격 : 3억
#
# class house:
#     def __init__(self, 이름, 연식, 위치, 평수, 가격):
#         self.힐스테이트 = 이름
#         self.연식 = 2008년
#         self.위치 = 서울구로구
#         self.


class building:
        def __init__(self, loc, y, p, a):
            self.location = loc
            self.year = y
            self.price = p
            self.area = a

        def print_info(self):
            print(self.location, self.year, self.price,self.area)
building = building("강남", "2008", "22억", "25평")
