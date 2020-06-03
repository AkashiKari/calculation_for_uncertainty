import numpy as np
from uncertainty import *
import math

data = [100.90, 100.85, 100.90, 100.85, 100.80]
uncetainty_b = 0.1 / (3 ** 0.5)

print(f"数据 [100.90, 100.85, 100.90, 100.85, 100.80] 的均值为{average_and_count(data)[0]}，A类不确定度为{uncertainty_A(data)}，结果为" + result(data, uncetainty_b))