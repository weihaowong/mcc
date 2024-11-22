with open('word.txt','r') as wordfile:
    d = open('output.txt','w')
    d.write('')
    data = wordfile.read().split('\n')
    nextline = False
    for line in data:
        d = open("output.txt", "a")
        if nextline:
            nextline = False
            num = int(line)
            print(f'num is {num}')
            ff = num % (10**9+7)
            d.write(f'{ff}')
            d.write('\n')
            continue
        if len(line) == 1 and line == '1':
            nextline = True
            continue
        elif ' ' not in line or len(line)==1:
            continue
        orbs = line.split(' ')
        orbs = [int(orb) for orb in orbs]
        orbs = sorted(orbs, reverse=True)
        while len(orbs) > 1:
            y = orbs[0]*2
            x = orbs[1]
            s = x + y
            orbs = orbs[1:]
            orbs[0] = s
            final = orbs[0] % (10**9+7)
        d.write(f'{final}')
        d.write('\n')
