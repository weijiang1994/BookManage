# BookManage
python + pyqt5搭建一个图书管理系统

终于第一个版本发布上来了,基本实现都比较简陋

### 开始
#### 安装依赖
```sh
pip install PyQt5 -i https://pypi.douban.com/simple
pip install pymysql -i https://pypi.douban.com/simple 
```

#### 安装数据库
安装任意一种服务器类型数据库即可[Mariadb下载](https://mariadb.org/)
#### 创建数据库以及建表
进入项目根目录`cd BookManage`,运行`python generate_data.py`生成数据库文件 

#### 修改数据库的连接属性
进入`util->dbutil`文件,修改里面的数据库连接属性。

#### 运行
进入到项目的根目录下，
`python run.py`
既可以运行项目。

### 包含功能
1. 权限分级
    - 普通用户
    - 管理员用户
2. 普通用户
    - 借书
    - 还书
    - 续借
3. 管理员用户
    - 添加图书
    - 编辑图书
    - 删除图书
    - 催还———`20200629`

### 部分示例页面
#### 1.登陆页面
![登陆页面](https://github.com/weijiang1994/BookManage/blob/master/screenshoot/login.png)
#### 2.借阅管理页面
![借阅管理页面](https://github.com/weijiang1994/BookManage/blob/master/screenshoot/borrow_book.png)
#### 3.主界面
![主页面](https://github.com/weijiang1994/BookManage/blob/master/screenshoot/main.png)
#### 4. 主页
![主页](https://github.com/weijiang1994/BookManage/blob/master/screenshoot/homepage.png)

