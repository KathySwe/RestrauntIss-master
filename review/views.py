from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Restaurant,Review,Comment,Category


def index(request,catid=0):
    context = {}
    category = Category.objects.all()

    cat_dict = dict()
    print(category.get(Cid=1))

    for dd in category:
        print(dd.Cid)
        cat_dict[dd.Cid] = dd.Cname

    rest = object

    if(catid==0):
        rest = Restaurant.objects.all()

    else:
        rest = Restaurant.objects.all().filter(Cid=catid)
    #
    context = {
        'cat': cat_dict,
        'restaurant': rest,
    }

    return render(request, 'home.html', context)


def rate(request):
    context={}
    print(" key of rest ")
    # if request.method == 'POST':
    c=request.POST['rkey']
    rating = request.POST['starkey']
    descc = request.POST['ratedesc']
    print(" id " +c+", rating "+rating+" , descript "+descc)

    context = {}
    category = Category.objects.all()

    cat_dict = dict()
    print(category.get(Cid=1))

    for dd in category:
        print(dd.Cid)
        cat_dict[dd.Cid] = dd.Cname

    rest = object

    rest = Restaurant.objects.all()


    context = {
        'cat': cat_dict,
        'restaurant': rest,
    }
    return render(request, 'home.html', context)


    # return render(request, 'home.html', context)


