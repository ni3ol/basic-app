from flask import Flask, request
from jinja2 import Environment, FileSystemLoader


app = Flask(__name__)


environment = Environment(loader=FileSystemLoader('./views'))


people = []


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        people.append(request.form['name'])

    template = environment.get_template('index.html')
    return template.render(people=people)


def main():
    app.run()


if __name__ == '__main__':
    main()
