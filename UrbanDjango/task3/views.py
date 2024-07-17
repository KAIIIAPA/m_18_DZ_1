from django.shortcuts import render

# Create your views here.

def platform(request):
    title_platform = 'ComMag - Магазин комиксов'
    context = {
        'title_platform': title_platform
    }
    return render(request, 'third_task/platform.html', context=context)


def comics(request):
    title_comics = 'Комиксы'
    buy = 'Купить'
    back = 'Назад'
    context = {
        'title_comics': title_comics,
        'buy': buy,
        'back': back
    }
    return render(request, "third_task/comics.html", context=context)


def basket(request):
    title_basket = 'Корзина'
    back = 'Назад'
    context = {
        'title_basket': title_basket,
        'back': back
    }
    return render(request, "third_task/basket.html", context=context)
