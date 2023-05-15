"""
    pyMySql模块与MySql数据库交互流程:
        1. 创建数据库链接对象:
                用pymysql模块中的connect()函数来创建连接对象,代码如下:
               conn = connect(参数表):
                   参数host:连接的MySQL主机,如果是本机是'localhost'
                   参数port:连接的MySQL主机端口,默认是3306
                   参数user:连接的用户名
                   参数password:连接的密码
                   参数database:数据库的名称
                   参数charset:通信采用的编码方式,推荐使用utf-8
               连接对象conn操作说明:
                   关闭连接:conn.close()
                   提交数据:conn.commit()
                   撤销数据:conn.rollback()
        2. 获取游标对象
              调用连接对象的cursor()方法获取游标对象:cur = conn.cursor()
                 获取游标对象的目标是要执行sql语句,完成对数据库的增、删、改、查操作
                 游标可以记录获取数据的个数,第一次取出第一条数据,第二次会从第二条从数据开始读取
        3. 执行SQL语句:
            cursor.execute(sql语句, [参数1, 参数2, ...])
        4. 数据修改后提交数据库
            conn.commit()
        5. 关闭游标对象:
            cursor.close()
        6. 断开数据库连接
            conn.close()
"""
