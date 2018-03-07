import string
import time
d=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
def count(a):
 o=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
 for i in a:
  o[d.index(i.upper())]+=1
 return o
def main():
 c=count(raw_input("word="))
 tim=time.time()
 file=open("dict/dictionary.txt","r+")
 l=file.read().replace("/r/n","")
 l=l.split()
 file.close()
 pos=[]
 for i in l:
  if count(i)==c:
   pos.append(i)
 if len(pos)>0:
  print "Possible matches:\n\n[+] "+string.join(pos,"\n[+] ")
 else:
  print "\nNothing found!"
 print "\nTask completed in "+str(time.time()-tim)+"s"
if __name__ == '__main__':
 main()
