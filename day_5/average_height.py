students_height = [int(h) for h in input().split(" ")]
average_height = int(sum(students_height) / len(students_height))
print(average_height)