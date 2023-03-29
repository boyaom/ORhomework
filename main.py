from SimulatedAnnealing import SA
import os

def inputdata(path, debug=False):
    n, w, d, numlist = 0, [], [], []
    with open(path, "r") as f:
        idx = -1
        for line in f.readlines():
            idx += 1
            if idx == 0:
                if line == "" or line == "\n" or line == "\r":
                    if debug:
                        print(f"本文件 {path} 第一行就是空行！")
                    idx -= 1
                    continue
                else:
                    a = [int(v) for v in line.split()]
                    if len(a) >= 2:
                        if debug:
                            print(f"本文件 {path} 第一行有两个数！")
                            exit(0)
                    n = a[0]
            else:
                a = [int(v) for v in line.split()]
                numlist = numlist + a
    for i in range(n):
        w.append(numlist[i*n : (i+1)*n])
    for i in range(n):
        d.append(numlist[(n+i)*n : (n+i+1)*n])
    assert len(numlist) == 2 * n * n
    return n, w, d

def test_input_data():
    datafiles = os.listdir("./data")
    for idx, file in enumerate(datafiles):
        path = os.path.join("./data", file)
        file_str_dot_pos = file.find(".")
        sol_str = file[:file_str_dot_pos] + ".sln"
        pathsol = os.path.join("./sol", sol_str)
        sol_n, refans, refansp = inputsol(pathsol, debug=True)
        data_n, w, d = inputdata(path, debug=True)
        assert data_n == sol_n
        print(idx, data_n, path)
    print("所有文件均读入成功！")

def inputsol(path, debug=False):
    n, refans, refansp = 0, [], []
    with open(path, "r") as f:
        idx = -1
        for line in f.readlines():
            idx += 1
            if idx == 0:
                if line == "" or line == "\n" or line == "\r":
                    if debug:
                        print(f"本文件 {path} 第一行就是空行！")
                    idx -= 1
                    continue
                else:
                    a = [int(v) for v in line.split()]
                    if len(a) != 2:
                        if debug:
                            print(f"本文件 {path} 第一行不是两个数！")
                            exit(0)
                    n, refans = a[0], a[1]
            else:
                a = [int(v) for v in line.split()]
                refansp = refansp + a
    assert len(refansp) == n
    return n, refans, refansp

def solve():
    datafiles = os.listdir("./data")
    for idx, file in enumerate(datafiles):
        path = os.path.join("./data", file)
        file_str_dot_pos = file.find(".")
        sol_str = file[:file_str_dot_pos] + ".sln"
        pathsol = os.path.join("./sol", sol_str)
        sol_n, refans, refansp = inputsol(pathsol)
        data_n, w, d = inputdata(path)
        assert data_n == sol_n

        # 您们改下面两行就好
        sa = SA(data_n, w, d, init_with_shuffle=True, random_seed=42)
        ans, ansp = sa.solve(iterator_times=100, t0=10.0, d=0.9)

        # 我们还需要一个比较强大的评估指标
        if refans == 0:
            print("本段为模拟退火代码，在 {} 文件上，算法计算总费用 / 参考答案总费用为：{}/{}".format(file, ans, refans))
        else:
            print("本段为模拟退火代码，在 {} 文件上，算法计算总费用 / 参考答案总费用为：{}/{}，大概计算了有 {}%".format(file, ans, refans, 100.0 * ans / refans))

if __name__ == '__main__':
    solve()