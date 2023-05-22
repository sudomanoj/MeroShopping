from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from django.contrib.auth import views as auth_views
from app import views
urlpatterns = [
    path('', views.ProductView.as_view(), name='home'),
    path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='showcart'),
    path('pluscart/', views.plus_cart, name='plus_cart'),
    path('minuscart/', views.minus_cart, name='minus_cart'),
    path('removecart/', views.remove_cart, name='remove_cart'),
    path('search/', views.search, name='search'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),    
    path('changepassword/', auth_views.PasswordChangeView.as_view(template_name='app/passwordchange.html', form_class=views.CustomerPasswordChangeForm, success_url='/passwordchangedone'), name='changepassword'),
    
    path('passwordchangedone/', auth_views.PasswordChangeDoneView.as_view(template_name = 'app/passwordchangedone.html',), name='passwordchangedone'),
    
    path('password-reset', auth_views.PasswordResetView.as_view(template_name='app/password_reset.html', form_class=views.CustomerPasswordResetForm), name='password_reset'),
    
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'), name='password_reset_done'),
    
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html', form_class=views.CustomerSetPasswordForm), name='password_reset_confirm'),
    
    path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'), name='password_reset_complete'),
    
    path('mobile', views.mobile, name='mobile'),
    path('mobile/<slug:data>', views.mobile, name='mobiledata'),
    
    path('checkout/', views.checkout, name='checkout'),
    path('paymentdone/', views.payment_done, name='paymentdone'),
    
    path('laptop', views.laptop, name='laptop'),
    path('laptop/<slug:data>', views.laptop, name='laptopdata'),
    
    path('laptop', views.laptop, name='laptop'),
    path('laptop/<slug:data>', views.laptop, name='laptopdata'),
    
    path('bottomwear', views.bottomwear, name='bottomwear'),
    path('bottomwear/<slug:data>', views.bottomwear, name='bwdata'),
    
    path('topwear', views.topwear, name='topwear'),
    path('topwear/<slug:data>', views.topwear, name='twdata'),
    
    # path('sneakers', views.sneakers, name='sneakers'),
    # path('sneakers/<slug:data>', views.sneakers, name='sneakersdata'),
    
    # path('formal-shoes', views.formal_shoes, name='formalshoes'),
    # path('formal-shoes/<slug:data>', views.formal_shoes, name='formalshoes'),
    
    
    path('accounts/login/', auth_views.LoginView.as_view(template_name='app/login.html', authentication_form=views.LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
