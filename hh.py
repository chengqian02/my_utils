

# def get_millisecond():
#     """
#     :return: 获取精确毫秒时间戳,13位
#     """
#     millis = int(round(time.time() * 1000))
#     return millis
# import time

# print(time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(1678065588209/1000)))

# import collections

# a = "sdf "
# print(isinstance(a,collections.abc.Sequence))


# import requests
# import json
# import time

# headers = {
# 	"Accept": "application/json, text/javascript, */*; q=0.01",
# 	"Accept-Encoding": "gzip, deflate, br",
# 	"Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
# 	"Connection": "keep-alive",
# 	"Content-Length": "3501",
# 	"Content-Type": "application/x-www-form-urlencoded",
    
# 	"Cookie": "HWWAFSESID=ef2c7732cc345216db; HWWAFSESTIME={}; JSESSIONID=wKgAVhroZAagnAoansjKYUMFttqoJV8IHC8A".format(str(int(time.time())*1000)),
# 	"Host": "yongchanggroup.kdeascloud.com",
# 	"Origin": "https://yongchanggroup.kdeascloud.com",
# 	"Referer": "https://yongchanggroup.kdeascloud.com/shr/dynamic.do?uipk=com.kingdee.eas.hr.ats.app.PunchCardRecord.list&serviceId=MDtpxQ0pRKarT5UNd%2FwqSPI9KRA%3D&inFrame=true",
# 	"sec-ch-ua": "\"Google Chrome\";v=\"107\", \"Chromium\";v=\"107\", \"Not=A?Brand\";v=\"24\"",
# 	"sec-ch-ua-mobile": "?0",
# 	"sec-ch-ua-platform": "\"Windows\"",
# 	"Sec-Fetch-Dest": "empty",
# 	"Sec-Fetch-Mode": "cors",
# 	"Sec-Fetch-Site": "same-origin",
# 	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
# 	"X-Requested-With": "XMLHttpRequest"
# }
# session = requests.session()
# data:json = {
# 	"_search": "false",
# 	"nd": str(int(time.time())*1000),
# 	"rows": "50",
# 	"page": "1",
# 	"sidx": "",
# 	"sord": "asc",
# 	"componentID": "grid",
# 	"query": "com.kingdee.eas.hr.ats.app.PunchCardRecordQuery",
# 	"filterItems": "",
# 	"encryptKeys": "filterItems%2Cfilter%2CfastFilterItems%2CsorterItems%2CadvancedFilter%2CcolumnModel",
# 	"filter": "",
# 	"fastFilterItems": "_SHRREQPARA_JTdCJTIyaHJPcmdVbml0JTIyJTNBJTdCJTIydmFsdWVzJTIyJTNBJTIyJTIyJTJDJTIyaXNTYXZlVG9TY2hlbWUlMjIlM0F0cnVlJTJDJTIyZGF0YVR5cGUlMjIlM0ElMjJTdHJpbmclMjIlMkMlMjJ1cmwlMjIlM0ElMjIlMkZkeW5hbWljLmRvJTNGbWV0aG9kJTNEZ2V0SHJPcmdVbml0RGF0YSUyMiUyQyUyMmlzU2VhbFVwJTIyJTNBZmFsc2UlN0QlMkMlMjJJU0RFRkFVTFRNQU5BR0UlMjIlM0ElN0IlMjJ2YWx1ZXMlMjIlM0ElMjIlMjIlMkMlMjJpc1NhdmVUb1NjaGVtZSUyMiUzQXRydWUlMkMlMjJkYXRhVHlwZSUyMiUzQSUyMlN0cmluZyUyMiUyQyUyMnVybCUyMiUzQSUyMiUyRmR5bmFtaWMuZG8lM0Z1aXBrJTNEY29tLmtpbmdkZWUuZWFzLmhyLmF0cy5hcHAuSG9saWRheUxpbWl0Lmxpc3QlMjZtZXRob2QlM0RnZXREZWZhdWx0TWFuYWdlciUyMiU3RCUyQyUyMmFkbWluT3JnVW5pdCUyMiUzQSU3QiUyMnZhbHVlcyUyMiUzQSUyMiUyMiUyQyUyMmlzU2F2ZVRvU2NoZW1lJTIyJTNBdHJ1ZSUyQyUyMmRhdGFUeXBlJTIyJTNBJTIyRjclMjIlMkMlMjJ1aXBrJTIyJTNBJTIyY29tLmtpbmdkZWUuZWFzLmJhc2VkYXRhLm9yZy5hcHAuQWRtaW5PcmdVbml0LkY3JTIyJTJDJTIyaW5jbHVkZVN1YiUyMiUzQSUyMjAlMjIlMkMlMjJpc0luY2x1ZGVTdWIlMjIlM0F0cnVlJTJDJTIyZGF0YUl0ZW0lMjIlM0ElNUIlNUQlN0QlMkMlMjJwdW5jaENhcmREYXRlJTIyJTNBJTdCJTIydmFsdWVzJTIyJTNBJTdCJTIyc3RhcnREYXRlJTIyJTNBJTIyMjAyMy0wMy0wNSUyMiUyQyUyMmVuZERhdGUlMjIlM0ElMjIyMDIzLTAzLTA1JTIyJTJDJTIyc2VsZWN0RGF0ZSUyMiUzQSUyMmN1c3RvbSUyMiU3RCUyQyUyMmlzU2F2ZVRvU2NoZW1lJTIyJTNBdHJ1ZSUyQyUyMmRhdGFUeXBlJTIyJTNBJTIyRGF0ZSUyMiUyQyUyMmRhdGFJdGVtJTIyJTNBJTIyY3VzdG9tJTIyJTJDJTIycXVlcnlEYXRlVHlwZSUyMiUzQSUyMiUyMiU3RCUyQyUyMnB1bmNoQ2FyZFN0YXRlJTIyJTNBJTdCJTIydmFsdWVzJTIyJTNBJTIyJTIyJTJDJTIyaXNTYXZlVG9TY2hlbWUlMjIlM0F0cnVlJTJDJTIyZGF0YVR5cGUlMjIlM0ElMjJFbnVtJTIyJTJDJTIyZW51bVNvdXJjZSUyMiUzQSUyMmNvbS5raW5nZGVlLmVhcy5oci5hdHMuUHVuY2hDYXJkU3RhdGVFbnVtJTIyJTJDJTIyaXNDdXN0b21EZWZpbmUlMjIlM0FmYWxzZSU3RCU3RA%3D%3D",
# 	"sorterItems": "_SHRREQPARA_cHJvcG9zZXIubnVtYmVyJTJDcHVuY2hDYXJkRGF0ZSUyMGRlc2M%3D",
# 	"advancedFilter": "_SHRREQPARA_JTdCJTIyY29uZGl0aW9uJTIyJTNBJTIyKHQxKSUyMiUyQyUyMmZpbHRlckl0ZW1NYXBpbmclMjIlM0ElN0IlMjJ0MSUyMiUzQSU3QiUyMmNvbmRpdGlvbl9rZXklMjIlM0ElN0IlMjJpZCUyMiUzQTElMkMlMjJuYW1lJTIyJTNBJTIyJUU1JUE3JTkzJUU1JTkwJThEJTIyJTJDJTIydHlwZSUyMiUzQSUyMlN0cmluZyUyMiUyQyUyMnVpcGslMjIlM0FudWxsJTJDJTIyZW51bVNvdXJjZSUyMiUzQW51bGwlMkMlMjJpc1RyZWUlMjIlM0FmYWxzZSUyQyUyMnRyZWVVcmwlMjIlM0FudWxsJTJDJTIyZmllbGQlMjIlM0ElMjJwcm9wb3Nlci5uYW1lJTIyJTJDJTIyaXNNdWx0aWxpbmd1YWwlMjIlM0F0cnVlJTJDJTIyZGJUeXBlJTIyJTNBJTIyTlZBUkNIQVIlMjIlMkMlMjJxdWVyeUN0cmwlMjIlM0FudWxsJTJDJTIyZXh0ZW5kT3B0aW9ucyUyMiUzQSU3QiU3RCU3RCUyQyUyMm5hbWUlMjIlM0ElMjJwcm9wb3Nlci5uYW1lJTIyJTJDJTIyY29tcGFyZVR5cGUlMjIlM0ElMjJsaWtlJTIyJTJDJTIydmFsdWUlMjIlM0ElMjIlRTUlQUQlOTklRTYlODIlQTYlMjIlMkMlMjJ2YWx1ZU11bHRpTGFuZyUyMiUzQSU3QiUyMmwyJTIyJTNBJTIyJUU1JUFEJTk5JUU2JTgyJUE2JTIyJTdEJTJDJTIydHlwZSUyMiUzQSUyMlN0cmluZyUyMiUyQyUyMmFsaWFzJTIyJTNBJTIyJUU1JUE3JTkzJUU1JTkwJThEJTIwJUU1JThDJTg1JUU1JTkwJUFCJTIwJUU1JUFEJTk5JUU2JTgyJUE2JTIyJTdEJTdEJTJDJTIybG9naWNhbFJlbGF0aW9uc2hpcCUyMiUzQSUyMjElMjIlN0Q%3D",
# 	"custom_params": "%7B%22uipk%22%3A%22com.kingdee.eas.hr.ats.app.PunchCardRecord.list%22%2C%22inFrame%22%3A%22true%22%2C%22serviceId%22%3A%22MDtpxQ0pRKarT5UNd%2FwqSPI9KRA%3D%22%7D",
# 	"keyField": "id",
# 	"columnModel": "_SHRREQPARA_cHJvcG9zZXIubmFtZSUyQ2FkbWluT3JnVW5pdC5kaXNwbGF5TmFtZSUyQ2hyT3JnVW5pdC5uYW1lJTJDYXR0ZW5kYW5jZU51bSUyQ3B1bmNoQ2FyZERhdGUlMkNwdW5jaENhcmRUaW1lJTJDcHVuY2hDYXJkU291cmNlJTJDcHVuY2hDYXJkUGxhY2UlMkNkZXNjcmlwdGlvbiUyQ3B1bmNoQ2FyZFN0YXRlJTJDaWQlMkM%3D",
# 	"uipk": "com.kingdee.eas.hr.ats.app.PunchCardRecord.list"
# }
# login_data:json = {
# 	"email": "13293785075",
# 	"password": "4kJiSvEDlo2/a3syu4UXUg==",
# 	"remember": "false",
# 	"forceToNetwork": "false",
# 	"redirectUrl": "",
# 	"accountType": "",
# 	"clientId": "",
# 	"imgCode": "",
# 	"imgCodeId": "",
# 	"networkId": "",
# 	"loginExtendInfo": "{\"userDefinedDeviceName\":\"\"}"
# }

