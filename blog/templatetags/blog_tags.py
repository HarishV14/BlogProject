from django import template
from ..models import Post

register = template.Library()


@register.simple_tag
def total_posts():
    return Post.published.count()


@register.inclusion_tag("blog/post/latest_posts.html")
def show_latest_posts(count=1):
    latest_posts = Post.published.order_by("-publish")[:count]
    return {"latest_posts": latest_posts}

from django.db.models import Count


@register.inclusion_tag("blog/post/most_comment_posts.html")
def get_most_commented_posts(count=1):
    CommentPost = Post.published.annotate(total_comments=Count("comments")).order_by(
        "-total_comments"
    )[:count]
    return {"CommentPost": CommentPost}


from django.utils.safestring import mark_safe
import markdown


@register.filter(name="markdown")
def markdown_format(text):
    return mark_safe(markdown.markdown(text))
