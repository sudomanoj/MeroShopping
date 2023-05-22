from django.shortcuts import render, redirect
from django.views import View
from app.models import Customer, Cart, OrderedPlaced, Product
from app.forms import *
from django.contrib import messages
from app.forms import LoginForm
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class ProductView(View):
    def get(self, request):
        topwears = Product.objects.filter(category='TW')
        bottomwears = Product.objects.filter(category='BW')
        mobiles = Product.objects.filter(category='M')
        laptops = Product.objects.filter(category='L')
        count = ''
        if request.user.is_authenticated:
            count = Cart.objects.filter(user=request.user).count()
        context = {
            'topwears' : topwears,
            'bottomwears' : bottomwears,
            'mobiles' : mobiles,
            'laptops' : laptops,
            'count' :count,
        }
        return render(request, 'app/home.html', context)
    

class ProductDetailView(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        item_already_in_cart = False
        count = ''
        if request.user.is_authenticated:
            item_already_in_cart = Cart.objects.filter(Q(product=product.id) & Q(user=request.user)).exists()
            count = Cart.objects.filter(user=request.user).count()
        context = {
            'product':product,
            'item_already_in_cart':item_already_in_cart,
            'count':count,
            }
        return render(request, 'app/productdetail.html', context)

@login_required
def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('product_id')
    product = Product.objects.get(id=product_id)
    Cart(user=user, product=product).save()
    return redirect('/cart')

@login_required
def show_cart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=request.user)
        count = Cart.objects.filter(user=user).count()
        amount = 0.0
        shipping_fee = 0.0
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == user]
        if cart_product:
            for p in cart_product:
                if p.quantity >= 1:
                    shipping_fee = 50.0
                tempamount = p.quantity * p.product.discounted_price
                amount += tempamount
                total_amount = amount + shipping_fee
            context = {'carts':cart, 'amount':amount, 'total_amount':total_amount, 'shipping_fee':shipping_fee, 'count':count}
            return render(request, 'app/addtocart.html', context)
        else:
            return render(request, 'app/emptycart.html', {'count':count})
        
        
@login_required      
def plus_cart(request):
    count = Cart.objects.filter(user=request.user).count()
    if request.method == 'GET':
        product_id = request.GET.get('product_id')
        c = Cart.objects.get(Q(product=product_id) & Q(user=request.user))
        c.quantity += 1
        c.save()
        amount = 0.0
        shipping_fee = 0.0
        if c.quantity >= 1:
            shipping_fee = 50.0          
        cart_product = [p for p in Cart.objects.all() if p.user==request.user]
        for p in cart_product:
            tempamount = p.quantity * p.product.discounted_price
            amount += tempamount
            totalamount = amount + shipping_fee
        context = {
            'shipping_fee':shipping_fee,
            'amount':amount,
            'totalamount':totalamount,
            'quantity':c.quantity,
            'count':count,
        }
        return JsonResponse(context)


@login_required
def minus_cart(request):
    count = Cart.objects.filter(user=request.user).count()
    if request.method == 'GET':
        product_id = request.GET.get('product_id')
        c = Cart.objects.get(Q(product=product_id) & Q(user=request.user))
        c.quantity -= 1
        c.save()
        amount = 0.0
        shipping_fee = 0.0
        if c.quantity >= 1:
            shipping_fee = 50.0
        cart_product = [p for p in Cart.objects.all() if p.user==request.user]
        for p in cart_product:
            tempamount = p.quantity * p.product.discounted_price
            amount += tempamount
            totalamount = amount + shipping_fee
        context = {
            'shipping_fee':shipping_fee,
            'amount':amount,
            'totalamount':totalamount,
            'quantity':c.quantity,
            'count':count,
        }
        return JsonResponse(context)


@login_required      
def remove_cart(request):
    if request.method == 'GET':
        count = Cart.objects.filter(user=request.user).count()
        product_id = request.GET.get('product_id')
        c = Cart.objects.get(Q(product=product_id) & Q(user=request.user))
        c.delete()
        amount = 0.0
        shipping_fee = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            temp_amount = p.quantity * p.product.discounted_price
            amount += temp_amount
            if p.quantity >= 1:
                shipping_fee = 50.0
            
        
        data = {
            'amount':amount,
            'shipping_fee':shipping_fee,
            'totalamount':amount + shipping_fee,
            'count':count,
        }
        return JsonResponse(data)

@login_required   
def buy_now(request):
 return render(request, 'app/buynow.html')

@login_required
def address(request):
    count = Cart.objects.filter(user=request.user).count()
    address = Customer.objects.filter(user=request.user)
    return render(request, 'app/address.html', {'address':address, 'active':'btn-success', 'count':count})

