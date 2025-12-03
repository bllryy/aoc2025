with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

digits = 12 # jus change to 12 looooool 
total = 0

for line in lines:
    lastpos = 0
    linenum = ''

    for d in range(digits):
        maxnum = '0'
        maxpos = lastpos

        # Remaining digits to pick = digits - d
        # So we can only search up to index len(line) - (digits - d)
        limit = len(line) - (digits - d) + 1
        for pos in range(lastpos, limit):
            if line[pos] > maxnum:
                maxnum = line[pos]
                maxpos = pos

        linenum += maxnum
        lastpos = maxpos + 1

    total += int(linenum)

print(total)
