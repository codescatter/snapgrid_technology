"""snapgrid URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views
from myapp.form import PassResetForm,SetNewPassForm
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('contact', views.contact, name="contact"),
    path('services', views.services, name="services"),
    path('about', views.about, name="about"),
    path('php_project', views.php_project, name="php_project"),
    path('ai_project', views.ai_project, name="ai_project"),
    path('ml_project', views.ml_project, name="ml_project"),
    path('django_project', views.django_project, name="django_project"),
    path('python_project', views.python_project, name="python_project"),
    path('java_project', views.java_project, name="java_project"),
    path('asp_net_project', views.asp_net_project, name="asp_net_project"),
    path('android_project', views.android_project, name="android_project"),
    path('app_dev', views.app_dev, name="app_dev"),
    path('digital_marketing', views.digital_marketing, name="digital_marketing"),
    path('ecommerce', views.ecommerce, name="ecommerce"),
    path('hosting', views.hosting, name="hosting"),
    path('ml', views.ml, name="ml"),
    path('my_account', views.my_account, name="my_account"),
    path('seo', views.seo, name="seo"),
    path('support', views.support, name="support"),
    path('php_intern', views.php_intern, name="php_intern"),
    path('Ml_intern', views.Ml_intern, name="Ml_intern"),
    path('Android_intern', views.Android_intern, name="Android_intern"),
    path('Java_intern', views.Java_intern, name="Java_intern"),
    path('Ds_intern', views.Ds_intern, name="Ds_intern"),
    path('Ai_intern', views.Ai_intern, name="Ai_intern"),
    path('Python_intern', views.Python_intern, name="Python_intern"),
    path('Django_intern', views.Django_intern, name="Django_intern"),
    path('ui', views.ui, name="ui"),
    path('web_design', views.web_design, name="web_design"),
    path('web_development', views.web_development, name="web_development"),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('login_form/', views.login_form, name='login_form'),
    path('signup_form/', views.signup_form, name='signup_form'),
    path('change_password/', views.change_password, name='change_password'),
    path('Logout/', views.Logout, name='Logout'),
    
    
    #Password Reset
    path("password_reset/", auth_views.PasswordResetView.as_view(template_name='password_reset.html',form_class=PassResetForm), name="password_reset"),
    path("password_reset_done/", auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name="password_reset_done"),
    path("password_reset_confirm/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html',form_class=SetNewPassForm), name="password_reset_confirm"),
    path("password_reset_complete/", auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name="password_reset_complete"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
