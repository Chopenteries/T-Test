# x = [2085.06 2082.78 2074.28 2098.63 2108.92 2116.04 2125.10 2128.03 2129.87 2121.64]
#
# y = [2071.02 2067.00 2056.32 2056.64 2095.38 2101.78 2108.58 2119.89 2112.50 2109.38]
import math

import numpy as np
from scipy import stats
from SDfunction import cal_sd, \
    cal_var, \
    cal_var_new_mu

rng = np.random.default_rng()
rvs = stats.norm.rvs(loc=5, scale=10, size=(50, 2), random_state=rng)

x = [2085.06, 2082.78, 2074.28, 2098.63, 2108.92, 2116.04, 2125.10, 2128.03, 2129.87, 2121.64]

y = [2071.02, 2067.00, 2056.32, 2056.64, 2095.38, 2101.78, 2108.58, 2119.89, 2112.50, 2109.38]

z = [0, 1, 2, 3]

print(stats.ttest_ind(x, y))
print(stats.ttest_ind(x, y, trim=.2))
# ((t * (find_population_sd(x) / math.sqrt(len(x)))) - x_bar)
n = len(y)
sd = cal_sd(y)
x_bar = sum(y) / n
t = 1.645
mu_plus = x_bar + (t / math.sqrt(n))
mu_minus = x_bar - (t / math.sqrt(n))
mean_mu = (mu_plus + mu_minus) / 2
mu = x_bar - ((mu_plus - mu_minus) * (len(y)))
mu_2 = (t * (sd / math.sqrt(n)) - x_bar)
if mu < 0:
    mu *= -1
if mu_2 < 0:
    mu_2 *= -1
print(cal_var(y))
print(cal_var_new_mu(y, mu_2))
print(mu_plus)
print(mu_minus)
print(mean_mu)
print(mu)
print(mu_2)

total_mean = 0
for p in range(0, len(x)):
    this_x = float(x[p])
    this_y = float(y[p])
    this_mean = (this_x + this_y) / 2
    total_mean += this_mean

final = total_mean / 10

# print(final)
