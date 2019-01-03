from aocd import get_data
inputstring = get_data(day=4, year=2015)
import hashlib
index = 0
running = True
while running:
    m = hashlib.md5()
    m.update((inputstring + str(index)).encode('utf-8'))
    if m.hexdigest()[:5] == '00000':
        running = False
        print(index)
    index += 1
