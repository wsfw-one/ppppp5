'''
演示python pymysql 库的基础操作
'''

from pymysql import Connection

# 构建到MySQL数据库的链接
conn = Connection(host='localhost',   # 主机名
                  port=3306,          # 端口
                  user='root',        # 账户
                  password='dly221703', # 密码
                  autocommit=True       # 自动确认
)

# print(conn.get_server_info())
# 执行非查询性质SQL
# cursor = conn.cursor()  #获取到游标对象
# # 选择数据库
# conn.select_db('test')
# # 执行数据库
# cursor.execute('create table test_pymysql(id int);')

# # 执行查询性质SQL
# cursor = conn.cursor()  #获取到游标对象
# # 选择数据库
# conn.select_db('world')
# # 执行数据库
# cursor.execute("select ......")
#
# results = cursor.fetchall()
# for row in results:
#     print(row)
#
# # 关闭链接
# conn.close()

# cursor = conn.cursor()  #获取到游标对象
# 选择数据库
# conn.select_db('world')
# 执行数据库--数据插入或更改
# cursor.execute("insert into student values(10002, 'linjunjie', 31)")
# 通过commit确认
# conn.commit()

# 关闭链接
# conn.close()

'''
综合案例
'''

# 读取数据