import random
import time

# 2,3강 반복하기
# for i in range(30):
#     print(random.choice(["된장찌개", "피자", "제육볶음", "치킨", "떡볶이", "라면","감자튀김"]))
#     time.sleep(1)

# while True:
#     print(random.choice(["된장찌개", "피자", "제육볶음", "치킨", "떡볶이", "라면","감자튀김"]))
#     time.sleep(1)
#     break


# 4강 : 데이터 상자 만들기
# lunch = random.choice(["된장찌개", "피자", "제육볶음", "치킨", "떡볶이", "라면","감자튀김"])
# lunch = "냉장고"
# dinner = random.choice(["김밥", "쫄면", "돈까스"])

# print(lunch)


# 5강 Dictionary
# information = {"고향": "대구", "취미": "산책", "좋아하는 음식" : "일식"}
# print(information)
# print(information.get("취미"))

# information2 = {"특기": "피아노", "사는곳": "서울"}
# print(information2.get("특기"))

# 6강 List와 Dictionary
# information = {"고향": "대구", "취미": "산책", "좋아하는 음식" : "일식"}
# print(information.get("취미"))
# information["특기"] = "피아노"
# information["사는곳"] = "서울"
# print(information)
# del information["좋아하는 음식"]
# print(information)
# print(len(information))
# information.clear()
# print(information)

# foods = ["된장찌개", "피자", "제육볶음"]
# print(foods[0])
# print(foods[-1])
# foods.append("김밥")
# print(foods)
# foods.pop()
# print(foods)
# del foods[1]
# print(foods)


# 7강 반복하기
# for x in range(30):
#     print(x)

# foods = ["된장찌개", "피자", "제육볶음"]
# for i in foods:
#     print(i)

# information = {"고향":"수원", "취미":"영화관람", "좋아하는 음식":"국수"}
# for x, y in information.items():
#     print(x)
#     print(y)


# 8,9강 집합
# foods = ["된장찌개", "피자", "제육볶음"]
# foods_set1 = set(foods)
# foods_set2 = set(["된장찌개", "피자", "제육볶음"])
# print(foods_set1)
# print(foods_set2)
# print("------")

# foods = ["된장찌개", "피자", "제육볶음", "된장찌개"]
# foods_set = set(foods)
# print(foods)
# print(foods_set)
# print("-----")

# menu1 = set(["된장찌개", "피자", "제육볶음"])
# menu2 = set(["된장찌개", "떡국", "김밥"])
# menu3 = menu1 | menu2 #합집합
# print(menu3)
# menu3 = menu1 & menu2 #교집합
# print(menu3)
# menu3 = menu1 - menu2 #차집합
# print(menu3)


#10강 조건문
# import random

# food = random.choice(["된장찌개","피자","제육볶음"])

# print(food)
# if(food == "제육볶음"):
#     print("곱배기 주세요")
# else:
#     print("그냥 주세요")
# print("종료")


#11~ 오늘 뭐드실? 제작하기
lunch = ["된장찌개","피자","제육볶음","짜장면"]

while True:
    print(lunch)
    item = input("음식을 추가해주세요(q를 입력하면 입력 종료) : ")
    if item == "q":
        break
    else:
        lunch.append(item)
    
print(lunch)
set_lunch = set(lunch)

while True:
    print(set_lunch)
    item = input("음식을 삭제해주세요(q를 입력하면 입력 종료) : ")
    if item == "q":
        break
    else:
        set_lunch = set_lunch - set([item])

print(set_lunch,"중에서 선택합니다.")

for i in range(5,0,-1):
    print(i)
    time.sleep(1)

print(random.choice(list(set_lunch)))