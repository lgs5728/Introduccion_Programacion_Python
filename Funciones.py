import turtle

# https://en.wikipedia.org/wiki/L-system


def GenFractal(F, R1, R2):

 lf = len(F)
 FN = ''

 for i in range(lf):
    if F[i] == 'F':
       FN = FN + R1
    if F[i] == 'G':
       FN = FN + R2
    if F[i] == '+':
       FN = FN + F[i]
    if F[i] == '-':
       FN = FN + F[i]

 F = FN 
 return F

def GrafFractal(F, teta, inc):
 FR = F

 nl = len(FR)
 print(nl)

 turtle.up()
 turtle.goto(-200,-200)
 turtle.down()

 for i in range(nl):
  if FR[i] in {'F', 'G'}:
    turtle.forward(inc)
  elif FR[i] == '+':
    turtle.right(teta)
  elif FR[i] == '-':
    turtle.left(teta)

 turtle.mainloop()


