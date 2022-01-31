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
for x in range(30):
    print(x)

foods = ["된장찌개", "피자", "제육볶음"]
for i in foods:
    print(i)

information = {"고향":"수원", "취미":"영화관람", "좋아하는 음식":"국수"}
for x, y in information.items():
    print(x)
    print(y)