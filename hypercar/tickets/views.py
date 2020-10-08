from django.views import View
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView

menus = {'change_oil': 'Change oil', 'inflate_tires': 'Inflate tires', 'diagnostic': 'Get diagnostic test'}


class WelcomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'tickets/menu.html', context={"menus": menus})

class MenuPages(TemplateView):
    template_name = 'tickets/get_ticket.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['n_chapter'] = kwargs['n_chapter']
        return context
