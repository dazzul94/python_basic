# 자료 보기쉽게 print   

complicated = ['spam', (1, 2, 3), ('ham','egg',('ab','cd',('abc','def')))]
complicated = complicated * 3
print(complicated)

import pprint
pprint.pprint(complicated)