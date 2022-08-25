print("Hello Python")

print(10//3)

print(2**3)

# types
print(type("Hello World"))
print(type(10))
print(type(10.30))

# String

print("""It's a computer programming language""")
print("It's a computer programming language")
print('''It's a computer programming language''')


# type converting
print(3.76, int(3.76))
print(3, float(3))
print(-3.98, float(-3.98))
print("320", int("320"))
# print(int("20pens"))
print(str(20))
print(str(20.45))
print(type(str(20.45)))


# variable
text = "Some text here"
print(text)

m = 40
n = 20

pi = 3.1416

print(m+n)
print(m-n)

print(type(pi))

abc = 10
Abc = "text"
aBc = 5.80
print(abc, Abc, aBc)

print(len(Abc))


# inputs
#
# n = input("Enter the name: ")
# print("Hello", n)

str_seconds = input("Enter the number of seconds: ")
total_secs = int(str_seconds)

hours = total_secs // 3600
secs_still_remaining = total_secs % 3600
minutes = secs_still_remaining // 60
secs_finally_remaining = secs_still_remaining % 60

print("Hours: ", hours, "mins: ", minutes, "secs: ", secs_finally_remaining)