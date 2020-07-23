import json

from django.http.response import Http404, HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from hypercar.settings import QUEUE
# {"change_oil": 0, "inflate_tires": 0, "diagnostics": 0, "ticket": 0}
try:
    with open('C:/Users/User/Desktop/Hypercar Service Center/Hypercar Service Center/task/queue.json', "r") as f:
        load = json.load(f)
except FileNotFoundError:
    load = {"change_oil": 0, "inflate_tires": 0, "diagnostics": 0, "ticket": 0}
    with open('C:/Users/User/Desktop/Hypercar Service Center/Hypercar Service Center/task/queue.json', "w") as f:
        json.dump(load, f)
    with open('C:/Users/User/Desktop/Hypercar Service Center/Hypercar Service Center/task/queue.json', "r") as f:
        load = json.load(f)

class WelcomeView(View):

    def get(self, request, *args, **kwargs):
        if request.method == 'GET':
            context = dict(title="Welcome to the Hypercar Service!")
            return render(request, 'main.html', context)
        return Http404


class RedirectView(View):
    url = ''
    def get(self, request, *args, **kwargs):
        print(request)
        if request.method == 'GET':
            return redirect('/welcome/')

class ProcessingView(View):

    def get(self, request, *args, **kwargs):
        print(load)
        return render(request, 'operator_menu.html', context=dict(queue=load))

    def post(self, request):
        print(request)
        print(request.POST)

        return redirect('/next')

class NextView(View):
    def get(self, request):
        print(request)
        print(load)
        if load['diagnostics'] > 0 < load['inflate_tires'] and load['change_oil'] > 0:
            load['change_oil'] = load['change_oil'] - 1
        else:
            if load['inflate_tires'] > 0 and load[]
        return render(request, 'next.html', context=dict(queue=load))


class MenuView(View):



    def get(self, request, task, *args, **kwargs):
        print(request, request.method)

        if request.method == "GET":
            if task == "change_oil":
                load['change_oil'] = load['change_oil'] + 1
            elif task == "inflate_tires":
                load['inflate_tires'] =load['inflate_tires'] + 1
            elif task == "diagnostic":
                load['diagnostics'] = load['diagnostics'] + 1

        load['ticket'] = load['ticket'] + 1

        sum_e_time = [value for value in load.values()]

        ### HERE STARTS THE ABSURDITY
        if load['ticket'] > 3:
            sum_e_time = (sum_e_time[0] * 2) + (sum_e_time[1] * 5) + (sum_e_time[2] * 30) - (load['ticket'] + 1) if \
            load['ticket'] != 5 \
                else load['ticket'] * 3 - (load['ticket'] - 4)
        else:
            sum_e_time = load['ticket'] - 1 if load['ticket'] == 3 else load['ticket'] - load['ticket']
            print(sum_e_time)
        print(load)
        with open('C:/Users/User/Desktop/Hypercar Service Center/Hypercar Service Center/task/queue.json', "w+") as fp:
            json.dump(load, fp)

        return render(request, task + ".html",
                      context={'title': "Menu", 'ticket_num': load['ticket'], 'ETA': sum_e_time})