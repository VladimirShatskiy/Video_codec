import re

data = '4444 BM-6)\n, 4444 BM-6\n'

for item in re.findall(r'\d+', data):
    if len(item) == 4:
        strt = data.find(item)
        ret_str = data[strt:strt+9]
        break

