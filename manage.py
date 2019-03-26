from flask_script import Manager
from flask_script_demo import app
from database_script import db_manager

manager = Manager(app)

@manager.command
def runserver():
    print('服务器跑起来了')

# 把数据库的命令都写在manager.py中
# 用manager.add_command()方法添加
# 在命令行中的运行格式  python magager.py的绝对路径 父命令 小命令
# python C:\Users\DaneaLuo\myproject\manage.py db migrate
"""
总结：
1.如果直接在主manager.py中写命令，在终端只需要输入 python command_name就可以
2.如果把一些命令集中在一个文件中，那么在终端就需要输入一个父命令

"""
manager.add_command('db',db_manager)

if __name__ == '__main__':
    manager.run()