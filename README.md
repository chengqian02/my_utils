# my_utils工具包使用手册

## 文件说明：

- calculate_run_time_Decorators.py：定了2个装饰器，可以用于计算程序的运行时间
- convert_ipynb_mardown.py：批量将jupyter中的笔记转为markdown格式的笔记
- craw_gzh_history.py：用程序定时获取公众号每天的标题内容
- craw_main.py：爬虫获取网页数据接口
- delete_In.py：删除Ipython前边的标识内容
- FindingSentenceSimilarity.py：计算两个句子之间的相似度
- get_file_names.py：获取目录下的所有文件，所有子目录文件
- print_s.py：格式化输出可迭代列表，或json数据
- excel_utils：处理excel数据接口。

### excel_utils：

#### 使用方法：

##### 初始化

```python
data = {
    'filename':'***.xlsx',
    'sheet':'Sheet1',
    'data_range':'D,5:BH,213',
    'data_pair':['D','BG'],
}
data2 = {
    'filename':'***.xlsx',
    'sheet':'Sheet1',
    'data_range':'D,5:BH,213',
    'data_pair':['D','BG'],
}
mixedOperation = MixedOperation(data,data2)

# - filename：要处理的excel文件名
# - sheet：要获取的sheet工作空间名字，用sheet名或者第几个如第一个工作区：1
# - data_range:读取的工作范围
# - 要读取的数据列
```

### calculate_run_time_Decorators

```python
from my_utils.calculate_run_time_Decorators import runTime

@runTime
def getCookie(self):
```



##### 
