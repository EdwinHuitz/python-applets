import pytest
import math
import answers
from answers import *
# import challenges
# from challenges import *

parametrize = pytest.mark.parametrize
skip = pytest.mark.skipif
ans = answers
#! remember to change ans from answers to challenges
@parametrize('ans',['hello'])
@skip('sayHello' not in dir(ans),reason="This function has yet to be declared")
def test_00(ans):
   assert sayHello() == ans

@parametrize('p1,ans',[(-1,0),(2,3),(5,6)])
@skip('addOne' not in dir(ans),reason="This function has yet to be declared")
def test_01(p1,ans):
   assert addOne(p1) == ans

@parametrize('p1,p2,ans',[(1,1,2),(1,2,3),(-10,16,6),('Hello',5,'nan')])
@skip('addTwoNumbers' not in dir(ans),reason="This function has yet to be declared")
def test_02(p1,p2,ans):
   assert addTwoNumbers(p1,p2) == ans

@parametrize('p1,ans',[([10],10),([2,10,-5],7),([5,10],15),([],0)])
@skip('sumNumbers' not in dir(ans),reason="This function has yet to be declared")
def test_03(p1,ans):
   assert sumNumbers(p1) == ans

@parametrize('p1,ans',[((2,7,0),9),((0,7,-1),6)])
@skip('addList' not in dir(ans),reason="This function has yet to be declared")
def test_04(p1,ans):
   assert addList(p1[0],p1[1],p1[2]) == ans
   assert addList() == 0

@parametrize('p1,p2,ans',[(4,0,math.inf),(10,2,0),(10.5,3,1.5)])
@skip('computeRemainder' not in dir(ans),reason="This function has yet to be declared")
def test_05(p1,p2,ans):
   assert computeRemainder(p1,p2) == ans

@parametrize('p1,p2,ans',[(5,2,'First argument must be less than second'),(1,4,[1,2,3]),(1,1,[]),(-2,3,[-2,-1,0,1,2])])
@skip('ranges' not in dir(ans),reason="This function has yet to be declared")
def test_06(p1,p2,ans):
   assert ranges(p1,p2) == ans

@parametrize('p1,ans',[('SEI Rocks!','!SKCOR IES')])
@skip('reverseUpcaseString' not in dir(ans),reason="This function has yet to be declared")
def test_07(p1,ans):
   assert reverseUpcaseString(p1) == ans

@parametrize('p1,ans',[('a',''),('abc','b'),('123456789','2345678')])
@skip('removeEnds' not in dir(ans),reason="This function has yet to be declared")
def test_08(p1,ans):
   assert removeEnds(p1) == ans

@parametrize('p1,ans',[('hello',{ 'h': 1, 'e': 1, 'l': 2, 'o': 1 }),('Today is fantastic!',{ 'T': 1, 'o': 1, 'd': 1, 'a': 3, 'y': 1, ' ': 2, 'i': 2, 's': 2, 'f': 1, 'n': 1, 't': 2, 'c': 1, '!': 1 })])
@skip('charCount' not in dir(ans),reason="This function has yet to be declared")
def test_09(p1,ans):
   assert charCount(p1) == ans

@parametrize('p1,p2,p3,ans',[(1234,'*',3,'1234'),(123,'0',5,'00123'),(42,'*',10,'********42')])
@skip('formatWithPadding' not in dir(ans),reason="This function has yet to be declared")
def test_10(p1,p2,p3,ans):
   assert formatWithPadding(p1,p2,p3) == ans

@parametrize('p1,ans',[('',True),('A',True),('abc',False),('A nut for a jar of tuna',True)])
@skip('isPalindrome' not in dir(ans),reason="This function has yet to be declared")
def test_11(p1,ans):
   assert isPalindrome(p1) == ans

@parametrize('p1,p2,ans',[('abc','abc',0),('a1c','a2c',1),('!!!!','****',4)])
@skip('hammingDistance' not in dir(ans),reason="This function has yet to be declared")
def test_12(p1,p2,ans):
   assert hammingDistance(p1,p2) == ans

