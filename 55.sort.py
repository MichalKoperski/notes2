# sort() method     =   used with lists

students = [("Squidward", "F",60),
            ("Sandy","A",33),
            ("Patrick","D",36),
            ("Spongebob","B",20),
            ("Mr. Krabs", "C",78)]

grade = lambda grades:grades[1]
students.sort(key=grade)

for i in students:
    print(i)

print("_"*40)
age = lambda ages:ages[2]
students.sort(key=age)

for i in students:
    print(i)

print("_"*40)
# sort() function   =   used with iterables
students = (("Squidward", "F",60),
            ("Sandy","A",33),
            ("Patrick","D",36),
            ("Spongebob","B",20),
            ("Mr. Krabs", "C",78))

grade = lambda grades:grades[1]
sorted_students = sorted(students, key=grade)

for i in sorted_students:
    print(i)