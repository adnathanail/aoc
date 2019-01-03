inputstring = "yzbqklnj"
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
