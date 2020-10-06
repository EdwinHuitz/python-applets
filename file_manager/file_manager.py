from shutil import *
import os

def checkIt(x):
   inputN=str(x).replace('//','/')
   if os.path.exists(inputN):return(True)
   else:return(False)
   #return(True)

class files():
   def createIt(self):
      if checkIt(self)==False:
         open(str(self),mode='x',encoding='utf-8')
         return(True)
      else:return(False)

   def renameIt(self,newN):
      if checkIt(self)==True:
         num=self.rfind('/')
         newName=self[0:num+1]+newN
         os.rename(str(self),str(newName))
         return(True)
      else:return(False)

   def moveIt(self,newD):
      if checkIt(self)==True:
         num=self.rfind('/')
         end=len(self)
         newName=newD+self[num-1:end]
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
         num=self.rfind('/')
         newName=self[0:num+1]+newN
         os.rename(str(self),str(newName))
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

#print(files.moveIt('a/b/test/c/test.txt','123'))

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