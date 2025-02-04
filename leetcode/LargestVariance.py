string = 'aababbb'
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

freqMap = {}
for char in freqList:
    if char not in freqMap:
        freqMap[char] = 1
    else:
        freqMap[char] += 1
#print(freqMap)

freqSet = set(freqList)
#print(freqSet)

result = (2*freqList.count(freqList[0]) - string.rfind(freqList[0]) + string.find(freqList[0]) - 1)
#print(result)

for char in freqSet:
    temp = (2*freqList.count(char) - string.rfind(char) + string.find(char) - 1)
    if(temp > result):
        result = temp
print(result)

