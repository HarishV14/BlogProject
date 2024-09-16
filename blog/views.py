from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage,\
 PageNotAnInteger

""" Class based view --- generic view
HTTP methods, such as GET, POST, or PUT, in
separate methods, instead of using conditional branching

Using multiple inheritance to create reusable view classes (also known as
mixins)

like this should be used in the pagination 
for class based{% include "pagination.html" with page=page_obj %}

"""
from django.views.generic import ListView

class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = "posts"
    paginate_by = 2
    template_name = "blog/post/list.html"

# function based view
def post_list(request):
    posts = Post.published.all()
    paginator = Paginator(posts, 1) # 1 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
    # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
    # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)

    return render(request,
        'blog/post/list.html',{'page': page,'posts': posts})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        slug=post,
        status="published",
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )

    return render(request, "blog/post/detail.html", {"post": post})
