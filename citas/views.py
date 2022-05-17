from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic, View
from citas.models import Lugares, Critica_sitios
#from django.core.urlresolvers import reverse
from django.views.generic import ListView
from .forms import PostForm, CitasForm
from django.views.generic.edit import FormView

#login
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(generic.ListView):

    template_name = 'citas/index.html'
    context_object_name = 'vista_productos'
    model = Critica_sitios


    def get_context_data(self, **kwargs):
        #No visitado segmento
        context = super(IndexView, self).get_context_data(**kwargs)

        a= Critica_sitios.objects.filter(ya_visitado="False")
        context['titulos'] = a
        c=0
        for a in context['titulos']:
            if c == 0:
                segundo=[a.lugar]
                c=c+1
            else:
                if a.lugar not in segundo:
                    segundo.append(a.lugar)
        
        context['titulos_lugar']=segundo
        #ya visitado

        a1 =Critica_sitios.objects.filter(ya_visitado="True")
        context['titulos2']=a1
        d=0
        for c1 in context['titulos2']:

            if d==0:

                segundo2=[c1.lugar]
                
                d=d+1
            else:
                if  c1.lugar not in segundo2:
                    segundo2.append(c1.lugar)
        cont1=0
        for repetido in context['titulos_lugar']:
            try:
                filtro_f=segundo2.index(repetido)
                segundo2.pop(filtro_f)
            except:
                pass

        try:
            context['titulos_lugar2']=segundo2
            
        except:
            context['titulos_lugar2']="Sin elementos"



        

        return context


        




    def get_queryset(self):
        """DEFINE LISTA DE CONSULTAS"""
        #informacion =Critica_sitios.objects.filter(ya_visitado="True")
        pass
        


        

    
class BaseView(generic.ListView):
    template_name = 'citas/base.html'
    context_object_name = 'vista_productos'
    def get_queryset(self):
        """DEFINE LISTA DE CONSULTAS"""
        pass







class ResenaView(generic.ListView):
    template_name = 'citas/Resena.html'
    context_object_name = 'vista_productos'
    model=Lugares

    def get_context_data(self, **kwargs):

        context = super(ResenaView, self).get_context_data(**kwargs)

        self.filtrado=Lugares.objects.filter(pk = self.kwargs['review'])#filtro de objetos con pk dinamico
       
        self.contenido_lugar =Critica_sitios.objects.filter(lugar= self.kwargs['review'])

        context['contenido_l']=self.contenido_lugar

        context['prueba']=self.filtrado
        suma = 0
        contador=0
        for a in self.contenido_lugar:
            contador = contador + 1
            suma = suma + a.calificacion



        context['final']= suma/contador
       
              
        return context  






class EdicionFormView(LoginRequiredMixin, FormView):
    
    form_class = PostForm
    initial = {'key': 'value'}
    template_name = 'citas/Edicion.html'
    

    def get(self, request, *args, **kwargs):
        form= self.form_class(initial=self.initial)

       
        return render(request, self.template_name, {'form':form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        
        if form.is_valid():
           

           post=form.save()
           

           return HttpResponseRedirect('/citas/edicion_2')

        return render(request, self.template_name, {'form': form})
           
           
            #debo aprender a realizar negociaciones


class EdicionFormView2(LoginRequiredMixin, FormView):
    form_class=CitasForm
    initial={'key':'value'}
    template_name= 'citas/Edicion2.html'
    def get(self, request, *args, **kwargs):
        form = self.form_class(initial = self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request, *args, **kwars):
        form = self.form_class(request.POST)
        if form.is_valid():

            post = form.save()

            return HttpResponseRedirect('/citas')

        return render(request, self.template_name, {'form':form})


class EditFormView(FormView):
    pass




class LogeView(generic.ListView):
    """docstring for LogView"""
    template_name = 'citas/login.html'
    context_object_name = 'vista_productos'
    def get_queryset(self):
        pass




"""
class EdicionFormView(FormView):
    
    form_class = PostForm
    initial = {'key': 'value'}
    template_name = 'citas/Edicion.html'
    success_url = 'citas:resena'

    def get(self, request, *args, **kwargs):
        form= self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        def form_valid(self, form):
           
            form=post.save()
            return super().form_valid(form)
            #debo aprender a realizar negociaciones
"""        