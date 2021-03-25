from django.urls import path

from . import views #, LogMessage

"""
home_list_view = views.HomeListView.as_view(
    #queryset=LogMessage.objects.order_by("-log_date")[:5],  # :5 limits the results to the five most recent
    context_object_name="message_list",
    template_name="HelloDjangoApp/index.html",
)
"""

urlpatterns = [
    path("", views.index, name='index'),
    path("home", views.index, name='home'),

    # Added with tutorial step 3-3
    path("about", views.about, name='about'),
]
