# first method
# 'mu: \u03BC'
# t = x_bar - mu / (s / math.sqrt(n))
# x_bar = sum(x) / n
# mu = sum(x) / population
# s = SD(x)

# second method
# t0 = (x1_bar - x2_bar)
# t1 = (SD(x1) \ len(x1)) + (SD(x2) \ len(x2))
# t2 = math.sqrt(t1)
# t = t0 / t2

from function import \
    has_2_samples,\
    run

run(has_2_samples())

# print('mu: \u03BC')
