file = open('input')
data = [int(i) for i in file.readlines()]

# track n of increases
increased=0

# loop through list indices
for i in range(0,len(data)-3):
    # calculate sums for series of 3 and next series
    sum1 = sum(data[i:i+3])
    sum2 = sum(data[i+1:i+4])
    # compare, increment increased if increase
    if sum1<sum2:
        increased = increased+1
print(increased)