from django.conf.urls import url
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    # I'll keep this here for compatibility with links shared
    # on Facebook.
    url(r'^new/$', RedirectView.as_view(pattern_name='meupet:register', permanent=True)),
    url(r'^search/$', RedirectView.as_view(pattern_name='meupet:search', permanent=True)),
    url(r'^lost/(?P<kind>[0-9]+)/$', RedirectView.as_view(pattern_name='meupet:lost', permanent=True)),
    url(r'^adoption/(?P<kind>[0-9]+)/$', RedirectView.as_view(pattern_name='meupet:adoption', permanent=True)),

    url(r'^$', views.PetIndexView.as_view(), name='index'),
    url(r'^novo/$', views.RegisterPetView.as_view(), name='register'),
    url(r'^desaparecidos/(?P<kind>[-\w]*)/$', views.lost_pets, name='lost'),
    url(r'^para-adocao/(?P<kind>[-\w]*)/$', views.adoption_pets, name='adoption'),
    url(r'^busca/$', views.SearchView.as_view(), name='search'),
    url(r'^atualizar-cadastro/(?P<request_key>\w+)/$', views.update_register, name='update_register'),
    url(r'^pet/(?P<slug>[-\w]*)/foto/$', views.upload_image, name='upload_image'),
    url(r'^(?P<slug>[-\w]*)/editar/$', views.EditPetView.as_view(), name='edit'),
    url(r'^(?P<slug>[-\w]*)/poster/$', views.poster, name='poster'),
    url(r'^(?P<slug>[-\w]*)/editar/situacao/$', views.change_status, name='change_status'),
    url(r'^(?P<slug>[-\w]*)/deletar/$', views.delete_pet, name='delete_pet'),
    url(r'^(?P<slug>[-\w]*)/registrado/$', views.registered, name='registered'),

    url(r'^(?P<pk_or_slug>[-\w]*)/$', views.pet_detail_view, name='detail'),
    url(r'^(?P<pk>[0-9]+)/$', views.pet_detail_view, name='detail_by_pk'),
]
