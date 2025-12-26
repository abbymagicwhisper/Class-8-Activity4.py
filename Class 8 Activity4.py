a = 15 #km/h
b = 20 #km/h
c = 30 #km/h

avg = (a + b + c)/3
print("The average speed of the cyclists are", avg)

if a < avg and b > avg and c > avg:
    print("The cyclist number 1 is slower than the average speed")
elif a < avg and b < avg and c > avg:
    print("The cyclist number 1 & 2 are slower than the average speed")
elif a < avg and b < avg and c < avg:
    print("All the cyclists are slower than the average speed")
elif a > avg and b < avg and c > avg:
    print("The cyclist number 2 is slower than the average speed")
elif a > avg and b < avg and c < avg:
    print("The cyclist number 2 & 3 are slower than the average speed")
elif a > avg and b > avg and c < avg:
    print("The cyclist number 3 is slower than the average speed")
elif a < avg and b > avg and c < avg:
    print("The cyclist number 1 & 3 are slower than the average speed")
else:
    print("An unexpected error has occurred")