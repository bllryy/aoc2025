"""
0 - 99
start 50
L  = turn to lower
R = turn to higher

when you go past the end it wraps 
left from 0 - 99
right 99 - 0

need - simulate the roatations in order and count how
how many times after a rotation the dial ends up at 0
"""

def main():
    pos = 50
    count = 0

    with open("input.txt", "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            direction = line[0]
            distance = int(line[1:])

            step = -1 if direction == 'L' else 1

            # simulate each single click
            for _ in range(distance):
                pos = (pos + step) % 100
                if pos == 0:
                    count += 1

    print(count)

main()

