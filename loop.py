# While loop
# Incrementing
number = 25
while number <= 30:
    print(number)
    number += 1


# Decrementing
count = 10
while count >= 1:
    print("Number  is", count)
    count -= 1


# Break and continue statement
x = 100
while x <= 105:
    print(x)
    if x == 103:
        break
    x += 1

y = 34
while y < 40:
    y += 1
    if y == 37:
        continue
    print(y)

# For loop
for num in range(10):
    print(num)

for z in range(70, 80):
    print(z)

for w in range(100, 110, 4):
    print(w)

languages = ["Python, Java, Kotlin "]
for lang in languages:
    print(lang)
