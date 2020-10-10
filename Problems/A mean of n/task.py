import statistics
iterate = int(input())

count = []

while len(count) < iterate:
    n = int(input())
    count.append(n)

print(float(statistics.mean(count)))
