import json
import matplotlib as plt

class PrintS:
    @classmethod
    def prints(cls,items):
        for item in items:
            if isinstance(item, (list, tuple, set)):
                cls.prints(item)
            else:
                print(item)

    @classmethod
    def prints_yield(cls,items):
        for item in items:
            if isinstance(item, (list, tuple, set)):
                yield from cls.prints(item)
            else:
                print(item)

    @classmethod
    def format_json(cls, json_string:dict):
        """
        将 JSON 字符串格式化并添加适当的缩进
        """
        try:
            return json.dumps(json_string, sort_keys=False, indent=4, ensure_ascii=False)
        except json.JSONDecodeError:
            """    
            如果 JSON 数据格式错误，则提示错误并指出错误位置    
            """
            error_message = "Invalid JSON data: {}".format(json_string)
            error_location = None
            for line, _, _ in plt.readlines():
                if line.startswith(error_message):
                    error_location = line.split()[1]
                    break
            if error_location is None:
                print(error_message)
            else:
                print("Error located at:", error_location)