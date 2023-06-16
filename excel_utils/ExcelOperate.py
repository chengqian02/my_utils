import numbers
import os
import re

import numpy as np
import openpyxl
from openpyxl.utils import column_index_from_string as Col2Int
from openpyxl.utils.cell import coordinate_from_string
from openpyxl.utils import get_column_letter
# 操作excel

class ExcelOperate:
    def __init__(self, data: dict = None)  -> None:

        self.filename = data.get('filename', '')
        self.sheet = data.get('sheet', '')
        self.data_range = data.get('data_range', '')
        self.data_pair = data.get('data_pair', [])

        if not all([self.filename, self.sheet, self.data_range, self.data_pair]):
            raise ValueError("Invalid input data")

        # 获取excel所有范围
        self.range_one, self.range_two = self.data_range.split(":")

        # 读取所有的数据,和全部转为字符串的数据
        self.all_data_list, self.all_data_string_list = self.read_excel_data()

        # 读取需要判别的数据
        self.data_list = self.read_simple_data(self.all_data_list)

        # 读取需要判别的字符串数据
        self.data_string_list = self.read_simple_data(self.all_data_string_list)

    '''读取范围内的所有数据'''
    def read_excel_data(self, *args, **kwargs):
        # 打开文件
        wb_id1 = openpyxl.load_workbook(self.filename, data_only=True)
        # 打开sheet
        if isinstance(self.sheet, numbers.Number):
            sheet_list = wb_id1.sheetnames
            sheetDataSet1 = wb_id1[sheet_list[int(self.sheet)]]
        else:
            sheetDataSet1 = wb_id1[self.sheet]
        data_list = []
        data_string_list = []
        for i in sheetDataSet1[self.range_one:self.range_two]:
            tmp_list = []
            tmp_string_list = []
            for j in i:
                tmp_list.append(j.value)
                tmp_string_list.append(str(j.value).replace(',','，'))
            data_list.append(tmp_list)
            data_string_list.append(tmp_string_list)
        return data_list, data_string_list

    '''读取范围内的所有数据，全部转为字符串'''
    def read_excel_data_for_string(self, *args, **kwargs):
        # 打开文件
        wb_id1 = openpyxl.load_workbook(self.filename, data_only=True)
        # 打开sheet
        sheetDataSet1 = wb_id1[self.sheet]
        data_list = []
        for i in sheetDataSet1[self.range_one:self.range_two]:
            tmp_list = []
            for j in i:
                tmp_list.append(str(j.value))
            data_list.append(tmp_list)
        return data_list

    '''读取用到的数据'''
    def read_simple_data(self, all_data_list):
        one_col, one_row = coordinate_from_string(self.data_range.split(":")[0])
        data_list = []
        for i in all_data_list:
            tmp_list = [i[Col2Int(data_pair_one) - Col2Int(one_col)] for data_pair_one in self.data_pair ]
            data_list.append(tmp_list)
        return data_list

    '''返回列表中有同样值的数据'''
    def repeat_value(self) -> dict:
        dict_char_tmp = {i[0]: self.data_list.count(i) for i in self.data_list if self.data_list.count(i) > 1}
        return dict_char_tmp

    '''List数据插入excel'''
    def write_list_excel(self, result_list, file_name='output', header=None):
        if header:
            header = header
        else:
            if len(result_list) > 1:
                header = [get_column_letter(i+1) for i in range(len(result_list[0]))]
            else:
                header = [get_column_letter(i+1) for i in range(len(result_list))]

        wb = openpyxl.Workbook()
        sheet = wb.create_sheet(title='Sheet1',index=0)
        for h_col in range(1, len(header)+1):
            _ = sheet.cell(column=h_col, row=1, value="{0}".format(header[h_col-1]))
        i=1
        for result in result_list:
            j = 1
            for v in result:
                _ = sheet.cell(row=i,column=j,value="{}".format(v))
                j+=1
            i+=1
        wb.save(filename="{}".format(file_name+'.xlsx'))
        print("写入数据成功{}".format(os.getcwd()+'\\'+file_name+'.xlsx'))

    '''Dict数据插入excel'''
    def write_dict_excel(self, result_dict:dict, file_name='output', header=None):
        if header:
            header = header
        else:
            if len(list(result_dict.values())[0]) > 1:
                header = [get_column_letter(i+1) for i in range(len(list(result_dict.values())[0])+1)]
            else:
                header = [get_column_letter(i+1) for i in range(len(list(result_dict.values())[0])+1)]
        wb = openpyxl.Workbook()
        sheet = wb.create_sheet(title='Sheet1', index=0)
        # for h_col in range(1, len(header) + 1):
        #     _ = sheet.cell(column=h_col, row=1, value="{0}".format(header[h_col - 1]))
        i = 1
        for k,v in result_dict.items():
            _ = sheet.cell(row=i, column=1, value="{}".format(k))
            j = 2
            for value in v:
                _ = sheet.cell(row=i, column=j, value="{}".format(value))
                j += 1
            i += 1
        wb.save(filename="{}".format(file_name + '.xlsx'))
        print("写入数据成功{}".format(os.getcwd()+'\\'+file_name+'.xlsx'))


    def process_all_content(self, pattern:[str,re], repl: [str,re]) -> None:
        """提取出来的所有内容替换操作（根据正则匹配模式，替换为某个内容）

        Args：
            pattern: 需要匹配的正则表达式或者内容
            repl: 替换的正则表达式或者目标内容

        Returns:
            None
        """
        for item in self.data_list:
            for i,item_content in enumerate(item):
                item[i] = re.sub(pattern, repl, item_content)

    def iterate_list(self, items):
        """遍历列表中的每一项内容

        Args:
            items: 需要遍历的内容

        Returns:
            返回一个生成器，可以遍历每一项内容
        """
        for item in items:
            if isinstance(item, (list, tuple, set)):
                yield from self.iterate_list(item)
            else:
                yield item

    def get_data_list(self):
        output = ""
        for content in self.iterate_list(self.data_list):
            output += content + "\n"
        return output

    def get_data_string_list(self):
        output = ""
        for content in self.iterate_list(self.data_string_list):
            output += content + "\n"
        return output

    def __repr__(self):
        output = ""
        for content in self.iterate_list(self.data_list):
            output += content + "\n"
        return output