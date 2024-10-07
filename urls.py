# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve
from django.views.i18n import JavaScriptCatalog
from django.shortcuts import render

js_info_dict = {
    'packages': ('helios', 'helios_auth'),
}

admin.autodiscover()

urlpatterns = [
    url(r'^auth/', include('helios_auth.urls')),
    url(r'^helios/', include('helios.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^jsi18n/$', JavaScriptCatalog.as_view(), name='i18n@JSCatalog'),

    #Ajuda-Gestor
    url(r'^ajuda-gestor/$', lambda request: render(request, 'ajuda-gestor/index.html'), name='ajuda-gestor'),
    url(r'^ajuda-gestor/eleitor/$', lambda request: render(request, 'ajuda-gestor/eleitor/index.html'), name='ajuda-gestor-eleitor'),
    url(r'^ajuda-gestor/criar/$', lambda request: render(request, 'ajuda-gestor/criar/index.html'), name='ajuda-gestor-criar'),
    url(r'^ajuda-gestor/abrir/$', lambda request: render(request, 'ajuda-gestor/abrir/index.html'), name='ajuda-gestor-abrir'),
    url(r'^ajuda-gestor/fechar/$', lambda request: render(request, 'ajuda-gestor/fechar/index.html'), name='ajuda-gestor-fechar'),
    url(r'^ajuda-gestor/estatisticas/$', lambda request: render(request, 'ajuda-gestor/estatisticas/index.html'), name='ajuda-gestor-estatisticas'),
    url(r'^ajuda-gestor/apurador-gerar/$', lambda request: render(request, 'ajuda-gestor/apurador-gerar/index.html'), name='ajuda-gestor-apurador-gerar'),
    url(r'^ajuda-gestor/apurador-usar/$', lambda request: render(request, 'ajuda-gestor/apurador-usar/index.html'), name='ajuda-gestor-apurador-usar'),
    url(r'^ajuda-gestor/faq/$', lambda request: render(request, 'ajuda-gestor/faq/index.html'), name='ajuda-gestor-faq'),

    #Ajuda-Usuario
    url(r'^ajuda/$', lambda request: render(request, 'ajuda/index.html'), name='ajuda'),
]

if settings.AUTH_DEFAULT_AUTH_SYSTEM == 'shibboleth':
    urlpatterns += [
        url(r'^', include('heliosinstitution.urls')),
    ]
else:
    urlpatterns += [
        url(r'^', include('server_ui.urls')),

    ]

if settings.DEBUG:  # otherwise, they should be served by a webserver like apache
    urlpatterns += [
        # SHOULD BE REPLACED BY APACHE STATIC PATH
        url(r'booth/(?P<path>.*)$', serve, {'document_root' : settings.ROOT_PATH + '/heliosbooth'}),
        url(r'verifier/(?P<path>.*)$', serve, {'document_root' : settings.ROOT_PATH + '/heliosverifier'}),

        url(r'static/auth/(?P<path>.*)$', serve, {'document_root' : settings.ROOT_PATH + '/helios_auth/media'}),
        url(r'static/helios/(?P<path>.*)$', serve, {'document_root' : settings.ROOT_PATH + '/helios/media'}),
        url(r'static/heliosinstitution/(?P<path>.*)$', serve, {'document_root' : settings.ROOT_PATH + '/heliosinstitution/media'}),
        url(r'static/(?P<path>.*)$', serve, {'document_root' : settings.ROOT_PATH + '/server_ui/media'}),
    ]
