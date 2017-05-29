from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from Aapp.models import Blog
from django.shortcuts import render_to_response, get_object_or_404
from django.forms import ModelForm
from django.contrib.auth.models import User
global user_id 



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('server_list')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
	

class ServerForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['title','category','Image','content']
	
def server_list(request, template_name='server_list.html'):
    Aapp = Blog.objects.all()
    data = {}
    data['object_list'] = Aapp
    return render(request, template_name, data)
	
	
def server_create(request, template_name='server_form.html'):
    form = ServerForm(request.POST or None)
    if form.is_valid():
		Blog =form.save(commit=False)
		Blog.Image=request.FILES['Image']
		Blog.user=request.user
		Blog.save()
		return redirect('server_list')
    return render(request, template_name, {'form':form})
	
	
def server_create1(request, template_name='img.html'):
    Aapp = Blog.objects.all()
    data = {}
    data['object_list'] = Aapp
    return render(request, template_name, data)
	
def server_create2(request, template_name='update.html'):
 
    Aapp = Blog.objects.filter(user=request.user)
    data = {}
    data['object_list'] = Aapp
    return render(request, template_name, data)
	


	
def server_update(request, pk, template_name='update_form.html'):
    blog = get_object_or_404(Blog, pk=pk)
    form = ServerForm(request.POST or None,request.FILES or None, instance=blog)
    if form.is_valid():
        form.save()
        return redirect('server_list')
    return render(request, template_name, {'form':form})

def server_delete(request, pk, template_name='server_confirm_delete.html'):
    blog = get_object_or_404(Blog, pk=pk)    
    if request.method=='POST':
        blog.delete()
        return redirect('server_list')
    return render(request, template_name, {'object':blog})