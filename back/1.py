from flask import Flask, request, jsonify
from flask_cors import CORS

from DICTATIONS import universities, olympiads_math
from yandexGPT import YandexGPT

app = Flask(__name__)
gpt = YandexGPT()
CORS(app=app, resources={r"*": {"origins": "*"}})


@app.get("/universities")
def get_universities():
    city = request.args.get('city')
    sp = []
    for name, value in universities.items():

        if value["city"] == city:
            sp.append({name: f"Уровень олимпиады: {value['программы']['уровень']}"})
    return jsonify(sp)


@app.get("/olympiads")
def get_olympiads():
    subject = request.args.get('subject')
    training_class = int(request.args.get('training_class'))
    sp = []
    if subject == "математика":
        for name, value in olympiads_math.items():
            if training_class == 11 and value["уровень"] == 3:
                sp.append({name: value})
            elif training_class in (9, 10):
                sp.append({name: value})
    return jsonify(sp)


@app.get("/fast_get")
def fast_get():
    city = request.args.get('city')
    class_education = request.args.get('class_education')
    better_object = request.args.get('better_object')
    return jsonify(gpt.post(
        f"Я хочу обучаться в {city}, мой любимый предмет {better_object}, сейчас я обучаюсь в {class_education}"))


@app.get("/fast_get_text")
def fast_get_text():
    text = request.args.get('text')
    res = jsonify(text=gpt.post(text).replace("\n", "<br>"))
    print(res.json)

    return res.json


if __name__ == '__main__':
    gpt = YandexGPT()
    app.run('127.0.0.1', debug=True)
