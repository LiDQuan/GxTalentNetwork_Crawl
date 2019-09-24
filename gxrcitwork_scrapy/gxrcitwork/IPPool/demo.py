import sqlite3
import gxrcitwork.IPPool.GetIP
import gxrcitwork.IPPool.Config
import gxrcitwork.IPPool.ProxiesDataBase
import gxrcitwork.IPPool.Util


def main():
    # 初始化数据库和数据表
    gxrcitwork.IPPool.ProxiesDataBase.InitDB()
    # 刷新数据库，添加新数据
    gxrcitwork.IPPool.Util.Refresh()
    # 获取一个代理使用
    proxies = gxrcitwork.IPPool.Util.Get()
    print(proxies)

    # 查询数据库多少条数据
    conn = sqlite3.connect(gxrcitwork.IPPool.Config.DBName)
    cu = conn.cursor()
    print(cu.execute("""SELECT * FROM {};""".format(gxrcitwork.IPPool.Config.TabelName)).fetchall().__len__())
    cu.close()
    conn.close()


if __name__ == '__main__':
    main()
