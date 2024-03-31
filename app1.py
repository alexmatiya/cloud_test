from flask import Flask, request
from jinja2 import Template
from markupsafe import Markup, escape

app = Flask(__name__)


# изначальный вариант с уязвимостью
@app.route("/page1")
def page1():
    name = request.values.get("name")
    age = request.values.get("age", "unknown")
    output = Template("Hello " + name + "! Your age is " + age + ".").render()
    return output


# использование безопасного синтаксиса шаблонизации с автоматическим экранированием
@app.route("/page2")
def page2():
    name = request.values.get("name")
    age = request.values.get("age", "unknown")
    output = Template("Hello {{ name }}! Your age is {{ age }}.").render(
        name=name, age=age
    )
    return output


# Использование markupsafe вместо jinja2 для экранирования
@app.route("/page3")
def page3():
    name = escape(request.values.get("name", ""))
    age = escape(request.values.get("age", "unknown"))
    output = Markup("Hello %s! Your age is %s." % (name, age))
    return output


if __name__ == "main":
    app.run(debug=True)
