#multiple variable
x,y,z = "sajib","rakib","habib"
print(x)
print(y)
print(z)

a=b=c = "Atta"
print(a)
print(b)
print(c)

name = ["Sajib","Rakib","Habib"]
x = name
y = name
z = name
print(x)
print(y)
print(z)
name = "SAjib"
dep = "CSE"
group = "Science"
print(name,dep,group)
print(name+dep+group)
name = "ATTA"
roll = 2122
print(name,roll)
name = 10
roll = 20
print(name+roll)

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
# DATA TYPE :
x = str("Hello World")
print(x);
x = int(20)
print(x)
x = float(20.5)
print(x)
x = complex(1j)
print(x)
x = list["apple", "banana", "cherry"]
print(x)
x = tuple(("apple", "banana", "cherry"))
print(x)
x = range(6)
print(x)
x = dict(name="John", age=36)
print(x)
x = set(("apple", "banana", "cherry"))
print(x)
x = frozenset(("apple", "banana", "cherry"))
print(x)
x = bool(5)
print(x)
x = bytes(5)
print(x)
x = bytearray(5)
print(x)
x = memoryview(bytes(5))
print(x)

x = 1    # int
y = 2.8  # float
z = 1j   # complex
print(x)
print(y)
print(z)
print(type(x))
print(type(y))
print(type(z))

x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

x = 35e3
y = 12E4
z = -87.7e100
print("New")
print(type(x))
print(type(y))
print(type(z))

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
#Complex NUmber
print("COMPLEX NU<MBER")
x = 3+5j
y = 5j
z = -5j


print(type(x))
print(type(y))
print(type(z))

print(x)
print(y)
print(z)

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

for x in "banana":
  print(x)

txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

txt = "The best things in life are free!"
print("expensive" not in txt)