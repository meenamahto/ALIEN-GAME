
from random import randint

s=10
def report(s):
  if s>8:
    print("bahot maro...")
  elif s>5:
    print("aur maro...")
  elif s>3:
    print("thoda aur maro....")
  elif s>0:
    print(" bas thoda aur maro...")
  else:
    print("mar gya sala...ha ha ha....")
def fight(s):
  while s>0:
    r=input("""choise the move
              1 hit
              2 attack
              3 run
              4 fight

enter any choice : """)
    b=randint(0,s)
    s=s-b
    if r=="hit" or r=="attack":
      print("random stamina=",b)
      print("remaining stamina=",s)
      report(s)
    elif r=="fight":
      print("random stamina=",b)
      print("remaining stamina=",s)
      print("lado aur maro....")
    elif r=="run":
      print("random stamina=",b)
      print("remaining stamina=",s)
      print("bhag ke kha jayega khel...")
    else:
      return True
alive=fight(s)
if s==True:
  print(" not win")
else:
  print("you win")



