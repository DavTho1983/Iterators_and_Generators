def Reverse(data) :
    for index in range(len(data) - 1, -1, -1) : #start at len -1, stop at -1, take step -1
        yield data[index]


def Main() :
    rev = Reverse('Drapsicle')
    for char in rev :
        print(char)

    data = 'Drapsicle'
    print(list(data[i] for i in range(len(data) -1, -1, -1)))

if __name__ == '__main__' :
    Main()
