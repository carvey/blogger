from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext
from django.views.generic import View

class Index(View):
    template = 'blogger/index.html'

    def get(self, request):
        return render(request, self.template, {})

