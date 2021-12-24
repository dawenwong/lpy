from flask import Flask, render_template, request
import datetime

app = Flask(__name__)


# @app.route('/')  # 路由解析，通过用户访问的路径，匹配相应的函数
# def hello_world():  # put application's code here
#     return 'Hello World!'

# 开启debug模式，方便调试

@app.route('/index')
def greeting():
    return "你好👋👋"


# 通过访问路径获取字符串参数
@app.route('/user/<name>/<age>')
def getName(name, age):
    return "你好，%s %s" % (name, age)


# 通过访问路径获取int参数,还有<float:price>
@app.route('/user/<int:id>')
def getNum(id):
    return "你好，你的学号是%d" % id


# 路由路径不能重复

# jinja2的render_template
# @app.route('/')
# def index():  # 在templates文件夹创建html文件，只能在templates文件夹中创建，然后使用render_template("xxx.html")
#     return render_template("index.html")

# 先页面传递变量
@app.route("/")
def index():
    time = datetime.date.today()  # 普通变量
    name = ['张三', '李四', '王五']  # list
    task = {"任务": "打扫卫生", "时间限制": "30分钟"}  # 字典
    return render_template("index.html", var=time, list=name, task=task)  # 在html文件中，用{{var}}来接收变量


# 表单提交
@app.route('/test/register')
def register():
    return render_template("test/register.html")


# 接收表单提交的路由为post，methods = ['POST']
@app.route('/test/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        results = request.form
        return render_template('test/result.html', results=results)


if __name__ == '__main__':
    app.run()
