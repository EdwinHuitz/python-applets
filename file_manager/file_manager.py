from shutil import *
import os

def checkIt(x):
   inputN=str(x).replace('//','/')
   if os.path.exists(inputN):return(True)
   else:return(False)

class files():
   def createIt(self):
      if checkIt(self)==False:
         open(str(self),mode='x',encoding='utf-8')
         return(True)
      else:return(False)

   def renameIt(self,newN):
      if checkIt(self)==True:
         os.rename(str(self),str(newN))
         return(True)
      else:return(False)

   def moveIt(self,newD):
      if checkIt(self)==True:
         move(str(self),str(newD))
         return(True)
      else:return(False)

   def deleteIt(self):
      if checkIt(self)==True:
         os.remove(str(self))
         return(True)
      else:return(False)

class folders():
   def createIt(self):
      if checkIt(self)==False:
         os.mkdir(str(self))
         return(True)
      else:return(False)

   def renameIt(self,newN):
      if checkIt(self)==True:
         os.rename(str(self),str(newN))
         return(True)
      else:return(False)

   def moveIt(self,newD):
      if checkIt(self)==True:
         move(str(self),str(newD))
         return(True)
      else:return(False)

   def deleteIt(self):
      if checkIt(self)==True:
         os.rmdir(str(self))
         return(True)
      else:return(False)

#print(checkIt('a/b/c'))

#creates a file
#r=read,a=append,w=write,x=create. Add + to the end to enable reading and writing permissions
#f = open('a.txt',mode='x',encoding='utf-8')

#renames file/folder if the destination doesn't exist
#move('a.txt','f2/')

#deletes file
#os.remove('a.txt')

#checks for existing file/folder
#if os.path.exists('aa.txt'):print('yes')
#else:print('no')