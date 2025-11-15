class animal:
  def speak(self):
    print("i am an animal")

class dog(animal):
  def speak(self):
    print("i bark")

obj=animal()
book=dog()
obj.speak()
book.speak()
