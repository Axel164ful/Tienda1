from django import forms

from .models import  Lugares, Critica_sitios

class PostForm(forms.ModelForm):

    class Meta:
        model = Lugares
       	fields = ('Sujeto',)


class CitasForm(forms.ModelForm):
	class Meta:
		model = Critica_sitios
		fields = ('opinion', 'calificacion','evaluador', 'ya_visitado', 'lugar')
			
