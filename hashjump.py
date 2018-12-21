#Sujata Patil
import sys
limit=10000
hashList = [None]*limit

class Node:
    def __init__(self,index,data):
        self.index=index
        self.data=data

def hasher(s):
    result=0
    for c in s:
        result+=ord(c)
    result%=limit
    return result

def placeNode(arr,ind,node):
    num=ind
    found= False
    while(not found):
        if(arr[num]==None):
            arr[num]=node
            found=True
        else:
            num  += 1
        if(num >= limit):
            num = 0

def deleteNode(arr,ind,key):
    num=ind
    found1= False
    while(not found1):
       if(arr[num]== None or arr[num].index != key):
          num += 1
       else:
          arr[num]=None
          found = True
          return
       if(num >= limit):
          num = 0
       if(num == ind):
          return "End of limit"

def searchArray(arr,hashedind,unhash):
    found=False
    num=hashedind
    while(not found):
        if(arr[num]==None):
            return "not found"
        if(arr[num].index == unhash):
            return arr[num].data
        else:
            num +=1
        if(num >= limit):
            num=0
        if(num == hashedind):
            return "End of limit"

if(len(sys.argv)!=5):
    print("Incorrect number of arguments")
    exit()

inputFile = sys.argv[1]
readFile = sys.argv[3]
outputFile = sys.argv[4]
option =sys.argv[2]
print("input file name:" + inputFile)
print("read file name:" + readFile)
print("output file name:" + outputFile)
print("option:" + option)


f= open(inputFile,"r")
for line in f:
    newLine=line.strip().split(":")
    hashIndex = hasher(newLine[0])
    newNode = Node(newLine[0],newLine[1])
    placeNode(hashList,hashIndex,newNode)
f.close()


if option == 'search':
   f=open(readFile,"r")
   f1= open(outputFile,"a")
   for line in f:
      newLine=line.strip()
      hashIndex = hasher(newLine)
      f1.write(newLine + ":" + searchArray(hashList,hashIndex,newLine)+'\n')
   f1.close()
   f.close()

if option == 'delete':
   f=open(readFile,"r")
   f1=open(outputFile,"a")
   for line in f:
      newLine=line.strip()
      hashIndex = hasher(newLine)
      deleteNode(hashList,hashIndex,newLine)
   for i in range(0,limit):
      if(hashList[i] != None):
          f1.write(hashList[i].index + ":" + hashList[i].data+"\n")
   f.close()
   f1.close()
