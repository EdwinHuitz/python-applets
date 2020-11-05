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
#7
def reverseUpcaseString(x):
   ans = x.upper()
   return ans[::-1]
#8
def removeEnds(x):
   if len(x) < 3:
      return ''
   else:
      return x[1:-1]
#9
def charCount(x):
   ans={}
   for i in x:
      n,ans[i]=0,0
      while n < len(x):
         if i == x[n]:
            ans[i]+=1
         n+=1
   return ans
#10
def formatWithPadding(x,y,z):
   diff,i,ans = z-len(str(x)),0,''
   if diff > 0:
      while i < diff:
         ans+=y
         i+=1
      ans+=str(x)
      return ans
   else:
      return str(x)
#11
def isPalindrome(x):
   orig = x.replace(' ','').lower()
   rev=orig[::-1]
   if orig == rev:
      return True
   else: return False
#12
def hammingDistance(x,y):
   i,ans=0,0
   while i < len(x):
      if x[i] != y[i]:
         ans+=1
      i+=1
   return ans
#13
def mumble(x):
   n,ans=1,''
   for i in x:
      a=0
      while a < n:
         ans+=str(i)
         a+=1
      ans+='-'
      n+=1
   return ans[0:-1]
#14
def fromPairs(x):
   ans={}
   for i in x:
      ans[i[0]]=i[1]
   return ans
#15
def mergeObjects(*args):
   ans={}
   for dic in args:
      for key in dic:
         ans[key]=dic[key]
   if len(ans) == 1:
      return {}
   return ans
#16
def findHighestPriced(x):
   vals,n=[],0
   while n<len(x):
      vals.append(x[n]['price'])
      n+=1
   vals.sort(reverse=True)
   for i in x:
      if i['price'] == vals[0]:
         break
   return i
#17
def mapArray(x,y):
   ans,n=[],0
   for i in x:
      ans.append(y(i,n))
      n+=1
   return ans
#18
def reduceArray(x,y,z):
   t,n=z,0
   for i in x:
      t=y(t,i,n)
      n+=1
   return t
#19
def flatten(x):
   ans=[]
   def flat(a):
      for b in a:
         if isinstance(b,list):
            flat(b)
         else:
            ans.append(b)
   for y in x:
      if isinstance(y,list):
         flat(y)
      else:
         ans.append(y)
   return ans
#20
def isPrime(x):
   if x%1 != 0 or x == 1:
      return False
   elif x < 4:
      return True
   elif x%2 != 0 and x%3 != 0:
      return True
   else:
      return False
#21
#def primeFactors(x):
#22
def intersection(x,y):
   a,b,ans=x,y,[]
   for first in a:
      num=0
      for second in b:
         if first == second:
            ans.append(first)
            b.pop(num)
         num+=1
   return ans
#23
def balancedBrackets(x):
   i,ans,half=1,False,round((len(x)/2))
   if len(x)%2 != 0:
      return ans
   for a in x:
      b=str(a)
      if i <= half:
         if b == '{' and str(x[-i]) == '}':
            ans=True
         elif b == '[' and str(x[-i]) == ']':
            ans=True
         elif b == '(' and str(x[-i]) == ')':
            ans=True
         i+=1
   return ans
#24
def isWinningTicket(x):
   for i in x:
      b,num=0,0
      while b<len(i[0]):
         if ord(i[0][b]) == i[1]:
            num=1
         b+=1
      if num == 0:return False
      else:return True
#25
def getNumForIP(x):
   num,ans,a=1,0,x.split('.')
   while num<len(a)+1:
      ans+=int(a[-num])*(256**(num-1))
      num+=1
   return ans
#26
def toCamelCase(x):
   num,lis,ans=0,x,''
   if lis.find('-')>=1:
      lis=lis.split('-')
   else:
      lis=lis.split('_')
   for i in lis:
      if num==0:pass
      else:
         lis[num]=i.replace(i[0],i[0].upper())
      num+=1
   return ans.join(lis)