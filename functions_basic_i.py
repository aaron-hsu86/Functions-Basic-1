#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
# Prediction: 
# 5

#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
# Prediction: 
# Error, function not defined

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
# Prediction: 
# 5

#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
# Prediction: 
# 5

#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
# Prediction:
# 5
# None - function did not return anything to x

#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
# Prediction:
# 3 - printed from add(1,2)
# 5 - printed from add(2,3)
# TypeError - no value is returned from each function, and you can't add None + None

#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
# Prediction: 
# 25 - since the concatenating strings puts them into one string, string 2 + string 5 = 25

#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
# Prediction: 
# 100 - print b = 100 from the function
# 10 - value of 10 is returned, so this is printed

#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
# Prediction:
# 7 - 2 is less than 3, so 7 is returned and printed
# 14 - 5 is greater than 3, so 14 is returned and printed
# 21 - returned values are Numbers, 7 + 14 = 21 so it prints 21

#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
# Predictions: 
# 8

#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
# Prediction:
# 500
# 500 - b still has the value of 500 since function hasn't been declared yet
# 300 - function called, value of b is changed to 300, print called from inside function
# 300 - b has the new value of 300, so this is printed

#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
# Prediction:
# 500 - printing declared value of b = 500
# 500 - function hasn't been called, so b is still 500
# 300 - function called, b value changed to 300, printed new value of b
# 500 - function has a return call, so the new value of b is returned from the function, but the return also returns to the previous state where b = 500, so b on the Global scale is not affected from the function changes

#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
# Prediction:
# 500 - printing declared value of b = 500
# 500 - function hasn't been called, so b is still 500
# 300 - function called, b value changed to 300, printed new value of b
# 300 - b was changed to the returned value of the function, which was 300, so 300 is printed

#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
# Prediction:
# 1 
# 3 - bar() function is called inside foo() function, resulting in this being printed
# 2 - printed from foo() function after bar() function completes

#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
# Prediction:
# 1 - foo() prints this value
# 3 - bar() prints this value
# 5 - x is declared to equal bar(), which returned 5, so 5 is printed
# 10 - y is declared to equal foo(), which returned 10, so 10 is printed