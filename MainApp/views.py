from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


# Глобальная переменная с товарами
items = [
    {"id": 1, "name": "Кроссовки abibas", "quantity": 5},
    {"id": 2, "name": "Куртка кожаная", "quantity": 2},
    {"id": 5, "name": "Coca-cola 1 литр", "quantity": 12},
    {"id": 7, "name": "Картофель фри", "quantity": 0},
    {"id": 8, "name": "Кепка", "quantity": 124},
]

#1

def index(request):
    author = "Иванов И.П."
    html_content = f"<h1>\"Изучаем django\"</h1><strong>Автор</strong>: <i>{author}</i>"
    return HttpResponse(html_content)

#2
def about(request):
    user_info = {
        "first_name": "Иван",
        "middle_name": "Петрович",
        "last_name": "Иванов",
        "phone": "8-923-600-01-02",
        "email": "vasya@mail.ru"
    }
    html_content = f"""
    Имя: {user_info['first_name']}<br>
    Отчество: {user_info['middle_name']}<br>
    Фамилия: {user_info['last_name']}<br>
    Телефон: {user_info['phone']}<br>
    Email: {user_info['email']}
    """
    return HttpResponse(html_content)

#3
def item_list(request):
    html_content = "<ol>"
    for item in items:
        html_content += f"<li><a href='/item/{item['id']}'>{item['name']}</a></li>"
    html_content += "</ol>"
    return HttpResponse(html_content)

#4
def item_detail(request, item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item:
        html_content = f"Название: {item['name']}<br>Количество: {item['quantity']}"
    else:
        html_content = f"Товар с id={item_id} не найден"
    return HttpResponse(html_content)

#5
def items(request):
    html_content = "<ol>"
    for item in items:
        html_content += f"<li><a href='/item/{item['id']}'>{item['name']}</a></li>"
    html_content += "</ol>"
    return HttpResponse(html_content)

