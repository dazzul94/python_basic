# #!/usr/bin/env python3      
import sys

print("Output: /lyrics/2002.txt")
print()

input_file = sys.argv[1]

# 가급적이면 with문을 써라 close안해도 되기 때문
with open(input_file, 'r', newline='') as filereader:
    for row in filereader:
        print("{}".format(row.strip()))

# python openTxt2.py lyrics/2002.txt