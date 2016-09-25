"""recruit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from core.views import home
from contas import views as contas_views
from core import views as core_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^login/$', contas_views.Login.as_view(), name='login'),
    # Views de contratante
    url(r'^contratante/new/$', contas_views.ContratanteCreate.as_view(), name='contratante_new'),
    url(r'^contratante/(?P<pk>[0-9]+)/$', contas_views.ContratanteUpdate.as_view(), name='contratante_edit'),
    url(r'^contratantes/$', contas_views.ContratanteListView.as_view(), name='contratante_list'),
    url(r'^contratante/(?P<pk>[0-9]+)/delete/$', contas_views.ContratanteDelete.as_view(), name='contratante_delete'),
    # Views de candidato
    url(r'^candidato/new/$', contas_views.CandidatoCreate.as_view(), name='candidato_new'),
    url(r'^candidato/(?P<pk>[0-9]+)/$', contas_views.CandidatoUpdate.as_view(), name='candidato_edit'),
    url(r'^candidatos/$', contas_views.CandidatoListView.as_view(), name='candidato_list'),
    url(r'^candidato/(?P<pk>[0-9]+)/delete/$', contas_views.CandidatoDelete.as_view(), name='candidato_delete'),
    # Views de recrutador
    url(r'^recrutador/new/$', contas_views.RecrutadorCreate.as_view(), name='candidato_new'),
    url(r'^recrutador/(?P<pk>[0-9]+)/$', contas_views.RecrutadorUpdate.as_view(), name='candidato_edit'),
    url(r'^recrutadors/$', contas_views.RecrutadorListView.as_view(), name='candidato_list'),
    url(r'^recrutador/(?P<pk>[0-9]+)/delete/$', contas_views.RecrutadorDelete.as_view(), name='candidato_delete'),
    # Views de empresa
    url(r'^empresa/new/$', core_views.EmpresaCreate.as_view(), name='empresa_new'),
    url(r'^empresa/(?P<pk>[0-9]+)/$', core_views.EmpresaUpdate.as_view(), name='empresa_edit'),
    url(r'^empresas/$', core_views.EmpresaListView.as_view(), name='empresa_list'),
    url(r'^empresa/(?P<pk>[0-9]+)/delete/$', core_views.EmpresaDelete.as_view(), name='empresa_delete'),
    # Views de vaga
    url(r'^vaga/new/$', core_views.VagaCreate.as_view(), name='vaga_new'),
    url(r'^vaga/(?P<pk>[0-9]+)/$', core_views.VagaUpdate.as_view(), name='vaga_edit'),
    url(r'^vagas/$', core_views.VagaListView.as_view(), name='vaga_list'),
    url(r'^vaga/(?P<pk>[0-9]+)/delete/$', core_views.VagaDelete.as_view(), name='vaga_delete'),
    # Views de Area de Atuação
    url(r'^area_atuacao/new/$', core_views.AreaAtuacaoCreate.as_view(), name='area_atuacao_new'),
    url(r'^area_atuacao/(?P<pk>[0-9]+)/$', core_views.AreaAtuacaoUpdate.as_view(), name='area_atuacao_edit'),
    url(r'^area_atuacoes/$', core_views.AreaAtuacaoListView.as_view(), name='area_atuacao_list'),
    url(r'^area_atuacao/(?P<pk>[0-9]+)/delete/$', core_views.AreaAtuacaoDelete.as_view(), name='area_atuacao_delete'),

]
