import itertools
import json
import random

from django.shortcuts import render, HttpResponseRedirect, HttpResponse, redirect, Http404, HttpResponseRedirect
from django.views import View
from datetime import datetime


# Create your views here.
def simple_date_fun(date):
    return datetime.strptime(date, "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d")


def main_view(request, *args, **kwargs):
    print(request)
    print(request.user)
    query = request.GET.get('q')
    if query == '':
        query = None
        print(query)

    if query == None:
        with open("C:/Users/User/Desktop/HyperNews Portal/HyperNews Portal/task/news.json", 'r') as jfile:
            jlist = json.load(jfile)

        jlist.sort(key=lambda x: datetime.strptime(x['created'], "%Y-%m-%d %H:%M:%S"), reverse=True)
        all_news = [{'date': date, 'values': list(news)} for date, news in
                    itertools.groupby(jlist, lambda x: simple_date_fun(x['created']))]
        print(all_news)
        context = dict(title="Hyper news", content=all_news[0]['date'], pages=all_news)
        return render(request, "main.html", context=context)
    else:
        find_page = "/news/{}".format(query)
        with open("C:/Users/User/Desktop/HyperNews Portal/HyperNews Portal/task/news.json", 'r') as jfile:
            jlist = json.load(jfile)

        select = [page for page in jlist if query in page['title'].lower() or query.title() in page['title']]
        print(select)
        #except ValueError:
        #   select = [page for page in jlist if page['title'] == query.replace('+','')]
        if select == []:
            raise Http404
        select.sort(key=lambda x: datetime.strptime(x['created'], "%Y-%m-%d %H:%M:%S"), reverse=True)
        all_news = [{'date': date, 'values': list(news)} for date, news in
                    itertools.groupby(select, lambda x: simple_date_fun(x['created']))]
        print(all_news)
        context = dict(title="Hyper news", content=all_news[0]['date'], pages=all_news)
        #return HttpResponseRedirect("news/")
        return render(request, "main.html", context=context)



def future_page(request, *args, **kwargs):
    print(request)
    return HttpResponseRedirect("/news")
# , context=dict(title="Coming soon", content="Coming soon")


def news_page(request, link):
    print(link)
    chosen_page = None
    with open("C:/Users/User/Desktop/HyperNews Portal/HyperNews Portal/task/news.json", 'r') as jfile:
        jlist = json.load(jfile)

    for pages in jlist:
        if pages['link'] == link:
            chosen_page = pages

    print("Chosen", chosen_page)
    return render(request, "index.html", context=chosen_page)

def create_page(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        text = request.POST.get('text')

        with open("C:/Users/User/Desktop/HyperNews Portal/HyperNews Portal/task/news.json", 'r') as jfile:
            jlist = json.load(jfile)
        context = []
        li = random.randint(0, 99999)
        for page in jlist:
            while page['link'] == li:
                link = random.randint(0, 99999)
            else:
                context = [dict(created=datetime.now().strftime("%Y-%m-%d %H:%M:%S"), title=title, text=text,
                                link=li)]
                break
        new_json = jlist + context
        with open("C:/Users/User/Desktop/HyperNews Portal/HyperNews Portal/task/news.json", 'w+') as jfile:
            json.dump(new_json, jfile)
        return redirect('/news/')
    else:
        return render(request, 'create.html', context=dict(title="Create News Page"))
    #def post(self, request, *args, **kwargs):
    #    return HttpResponse("POST")



    #def delete(self, request, *args, **kwargs):
    #    return HttpResponse("delete")
