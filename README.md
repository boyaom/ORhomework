# 问题

已知有 $n$ 个位置和 $n$ 家工厂，各个位置之间的距离矩阵设为 $D=(d_{ij})_{n \times n}$，各工厂之间的运输量矩阵为 $W = (w_{ij})_{n \times n}$。现在要将 $n$ 家工厂建造在这 $n$ 个位置上，使得总费用最小。

设 $d_{ij}$ 表示位置 $i$ 和位置 $j$ 之间的距离，$w_{ij}$ 表示工厂 $i$ 和工厂 $j$ 之间的费用。故工厂 $i$ 建造在位置 $k$ 且工厂 $j$ 建造在位置 $l$ 所导致的费用为 $d_{kl}w_{ij}$.

请求出一种分配方式，使得 $\sum d_{kl}w_{ij}$ 最小。

## 正式定义

给定两个集合，P("facilities") 和 L("locations")，它们有相等的大小，共同有一个权重函数 $w: P \times P \rightarrow R$ 和一个距离函数 $d: L \times L \rightarrow R$。找出一个双射 $f: P \rightarrow L("assignment")$ 使得费用函数：
$$
\sum_{a,b \in P} w(a,b) \cdot d(f(a), f(b))
$$
最小。

# 处理数据

数据来源：https://www.opt.math.tugraz.at/qaplib/inst.html

先执行 `python dataprocess.py` 即可删除 `data` 文件夹下和 `sol` 文件夹下不同的文件。

执行后删除文件如下（注意由于是在 windows 下操作，所以有反斜线）：

```
删除 ./data\esc32a.dat 文件。
删除 ./data\esc32b.dat 文件。
删除 ./data\esc32c.dat 文件。
删除 ./data\esc32d.dat 文件。
删除 ./data\esc32h.dat 文件。
删除 ./data\esc64a.dat 文件。
删除 ./data\sko42.dat 文件。
删除 ./data\sko49.dat 文件。
删除 ./data\sko56.dat 文件。
删除 ./data\sko64.dat 文件。
删除 ./data\sko72.dat 文件。
删除 ./data\tai100a.dat 文件。
删除 ./data\tai10a.dat 文件。
删除 ./data\tai10b.dat 文件。
删除 ./data\tai25a.dat 文件。
删除 ./data\tai30a.dat 文件。
删除 ./data\tai35a.dat 文件。
删除 ./data\tai40a.dat 文件。
删除 ./data\tai50a.dat 文件。
删除 ./data\tho40.dat 文件。
删除 ./data\wil50.dat 文件。
操作完毕，共删除 21 个。

进程已结束，退出代码为 0
```

然后我们调用 `check_sol_format()` 函数可以发现虽然参考解的格式行数由于排列不太一样， 
但是至少第一行一定是两个数，分别是 $n$ 和最终的函数答案。

```
操作完毕，共删除 0 个。
文件 bur26a.sln 共有 3 行。
文件 bur26b.sln 共有 3 行。
文件 bur26c.sln 共有 3 行。
文件 bur26d.sln 共有 3 行。
文件 bur26e.sln 共有 3 行。
文件 bur26f.sln 共有 3 行。
文件 bur26g.sln 共有 3 行。
文件 bur26h.sln 共有 3 行。
文件 chr15b.sln 共有 3 行。
文件 chr18b.sln 共有 3 行。
文件 chr20a.sln 共有 3 行。
文件 chr20b.sln 共有 3 行。
文件 chr20c.sln 共有 3 行。
文件 chr22a.sln 共有 3 行。
文件 chr22b.sln 共有 3 行。
文件 chr25a.sln 共有 3 行。
文件 els19.sln 共有 3 行。
文件 esc128.sln 共有 10 行。
文件 esc32e.sln 共有 4 行。
文件 esc32f.sln 共有 4 行。
文件 esc32g.sln 共有 3 行。
文件 had14.sln 共有 3 行。
文件 kra30a.sln 共有 4 行。
文件 kra30b.sln 共有 7 行。
文件 kra32.sln 共有 7 行。
文件 lipa20a.sln 共有 3 行。
文件 lipa20b.sln 共有 3 行。
文件 lipa30a.sln 共有 4 行。
文件 lipa30b.sln 共有 4 行。
文件 lipa40a.sln 共有 4 行。
文件 lipa40b.sln 共有 4 行。
文件 lipa50a.sln 共有 5 行。
文件 lipa50b.sln 共有 5 行。
文件 lipa60a.sln 共有 5 行。
文件 lipa60b.sln 共有 5 行。
文件 lipa70a.sln 共有 6 行。
文件 lipa70b.sln 共有 6 行。
文件 lipa80a.sln 共有 6 行。
文件 lipa80b.sln 共有 6 行。
文件 lipa90a.sln 共有 7 行。
文件 lipa90b.sln 共有 6 行。
文件 nug12.sln 共有 3 行。
文件 nug14.sln 共有 3 行。
文件 nug15.sln 共有 3 行。
文件 nug16a.sln 共有 3 行。
文件 nug16b.sln 共有 3 行。
文件 nug17.sln 共有 3 行。
文件 nug18.sln 共有 3 行。
文件 nug20.sln 共有 4 行。
文件 nug21.sln 共有 3 行。
文件 nug22.sln 共有 3 行。
文件 nug24.sln 共有 3 行。
文件 nug25.sln 共有 3 行。
文件 nug30.sln 共有 3 行。
文件 rou12.sln 共有 3 行。
文件 rou15.sln 共有 3 行。
文件 rou20.sln 共有 3 行。
文件 scr12.sln 共有 3 行。
文件 scr15.sln 共有 3 行。
文件 scr20.sln 共有 3 行。
文件 sko100a.sln 共有 8 行。
文件 sko100b.sln 共有 8 行。
文件 sko100c.sln 共有 8 行。
文件 sko100d.sln 共有 8 行。
文件 sko100e.sln 共有 8 行。
文件 sko100f.sln 共有 8 行。
文件 sko81.sln 共有 7 行。
文件 sko90.sln 共有 7 行。
文件 ste36a.sln 共有 4 行。
文件 ste36b.sln 共有 3 行。
文件 ste36c.sln 共有 3 行。
文件 tai100b.sln 共有 7 行。
文件 tai12a.sln 共有 3 行。
文件 tai150b.sln 共有 10 行。
文件 tai17a.sln 共有 3 行。
文件 tai20a.sln 共有 3 行。
文件 tai20b.sln 共有 3 行。
文件 tai256c.sln 共有 19 行。
文件 tai25b.sln 共有 4 行。
文件 tai30b.sln 共有 4 行。
文件 tai35b.sln 共有 4 行。
文件 tai40b.sln 共有 4 行。
文件 tai50b.sln 共有 5 行。
文件 tai60a.sln 共有 5 行。
文件 tai60b.sln 共有 5 行。
文件 tai64c.sln 共有 6 行。
文件 tai80a.sln 共有 7 行。
文件 tai80b.sln 共有 7 行。
文件 tho150.sln 共有 20 行。
文件 tho30.sln 共有 7 行。
文件 wil100.sln 共有 8 行。
在 ./sol\nug30.sln 文件中存在逗号分割的情况

进程已结束，退出代码为 0
```

还意外地发现了有逗号分割排列的情况，因此我们将逗号替换为空格。

为了使得 data 输入没啥问题，因此采用比较保守的策略进行读入，即读入第一个数后，然后
一个一个地弄到一个 list 里，然后再给 $w$ 矩阵和 $d$ 矩阵赋值。

调用 `test_input_data()` 函数可以发现，部分数据第一行是空行，但是并没有第一行有两个数的情况。