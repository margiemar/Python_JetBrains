import itertools
from datetime import datetime
import random

from django.shortcuts import render, redirect
from django.views import View
from django.http.response import HttpResponse
import json
from hypernews import settings

class Service:

    @classmethod
    def json_read(cls):
        with open (settings.NEWS_JSON_PATH) as json_file:
            return json.load(json_file)

    @classmethod
    def dict_from_json_content(cls):
        articles = dict()
        content = cls.json_read()
        for item in content:
            articles[item["link"]] = item
        return articles

    @classmethod
    def json_write(cls, news_text):
        with open (settings.NEWS_JSON_PATH, 'w') as json_file:
            json.dump(news_text, json_file)

class WelcomeView(View):
    def get(self, request):
        return HttpResponse('Coming soon')

class InfoView(View):

    def get(self, request, link_identifier):

        context = dict()
        articles = Service.dict_from_json_content()

        for key in articles[link_identifier]:
            context[key] = articles[link_identifier][key]

        return render(request, 'newspage.html', context=context)

class AllNewsView(View):
    def get(self, request):

        search_title = request.GET.get("q")
        content = Service.json_read()

        def simple_date(date):
            return datetime.strptime(date, "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d")

        if search_title:
            for page in content:
                if search_title in page["title"]:
                    searched_news = [{'date': simple_date(page["created"]), 'values': [page]}]
                    return render(request, 'mainpage.html', context={"all_news_sorted": searched_news})

            all_news_sorted = [{'date': '', 'values': [{'created': None, 'text': None, 'title': '', 'link': None}]}]
            return render(request, 'mainpage.html', context={"all_news_sorted": all_news_sorted})
        else:
            content.sort(key=lambda x: datetime.strptime(x['created'], "%Y-%m-%d %H:%M:%S"), reverse=True)



            all_news_sorted = [{'date': date, 'values': list(news)} for date, news in
                    itertools.groupby(content, lambda x: simple_date(x['created']))]

            return render(request, 'mainpage.html', context={'all_news_sorted': all_news_sorted})


class CreateNewView(View):
    def post(self,request):
        title = request.POST.get("title")
        text = request.POST.get("text")
        created = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        link = random.randint(10, 1000000)
        new_news = {"created": created,
                    "text": text,
                    "title": title,
                    "link": link}

        update_news = Service.json_read()
        update_news.append(new_news)
        Service.json_write(update_news)
        return redirect('/news/')

    def get(self, request):
        return render(request, 'create_news.html')