# login_headers ={
# 	"accept": "*/*",
# 	"accept-encoding": "gzip, deflate, br",
# 	"accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
# 	"content-length": "219",
# 	"content-type": "application/x-www-form-urlencoded; charset=UTF-8",
# 	"cookie": "JSESSIONID=103kfnu6re6gw1w2zbi4yutzxh; toweibologin=login; accessId=ce3d5ef0-6836-11e6-85a2-2d5b0666fd02; Hm_lvt_45f5f201f5af9cfeffd1f82177d2cceb=1676697420,1676777870,1677991650,1678081496; uuid_ce3d5ef0-6836-11e6-85a2-2d5b0666fd02=9b797da0-05ed-48ab-b38a-da4a612a4ce3; Hm_lvt_a96914087b350d1aa86c96cdbf56d5e5=1676697420,1676777870,1677991650,1678081496; href=https%3A%2F%2Fwww.yunzhijia.com%2Fhome%2F; cd=yunzhijia.com; cn=61ee5b7ce4b051b535e2473a; cu=62bfef07e4b0b34d0df15ebb; __loginType=; redirectIndexUrl=/yzj-layout/home; webLappToken=\"RTXcirUwxXdnd0q%2FsT%2FxQ%2FFZjwhZJtOMKBA09Y9hUzCcZU76UZ8SWYZ6PMLY82TgQMuRr94q5Y7U5xjLnPxt%2BQ%2ByFoOrLb3VvMOwlAT12Xs%3D\"; sync_networkid=61ee5b7ce4b051b535e2473a; sync_userid=62bfef07e4b0b34d0df15ebb; cd=yunzhijia.com; cn=61ee5b7ce4b051b535e2473a; gl=3ccf0494-977b-4a5c-a3d7-d86239e499c7; gl=3ccf0494-977b-4a5c-a3d7-d86239e499c7; Hm_lpvt_45f5f201f5af9cfeffd1f82177d2cceb=1678154881; qimo_seosource_0=%E7%AB%99%E5%86%85; qimo_seokeywords_0=; qimo_seosource_ce3d5ef0-6836-11e6-85a2-2d5b0666fd02=%E7%AB%99%E5%86%85; qimo_seokeywords_ce3d5ef0-6836-11e6-85a2-2d5b0666fd02=; qimo_xstKeywords_ce3d5ef0-6836-11e6-85a2-2d5b0666fd02=; at=12eaaef9-169a-4c92-a80f-3a93a3a6f30f; uuid=4c4a5948-6f18-40b5-ac08-adfc0e9a7e99; Hm_lpvt_a96914087b350d1aa86c96cdbf56d5e5=1678155031; pageViewNum=12",
# 	"origin": "https://www.yunzhijia.com",
# 	"referer": "https://www.yunzhijia.com/home/?m=open&a=login&utm_source=&utm_medium=",
# 	"sec-ch-ua": "\"Google Chrome\";v=\"107\", \"Chromium\";v=\"107\", \"Not=A?Brand\";v=\"24\"",
# 	"sec-ch-ua-mobile": "?0",
# 	"sec-ch-ua-platform": "\"Windows\"",
# 	"sec-fetch-dest": "empty",
# 	"sec-fetch-mode": "cors",
# 	"sec-fetch-site": "same-origin",
# 	"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
# }



# url = "https://yongchanggroup.kdeascloud.com/shr/dynamic.do?method=getListData"
# # login_url = "https://www.yunzhijia.com/space/c/rest/user/v2/login?"+str(int(time.time())*1000)
# # response_text = session.post(url=login_url,headers=login_headers,data=json.dumps(login_data))

# response_text = session.post(url=url,headers=headers, data=json.dumps(data))
# print(response_text.text)

from interval import Interval
import time
def judge_time(currentTime , time_interval_one, time_interval_two):
    if currentTime in Interval(time_interval_one, time_interval_two):
        return True
    return False

a1 = "2023-03-07 11:31"
timeArray = time.strptime(a1, "%Y-%m-%d %H:%M")
currentTime = int(time.mktime(timeArray))
currentTime = time.strftime("%H:%M:%S", time.localtime(currentTime))
print(currentTime)
print(judge_time(currentTime,"11:30:00", "12:30:00"))


