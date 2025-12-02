"""
What do you get if you add up all of the invalid IDs?
two problems parse and check if x + x
11-22 has two invalid IDs, 11 and 22
Must be a even len to count as a double
using 2 loops one ahead of the other 

What do you get if you add up all of the invalid IDs using these new rules?
"""

f = open("input.txt","r")

totalSum = 0

for line in f:
    pairs = line.split(",")
    
    for pair in pairs:
        ID1,ID2 = pair.split("-")
        
        for num in range(int(ID1),int(ID2)+1):
            num = str(num)
            
            for chunkSize in range(1,len(num)):
                chunk = num[0:chunkSize]
                newNum = num.replace(chunk,"")
                if(newNum == ""):
                    totalSum = totalSum + int(num)
                    break

print(totalSum)
