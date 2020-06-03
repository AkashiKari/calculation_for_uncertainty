import numpy as np
import math

def average_and_count(data):
    the_sum = 0
    the_count = 0
    for x in data:
        the_sum += x
        the_count += 1
    x_bar = the_sum / the_count
    output = [x_bar, the_count]
    return output

def uncertainty_A(data):
    # 先计算样本均值
    avr_and_cnt= average_and_count(data)
    x_bar = avr_and_cnt[0]
    the_count = avr_and_cnt[1]
    # 再计算样本方差
    s_squared = 0
    for x in data:
        s_squared += (x - x_bar)**2
    s_squared = s_squared/(the_count - 1)
    # 当n>5时，可以认为t(P, n) = 1
    # u_a = t(P, n)\sqrt{s^2/n} = \sqrt{s^2/n}
    uncertanty_a_of_data = (s_squared / the_count)**0.5
    return uncertanty_a_of_data

def uncertainty(uncertainty_a, uncertainty_b):
    u = (uncertainty_a**2 + uncertainty_b**2)**0.5
    # 以下控制u只有两位有效数字。注意，u的估值通过进一法完成。
    power = 1
    while (u < 10):
        power *= 10
        u *= 10
    while (u >= 100):
        power *= 0.1
        u *= 10
    u = math.ceil(u)
    output = [u / power, power]
    return output

def result(data, uncertainty_b):
   average = average_and_count(data)[0]
   uncertainty_a = uncertainty_A(data)
   uncertainty_vector = uncertainty(uncertainty_a, uncertainty_b)
   u = uncertainty_vector[0]
   power = uncertainty_vector[1]
   main = round(average * power) / power
   output = ("%.*f" %(len(str(u).split(".")[1]), main)) + " pm " + str(u)
   return output
