"""vello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
import velo.views
import object.views
import registration.views
import articles.views
import about.views
import navigator.views
import accounts.views
import save.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', velo.views.showmain, name='showmain'),

    path('<int:marsh_id>/', velo.views.showoMarsh, name='showoMarsh'),
    path('/articles', articles.views.showarticles, name='articles'),
    path('/articles/<int:article_id>/', articles.views.specific_article, name='specific_article'),
    path('/objects', object.views.showobject, name='objects'),
    path('/objects/<int:object_id>/', object.views.specific_object, name='specific_object'),
    path('registration', registration.views.signup, name='registration'),
    path('/navigator', navigator.views.navigator, name='navigator'),
    path('saved', save.views.cart_detail, name='saved'),
    path('cart/add/<int:marsh_id>user', save.views.add_cart, name='add_cart'),
    path('/about', about.views.about, name='about'),
    path('login/', accounts.views.LoginView.as_view(), name='login'),
    path('logout/', accounts.views.LogoutView.as_view(), name='logout'),
    path('password-reset/', accounts.views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', accounts.views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', accounts.views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', accounts.views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('password-change/', accounts.views.PasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', accounts.views.PasswordChangeDoneView.as_view(), name='password_change_done'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
