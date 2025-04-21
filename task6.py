import math

N, K, M = map(int, input().split())
sessions = math.ceil(2 * N / K)
total_time = sessions * M

print(total_time)