strength = [1,3,1,2]

length = len(strength)
#print(min(strength[1:2]) * sum(strength[1:2]))
result = 0
for i in range(length):
    j = 0
    while ((j < length)):
        print('j = ' + str(j))
        print('i = ' + str(i+1))
        end = i + 1
        if(j < end):
            result = result + min(strength[j:end]) * sum(strength[j:end])
            print(min(strength[j:end]) * sum(strength[j:end]))
        else:
            break
        j += 1

print(result)
