import pytest
import math
import answers
from answers import *
#import challenges
#from challenges import *

@pytest.mark.parametrize('ans',['hello'])
def test_zero(ans):
   assert sayHello() == ans

@pytest.mark.parametrize('p1,ans',[(-1,0),(2,3),(5,6)])
def test_one(p1,ans):
   assert addOne(p1) == ans

@pytest.mark.parametrize('p1,p2,ans',[(1,1,2),(1,2,3),(-10,16,6),('Hello',5,'nan')])
def test_two(p1,p2,ans):
   assert addTwoNumbers(p1,p2) == ans

@pytest.mark.parametrize('p1,ans',[([10],10),([2,10,-5],7),([5,10],15),([],0)])
def test_three(p1,ans):
   assert sumNumbers(p1) == ans

@pytest.mark.parametrize('p1,ans',[((2,7,0),9),((0,7,-1),6)])
def test_four(p1,ans):
   assert addList(p1[0],p1[1],p1[2]) == ans
   assert addList() == 0

@pytest.mark.parametrize('p1,p2,ans',[(4,0,math.inf),(10,2,0),(10.5,3,1.5)])
def test_five(p1,p2,ans):
   assert computeRemainder(p1,p2) == ans

@pytest.mark.parametrize('p1,p2,ans',[(5,2,'First argument must be less than second'),(1,4,[1,2,3]),(1,1,[]),(-2,3,[-2,-1,0,1,2])])
def test_six(p1,p2,ans):
   assert ranges(p1,p2) == ans

@pytest.mark.parametrize('p1,ans',[('SEI Rocks!','!SKCOR IES')])
def test_seven(p1,ans):
   assert reverseUpcaseString(p1) == ans

@pytest.mark.parametrize('p1,ans',[('a',''),('abc','b'),('123456789','2345678')])
def test_eight(p1,ans):
   assert removeEnds(p1) == ans

@pytest.mark.parametrize('p1,ans',[('hello',{ 'h': 1, 'e': 1, 'l': 2, 'o': 1 }),('Today is fantastic!',{ 'T': 1, 'o': 1, 'd': 1, 'a': 3, 'y': 1, ' ': 2, 'i': 2, 's': 2, 'f': 1, 'n': 1, 't': 2, 'c': 1, '!': 1 })])
def test_nine(p1,ans):
   assert charCount(p1) == ans

@pytest.mark.parametrize('p1,p2,p3,ans',[(1234,'*',3,'1234'),(123,'0',5,'00123'),(42,'*',10,'********42')])
def test_ten(p1,p2,p3,ans):
   assert formatWithPadding(p1,p2,p3) == ans

@pytest.mark.parametrize('p1,ans',[('',True),('A',True),('abc',False),('A nut for a jar of tuna',True)])
def test_eleven(p1,ans):
   assert isPalindrome(p1) == ans

@pytest.mark.parametrize('p1,p2,ans',[('abc','abc',0),('a1c','a2c',1),('!!!!','****',4)])
def test_twelve(p1,p2,ans):
   assert hammingDistance(p1,p2) == ans

@pytest.mark.parametrize('p1,ans',[('X','X'),('abc','a-bb-ccc'),('121','1-22-111'),('!A 2','!-AA-   -2222')])
def test_thirteen(p1,ans):
   assert mumble(p1) == ans

@pytest.mark.parametrize('p1,ans',[([['a', 1],['b', 2],['c', 3]],{'a': 1, 'b': 2, 'c': 3}),([["name", "Sam"], ["age", 24], ["name", "Sally"]],{ 'name': "Sally", 'age': 24 }),([["i", "like"], ["to", "eat"], ["banana", "chips"]],{ 'i': "like", 'to': "eat", "banana": "chips" })])
def test_fourteen(p1,ans):
   assert fromPairs(p1) == ans
