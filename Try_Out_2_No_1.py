list_awal = [[1,2,3],
             [4,5,6],
             [7,8,9]]

def counterClockwise (a):
    proses = list(map( list, zip(*list_awal)))[::-1]
    
    for i in range(3):
        print(proses[i])

(counterClockwise(list_awal))

