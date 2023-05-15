"""
    pymongo ==> python中操作MongoDB数据库的第三方包
        pymongo模块使用:
            1. 创建连接对象: conn = pymongo.MongoClient('localhost', 27017)
            2. 创建库对象: db = conn['库名']
            3. 创建集合对象: myset = db['集合名']
            4. 在集合中插入一条文档(写入数据): myset.insert_one({})
            5. 在集合中插入多条文档(写入多条数据):myset.insert_many([{}, {}, {}, {}.....{}])
"""
