from datetime import datetime, timedelta
a, b, c = input().split()
d = int(input())
dat_now = datetime(int(a), int(b), int(c))
dat_fut = timedelta(d)
dat_sum = dat_now + dat_fut
print(dat_sum.year, dat_sum.month, dat_sum.day)
