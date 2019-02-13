import Funciones as fun

F = 'F-G-G'
R1 = 'F-G+F+G-F'
R2 = 'GG'
teta = 120
inc = 20

for i in range(5):
 F = fun.GenFractal(F, R1, R2)

print(F)

fun.GrafFractal(F, teta, inc)


