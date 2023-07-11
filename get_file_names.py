import os
from print_s import PrintS

def print_tree(directory, prefix=''):
    # 打印当前目录名
    print(prefix + os.path.basename(directory) + '/')

    # 遍历目录下的所有文件和子目录
    for filename in os.listdir(directory):
        # 获取文件或子目录的完整路径
        path = os.path.join(directory, filename)
        # 如果是文件，则打印文件名
        if os.path.isfile(path):
            print(prefix + '|--' + filename)
        # 如果是子目录，则递归调用print_tree()函数，并修改前缀
        elif os.path.isdir(path):
            print_tree(path, prefix + '|  ')

def get_file_names(directory):
    # 获取目录下的所有文件名
    file_names = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    return file_names



# 调用print_tree()函数并传入目录路径作为参数，即可以树形结构输出该目录下所有文件的文件名
# print_tree('./')

# 调用get_file_names()函数并传入目录路径作为参数，即可返回该目录下所有文件的文件名。
file_names = get_file_names('./')

PrintS.prints(file_names)