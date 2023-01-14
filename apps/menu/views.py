from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from . import models, logic


class HomeMenu(View):
    template_name = "menu/home_menu.html"

    def get(self, request, *args, **kwargs):
        menu_model = models.Menu.objects.filter(deleted=False)
        menu_data = {}
        for i in menu_model:
            menu_data[i.name] = models.SubMenu.objects.filter(deleted=False, menu_id__name=i.name)
        return render(request, self.template_name, {"menu": menu_data})


class SubMenu(View):
    template_name = "menu/sub_menu.html"

    def get(self, request, name):
        logic.rating(name)
        menu_model = models.SubMenu.objects.filter(menu_id__name=name)
        return render(request, self.template_name, {"menu": menu_model, "sub_menu": name, 'ls_data': logic.rating_data()})


class DetailMenu(View):
    template_name = "menu/detail_menu.html"

    def get(self, request, name):
        logic.rating(name)
        return render(request, self.template_name, {"sub_menu": name, 'ls_data': logic.rating_data()})


