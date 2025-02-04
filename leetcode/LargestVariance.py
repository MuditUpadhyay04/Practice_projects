## Only working for a specific test case...
##
## --Breaks when all have frequency 1
## --Breaks when abbbcc

string = 'aabb'
# a_start = (string.find('a')) + 1
# a_end = (string.rfind('a')) + 1
# counter1 = string.count('a')

# b_start = (string.find('b')) + 1
# b_end = (string.rfind('b')) + 1
# counter2 = string.count('b')
freqList = []
for char in string:
    freqList.append(char)
#print(freqList)
result = 0
freqMap = {}
for char in freqList:
    if char not in freqMap:
        freqMap[char] = 1
    else:
        freqMap[char] += 1
print(freqMap)

freqSet = set(freqList)
#print(freqSet)

freqEle = freqList[0]

for char in freqSet:
    if freqMap.get(char) > freqMap.get(freqEle):
        freqEle = char

freqLow = freqList[0]
for char in freqSet:
    if freqMap.get(char) < freqMap.get(freqLow):
        freqLow = char
print(freqLow)
print(freqEle)
if(freqEle == freqLow):
    print("I am dumb")
if(freqEle != freqLow):
    result = freqMap.get(freqEle) - 1

# result = (2*freqList.count(freqList[0]) - string.rfind(freqList[0]) + string.find(freqList[0]) - 1)
# #print(result)

# for char in freqSet:
#     temp = (2*freqList.count(char) - string.rfind(char) + string.find(char) - 1)
#     if(temp > result):
#         result = temp
print(result)

