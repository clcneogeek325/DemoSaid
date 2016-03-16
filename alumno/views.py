from django.shortcuts import render_to_response
from django.template  import RequestContext
from alumno.models import alumno
from alumno.forms import alumnoForm
from django.http import HttpResponseRedirect


def index(request):
	lista_alumnos = alumno.objects.all()
	ctx = {'alumnos':lista_alumnos}
	return render_to_response("alumno/index.html",ctx,
		context_instance=RequestContext(request))



def view_add(request):
	if request.method == "POST":
		form = alumnoForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/")
		else:
			form  = alumnoForm()
			msg="Revisa bien los datos"
			ctx = {'form':form,'msg':msg}
			return render_to_response('alumno/add.html',ctx,
				context_instance=RequestContext(request))

	else:
		form = alumnoForm()
		msg="Ingresa los datos"
		ctx = {'form':form,'msg':msg}
		return render_to_response('alumno/add.html',ctx,
				context_instance=RequestContext(request))



def view_add(request):
	if request.method == "POST":
		form = alumnoForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/")
		else:
			form  = alumnoForm()
			msg="Revisa bien los datos"
			ctx = {'form':form,'msg':msg}
			return render_to_response('alumno/add.html',ctx,
				context_instance=RequestContext(request))

	else:
		form = alumnoForm()
		msg="Ingresa los datos"
		ctx = {'form':form,'msg':msg}
		return render_to_response('alumno/add.html',ctx,
				context_instance=RequestContext(request))




def view_edit(request,id):
	p = alumno.objects.get(pk=id)
	if request.method == "POST":
		form = alumnoForm(request.POST,instance=p)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/alumnos/")
		else:
			form = alumnoForm(p)
			msg="Revisa bien los datos"
			ctx = {'form':form,'msg':msg}
			return render_to_response('alumno/edit.html',ctx,
				context_instance=RequestContext(request))

	else:
		form = alumnoForm(instance=p)
		msg="Ingresa los datos"
		ctx = {'form':form,'msg':msg}
		return render_to_response('alumno/edit.html',ctx,
				context_instance=RequestContext(request))



def view_del(request,id):
	p = alumno.objects.get(pk=id)
	p.delete()
	return HttpResponseRedirect("/")
