import time
def bubble_sort  (data, drawData,):
    for _ in range(len(data)-1):
        for j in range(len(data)-1):
            if data[j]>data[j+1]:
                temp = data[j]
                data[j] =data[j+1]
                data[j+1]=temp

            drawData(data, ["purple" if x==j or x==j+1 else 'black'for x in range(len(data))] )
            time.sleep(0.2)
    drawData(data, ['purple' for x in range(len(data))])