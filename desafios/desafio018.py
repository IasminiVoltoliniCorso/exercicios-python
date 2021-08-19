import math
n = float(input('Digite um ângulo: '))
s = math.sin(math.radians(n))
c = math.cos(math.radians(n))
t = math.tan(math.radians(n))
print('O seno do ângulo {} é {:.2f}'.format(n, s))
print('O cosseno do ângulo {} é {:.2f}'.format(n, c))
print('A tangente do ângulo {} é {:.2f}'.format(n, t))



