from django.urls import path, re_path
from app.models import Poll
import app.views

app_name = 'app'

urlpatterns = [
    path('',
        app.views.PollListView.as_view(
            queryset=Poll.objects.order_by('-pub_date')[:5],
            context_object_name='latest_poll_list',
            template_name='app/index.html',),
        name='home'),
    re_path('^(?P<pk>\d+)/$',
        app.views.PollDetailView.as_view(
            template_name='app/details.html'),
        name='detail'),
    re_path(r'^(?P<pk>\d+)/results/$',
        app.views.PollResultsView.as_view(
            template_name='app/results.html'),
        name='results'),
    re_path(r'^(?P<poll_id>\d+)/vote/$', app.views.vote, name='vote'),
]
