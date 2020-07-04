import random

def primary():
  # print("Keep it logically awesome.")

  f = open("quotes_appended.txt", "w+")
  #quotes = f.readlines()
  for i in range(10):
    f.write("Appended line %d\r" %(i+1))
  f.close()

 # last = len(quotes)-1
 # rnd = random.randint(0,last)
 # rnd2 = random.randint(0,last)
 # print(quotes[rnd] + quotes[rnd2])
  

if __name__== "__main__":
  primary()
