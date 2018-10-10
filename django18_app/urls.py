from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views
from django18_app.apps.profiles.forms import LoginForm, RegistrationForm
from django18_app.apps.profiles.views import register


urlpatterns = [
    # Examples:
    # url(r'^$', 'django18_app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'', include('django18_app.apps.profiles.urls')),
    url(r'^login/$', views.login, {'template_name': 'login.html', 'authentication_form': LoginForm}),
    url(r'^logout/$', views.logout,  {'next_page': '/login'}),
    url(r'^register/$', register ,name='register'),
]
