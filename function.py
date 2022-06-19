# first method
# 'mu: \u03BC'
# t = x_bar - mu / (s / math.sqrt(n))
# x_bar = sum(x) / n
# mu = sun(x) / population
# s = SD(x)

# second method
# t0 = (x1_bar - x2_bar)
# t1 = (SD(x1) \ len(x1)) + (SD(x2) \ len(x2))
# t2 = math.sqrt(t1)
# t = t0 / t2

import math
import warnings

from SDfunction import cal_sd,\
    cal_var


def has_2_samples():
    samples = input("\nDo you know your variables ?\n"
                    "\n1: T-Distribution \n"
                    "describes the standardized distances of sample means to the population mean when the population "
                    "standard deviation is not known, and the observations come from a normally distributed "
                    "population. \n"
                    "\n2: T-Test \n"
                    "A t-test is the most commonly applied when the test statistic would follow a normal distribution "
                    "if the value of a scaling term in the test statistic were known. When the scaling term is "
                    "unknown and is replaced by an estimate based on the data, the test statistics (under certain "
                    "conditions) follow a Student's t distribution. The t-test can be used, for example, to determine "
                    "if the means of two sets of data are significantly different from each other.\n\n"
                    "How many of your sample set?(1 or 2 or 'y'): \n")
    return samples


def int_exception(x):
    try:
        val = int(x)
        return val
    except ValueError:
        try:
            val = float(x)
            return val
        except ValueError:
            if x == "y" or x == "Y":
                return "y"
            return 0


def run(which_type):
    # T-test has chosen
    if int_exception(which_type) == 2:
        # Looping X1
        sample_x1 = input("Input your 'X1' samples: \n").split()
        for i in range(0, len(sample_x1)):
            sample_x1[i] = float(sample_x1[i])
        # Looping X2
        sample_x2 = input("Input your 'X2' samples: \n").split()
        for n in range(0, len(sample_x2)):
            sample_x2[n] = float(sample_x2[n])
        numberical_illustrations_of_various_t_test(sample_x1, sample_x2)

    # T-Distribution has chosen
    elif int_exception(which_type) == 1:
        # Looping X1
        sample_x1 = input("Input your 'X1' samples: \n").split()
        for i in range(0, len(sample_x1)):
            sample_x1[i] = float(sample_x1[i])
        # Looping X2
        sample_x2 = input("Input your 'X2' samples: \n").split()
        for n in range(0, len(sample_x2)):
            sample_x2[n] = float(sample_x2[n])
        t_distribution(sample_x1, sample_x2)

    # known variables
    elif int_exception(which_type) == "y":
        t_distribution_with_known_variables()

    # x exception(x = 0 by wrong input)
    elif int_exception(which_type) > 2 or int_exception(which_type) < 1:
        warnings.warn("Wrong input, try again")
        run(has_2_samples())


def find_mu(x):
    t = 1.645
    n = len(x)
    sd = cal_sd(x)
    x_bar = sum(x) / n
    # mu_plus = x_bar + (t / math.sqrt(n))
    # mu_minus = x_bar - (t / math.sqrt(n))
    # mean_mu = (mu_plus + mu_minus) / 2
    # mu = x_bar - ((mu_plus - mu_minus) * (len(x)))
    mu = (t * (sd / math.sqrt(n)) - x_bar)
    if mu > 0:
        mu *= -1
    return mu


def t_distribution(x, y):
    # variables
    x_bar = sum(x) / len(x)
    sd_x = cal_sd(x)
    n = len(x)

    # calculation
    sum_x1_minus_x2 = 0
    d_arrays = []
    for n in range(0, len(x)):
        this_x = float(x[n])
        this_y = float(y[n])
        d_1 = this_x - this_y
        d_arrays.append(d_1)
        sum_x1_minus_x2 += d_1
    d = sum_x1_minus_x2 / len(x)
    t = d / (cal_sd(d_arrays) / math.sqrt(n))
    return print(t)


def t_distribution_with_known_variables():
    mean = input("Input your Sample mean: \n")
    mu = input("Input your \u03BC: \n")
    sd = input("Input your Standard Deviation: \n")
    sample_size = input("Input your samples size: \n")

    # calculation
    if int_exception(mean) != 0 and int_exception(mu) != 0 and int_exception(sd) != 0 \
            and int_exception(sample_size) != 0:
        mean = float(mean)
        mu = float(mu)
        sd = float(sd)
        sample_size = float(sample_size)
        t = (mean - mu) / (sd / math.sqrt(sample_size))
        print(t)
    else:
        warnings.warn("Wrong input, try again")
        run(has_2_samples())


def numberical_illustrations_of_various_t_test(x1, x2):
    # variables
    x1_bar = sum(x1) / len(x1)
    x2_bar = sum(x2) / len(x2)
    sd1 = cal_sd(x1)
    sd2 = cal_sd(x2)
    var1 = cal_var(x1)
    var2 = cal_var(x2)
    t_table_95 = 1.645
    n1 = len(x1)
    n2 = len(x2)
    print(x1)
    print(x2)

    # calculation
    mu_1 = (t_table_95 * (sd1 / math.sqrt(n1)) - x1_bar)
    if mu_1 < 0:
        mu_1 *= -1

    mu_2 = (t_table_95 * (sd2 / math.sqrt(n2)) - x2_bar)
    if mu_2 < 0:
        mu_2 *= -1

    t0 = (x1_bar - x2_bar) - (mu_1 - mu_2)
    t1 = (var1 / n1) + (var2 / n2)
    t2 = math.sqrt(t1)
    t = (t0 / t2)
    print(f"{t_table_95} * ({sd1} / {n1}) - {x1_bar}")
    print(f"{t_table_95} * ({sd2} / {n2}) - {x2_bar}")
    print(f"({x1_bar} - {x2_bar}) - ({mu_1} - {mu_2})")
    print(f"({var1} / {n1}) + ({var2} / {n2})")
    print(f"sqr {t2}")
    print(f"t = {t}")
