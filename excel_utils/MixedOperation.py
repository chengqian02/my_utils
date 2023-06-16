from .ExcelOperate import ExcelOperate
from .TwoExcelOperate import TwoExcelOperate
from collections import Counter
import re
class MixedOperation(ExcelOperate,TwoExcelOperate):
    '''excel混合操作，可以传入1个数据，或者2个数据
        Examples:
            Method_One：
                data = {
                    'filename':'***.xlsx',
                    'sheet':'Sheet1',
                    'data_range':'D5:BH213',
                    'data_pair':['D','BG'],
                }
                mixedOperation = MixedOperation(data)
            Method_Two：
                data = {
                    'filename':'***.xlsx',
                    'sheet':'Sheet1',
                    'data_range':'D5:BH213',
                    'data_pair':['D','BG'],
                }
                data2 = {
                    'filename':'***.xlsx',
                    'sheet':'Sheet1',
                    'data_range':'D5:BH213',
                    'data_pair':['D','BG'],
                }
                mixedOperation = MixedOperation(data,data2)

    '''
    def __init__(self, *args, **kwargs):
        if not args:
            raise TypeError("必须传递至少一个参数")

        if len(args) != 2:
            super().__init__(*args)  # 调用父类初始化方法
        else:
            TwoExcelOperate.__init__(self,*args)

if __name__ == '__main__':
    pass

