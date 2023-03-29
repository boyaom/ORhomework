import os

def delete_different_files():
    datafiles = os.listdir("./data")
    solfiles = os.listdir("./sol")
    sol_files_map = {}
    for file in solfiles:
        dotpos = file.find(".")
        predot = file[:dotpos]
        sol_files_map[predot] = 1
    remove_cnt = 0
    for file in datafiles:
        dotpos = file.find(".")
        predot = file[:dotpos]
        if predot not in sol_files_map:
            remove_path = os.path.join("./data", file)
            print(f"删除 {remove_path} 文件。")
            os.remove(remove_path)
            remove_cnt += 1
    print(f"操作完毕，共删除 {remove_cnt} 个。")

def check_sol_format():
    solfiles = os.listdir("./sol")
    for file in solfiles:
        path = os.path.join("./sol", file)
        with open(path, "r") as f:
            cnt_lines = 0
            for line in f.readlines():
                if cnt_lines == 0:
                    a = line.split()
                    if len(a) != 2:
                        print(f"文件 {file} 第一行共有 {len(a)} 个数。")
                cnt_lines += 1
            if cnt_lines > 2:
                print(f"文件 {file} 共有 {cnt_lines} 行。")

def replace_comma_with_space():
    # sol 文件中有最后给的排列不是用空格分隔而是逗号分割的
    solfiles = os.listdir("./sol")
    for file in solfiles:
        path = os.path.join("./sol", file)
        strlist = []
        with open(path, "r") as f:
            for line in f.readlines():
                if ',' in line:
                    print(f"在 {path} 文件中存在逗号分割的情况")
                    strlist.append(line.replace(',', ' '))
                else:
                    strlist.append(line)
        with open(path, "w") as f:
            f.writelines(strlist)

if __name__ == '__main__':
    delete_different_files()
    check_sol_format()
    replace_comma_with_space()