import pickle
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.linear_model import LinearRegression
from flask import (Flask, request, render_template) #сервер фреймворков

print("import удачно")
num_scaler = pickle.load(open('..\flask_app\models\ml_models\num_scaler_v11.pkl'))
lr = pickle.load(open('..\flask_app\models\ml_models\lr.pkl', 'rb'))

app = Flask (__name__)

@app.route('/', methods = ['POST', 'GET'])
def main():
    if request.method == 'GET':
        return render_template('main.html')
    if request.method == 'POST':
        ['Соотношение матрица-наполнитель'] == float(request.form['Соотношение матрица-наполнитель'])
        ['Плотность, кг/м3'] == float(request.form['Плотность, кг/м3'])
        ['модуль упругости, ГПа'] == float(request.form['модуль упругости, ГПа'])
        ['Количество отвердителя, м.%'] == float(request.form['Количество отвердителя, м.%'])
        ['Содержание эпоксидных групп,%_2'] == float(request.form['Содержание эпоксидных групп,%_2'])
        ['Температура вспышки, С_2'] == float(request.form['Температура вспышки, С_2'])
        ['Поверхностная плотность, г/м2'] == float(request.form['Поверхностная плотность, г/м2'])
        ['Модуль упругости при растяжении, ГПа'] == float(request.form['Модуль упругости при растяжении, ГПа'])
        ['Прочность при растяжении, МПа'] == float(request.form['Прочность при растяжении, МПа'])
        ['Потребление смолы, г/м2'] == float(request.form['Потребление смолы, г/м2'])
        #preprocessing
        X_num_from_form = ['Соотношение матрица-наполнитель',
                        'Плотность, кг/м3',	'модуль упругости, ГПа',	
                        'Количество отвердителя, м.%	Содержание эпоксидных групп,%_2',
                            'Температура вспышки, С_2',
                            'Поверхностная плотность, г/м2',
                            'Модуль упругости при растяжении, ГПа',
                            'Прочность при растяжении, МПа',
                            'Потребление смолы, г/м2']
        
        X = []
        X.extend(X_num_from_form)
        print('X на вход модели', X)

        X_scaled = num_scaler.transform(X)

        prediction = lr.predict(X_scaled)

        result = ['Модуль упругости при растяжении, ГПа'].inverse_transform(prediction)
        print('result', result)
        return render_template('main.html', result=result)

#инструкция для сервера
if __name__== '_main_':
    app.run(debug = True)