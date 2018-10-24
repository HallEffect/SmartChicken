# -*- coding: utf-8 -*-

from app import app
import control


@app.route('/')
@app.route('/index')
def index():

    humidity, temp = control.getCurrentTempHum()

        templateData = {
            'humidity': humidity,
            'temp': temp,
        }

    # Передаем словарь «templateData» в HTML-шаблон,
    # а затем возвращаем его пользователю:
    return render_template('main.html', **templateData)
