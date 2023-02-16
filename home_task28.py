def rec_sum(a, b):
   return a if b == 0 else rec_sum(a+1, b-1) if b > 0 else rec_sum(a-1, b+1)
print(rec_sum(2, 2))