@login_required
def orders(request):
    count = Cart.objects.filter(user=request.user).count()
    order_placed = OrderedPlaced.objects.filter(user=request.user)
    return render(request, 'app/orders.html', {'order_placed':order_placed, 'count':count})

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request, data=None):
    count = ''
    if request.user.is_authenticated:
        count = Cart.objects.filter(user=request.user).count()
    if data == None:
        mobiles = Product.objects.filter(category='M')
    elif data == 'budget':
        mobiles = Product.objects.filter(category='M').filter(discounted_price__lt=30000)
        
    elif data == 'midrange':
        mobiles = Product.objects.filter(category='M').filter(discounted_price__range=(30000, 60000))
        
    elif data == 'flexive':
        mobiles = Product.objects.filter(category='M').filter(discounted_price__gte=60000)
        
    else:
        try:
            mobiles = Product.objects.filter(category='M').filter(brand=data)
        except:
            mobiles = Product.objects.filter(category='M')
    return render(request, 'app/mobile.html', {'mobiles':mobiles, 'count':count})


def laptop(request, data=None):
    count = ''
    if request.user.is_authenticated:
        count = Cart.objects.filter(user=request.user).count()
    if data == None:
        laptops = Product.objects.filter(category='L')
    
    elif data == 'below':
        laptops = Product.objects.filter(category='L').filter(discounted_price__lt=100000)
        
    elif data == 'above':
        laptops = Product.objects.filter(category='L').filter(discounted_price__gte=100000)
    
    else:
        try:
            laptops = Product.objects.filter(category='L').filter(brand=data)
        except:
            laptops = Product.objects.filter(category='L')
    return render(request, 'app/laptop.html', {'laptops':laptops, 'count':count})

def bottomwear(request, data=None):
    count = ''
    if request.user.is_authenticated:
        count = Cart.objects.filter(user=request.user).count()
    if data == None:
        bwdata = Product.objects.filter(category='BW')
    else:
        try:
            bwdata = Product.objects.filter(category='BW').filter(brand=data)
        except:
            bwdata = Product.objects.filter(category='BW')
    return render(request, 'app/bottomwear.html', {'bwdata':bwdata, 'count':count})
    
    
def topwear(request, data=None):
    count = ''
    if request.user.is_authenticated:
        count = Cart.objects.filter(user=request.user).count()
    if data == None:
        twdata = Product.objects.filter(category='TW')
    else:
        try:
            twdata = Product.objects.filter(category='TW').filter(brand=data)
        except:
            twdata = Product.objects.filter(category='TW')
    return render(request, 'app/topwear.html', {'topwears':twdata, 'count':count})
    
def login(request):
 return render(request, 'app/login.html')



class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html', {'form':form})
        
    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Registrered!!')
        return render(request, 'app/customerregistration.html', {'form':form})
    

@login_required
def checkout(request):
    count = Cart.objects.filter(user=request.user).count()
    user = request.user
    address = Customer.objects.filter(user=user)
    cart_items = Cart.objects.filter(user=user)
    amount = 0.0
    shipping_fee = 50.0
    totalamount = 0.0
    cart_product = [p for p in Cart.objects.all() if p.user == user]
    if cart_product:
        for p in cart_product:
            tempamount = p.quantity * p.product.discounted_price
            amount += tempamount 
        totalamount = amount + shipping_fee
    return render(request, 'app/checkout.html', {'address':address, 'totalamount':totalamount, 'cart_items':cart_items, 'count':count})

@login_required
def payment_done(request):
    count = Cart.objects.filter(user=request.user).count()
    user = request.user
    custid = request.GET.get('customerid')
    customer = Customer.objects.get(id=custid)
    cart = Cart.objects.filter(user=user)
    for c in cart:
        OrderedPlaced(user=user, customer=customer, product=c.product, quantity=c.quantity).save()
        c.delete()
    return redirect('orders')

@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    
    def get(self, request):
        count = Cart.objects.filter(user=request.user).count()
        form = CustomerProfileForm()
        return render(request, 'app/profile.html', {'form':form, 'active':'btn-success', 'count':count})
    
    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            city = form.cleaned_data['city']
            locality = form.cleaned_data['city']
            zipcode = form.cleaned_data['zipcode']
            register = Customer(user=user, name=name, city=city, locality=locality, zipcode=zipcode)
            register.save()
            messages.success(request, 'Profile Updated Successfully!!')
        return render(request, 'app/profile.html', {'form':form, 'active':'btn-success'})
    
    
    
def search(request):
    query = request.POST.get('search', '')
    product = None
    if query:
        product = Product.objects.filter(
            Q(title__icontains=query) |  # Search in the name field, case-insensitive
            Q(description__icontains=query)  # Search in the description field, case-insensitive            
        )
    return render(request, 'app/search_results.html', {'query': query, 'product':product})
