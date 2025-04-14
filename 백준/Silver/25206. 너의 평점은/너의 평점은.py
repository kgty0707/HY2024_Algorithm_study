import sys

GOAL_GRADE = 3.3
GRADE_DICT = {"A+" : 4.5,
              "A0" : 4.0,
              "B+" : 3.5,
              "B0" : 3.0,
              "C+" : 2.5,
              "C0" : 2.0,
              "D+" : 1.5,
              "D0" : 1.0,
              "F"  : 0.0}
total_credit = []
all_credit = 0

for i in range(20):
    subject, credit, grade = map(str, sys.stdin.readline().split())
    if not grade == "P":
        total_credit.append(float(credit) * (GRADE_DICT[grade]))
        all_credit += float(credit)


result = sum(total_credit) / all_credit
print(result)