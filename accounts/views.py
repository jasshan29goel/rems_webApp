from django.shortcuts import redirect, render

# Create your views here.
def register(request):
    return render(request,'accounts/register.html')

def login(request):
    return render(request,'accounts/login.html')

def logout(request):
    return redirect('index')

def dashboard(request):
    return render(request,'accounts/dashboard.html')

def listing(request,listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
      'listing': listing
    }

    return render(request, 'listings/listing.html', context)       

def search(request):
    queryset_list=Listing.objects.all()

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__gte=bedrooms)
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    context = {
        'listings': queryset_list
    }         
    return render(request,'listings/search.html',context)    