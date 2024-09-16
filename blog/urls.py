from django.urls import path
from . import views

urlpatterns = [
    # post views
    # function based
    path("", views.post_list, name="post_list"),
    # class based view
    path("", views.PostListView.as_view(), name="post_list"),
    path(
        "<int:year>/<int:month>/<int:day>/<slug:post>/",
        views.post_detail,
        name="post_detail",
    ),
    path("<int:post_id>/share/", views.post_share, name="post_share"),
]
app_name = 'blog'
