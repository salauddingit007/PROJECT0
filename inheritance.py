#parent class ,superclass, base class
#child class,sub class,derive class

class phone:
    def call(self):
        print("you can call")

    def message (self):
        print("you can message")

class samsung (phone):
    def photo (self):
        print("you can take photo")

s=samsung()
s.message()
s.call()
s.photo()
print(issubclass(phone,samsung))