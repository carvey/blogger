from django.shortcuts import render
from django.views.generic import View

from zinnia.models import Category, Entry

class Index(View):
    template = 'blogger/index.html'

    def get(self, request):
        return render(request, self.template, {})


class CategoryView(View):
    template = ''

    def get(self, request):
        return render(request, self.template, {})


class PostView(View):
    template = 'blogger/post.html'

    def get(self, request, requested_category, id):
        category = Category.objects.get(title=requested_category)
        entry = Entry.objects.get(id=id)

        return render(request, self.template, {'category': category,
                                               'entry': entry,
                                               })