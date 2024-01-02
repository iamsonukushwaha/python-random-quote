import random

def write_quotes():
   new_quotes = [
        "To be or not to be, that is the question.",
        "All that glitters is not gold.",
        "The only thing we have to fear is fear itself.",
        "In three words I can sum up everything I've learned about life: it goes on."
   ]

   with open("quotes.txt", "a") as f:
      for quote in new_quotes:
         f.write(quote + "\n")
   

def primary():
   #print("Keep it logically awesome.")

   f = open("quotes.txt")
   quotes = f.readlines()
   f.close()
   
   last = len(quotes) - 1
   # print(last)
   rnd = random.randint(0, last)
   # print(quotes[rnd])
   print(quotes[rnd].strip())
   # for i in quotes:
   #    print(i.strip())
      

if __name__== "__main__":

   write_quotes()
#   primary()
