inputstring = "yzbqklnj"
import hashlib
index = 0
running = True
while running:
    if not index%100000:
        print(index)
    m = hashlib.md5()
    m.update((inputstring + str(index)).encode('utf-8'))
    if m.hexdigest()[:6] == '000000':
        running = False
        print(index)
    index += 1
