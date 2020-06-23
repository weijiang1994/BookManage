# BookManage
python + pyqt5搭建一个图书管理系统

终于第一个版本发布上来了,基本实现都比较简陋

### 开始
#### 安装依赖
1. pip install PyQt5
2. pip install pymysql
#### 安装数据库
安装任意一种服务器类型数据库即可
#### 创建数据库以及建表
进入项目根目录`cd BookManage`,运行`python generate_data.py`生成数据库文件 
#### user表

| 字段名             | 类型     | 长度 | 主键 |
| ------------------ | -------- | ---- | ---- |
| id                 | varchar  | 50   | 是   |
| username           | varchar  | 255  | 否   |
| password           | varchar  | 255  | 否   |
| role               | int      | 11   | 否   |
| create_time        | datetime | 0    | 否   |
| delete_flag        | int      | 11   | 否   |
| current_login_time | datetime | 0    | 否   |

#### borrow_info 表

| 字段名      | 类型     | 长度 | 主键 |
| ----------- | -------- | ---- | ---- |
| id          | varchar  | 50   | 是   |
| book_id     | varchar  | 255  | 否   |
| book_name   | varchar  | 255  | 否   |
| borrow_user | varchar  | 255  | 否   |
| borrow_num  | int      | 11   | 否   |
| borrow_days | int      | 11   | 否   |
| borrow_time | datetime | 0    | 否   |
| return_time | datetime | 0    | 否   |
| return_flag | int      | 11   | 否   |

#### book表

| 字段            | 类型     | 长度 | 主键 |
| --------------- | -------- | ---- | ---- |
| id              | varchar  | 50   | 是   |
| book_name       | varchar  | 255  | 否   |
| author          | varchar  | 255  | 否   |
| publish_company | varchar  | 255  | 否   |
| store_number    | int      | 11   | 否   |
| borrow_number   | int      | 11   | 否   |
| create_time     | datetime | 0    | 否   |
| publish_date    | datetime  | 255  | 否   |

#### 修改数据库的连接属性
进入util->dbutil文件,修改里面的数据库连接属性。

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
  - 催还

### 部分示例页面
#### 1.登陆页面
![登陆页面](https://github.com/weijiang1994/BookManage/blob/master/screenshoot/login.png)
#### 2.借阅管理页面
![借阅管理页面](https://github.com/weijiang1994/BookManage/blob/master/screenshoot/borrow_book.png)
#### 3.主界面
![主页面](https://github.com/weijiang1994/BookManage/blob/master/screenshoot/main.png)


