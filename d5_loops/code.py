for fruit in ["Apple", "Peach"]:
    print(fruit)

student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 199, 78, 65, 89, 86]

def sum_list(lst):
    summ = 0
    for i in lst:
        summ += i
    return summ

print(sum_list(student_scores))
print(max(student_scores))