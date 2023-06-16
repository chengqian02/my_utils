# author: hcx
import re

from my_utils.craw_main import CrawlMain
from lxml import etree

from bs4 import BeautifulSoup

def get_gzh_content(url_profile:str = '') -> dict:
    """获取公众号某个历史页面内容
    """
    from collections import defaultdict
    result_dict = defaultdict()
    crawlMain = CrawlMain()
    response_text = crawlMain.response_text(url_profile)
    response_text.encoding = 'utf-8'
    if not isinstance(response_text,str):
        if response_text.status_code == 200:
            soup = BeautifulSoup(response_text.text, 'lxml')
            # 解析 HTML 内容
            for item in soup.findAll('li', {'class': 'album__list-item'}):
                link = item.get('data-link')
                update_time, title_name = (i.strip() for i in item.get('data-title').split('｜'))
                result_dict[title_name] = {"url":link,'update_time':update_time}
        else:
            print('请求失败，状态码为：', response_text.status_code)
            exit()
    else:
        exit()

    return result_dict

if __name__ == '__main__':
    url_list = [
        'https://mp.weixin.qq.com/mp/appmsgalbum?action=getalbum&__biz=MzU3MTAwNTY5Mg==&scene=1&album_id=2483059132619587585&count=3#wechat_redirect',
        'https://mp.weixin.qq.com/mp/appmsgalbum?action=getalbum&__biz=MzU3MTAwNTY5Mg==&scene=1&album_id=2420753711892480000&count=3#wechat_redirect',
        'https://mp.weixin.qq.com/mp/appmsgalbum?action=getalbum&__biz=MzU3MTAwNTY5Mg==&scene=1&album_id=2432322762854842369&count=3#wechat_redirect',
        'https://mp.weixin.qq.com/mp/appmsgalbum?action=getalbum&__biz=MzU3MTAwNTY5Mg==&scene=1&album_id=2541629239817699330&count=3#wechat_redirect',
        'https://mp.weixin.qq.com/mp/appmsgalbum?action=getalbum&__biz=MzU3MTAwNTY5Mg==&scene=1&album_id=2588081946690355202&count=3#wechat_redirect',
        'https://mp.weixin.qq.com/mp/appmsgalbum?action=getalbum&__biz=MzU3MTAwNTY5Mg==&scene=1&album_id=2835866283627020288&count=3#wechat_redirect',
        'https://mp.weixin.qq.com/mp/appmsgalbum?action=getalbum&__biz=MzU3MTAwNTY5Mg==&scene=1&album_id=2830019599844016130&count=3#wechat_redirect',
        'https://mp.weixin.qq.com/mp/appmsgalbum?action=getalbum&__biz=MzU3MTAwNTY5Mg==&scene=1&album_id=2832946592323502081&count=3#wechat_redirect']

    # 获取上边连接中的所有文章
    result_dict = {}
    for url_profile in url_list:
        data_dict = get_gzh_content(url_profile)
        from collections import ChainMap

        # result_dict = ChainMap(result_dict, data_dict)
        result_dict.update(data_dict)

    # 对没一片文章，根据其上传时间排序
    dict_keys = sorted(result_dict, key=lambda i: result_dict[i].get('update_time'), reverse=True)

    # 获取所有内容
    for i in dict_keys:
        print({i: result_dict.get(i)})


