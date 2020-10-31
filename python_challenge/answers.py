#0
def sayHello():
   return 'hello'
#1
def addOne(x):
   return x+1
#2
def addTwoNumbers(x,y):
   if isinstance(x,str) or isinstance(y,str):
      return 'nan'
   return x+y
#3
def sumNumbers(x):
   return sum(x)
#4
def addList(*args):
   if len(args) == 0:
      return 0
   else:
      ans=0
      for i in args:
         ans+=i
   return ans
#5
def computeRemainder(x,y):
   if y == 0:
      return float('inf')
   else:
      return x%y
#6
def ranges(x,y):
   if x>y:
      return 'First argument must be less than second'
   else:
      ans = []
      for i in range(x,y):
         ans.append(i)
      return ans