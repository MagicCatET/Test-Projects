print("Which file would you like to run")
cat = int(input("1.Hello World 2.Mad Lib 3.Username: "))
if cat == 1:
  exec(open('Hello World.py').read()) 
if cat == 2:
  exec(open('Mad Lib.py').read()) 
if cat == 3:
  exec(open('Username.py').read()) 