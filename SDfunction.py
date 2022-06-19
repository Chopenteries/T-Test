import math


def cal_var_new_mu(o, mu_mu):
    a = len(o)
    sum_of_powered_x_minus_x_bar = 0
    for l in range(0, len(o)):
        this_x_cal = float(o[l])
        power_of_x_minus_x_bar = (this_x_cal - mu_mu) ** 2
        sum_of_powered_x_minus_x_bar += power_of_x_minus_x_bar
    v = sum_of_powered_x_minus_x_bar / a
    return v


def cal_sd(x):
    y = len(x)
    sum_of_powered_x_minus_x_bar = 0
    for n in range(0, len(x)):
        this_x = float(x[n])
        x_bar = sum(x) / len(x)
        power_of_x_minus_x_bar = (this_x - x_bar) ** 2
        sum_of_powered_x_minus_x_bar += power_of_x_minus_x_bar
    v = sum_of_powered_x_minus_x_bar / y
    answer = math.sqrt(v)
    return answer


def cal_var(x):
    y = len(x)
    sum_of_powered_x_minus_x_bar = 0
    for n in range(0, len(x)):
        this_x = float(x[n])
        x_bar = sum(x) / len(x)
        power_of_x_minus_x_bar = (this_x - x_bar) ** 2
        sum_of_powered_x_minus_x_bar += power_of_x_minus_x_bar
    v = sum_of_powered_x_minus_x_bar / y
    return v
