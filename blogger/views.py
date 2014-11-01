from django.shortcuts import render
from django.views.generic import View

from zinnia.models import Category, Entry

UNIVERSAL_CONTEXT = {
    'categories': Category.objects.all()
}


class Index(View):
    template = 'blogger/index.html'

    def get(self, request):
        entries = Entry.objects.all().order_by('-creation_date')

        context = {'entries': entries}
        context.update(UNIVERSAL_CONTEXT)
        return render(request, self.template, context)


class CategoryView(View):
    template = 'blogger/category.html'

    def get(self, request, cat):
        entries = Entry.objects.filter(categories__slug=cat)
        category = Category.objects.get(slug=cat)
        context = {'entries': entries,
                   'category': category}
        context.update(UNIVERSAL_CONTEXT)
        return render(request, self.template, context)


class PostView(View):
    template = 'blogger/post.html'

    def get(self, request, requested_category, slug):
        category = Category.objects.get(slug=requested_category)
        entry = Entry.objects.get(slug=slug)

        context = {'category': category,
                   'entry': entry,
                   }
        context.update(UNIVERSAL_CONTEXT)
        return render(request, self.template, context)