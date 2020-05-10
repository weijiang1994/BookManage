# BookManage
python + pyqt5搭建一个图书管理系统

终于第一个版本发布上来了,基本实现都比较简陋

### 开始
#### 安装依赖
pip install PyQt5
#### 安装数据库
`安装任意一种服务器类型数据库即可`
#### 手动建表
`本来应该是写个脚本文件自动生成数据库，由于时间匆忙，没来得及写，后续版本补上。`
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
| publish_date    | varchar  | 255  | 否   |

#### 修改数据库的连接属性
进入util->dbutil文件,修改里面的数据库连接属性。
