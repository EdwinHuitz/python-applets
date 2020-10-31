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
