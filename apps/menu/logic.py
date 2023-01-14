from . import models


def rating(name):

    try:
        model = models.Rating.objects.get(name=name)
        count_click = models.Rating.objects.get(name=name).rating+1
        models.Rating.objects.update(name=name, rating=count_click)

    except:
        models.Rating.objects.create(name=name, rating=1)


def rating_data():
    model = models.Rating.objects.all()
    list_data = [[i.name, i.rating] for i in model]
    return list_data
