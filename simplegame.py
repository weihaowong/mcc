with open('word.txt','r') as wordfile:
    data = wordfile.read()
    data = data.split('\n')
    data = data[1:]
    global coords
    coords = []
    for e in data:
        e = e.split(' ')
        coord = [int(e[0]), int(e[1])]
        coords.append(coord)

sumcoord = [sum(coord) for coord in coords]
global x, y, priorities
priorities = list(sorted(enumerate(sumcoord), key=lambda x: x[1]))
x = 0
y = 0

while len(priorities) != 0:
    def evirir():
        global x, y, coords, priorities
        maxobject = priorities[-1]
        maxindex = (maxobject)[0]
        x += coords[maxindex][0]
        priorities = priorities[:-1]

    def rhae():
        global x, y, coords, priorities
        maxobject = priorities[-1]
        maxindex = (maxobject)[0]
        y += coords[maxindex][1]
        priorities = priorities[:-1]

    evirir()
    rhae()


print(x-y)
