from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import PostForm


# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    order_comments = {}
    for p in posts:
        comments = Comment.objects.filter(post=p)
        order_comments[p] = comments
    ctx = {
        'order_comments': order_comments,
    }
    return render(request, 'posts/post_list.html', context=ctx)

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts:post_list')
        else:
            ctx = {
                'form': form,
            }
            return render(request, 'posts/post_new.html', ctx)
    elif request.method == 'GET':
        form = PostForm()
        ctx = {
            'form': form,
        }
        return render(request, 'posts/post_new.html', ctx)


import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# {% csrf_token %}
@csrf_exempt
def like_ajax(request):
    req = json.loads(request.body)  
    post_id = req['id']

    post = Post.objects.get(id=post_id)

    post.like += 1
    
    post.save()

    return JsonResponse({'id' : post_id })  


# {% csrf_token %}
@csrf_exempt
def delete_ajax(request):
    req = json.loads(request.body) 
    comment_id = req['id']

    comment = Comment.objects.get(id=comment_id)

    comment.delete()

    return JsonResponse({'id' : comment_id })



# {% csrf_token %}
@csrf_exempt
def post_ajax(request):
    req = json.loads(request.body) 
    post_id = req['id']
    post_content = req['content']

    reply = Comment.objects.create(post=Post.objects.get(id=post_id), content=post_content)
    reply.save()
        

    return JsonResponse({'id' : post_id, 'content' : post_content, 'comment_id' : reply.id})
