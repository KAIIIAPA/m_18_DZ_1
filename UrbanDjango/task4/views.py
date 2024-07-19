from django.shortcuts import render

# Create your views here.

def platform(request):
    title_platform = 'Магазин комиксов'
    context = {
        'title_platform': title_platform
    }
    return render(request, 'fourth_task/platform.html', context=context)


def comics(request):
    title_comics = 'Комиксы'
    buy = 'Купить'
    comicss = ['Атака на титанов. Книга 1', 'Невероятные Люди Икс. Том 3. Хороший, Плохой, Нелюдь',
              'Хранители. Начало: Комедиант. Роршах. Красный Корсар']
    context = {
        'title_comics': title_comics,
        'buy': buy,
        'comicss': comicss
    }
    return render(request, "fourth_task/comics.html", context=context)


def basket(request):
    title_basket = 'Корзина'
    context = {
        'title_basket': title_basket,
    }
    return render(request, "fourth_task/basket.html", context=context)

def menu(request):
    comics_magazine = 'Магазин комиксов'
    mane_page = 'Главная страница'
    comics_page = 'Комиксы'
    basket_page = 'Корзина'
    context = {
        'comics_magazine': comics_magazine,
        'mane_page': mane_page,
        'comics_page': comics_page,
        'basket_page': basket_page
    }
    return render(request, "fourth_task/menu.html", context=context)