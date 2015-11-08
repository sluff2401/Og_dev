from django.conf             import settings
from django.conf.urls.static import static
from django.conf.urls        import url
from .                       import views

urlpatterns = [
    url(r'^$',                                              views.event_list,       name='event_list'),
    url(r'^past$',                                          views.event_list_past,       name='event_list_past'),
    #url(r'^event/(?P<pk>[0-9]+)/$',                        views.event_detail,     name='event_detail'),
    url(r'^event/new/$',                                    views.event_new,        name='event_new'),
    url(r'^event/new/past/$',                               views.event_new_past,        name='event_new_past'),
    url(r'^event/(?P<period>[01])(?P<pk>[0-9]+)/edit/$',    views.event_edit,       name='event_edit'),
    url(r'^event/(?P<period>[01])(?P<pk>[0-9]+)/remove/$',  views.event_remove,     name='event_remove'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
