
#  public  , private and protected
'''
class A:                # x is public....
    def call(self,x):
        self.x=x
        print("X is ",self.x)

a=A()
a.call(23)
print(a.x)
'''
print()
'''
class A:                   # x is private....
    def call(self,x):      #  denoted by  __
        self.__x=x
        print("X is ",self.__x)

a=A()
a.call(23)

'''
print()
'''
class A:                   # private in function....
    def __call(self,x):      #  denoted by  __
        self.__x=x
        print("X is ",self.__x)

a=A()
a.call(23)

'''
print()
'''
class A:                    # 
    def __call(self):
        print("x is ",self.x)
    def hello(self,x):
        self.x=x
        print(self.x+self.x)
        A.__call(self)
a=A()
a.hello(23)
'''
class A:               # this is private .......
    def call(self,x):   # denoted by single _ ( underscore)
        self._x=x
        print("X is ", self._x)
    
a=A()
a.call(12)






















