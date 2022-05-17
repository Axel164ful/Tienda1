from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic




class IndexView(generic.ListView):
    template_name = 'cyber/index.html'
    context_object_name = 'vista_productos'

    def get_context_data(self, **kwargs):


        context = super(IndexView, self).get_context_data(**kwargs)

        context['some_data'] = 'NUESTRA UBICACIÓN'
        return context


    def get_queryset(self):
        """Return the last five published questions."""
        pass
