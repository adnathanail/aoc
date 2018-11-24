from aocd import get_data
inp = int(get_data(day=3))
x = 1
while (x+2)**2 < inp:
    x += 2
horiz = vert = int((x-1)/2) + 1
if inp == x**2:
    pass
elif inp <= (x**2 + x):
    vert = abs( (x+1)/2 - (inp - x**2) )
elif inp > (x**2 + x) and inp <= ( x**2 + 2*x + 2):
    horiz = abs( (x+3)/2 - (inp - (x**2 + x) ) )
elif inp > (x**2 + 2*x + 2) and inp <= ( x**2 + 3*x + 2 ):
    vert = abs( (x+1)/2 - (inp - (x**2 + 2*x + 2) ) )
elif inp > (x**2 + 3*x + 2 ):
    horiz = abs( (x+3)/2 - (inp - (x**2 + 3*x + 2) ) )
print(horiz+vert)