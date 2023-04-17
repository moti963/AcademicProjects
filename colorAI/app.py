import random
from flask import Flask, render_template, request, redirect, url_for, make_response

app = Flask(__name__)


def generate_color():
    characters = "0123456789abcdef"
    result = "#"
    for i in range(6):
        result += random.choice(characters)
    return result


@app.route('/', methods=['GET', 'POST'])
def create_buttons():
    

    if request.method == 'POST':
        form_name = request.form.get('form_name')
        if form_name=="button-gen-form":
            num_buttons = int(request.form['num_buttons'])
            buttons=[]
            for _ in range(num_buttons):
                buttons.append(generate_color())

            response = make_response(render_template(
                'create_buttons.html', buttons=buttons))
            response.set_cookie('buttons', ','.join(buttons))

            return response
    
        if form_name=="button-form":
            color="#000000"
            color = request.form['color']
            buttons_cookie = request.cookies.get('buttons')
            if buttons_cookie:
                buttons = buttons_cookie.split(',')
            else:
                buttons = []
            return render_template('view_circle.html', picked=color,buttons=buttons)

    return render_template('create_buttons.html')


@app.route('/view')
def view_circle():
    buttons_cookie = request.cookies.get('buttons')
    if buttons_cookie:
        buttons = buttons_cookie.split(',')
    else:
        buttons = []

    return render_template('view_circle.html', buttons=buttons)


if __name__ == '__main__':
    app.run(debug=True)
