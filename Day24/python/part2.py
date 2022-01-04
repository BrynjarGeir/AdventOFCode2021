# And if we play these out we should get something like
# input[4] = input[3] + 3
# input[7] = input[6] - 6
# input[9] = input[8] + 5
# input[11] = input[10] + 2
# input[12] = input[1] + 7
# input[13] = input[0] - 7
# input[5] = input[2] - 4

# This somehow should give us the answer for all the categories
# So rule 1 would, in my mind mean
# 4 could be 9 but then 3 would be 6
# 6 could be 9 but then 7 would be 3
# 9 could be 9 but 8 would be 4
# 11 could be 9 but 10 would be 7
# 12 could be 9 but then 1 would be 2
# 0 could be 9 but then 13 would be 2
# 2 could be 9 but 5 would be 5
# So the highest possible would be something like 92969593497992
# Ok so I didn't really see that but apparently that works and the number above is the right one so thanks again dphilipson

# Just for the sake of tradition I'll but this in another file. I'm going to do the exact same thing but now I'll always pick
# the lowest possible number. I'll actually order the above a bit before I start, just to make it easier for me.
# [0] = [13] + 7
# [1] = [12] - 7
# [2] = [5] + 4
# [3] = [4] - 3
# [4] = [3] + 3
# [5] = [2] - 4
# [6] = [7] + 6
# [7] = [6] - 6
# [8] = [9] - 5
# [9] = [8] + 5
# [10] = [11] - 2
# [11] = [10] + 2
# [12] = [1] + 7
# [13] = [0] - 7

# So using the above we would get something like 81514171161381

# Thanks a third time to dphilipson
