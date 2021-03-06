# 关于 uncertainty 中的函数的使用方法及输出结果

## average_and_count(data) 函数

如果想要知道数据的**均值**与数据的**数量**，可以运用此函数。

自变量：数据数组

输出结果：数组[数据均值, 数据数量]

## uncertainty_A(data) 函数

如果想知道数据的**A类不确定度**，可以运用此函数。

***注意：*** *在计算A类不确定度的时候，认为了 t(P, n) = 1，而这种近似只有在 n > 5 的条件下满足。因此，数据项应当大于5项。*

自变量：数据数组

输出结果：浮点数A类不确定度

## uncertainty(uncertainty_a, uncertainty_b) 函数

如果想知道数据的**合成不确定度**，可以运用此函数。

**提示：**这里的合成不确定度保留了两位有效数字。舍入方法是进一法。

自变量1：浮点数A类不确定度

自变量2：浮点数B类不确定度

***注意：*** *使用这个函数需要手动指定B类不确定度。对于米尺测量长度，B类不确定度是 `0.1/(3 ** 0.5)`（单位：cm）；对于停表测量时间，B类不确定度是 `0.2`（单位：s）。*

输出结果：数组[保留两位有效数字的合成不确定度, power]

（power 的确定规则：1. power 是10的整数幂；2. 合成不确定度乘上power就是整数；3. 这个整数是最小的）

## result(data, uncertainty_b) 函数

如果想直接得到数据的**最终结果表示**，可以运用此函数。

**提示：**这里的合成不确定度保留了两位有效数字。均值的最低位与合成不确定度（保留两位有效数字）的最低位相同。均值的舍入方法是四舍六入五配偶。

自变量1：数据数组

自变量2：浮点数B类不确定度

***注意：*** *使用这个函数需要手动指定B类不确定度。对于米尺测量长度，B类不确定度是 `0.1/(3 ** 0.5)`（单位：cm）；对于停表测量时间，B类不确定度是 `0.2`（单位：s）。*

输出结果：字符串"{舍入后的均值} pm {合成不确定度（保留两位小数）}"（这里 pm 代表±。）

***注意：*** *这里的最终结果不会表示出单位。请在计算过程中保持单位制的一致。*
