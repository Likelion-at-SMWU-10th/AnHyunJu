import random
import time

for i in range(30):
    print(random.choice(["된장찌개", "피자", "제육볶음", "치킨", "떡볶이", "라면","감자튀김"]))
    time.sleep(1)

while True:
    print(random.choice(["된장찌개", "피자", "제육볶음", "치킨", "떡볶이", "라면","감자튀김"]))
    time.sleep(1)
    break