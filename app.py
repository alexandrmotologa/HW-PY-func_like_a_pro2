import random

## producer
def produce():
    return [random.randint(1, 10) for i in range(5)]

## transformer
def transform(m):
    return [i/2 for i in m]

## consumer
def consume(m):
    for num in m:
        print(num)

#######################
n = produce()
n = transform(n)
consume(n)