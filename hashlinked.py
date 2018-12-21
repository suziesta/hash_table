#Sujata Patil
import sys
limit=10000
hashList = [None]*limit

class Node:
    def __init__(self,key,data):
        self.key=key
        self.data=data
        self.next=None

def hasher(s):
    result=0
    for c in s:
        result+=ord(c)
    result%=limit
    return result

def placeNode(arr,ind,node):
    num=ind
    arrnode=arr[ind]
    if arrnode is None:
        arr[num]=node
        return
    else:
        while arrnode is not None:
            prev=arrnode
            arrnode=arrnode.next
        prev.next= node

def deleteNode(arr,ind,key2):
    num=ind
    node1=arr[num]
    prev = None
    while(node1 != None and node1.key != key2):
        prev=node1
        node1=node1.next
    if(node1 == None):
        return
    else:
        if (prev == None):
            arr[num]=node1.next
        else:
            prev.next=node1.next
        return

def searchArray(arr,ind,key1):
    num=ind
    node1=arr[num]
    while(node1 != None and node1.key != key1):
        node1=node1.next
    if node1 is None:
        return None
    else:
        return node1.data

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
  f1=open(readFile,"r")
  f2= open(outputFile,"a")
  for line in f1:
      newLine=line.strip()
      hashIndex = hasher(newLine)
      f2.write(newLine + ":" + searchArray(hashList,hashIndex,newLine)+'\n')
  f2.close()
  f1.close()

if option == 'delete':
  f1=open(readFile,"r")
  f2= open(outputFile,"a")
  for line in f1:
      newLine=line.strip()
      hashIndex = hasher(newLine)
      deleteNode(hashList,hashIndex,newLine)
  for i in range(limit):
        ll=hashList[i]
        while(ll != None):
           f2.write(ll.key+":"+ll.data+"\n")
           ll=ll.next
  f2.close()
  f1.close()
