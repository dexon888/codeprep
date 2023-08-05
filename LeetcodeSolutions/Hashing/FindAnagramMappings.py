def findAnagramMappings(a, b):
    map = {}
    for index, num in enumerate(b):
        map[num] = index
    return [map[i] for i in a]

a = [12, 28, 46, 32, 50]
b = [50, 12, 32, 46, 28]
print(findAnagramMappings(a,b))