from django.conf.urls import url
from wimm import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.user_login, name='user_login'),
    url(r'^logout/$', views.user_logout, name='user_logout'),
    url(r'^add/$', views.add_wimm, name='add_wimm'),
    url(r'^add_wimm_for_date/(?P<day>[1-9]|[12]\d|3[01])/(?P<month>[1-9]|1[012])/(?P<year>2\d{3})/$', views.add_wimm_for_date, name='add_wimm_for_date'),
    url(r'^edit/(?P<wimm_id>\d+)/$', views.edit_wimm, name='edit_wimm'),
    url(r'^trash/$', views.show_trash, name='show_trash'),
    url(r'^trash/(?P<wimm_id>\d+)/$', views.trash_wimm, name='trash_wimm'),
    url(r'^restore/(?P<wimm_id>\d+)/$', views.restore_wimm, name='restore_wimm'),
    url(r'^delete/(?P<wimm_id>\d+)/$', views.delete_wimm, name='delete_wimm'),
    url(r'^state/edit/(?P<day>[1-9]|[12]\d|3[01])/(?P<month>[1-9]|1[012])/(?P<year>2\d{3})/$', views.edit_state, name='edit_state'),
    url(r'^state/add/$', views.add_state, name='add_state'),
    url(r'^state/del/(?P<state_id>\d+)/$', views.del_state, name='del_state'),
    url(r'^(?P<day>[1-9]|[12]\d|3[01])/(?P<month>[1-9]|1[012])/(?P<year>2\d{3})/$', views.show_day, name='show_day'),
]
