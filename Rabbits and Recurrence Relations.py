# Rabbits and Recurrence Relations


n = 5  # months
k = 3  # rabbits per month

t = 1  # total
y = 1  # young rabbits
o = 0  # old rabbits

#  first month: there are two rabbits

#  second month: young rabbits become adults
o = y
y = 0

n -= 2

#  From the third month
i = 0
while i < n:
    t = y + o + (o * k)
    o += y
    y = (o - y) * k

    i += 1

print('\n Rabbits total: ', t)






