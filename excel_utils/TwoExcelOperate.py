
from .ExcelOperate import ExcelOperate
import numpy as np

class TwoExcelOperate:
    def __init__(self, data1=None, data2=None):
        self.exceloperate = ExcelOperate(data1 or {})
        self.exceloperate_two = ExcelOperate(data2 or {})

    '''判断两个列表的差集'''
    def ListsCompareDifferences(self,*args,**kwargs):
        a1 = np.array(self.exceloperate.data_list)
        a2 = np.array(self.exceloperate_two.data_list)
        a1_rows = a1.view([('', a1.dtype)] * a1.shape[a1.ndim-1])
        a2_rows = a2.view([('', a2.dtype)] * a2.shape[a1.ndim-1])
        result_dict = {}
        result_dict[self.exceloperate.filename+"中有",self.exceloperate_two.filename+"没有"] = np.setdiff1d(a1_rows, a2_rows).view(a1.dtype).reshape(-1, a1.shape[a1.ndim-1])
        result_dict[self.exceloperate_two.filename+"中有",self.exceloperate.filename+"没有"] = np.setdiff1d(a2_rows, a1_rows).view(a1.dtype).reshape(-1, a1.shape[a1.ndim-1])
        return result_dict

    '''判断两个字典的键差集'''
    def DictKeyCompareDifferences(self, dict1, dict2):
        result_set = set(dict1.keys()) ^ set(dict2.keys())
        return result_set

    '''判断两个字典的差集'''
    def DictItemCompareDifferences(self, dict1, dict2):
        result_set = set(dict1.items()) ^ set(dict2.items())
        result_list = [i for i in dict(result_set).keys()]
        return result_set, result_list

    def IsertWages(self, *args, **kwargs) -> list:
        '''
            function:
                把第二个表中的数据按第一个表的顺序插入(返回List数据)
            UsageMethod:
                data = {
                    'filename':'***.xlsx',
                    'sheet':'Sheet1',
                    'data_range':'D5:BG104',
                    'data_pair':['D']
                }
                data2 = {
                    'filename':'***.xlsx',
                    'sheet': 'Sheet1',
                    'data_range':'C4:E200',
                    'data_pair':['C','E'],
                }
                performanceAppraisalForm = PerformanceAppraisalForm(data,data2)
                dict = performanceAppraisalForm.IsertWages()
                performanceAppraisalForm.WriteListExcel(dict)
        '''


        # 把源数据转为字典
        dict1 = {}
        err_list = []
        for i in range(len(self.exceloperate.data_string_list)):
            if self.exceloperate.data_string_list[i][0] not in dict1:
                dict1[self.exceloperate.data_string_list[i][0]] = ''
            else:
                # 判断异常数据

                # print(self.exceloperate.data_string_list[i][0])
                err_list.append(self.exceloperate.data_string_list[i][0])

        dict2 = {}
        for data in self.exceloperate_two.data_string_list:
            if data[0] not in dict2:
                dict2[data[0]] = [val for val in data]
            else:
                # 判断异常数据
                err_list.append(data[0])

        err_list.extend(val for val in self.DictKeyCompareDifferences(dict1,dict2))

        result_list = []

        # 把数据写入
        for i in self.exceloperate.data_string_list:
            if i[0] in dict2:
                result_list.append(dict2[i[0]])
            else:
                result_list.append([i[0]])

        # 异常人员：
        print("异常人员,请手动处理异常人员：\n{}".format("、".join(err_list)),end='\n\n')
        return result_list
