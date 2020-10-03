def math(i1,sym,i2):
   ans=''
   if i1 == '':
      one=0.0
      
   else:
      one=float(i1)
   if i2 == '':
      two=0.0
   else:
      two=float(i2)
   def adding(a,b):
      return str(a+b)
   def subtracting(a,b):
      return str(a-b)
   def multiplying(a,b):
      return str(a*b)
   def dividing(a,b):
      if b == 0:
         return 'Error: Cannot divide by zero'
      return str(a/b)
   if sym == '+':
      ans=adding(one,two)
   elif sym == '-':
      ans=subtracting(one,two)
   elif sym == '*':
      ans=multiplying(one,two)
   elif sym == '/':
      ans=dividing(one,two)
   return ans