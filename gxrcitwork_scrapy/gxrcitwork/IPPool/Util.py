import random

import gxrcitwork.IPPool.ProxiesDataBase
import gxrcitwork.IPPool.GetIP
import re

def Refresh():
    gxrcitwork.IPPool.GetIP.RefreshDB()
    gxrcitwork.IPPool.GetIP.GetIP()

def Get():
    proxies_dict = {}
    result = gxrcitwork.IPPool.ProxiesDataBase.GetItems()
    if result:
        tmp = random.choice(result)
        proxies_dict['http'] = '{}'.format(tmp)
        # proxies_dict['https'] = 'https://{}'.format(tmp)
    return proxies_dict

