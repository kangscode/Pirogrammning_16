from urllib import request
from django.shortcuts import render, get_object_or_404, redirect
from .models import Devtool, Idea
from .forms import IdeaForm, DevtoolForm

# Create your views here.
def idea_list(request):
    ideas = Idea.objects.all()
    ctx = {'ideas' : ideas}

    return render(request, template_name='idea_list.html', context=ctx)

def idea_create(request):
    if request.method == 'POST': 
        form = IdeaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ideas:idea_list')
        # idea = Idea()
        # idea.title = request.POST['title']
        # idea.image = request.FILES['poster']
        # idea.content = request.POST['content']
        # idea.interest = request.POST['interest']
        # devtool_name = request.POST['devtool']
        # devt = Devtool.objects.get(name=devtool_name)
        # idea.devtool = devt
        # idea.save()
        # return redirect('ideas:idea_list')
    else: #request.method == 'GET'
        form = IdeaForm()
        ctx = {'form' : form}

        return render(request, template_name='idea_create.html', context=ctx)

def idea_detail(request, pk):
    idea = Idea.objects.get(id=pk)
    ctx = {'idea' : idea}

    return render(request, template_name='idea_detail.html', context=ctx)

def idea_update(request, pk):
    idea = get_object_or_404(Idea, id=pk)

    if request.method == 'POST':
        form = IdeaForm(request.POST, instance=idea)
        if form.is_valid():
            form.save()
            return redirect('ideas:idea_detail', pk)
    else:
        form = IdeaForm(instance=idea)
        ctx = {'form' : form, 'idea': idea}
        
        return render(request, template_name='idea_create.html', context=ctx)

def idea_delete(request, pk):
    idea = Idea.objects.get(id=pk)
    idea.delete()
    return redirect('ideas:idea_list')

def devt_create(request):
    if request.method == 'POST': 
        devt = Devtool()
        devt.name = request.POST['name']
        devt.kind = request.POST['kind']
        devt.description = request.POST['description']
        devt.save()

        return redirect('ideas:devt_list')
    else: #request.method == 'GET'

        return render(request, template_name='devt_create.html')

def devt_list(request):
    devts = Devtool.objects.all()
    ctx = {'devts' : devts}

    return render(request, template_name='devt_list.html', context=ctx)

def devt_detail(request, pk):
    devt = Devtool.objects.get(id=pk)
    ideas = devt.idea_set.all()
    ctx = {
        'devt' : devt,
        'ideas' : ideas,
    }

    return render(request, template_name = 'devt_detail.html', context=ctx)

def devt_update(request,pk):
    devt = get_object_or_404(Devtool, id=pk)

    if request.method == 'POST':
        devt.name = request.POST['name']
        devt.kind = request.POST['kind']
        devt.description = request.POST['description']
        devt.save()
        
        return redirect('ideas:devt_detail', pk)
    else:
        # form = DevtoolForm(instance = devt)
        ctx = {'devt':devt}

        return render(request, template_name='devt_create.html', context=ctx)

def devt_delete(request, pk):
    devt = get_object_or_404(Devtool, id=pk)
    devt.delete()
    return redirect('ideas:devt_list')

