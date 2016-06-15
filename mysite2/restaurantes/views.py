from django.views.generic import CreateView,TemplateView,ListView,DeleteView,RedirectView
from .models import Restaurate
from django.core.urlresolvers import reverse_lazy, reverse


class RegistrarRestaurante(CreateView):
	template_name = 'restaurantes/registrar.html'
	fields="__all__"
	model = Restaurate
	success_url = reverse_lazy('restaurantes:reportar_restaurante')

class ResutanteView(RedirectView):
	def get_redirect_url(self,*args, **kwargs):
		Restaurate = Restaurate.objects.get(id=kwargs.get('pk'))
		Restaurate.status = Restaurate.status_deleted
		Restaurate.save()
		return reverse('restaurantes:reportar_restaurante')

class ReportarRestaurante(ListView):
	template_name = 'restaurantes/reportar.html'
	model = Restaurate
	def get_queryset(self):
		return Restaurate.active.filter(status = Restaurate.status_active)


class EliminarRestaurante(DeleteView):
	model = Restaurate
	success_url = reverse_lazy('restaurantes:reportar_restaurante')