@parametrize('p1,ans',[('X','X'),('abc','a-bb-ccc'),('121','1-22-111'),('!A 2','!-AA-   -2222')])
@skip('mumble' not in dir(ans),reason="This function has yet to be declared")
def test_13(p1,ans):
   assert mumble(p1) == ans

@parametrize('p1,ans',[([['a', 1],['b', 2],['c', 3]],{'a': 1, 'b': 2, 'c': 3}),([["name", "Sam"], ["age", 24], ["name", "Sally"]],{ 'name': "Sally", 'age': 24 }),([["i", "like"], ["to", "eat"], ["banana", "chips"]],{ 'i': "like", 'to': "eat", "banana": "chips" })])
@skip('fromPairs' not in dir(ans),reason="This function has yet to be declared")
def test_14(p1,ans):
   assert fromPairs(p1) == ans

@parametrize('p1,p2,p3,ans',[({},{},{'a':1},{}),({'a':1,'b':2,'c':3},{'d':4},{},{'a':1,'b':2,'c':3,'d':4}),({'a':1,'b':2,'c':3},{'d':4},{'b':22,'d':44},{'a':1,'b':22,'c':3,'d':44})])
@skip('mergeObjects' not in dir(ans),reason="This function has yet to be declared")
def test_15(p1,p2,p3,ans):
   assert mergeObjects(p1,p2,p3) == ans

@parametrize('p1,ans',[([{'sku':'a1','price':25},{'sku':'b2','price':5},{'sku':'c3','price':50},{'sku':'d4','price':10}],{ 'sku': 'c3', 'price': 50 }),([{'sku':'a1','price':25},{'sku':'b2','price':25}],{'sku':'a1','price':25})])
@skip('findHighestPriced' not in dir(ans),reason="This function has yet to be declared")
def test_16(p1,ans):
   assert findHighestPriced(p1) == ans

@parametrize('p1,p2,ans',[([],lambda a,b:a,[]),([1,2,3],lambda a,b:a*2,[2,4,6]),(['rose','tulip','daisy'],lambda a,b:f'{b+1} - {a}',['1 - rose','2 - tulip','3 - daisy'])])
@skip('mapArray' not in dir(ans),reason="This function has yet to be declared")
def test_17(p1,p2,ans):
   assert mapArray(p1,p2) == ans

@parametrize('p1,p2,p3,ans',[([1,2,3],lambda a,b,c:a+b,0,6),([1,2,3],lambda a,b,c:a+b+c,0,9),([1,2,3,-4,-5],lambda a,b,c:a-b-c,0,-7)])
@skip('reduceArray' not in dir(ans),reason="This function has yet to be declared")
def test_18(p1,p2,p3,ans):
   assert reduceArray(p1,p2,p3) == ans

@parametrize('p1,ans',[([1,[2,3]],[1,2,3]),([1, [2, [3, [4]]], 1, 'a', ['b', 'c']],[1, 2, 3, 4, 1, 'a', 'b', 'c'])])
@skip('flatten' not in dir(ans),reason="This function has yet to be declared")
def test_19(p1,ans):
   assert flatten(p1) == ans

@parametrize('p1,ans',[(1,False),(3.1,False),(2,True),(3,True),(4,False),(29,True),(200,False)])
@skip('isPrime' not in dir(ans),reason="This function has yet to be declared")
def test_20(p1,ans):
   assert isPrime(p1) == ans

@parametrize('p1,ans',[(1,[]),(2,[2]),(3,[3]),(4,[2,2]),(18,[2,3,3]),(29,[29]),(105,[3,5,7]),(200,[2,2,2,5,5])])
@skip('primeFactors' not in dir(ans),reason="This function has yet to be declared")
def test_20(p1,ans):
   assert primeFactors(p1).sort() == ans

