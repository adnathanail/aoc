from aocd import get_data
import re

inp = get_data(day=9)
inp = re.sub('!.', '', inp)
print(sum([len(x)-2 for x in re.findall('<[^>]*>', inp)]))