# lambda function   =   function written in 1 line using lambda keyword
#                       accepts any number of arguments, but only has one expression.
#                       (think of it as a shortcut)

# lambda parameters:expression

double = lambda x: x * 2
multiply = lambda x, y: x * y
add = lambda x, y, z: x + y + z
full_name = lambda first_name, last_name: first_name+" "+last_name
age_check = lambda age: True if age >= 18 else False

print(double(3))
print(multiply(3,5))
print(add(3,88,65))
print(age_check(18))