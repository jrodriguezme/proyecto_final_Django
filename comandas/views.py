from django.shortcuts import render
from django.forms import formset_factory
from django.forms.models import inlineformset_factory
from django.views.generic.edit import FormView
from .models import Formato
from persona.models import Personal 
from .models import Pedido
from django.urls import reverse_lazy
from django.urls import reverse
from .forms import addForm,pedidoForm
from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
	UpdateView,
	DeleteView,
	)

from django.http import HttpResponseRedirect
pedidoFormSet=inlineformset_factory(Formato,Pedido,form=pedidoForm,extra=1)
# Create your views here.
def comandas(request):
	personas=Personal.objects.all()
	return render(request,'comandas/comandas.html',{'personas':personas})

class agregar(CreateView):
	id=0
	model=Formato
	template_name='comandas/formato_form.html'
	form_class=addForm

	def get_context_data(self,**kwargs):
		context=super(agregar,self).get_context_data(**kwargs)

		context['form2']=pedidoFormSet(instance=Pedido())
		# if 'form' not in context:
		# 	context['form']=self.form_class(self.request.GET)
		# if 'form2' not in context:
		# 	context['form2']=self.second_form_class(self.request.GET)
		return context

	def post(self,request,*args,**kwargs):
		#self.object=self.get_object
		form=self.form_class(request.POST)
		# form2=self.second_form_class(request.POST)
		form2=pedidoFormSet(request.POST)

		if form.is_valid() and form2.is_valid():
			return self.form_valid(form,form2)
			# pedido=form.save(commit=False)
			# pedido.formato=form2.save()
			# pedido.save()
			# return HttpResponseRedirect(self.get_success_url())
		else:
			return self.form_invalid(form,form2)
			#return self.render_to_response(self.get_context_data(form=form,form2=form2))
	def form_valid(self,form,form2):
		self.object=form.save()
		id=Formato.objects.count()
		print("id es : ",id)
		for f in form2:
			form_dato=f.cleaned_data
			nom_plato=form_dato.get("platos")
			num_de_platos=form_dato.get("num_platos")
			#vinculo=form_dato.get("vincu")
			f.instance=self.object
			obj=Pedido.objects.create(platos=nom_plato,num_platos=num_de_platos)
			f.save()
		
		# form2.instance=self.object
		# form2.save()
		return HttpResponseRedirect(self.get_success_url())

	def form_invalid(self,form,form2):
		return self.render_to_response(self.get_context_data(form=form,form2=form2))

	def get_success_url(self):
		return reverse('comandas:agregar_comandas')


	# #formato_form=addForm
	# form_class=formset_factory(pedidoForm,extra=1)
	# extra_context = { 'formato_form': addForm(prefix='formato')}
	# #success_url=reverse('comandas:detalles_comandas', kwargs = {'pk': self.id})
	# formato=addForm
	# def form_valid(self,form):
	# 	for f in form:
	# 		form_dato=f.cleaned_data
	# 		nom_plato=form_dato.get("platos")
	# 		num_de_platos=form_dato.get("num_platos")
	# 		obj=Pedido.objects.create(platos=nom_plato,num_platos=num_de_platos)
	# 		f.save
	# 	num_pedi=form.numero_comanda
	# 	obj=Formato.objects.create(numero_comanda=num_pedi)
	# 	formato.save
	# 	return super(agregar,self).form_valid(form)
	
	# success_url="."
	


def detalles(request,*args,**kwargs):
	modelo1=Formato.objects.all()
	modelo2=Pedido.objects.all()
	pru=str(request)
	x= pru.index("d")
	i=x+4
	num=""
	while i<len(pru):
		if pru[i]!="/":
			num=num+pru[i]
			i=i+1
		else:
			i=len(pru)
	num=int(num)
	modelo3=[]
	modelo4=[]
	texto="Formato object ("+str(num)+")"

	for model in modelo1:
		if str(model) == str(texto):
			modelo3=model
	
	for model in modelo2:
		print(model.codigo)
		if int(modelo3.numero_comanda) ==int(model.codigo):
			modelo4.append(model)
			
	print(modelo3.numero_comanda)
	#modelo1=Formato.objects.filter(numero_comanda=num)
	#print(modelo1.numero_comanda)
	return render(request,'comandas/formato_detail.html',{'modelo3':modelo3,'modelo4':modelo4})


class listar(ListView):
	model=Pedido
	template_name = 'comandas/formato_lista.html'
	context_object_name = 'Formato'
	def get_context_data(self, **kwargs):
		context = super(listar, self).get_context_data(**kwargs)
		context['Pedido'] = Pedido.objects.all()
		return context

	def get_queryset(self):
		lista = Formato.objects.all()
		return lista



def modificar2(request):
	object_list=Formato.objects.all()
	return render(request,'comandas/formato_modificar.html',{'object_list':object_list})

class modificar(UpdateView):
	model = Formato
	fields = [
		'hora_marca',
		'fecha_hoy',
		'numero_comanda',
		'numero_mesa',
		'numero_comensales',
		'id_camarero',
	]
	template_name_suffix = '_update_form'

class eliminar(DeleteView):
	model = Formato
	success_url = reverse_lazy('comandas:listar_comandas')

def eliminar2(request):
	model = Formato
	object_list=Formato.objects.all()
	success_url = reverse_lazy('comandas:listar_comandas')
	return render(request,'comandas/formato_eliminar.html',{'object_list':object_list})


