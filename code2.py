class student:
  def __init__(self,name,id,age):
    self.name = name
    self.id = id
    self.age = age

  def display(self):
    print(self.name,self.id,self.age)

std1 = student("sajib",53,18)
std2 = student("rakib",54,22)
std3 = student("emarn",55,21)
std4 = student("anik",56,23)

std1.display()
std2.display()
std3.display()
std4.display()
