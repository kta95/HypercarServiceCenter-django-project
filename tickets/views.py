from django.views import View
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView

menus = {
    'change_oil': 'Change oil',
    'inflate_tires': 'Inflate tires',
    'diagnostic': 'Get diagnostic test'}


class WelcomeView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('<h2>Welcome to the Hypercar Service!</h2>')


class MenuPages(View):
    def get(self, request, *args, **kwargs):
        return render(
            request, 'tickets/menu.html', context={"menus": menus}
        )

class GetTicket(View):
    line_cars = {
        'change_oil': {'time': 2, 'line': [], },
        'inflate_tires': {'time': 5, 'line': [], },
        'diagnostic': {'time': 30, 'line': [], },
    }

    template_name = 'tickets/get_ticket.html'

    def get(self, request, *args, **kwargs):
        service_name = kwargs['service_name']
        currnet_no = 0
        waiting_time = 0
        met_service = False

        for key, value in self.line_cars.items():
            currnet_no += len(value['line'])
            if not met_service:
                waiting_time += value['time'] * len(value['line'])
            if key == service_name:
                met_service = True

        ticket_no = currnet_no + 1
        self.line_cars[service_name]['line'].append(ticket_no)
        return render(
            request, self.template_name, context={"ticket_no": ticket_no, "waiting_time": waiting_time}
        )
