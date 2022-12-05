f = open('/Users/trent.templet/Dev/WebApps/ZTM/Advent-of-Code-2022/Day 1/index.txt', 'r')
input_ml = f.read()

example = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""

# data = example.splitlines()
data = input_ml.splitlines( )

#creating dictionary

list1 = {0: 0}
elf = 0

for e, i in enumerate(data):
    if i == '':
        elf += 1 
        list1[elf] = 0
    else:
        list1[elf] = list1[elf]+int(i)

most1,most2,most3 = 0,0,0

for calories,vangaurd in list1.items():
    if vangaurd > most1:
        most3 = most2
        most2 = most1
        most1 = vangaurd
    elif vangaurd >= most2:
        most3 = most2
        most2 = vangaurd
    elif vangaurd >= most3:
        most3 = vangaurd

sum = most1 + most2 + most3 

print(f'Day 1 Solution: {most1}')
print(f'Day 1 Solution: {sum}')