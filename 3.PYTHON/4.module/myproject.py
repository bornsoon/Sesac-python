#import mymodule
#from mymodule import greet, greet_kr  # module. 앞에 안붙여도 됨
from mymodule import *  # 복수의 모듈을 불러올 때 중복에 주의!!

greeting = greet("SESAC")
print(greeting)

greeting = greet_kr("John")
print(greeting)