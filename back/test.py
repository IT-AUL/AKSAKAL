from requests import get


print(get('http://127.0.0.1:5000/fast_get?city=Москва&class_education=11&better_object=математика').json())
print("\n\n\n\n\n\n\n")
print(get('http://127.0.0.1:5000/fast_get_text?text=Санкт-Петербург_11_класс_информатика').json())