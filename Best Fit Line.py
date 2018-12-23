from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import random

style.use('ggplot')


# consider line equation y = ax + b
# ---------------------------------------------------------------

# calculating component 'a'
def best_fit_slope(xs, ys):

    return ( ((mean(xs) * mean(ys)) - mean(xs * ys)) /
          ((mean(xs) * mean(xs)) - mean(xs*xs)) )

# ---------------------------------------------------------------


# calculating component 'b'
def best_fit_intercept(xs, ys):

    return mean(ys) - best_fit_slope(xs, ys) * mean(xs)

# ---------------------------------------------------------------


# returns components 'a' and 'b'
def best_fit_slope_and_intercept(xs, ys):

    return best_fit_slope(xs, ys), best_fit_intercept(xs, ys)

# ---------------------------------------------------------------


def squared_error(ys_orig, ys_line):

    return sum((ys_line - ys_orig)**2)


# ---------------------------------------------------------------


def coefficient_of_determination(ys_orig, ys_line):

    y_mean_line = [mean(ys_orig) for y in ys_orig]
    squared_error_regr = squared_error(ys_orig, ys_line)
    squared_error_y_mean = squared_error(ys_orig, y_mean_line)
    return 1 - (squared_error_regr / squared_error_y_mean)


# ---------------------------------------------------------------


# creating a randomized dataset to test the functions
def randomize_dataset(how_many, variance, step=2, correlation=False):
    val = 1
    ys = []
    for i in range(how_many):
        y = val + random.randrange(-variance, variance)
        ys.append(y)
        if correlation and correlation == True:
            val += step
        elif correlation and correlation == False:
            val -= step
    xs = [i for i in range(len(ys))]

    return np.array(xs, dtype=np.float64), np.array(ys, dtype=np.float64)

# ---------------------------------------------------------------


# plotting the dataset along with the best fit line
def plot_best_fit_line(xs, ys):

    # coefficients
    a, b = best_fit_slope_and_intercept(xs, ys)
    regression_line = [(a * x) + b for x in xs]

    r_sq = coefficient_of_determination(ys, regression_line)

    plt.scatter(xs, ys)
    plt.plot(xs, regression_line, 'b')
    plt.title("Coefficient of deteremination: {0}".format(r_sq))
    plt.show()
    return regression_line


# ---------------------------------------------------------------


# SAMPLE PLOT
xs, ys = randomize_dataset(50, 10, 3, correlation=True)
reg_line = plot_best_fit_line(xs, ys)


