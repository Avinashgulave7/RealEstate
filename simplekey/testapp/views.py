from django.shortcuts import render,redirect
from .models import Buy,Rent,Land,Agent,Contact,Select_Property
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test


from . import forms

# Create your views here.


def index(request):

    buy=Buy.objects.all().order_by('-Date')[0:3]
    rent=Rent.objects.all().order_by('-Date')[0:3]
    land=Land.objects.all().order_by('-Date')[0:3]
    agent=Agent.objects.all()

    if request.method == 'POST':
        q = request.POST['search']
        buy = Buy.objects.filter(Property_name__icontains=q) | \
              Buy.objects.filter(Address__icontains=q) | \
              Buy.objects.filter(State__icontains=q) | \
              Buy.objects.filter(Pincode__icontains=q) | \
              Buy.objects.filter(City__icontains=q)

        rent = Rent.objects.filter(Property_name__icontains=q) | \
               Rent.objects.filter(Address__icontains=q) | \
               Rent.objects.filter(State__icontains=q) | \
               Rent.objects.filter(Pincode__icontains=q) | \
               Rent.objects.filter(City__icontains=q)

        land = Land.objects.filter(Address__icontains=q) | \
               Land.objects.filter(State__icontains=q) | \
               Land.objects.filter(Pincode__icontains=q) | \
               Land.objects.filter(City__icontains=q)

        return render(request, 'testapp/property.html', {'buy': buy, 'rent': rent, 'land': land})

    return render(request,'testapp/index.html',{'buy':buy,'rent':rent,'land':land,'agent':agent})
@login_required
def Property_Details(request,id):
    buy_details=Buy.objects.get(id=id)
    property = Buy.objects.get(pk=id)
    image_list = property.images.all()
    if request.method == "POST":
        try:



            name = request.POST['name']
            email = request.POST['email']
            mobile = request.POST['mob']
            date = request.POST['date']
            property_name = request.POST['p_name']
            msg = request.POST['msg']

            add_property=Select_Property.objects.create(name=name,email=email,mobile=mobile,date=date,property=property_name,msg=msg)

            add_property.save()

            messages.info(request, ' send message Successfully!')
            return redirect('/')
        except:
            messages.info(request, ' Somthing Wrong')
            return render(request,'testapp/property_details.html')


    return render(request,'testapp/property_details.html',{'i':buy_details,'images':image_list})


@login_required
def Property_Details_Rent(request,id):
    rent_details=Rent.objects.get(id=id)
    property = Rent.objects.get(pk=id)
    image_list = property.images.all()

    if request.method == "POST":
        try:



            name = request.POST['name']
            email = request.POST['email']
            mobile = request.POST['mob']
            date = request.POST['date']
            property_name = request.POST['p_name']
            msg = request.POST['msg']

            add_property=Select_Property.objects.create(name=name,email=email,mobile=mobile,date=date,property=property_name,msg=msg)

            add_property.save()

            messages.info(request, ' send message Successfully!')
            return redirect('/')
        except:
            messages.info(request, ' Somthing Wrong')
            return render(request,'testapp/property_details_rent.html')


    return render(request,'testapp/property_details_rent.html',{'i':rent_details,'images':image_list})

@login_required
def Property_Details_Land(request,id):
    land_details=Land.objects.get(id=id)
    property = Land.objects.get(pk=id)
    image_list = property.images.all()

    if request.method == "POST":
        try:



            name = request.POST['name']
            email = request.POST['email']
            mobile = request.POST['mob']
            date = request.POST['date']
            property_name = request.POST['p_name']
            msg = request.POST['msg']

            add_property=Select_Property.objects.create(name=name,email=email,mobile=mobile,date=date,property=property_name,msg=msg)

            add_property.save()

            messages.info(request, ' send message Successfully!')
            return redirect('/')
        except:
            messages.info(request, ' Somthing Wrong')
            return render(request,'testapp/property_details_land.html')




    return render(request,'testapp/property_details_land.html',{'i':land_details,'images':image_list})

def About(request):
    agent=Agent.objects.all()
    buy=Buy.objects.all().count()
    rent = Rent.objects.all().count()
    land = Land.objects.all().count()
    return render(request, 'testapp/about.html', {'agent': agent,'buy':buy,'rent':rent,'land':land})


def Buy_Page(request):

    buy=Buy.objects.all().order_by('-Date')
    buy_count = Buy.objects.all().count()


    paginator = Paginator(buy, 1)
    page_number = request.GET.get('page')
    try:
        buy = paginator.page(page_number)
    except PageNotAnInteger:
        buy = paginator.page(1)
    except EmptyPage:
        buy = paginator.page(paginator.num_pages)

    if request.method == 'POST':
        q = request.POST['search']
        buy = Buy.objects.filter(Property_name__icontains=q) | \
              Buy.objects.filter(Address__icontains=q) | \
              Buy.objects.filter(State__icontains=q) | \
              Buy.objects.filter(Pincode__icontains=q) | \
              Buy.objects.filter(City__icontains=q)

        buy_count = buy.count()

        paginator = Paginator(buy, 1)
        page_number = request.GET.get('page')
        try:
            buy = paginator.page(page_number)
        except PageNotAnInteger:
            buy = paginator.page(1)
        except EmptyPage:
            buy = paginator.page(paginator.num_pages)

        return render(request, 'testapp/buy.html', {'buy': buy, 'buy_count': buy_count})




    return render(request,'testapp/buy.html',{'buy':buy,'buy_count':buy_count})



def Rent_Page(request):
    rent=Rent.objects.all().order_by('-Date')
    rent_count = Rent.objects.all().count()

    paginator = Paginator(rent, 1)
    page_number = request.GET.get('page')
    try:
        rent = paginator.page(page_number)
    except PageNotAnInteger:
        rent = paginator.page(1)
    except EmptyPage:
        rent = paginator.page(paginator.num_pages)

    if request.method == 'POST':
        q = request.POST['search']
        rent = Rent.objects.filter(Property_name__icontains=q) | \
               Rent.objects.filter(Address__icontains=q) | \
               Rent.objects.filter(State__icontains=q) | \
               Rent.objects.filter(Pincode__icontains=q) | \
               Rent.objects.filter(City__icontains=q)


        rent_count = rent.count()

        paginator = Paginator(rent, 1)
        page_number = request.GET.get('page')
        try:
            rent = paginator.page(page_number)
        except PageNotAnInteger:
            rent = paginator.page(1)
        except EmptyPage:
            rent = paginator.page(paginator.num_pages)

        return render(request, 'testapp/rent.html', {'rent': rent, 'rent_count': rent_count})


    return render(request,'testapp/rent.html',{'rent':rent,'rent_count':rent_count})

def Land_Page(request):
    land=Land.objects.all().order_by('-Date')
    land_count = Land.objects.all().count()

    paginator = Paginator(land, 1)
    page_number = request.GET.get('page')
    try:
        land = paginator.page(page_number)
    except PageNotAnInteger:
        land = paginator.page(1)
    except EmptyPage:
        land = paginator.page(paginator.num_pages)

    if request.method == 'POST':
        q = request.POST['search']
        land = Land.objects.filter(Address__icontains=q) | \
               Land.objects.filter(State__icontains=q) | \
               Land.objects.filter(Pincode__icontains=q) | \
               Land.objects.filter(City__icontains=q)

        land_count = land.count()

        paginator = Paginator(land, 1)
        page_number = request.GET.get('page')
        try:
            land = paginator.page(page_number)
        except PageNotAnInteger:
            land = paginator.page(1)
        except EmptyPage:
            land = paginator.page(paginator.num_pages)

        return render(request, 'testapp/land.html', {'land': land, 'land_count': land_count})


    return render(request,'testapp/land.html',{'land':land,'land_count':land_count})

def Contact_page(request):
    if request.method == "POST":
        try:


            name = request.POST['name']
            email = request.POST['email']
            subject = request.POST['subject']
            msg = request.POST['msg']

            add_contact=Contact.objects.create(name=name,email=email,subject=subject,message=msg)

            add_contact.save()

            messages.info(request, ' send feedback Successfully!')
            return redirect('/')
        except:
            messages.info(request, ' Somthing Wrong')
            return render(request,'testapp/contact.html')

    return render(request,'testapp/contact.html')
@login_required
def Add_Property(request):
    username=request.user
    buy=Buy.objects.filter(Owner_name__exact=username)
    rent = Rent.objects.filter(Owner_name__exact=username)
    land = Land.objects.filter(Owner_name__exact=username)

    count_buy=Buy.objects.filter(Owner_name__exact=username).count()
    count_rent = Rent.objects.filter(Owner_name__exact=username).count()

    count_land = Land.objects.filter(Owner_name__exact=username).count()

    return render(request, 'testapp/add_property.html',{'buy':buy,'land':land,'rent':rent,'buy_count':count_buy,'rent_count':count_rent,'land_count':count_land})


def Add_Buy(request):
    if request.method == "POST":
        img1 = request.FILES['img1']


        owner = request.POST['owner']
        contact = request.POST['mobileno']
        property_name = request.POST['pname']
        property = request.POST['p_type']
        type = request.POST['type']
        rooms = request.POST['rooms']
        baths = request.POST['wc']
        area = request.POST['area']
        water = request.POST['water']
        playground = request.POST['playground']

        price = request.POST['price']
        desc = request.POST['desc']
        gym = request.POST['gym']
        hospital = request.POST['hospital']
        school = request.POST['school']
        mall = request.POST['mall']

        pincode = request.POST['pin']
        state = request.POST['state']
        city = request.POST['city']
        address = request.POST['address']
        # active = request.form['active']
        light = request.POST['light']

        park = request.POST['park']

        club = request.POST['club']

        fire = request.POST['fire']

        lift = request.POST['lift']

        wifi = request.POST['wifi']

        security = request.POST['security']

        temple = request.POST['temple']

        poll = request.POST['poll']

        hall = request.POST['hall']
        hotel = request.POST['hotel']

        cinema = request.POST['hall1']

        date = request.POST['date']

        add_buy=Buy.objects.create(Owner_name=owner,Contact=contact,Property_name=property_name,Property=property,Type=type,Rooms=rooms,
                    Baths=baths,Area=area,Water=water,Playground=playground,Price=price,Description=desc,Gym=gym,Hospital=hospital,
                    School=school,Mall=mall,Pincode=pincode,State=state,City=city,Address=address,Img1=img1,Electricity=light,
                    Parking=park,Club=club,Fire=fire,Lift=lift,Wifi=wifi,Security=security,Temple=temple,Poll=poll,Living=hall,
                    Hotel=hotel,Cinema=cinema,Date=date)
        add_buy.save()

        messages.info(request, ' Add property Successfully!')
        return redirect('/add_property')

    return render(request, 'testapp/add_buy.html')


def Update_Buy(request,id):
    e=Buy.objects.get(id=id)

    try:

        if request.method=='POST':
            img1 = request.FILES['img1']

            owner = request.POST['owner']
            contact = request.POST['mobileno']
            property_name = request.POST['pname']
            property = request.POST['p_type']
            type = request.POST['type']
            rooms = request.POST['rooms']
            baths = request.POST['wc']
            area = request.POST['area']
            water = request.POST['water']
            playground = request.POST['playground']

            price = request.POST['price']
            desc = request.POST['desc']
            gym = request.POST['gym']
            hospital = request.POST['hospital']
            school = request.POST['school']
            mall = request.POST['mall']

            pincode = request.POST['pin']
            state = request.POST['state']
            city = request.POST['city']
            address = request.POST['address']
        # active = request.form['active']
            light = request.POST['light']

            park = request.POST['park']

            club = request.POST['club']

            fire = request.POST['fire']

            lift = request.POST['lift']

            wifi = request.POST['wifi']

            security = request.POST['security']

            temple = request.POST['temple']

            poll = request.POST['poll']

            hall = request.POST['hall']
            hotel = request.POST['hotel']

            cinema = request.POST['hall1']


            e.Owner_name=owner
            e.Contact=contact
            e.Property_name=property_name
            e.Property=property
            e.Type=type
            e.Rooms=rooms
            e.Baths=baths
            e.Area=area
            e.Water=water
            e.Playground=playground
            e.Price=price
            e.Description=desc
            e.Gym=gym
            e.Hospital=hospital
            e.School=school
            e.Mall=mall
            e.Pincode=pincode
            e.State=state
            e.City=city
            e.Address=address
            e.Img1=img1
            e.Electricity=light
            e.Parking=park
            e.Club=club
            e.Fire=fire
            e.Lift=lift
            e.Wifi=wifi
            e.Security=security
            e.Temple=temple
            e.Poll=poll
            e.Living=hall
            e.Hotel=hotel
            e.Cinema=cinema

            e.save()


            messages.info(request, ' Update property Successfully!')
            return redirect('/add_property')
    except:
        messages.info(request, ' somthing Wrong')

    return render(request, 'testapp/update_user_prop.html',{'i':e})

@login_required
def User_Buy_Viewall(request,id):
    buy=Buy.objects.get(id=id)
    property = Buy.objects.get(pk=id)
    image_list = property.images.all()

    return render(request, 'testapp/user_buy_viewall.html', {'i': buy,'images':image_list})
@login_required
def User_Buy_delete(request,id):
    buy=Buy.objects.get(id=id)
    buy.delete()
    return redirect('/add_property')

def D(request):
    buy=Buy.objects.all()
    buy.delete()
    return redirect('/add_property')



def Add_rent(request):
    if request.method == "POST":
        try:
            img1 = request.FILES['img1']


            owner = request.POST['owner']
            contact = request.POST['mobileno']
            property_name = request.POST['pname']
            property = request.POST['p_type']
            type = request.POST['type']
            rooms = request.POST['rooms']
            baths = request.POST['wc']
            area = request.POST['area']
            water = request.POST['water']
            playground = request.POST['playground']

            price = request.POST['price']
            desc = request.POST['desc']
            gym = request.POST['gym']
            hospital = request.POST['hospital']
            school = request.POST['school']
            mall = request.POST['mall']

            pincode = request.POST['pin']
            state = request.POST['state']
            city = request.POST['city']
            address = request.POST['address']
            # active = request.form['active']
            light = request.POST['light']

            park = request.POST['park']

            club = request.POST['club']

            fire = request.POST['fire']

            lift = request.POST['lift']

            wifi = request.POST['wifi']

            security = request.POST['security']

            temple = request.POST['temple']

            poll = request.POST['poll']

            hall = request.POST['hall']
            hotel = request.POST['hotel']

            cinema = request.POST['hall1']

            date = request.POST['date']

            add_rent=Rent.objects.create(Owner_name=owner,Contact=contact,Property_name=property_name,Property=property,Type=type,Rooms=rooms,
                        Baths=baths,Area=area,Water=water,Playground=playground,Price=price,Description=desc,Gym=gym,Hospital=hospital,
                        School=school,Mall=mall,Pincode=pincode,State=state,City=city,Address=address,Img1=img1,Electricity=light,
                        Parking=park,Club=club,Fire=fire,Lift=lift,Wifi=wifi,Security=security,Temple=temple,Poll=poll,Living=hall,
                        Hotel=hotel,Cinema=cinema,Date=date)
            add_rent.save()

            messages.info(request, ' Add property Successfully!')
            return redirect('/add_property')
        except:
            messages.info(request, ' Somthing Wrong')
            return render(request, 'testapp/add_rent.html')


    return render(request, 'testapp/add_rent.html')

@login_required
def User_Rent_Viewall(request,id):
    rent=Rent.objects.get(id=id)
    property = Rent.objects.get(pk=id)
    image_list = property.images.all()

    return render(request, 'testapp/user_rent_viewall.html', {'i': rent,'images':image_list})


def Update_Rent(request,id):
    e=Rent.objects.get(id=id)

    try:

        if request.method=='POST':
            img1 = request.FILES['img1']

            owner = request.POST['owner']
            contact = request.POST['mobileno']
            property_name = request.POST['pname']
            property = request.POST['p_type']
            type = request.POST['type']
            rooms = request.POST['rooms']
            baths = request.POST['wc']
            area = request.POST['area']
            water = request.POST['water']
            playground = request.POST['playground']

            price = request.POST['price']
            desc = request.POST['desc']
            gym = request.POST['gym']
            hospital = request.POST['hospital']
            school = request.POST['school']
            mall = request.POST['mall']

            pincode = request.POST['pin']
            state = request.POST['state']
            city = request.POST['city']
            address = request.POST['address']
        # active = request.form['active']
            light = request.POST['light']

            park = request.POST['park']

            club = request.POST['club']

            fire = request.POST['fire']

            lift = request.POST['lift']

            wifi = request.POST['wifi']

            security = request.POST['security']

            temple = request.POST['temple']

            poll = request.POST['poll']

            hall = request.POST['hall']
            hotel = request.POST['hotel']

            cinema = request.POST['hall1']


            e.Owner_name=owner
            e.Contact=contact
            e.Property_name=property_name
            e.Property=property
            e.Type=type
            e.Rooms=rooms
            e.Baths=baths
            e.Area=area
            e.Water=water
            e.Playground=playground
            e.Price=price
            e.Description=desc
            e.Gym=gym
            e.Hospital=hospital
            e.School=school
            e.Mall=mall
            e.Pincode=pincode
            e.State=state
            e.City=city
            e.Address=address
            e.Img1=img1
            e.Electricity=light
            e.Parking=park
            e.Club=club
            e.Fire=fire
            e.Lift=lift
            e.Wifi=wifi
            e.Security=security
            e.Temple=temple
            e.Poll=poll
            e.Living=hall
            e.Hotel=hotel
            e.Cinema=cinema

            e.save()


            messages.info(request, ' Update property Successfully!')
            return redirect('/add_property')
    except:
        messages.info(request, ' somthing Wrong')

    return render(request, 'testapp/update_user_prop_rent.html',{'i':e})

@login_required
def User_Rent_delete(request,id):
    rent=Rent.objects.get(id=id)
    rent.delete()
    return redirect('/add_property')


def Add_land(request):
    if request.method == "POST":
        try:
            img1 = request.FILES['img1']
            owner = request.POST['owner']
            contact = request.POST['mobileno']
            property = request.POST['pname']
            property_type = request.POST['p_type']

            price = request.POST['price']
            area = request.POST['area']
            desc = request.POST['desc']
            document = request.POST['uthara']
            tax_recipt = request.POST['tax_recipt']
            survey = request.POST['survey']
            pincode = request.POST['pin']
            state = request.POST['state']
            city = request.POST['city']
            address = request.POST['address']
            date = request.POST['date']

            add_land = Land.objects.create(Owner_name=owner,Contact = contact,Property = property,Property_type = property_type,
                                        Price = price,Area = area,Description = desc,Document = document,
                                        Tax_Raciept = tax_recipt,Survey_Sketch = survey,Pincode = pincode,State = state,
                                        City = city,Address = address,Img1 = img1,Date=date)
            add_land.save()

            messages.info(request, ' Add property Successfully!')
            return redirect('/add_property')
        except:
            messages.info(request, ' Somthing Wrong')
            return render(request, 'testapp/add_land.html')

    return render(request, 'testapp/add_land.html')

def Update_Land(request,id):
    e=Land.objects.get(id=id)

    try:

        if request.method=='POST':
            img1 = request.FILES['img1']
            owner = request.POST['owner']
            contact = request.POST['mobileno']
            property = request.POST['pname']
            property_type = request.POST['p_type']

            price = request.POST['price']
            area = request.POST['area']
            desc = request.POST['desc']
            document = request.POST['uthara']
            tax_recipt = request.POST['tax_recipt']
            survey = request.POST['survey']
            pincode = request.POST['pin']
            state = request.POST['state']
            city = request.POST['city']
            address = request.POST['address']

            e.Owner_name = owner
            e.Contact = contact
            e.Property = property
            e.Property_type = property_type
            e.Price = price
            e.Area = area
            e.Description = desc
            e.Document = document
            e.Tax_Raciept = tax_recipt
            e.Survey_Sketch = survey
            e.Pincode = pincode
            e.State = state
            e.City = city
            e.Address = address
            e.Img1 = img1
            e.save()


            messages.info(request, ' Update property Successfully!')
            return redirect('/add_property')
    except:
        messages.info(request, ' somthing Wrong')

    return render(request, 'testapp/update_user_prop_land.html',{'i':e})

@login_required
def User_Land_Viewall(request,id):
    land=Land.objects.get(id=id)
    property = Land.objects.get(pk=id)
    image_list = property.images.all()

    return render(request, 'testapp/user_land_viewall.html', {'i': land,'images':image_list})
@login_required
def User_Land_delete(request,id):
    land=Land.objects.get(id=id)
    land.delete()
    return redirect('/add_property')


def Login(request):
    if request.method == 'POST':

        # AuthenticationForm_can_also_be_used__

        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            request.session.set_expiry(60)
            auth.login(request, user)

            return redirect('/')
        else:
            messages.info(request, 'Invalid ')
            return render(request, 'testapp/login.html')

    else:
        return render(request, 'testapp/login.html')


def SignUp(request):
    form=forms.SignupForm()
    if request.method == 'POST':
        form=forms.SignupForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect('/accounts/login')
    return render(request,'testapp/singup.html',{'form':form})
@login_required
def Logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/accounts/login')


def Property(request):
    buy=Buy.objects.all()
    rent = Rent.objects.all()
    land = Land.objects.all()

    if request.method == 'POST':
        q = request.POST['search']
        buy = Buy.objects.filter(Property_name__icontains=q)| \
              Buy.objects.filter(Address__icontains=q) | \
              Buy.objects.filter(State__icontains=q) | \
              Buy.objects.filter(Pincode__icontains=q)| \
              Buy.objects.filter(City__icontains=q)

        rent = Rent.objects.filter(Property_name__icontains=q)|\
               Rent.objects.filter(Address__icontains=q) | \
               Rent.objects.filter(State__icontains=q) | \
               Rent.objects.filter(Pincode__icontains=q)| \
               Rent.objects.filter(City__icontains=q)

        land = Land.objects.filter(Address__icontains=q)|\
               Land.objects.filter(State__icontains=q) | \
               Land.objects.filter(Pincode__icontains=q) | \
               Land.objects.filter(City__icontains=q)

        return render(request, 'testapp/property.html', {'buy': buy,'rent':rent,'land':land})


    return render(request, 'testapp/property.html', {'buy': buy,'rent':rent,'land':land})


def Price_Low_To_High(request):
    buy=Buy.objects.all().order_by('Price')
    rent = Rent.objects.all().order_by('Price')
    land = Land.objects.all().order_by('Price')

    return render(request,'testapp/property.html',{'buy': buy,'rent':rent,'land':land})

def Price_High_To_Low(request):
    buy=Buy.objects.all().order_by('-Price')
    rent = Rent.objects.all().order_by('-Price')
    land = Land.objects.all().order_by('-Price')

    return render(request,'testapp/property.html',{'buy': buy,'rent':rent,'land':land})

def Area_Low_To_High(request):
    buy=Buy.objects.all().order_by('Area')
    rent = Rent.objects.all().order_by('Area')
    land = Land.objects.all().order_by('Area')

    return render(request,'testapp/property.html',{'buy': buy,'rent':rent,'land':land})

def Area_High_To_Low(request):
    buy=Buy.objects.all().order_by('-Area')
    rent = Rent.objects.all().order_by('-Area')
    land = Land.objects.all().order_by('-Area')

    return render(request,'testapp/property.html',{'buy': buy,'rent':rent,'land':land})


def Buy_Price_Low_To_High(request):
    buy=Buy.objects.all().order_by('Price')
    buy_count = buy.count()

    paginator = Paginator(buy, 2)
    page_number = request.GET.get('page')
    try:
        buy = paginator.page(page_number)
    except PageNotAnInteger:
        buy = paginator.page(1)
    except EmptyPage:
        buy = paginator.page(paginator.num_pages)

    return render(request, 'testapp/buy.html', {'buy': buy, 'buy_count': buy_count})


def Buy_Price_High_To_Low(request):
    buy=Buy.objects.all().order_by('-Price')

    buy_count = buy.count()

    paginator = Paginator(buy, 2)
    page_number = request.GET.get('page')
    try:
        buy = paginator.page(page_number)
    except PageNotAnInteger:
        buy = paginator.page(1)
    except EmptyPage:
        buy = paginator.page(paginator.num_pages)

    return render(request, 'testapp/buy.html', {'buy': buy, 'buy_count': buy_count})

def Buy_Area_Low_To_High(request):
    buy=Buy.objects.all().order_by('Area')

    buy_count = buy.count()

    paginator = Paginator(buy, 2)
    page_number = request.GET.get('page')
    try:
        buy = paginator.page(page_number)
    except PageNotAnInteger:
        buy = paginator.page(1)
    except EmptyPage:
        buy = paginator.page(paginator.num_pages)

    return render(request, 'testapp/buy.html', {'buy': buy, 'buy_count': buy_count})


def Buy_Area_High_To_Low(request):
    buy=Buy.objects.all().order_by('-Area')

    buy_count = buy.count()

    paginator = Paginator(buy, 2)
    page_number = request.GET.get('page')
    try:
        buy = paginator.page(page_number)
    except PageNotAnInteger:
        buy = paginator.page(1)
    except EmptyPage:
        buy = paginator.page(paginator.num_pages)

    return render(request, 'testapp/buy.html', {'buy': buy, 'buy_count': buy_count})


def Rent_Price_Low_To_High(request):
    rent=Rent.objects.all().order_by('Price')
    rent_count = rent.count()

    paginator = Paginator(rent, 2)
    page_number = request.GET.get('page')
    try:
        rent = paginator.page(page_number)
    except PageNotAnInteger:
        rent = paginator.page(1)
    except EmptyPage:
        rent = paginator.page(paginator.num_pages)

    return render(request, 'testapp/rent.html', {'rent': rent, 'rent_count': rent_count})


def Rent_Price_High_To_Low(request):
    rent=Rent.objects.all().order_by('-Price')

    rent_count = rent.count()

    paginator = Paginator(rent, 2)
    page_number = request.GET.get('page')
    try:
        rent = paginator.page(page_number)
    except PageNotAnInteger:
        rent = paginator.page(1)
    except EmptyPage:
        rent = paginator.page(paginator.num_pages)

    return render(request, 'testapp/rent.html', {'rent': rent, 'rent_count': rent_count})

def Rent_Area_Low_To_High(request):
    rent=Rent.objects.all().order_by('Area')

    rent_count = rent.count()

    paginator = Paginator(rent, 2)
    page_number = request.GET.get('page')
    try:
        rent = paginator.page(page_number)
    except PageNotAnInteger:
        rent = paginator.page(1)
    except EmptyPage:
        rent = paginator.page(paginator.num_pages)

    return render(request, 'testapp/rent.html', {'rent': rent, 'rent_count': rent_count})


def Rent_Area_High_To_Low(request):
    rent=Rent.objects.all().order_by('-Area')

    rent_count = rent.count()

    paginator = Paginator(rent, 2)
    page_number = request.GET.get('page')
    try:
        rent = paginator.page(page_number)
    except PageNotAnInteger:
        rent = paginator.page(1)
    except EmptyPage:
        rent = paginator.page(paginator.num_pages)

    return render(request, 'testapp/rent.html', {'rent': rent, 'rent_count': rent_count})

def Land_Price_Low_To_High(request):
    land=Land.objects.all().order_by('Price')
    land_count = land.count()

    paginator = Paginator(land, 2)
    page_number = request.GET.get('page')
    try:
        land = paginator.page(page_number)
    except PageNotAnInteger:
        land = paginator.page(1)
    except EmptyPage:
        land = paginator.page(paginator.num_pages)

    return render(request, 'testapp/land.html', {'land': land, 'land_count': land_count})


def Land_Price_High_To_Low(request):
    land=Land.objects.all().order_by('-Price')

    land_count = land.count()

    paginator = Paginator(land, 2)
    page_number = request.GET.get('page')
    try:
        land = paginator.page(page_number)
    except PageNotAnInteger:
        land = paginator.page(1)
    except EmptyPage:
        land = paginator.page(paginator.num_pages)

    return render(request, 'testapp/land.html', {'land': land, 'land_count': land_count})

def Land_Area_Low_To_High(request):
    land=Land.objects.all().order_by('Area')

    land_count = land.count()

    paginator = Paginator(land, 2)
    page_number = request.GET.get('page')
    try:
        land = paginator.page(page_number)
    except PageNotAnInteger:
        land = paginator.page(1)
    except EmptyPage:
        land = paginator.page(paginator.num_pages)

    return render(request, 'testapp/land.html', {'land': land, 'land_count': land_count})


def Land_Area_High_To_Low(request):
    land=Land.objects.all().order_by('-Area')

    land_count = land.count()

    paginator = Paginator(land, 2)
    page_number = request.GET.get('page')
    try:
        land = paginator.page(page_number)
    except PageNotAnInteger:
        land = paginator.page(1)
    except EmptyPage:
        land = paginator.page(paginator.num_pages)

    return render(request, 'testapp/land.html', {'land': land, 'land_count': land_count})


@user_passes_test(lambda u: u.is_superuser)

def Send_Email(request,id):
    i = Select_Property.objects.get(id=id)

    try:

        if request.method == 'POST':
            email_from = request.POST['name']
            email_to = request.POST['email']
            subject = request.POST['subject']
            msg = request.POST['msg']

            try:
                send_mail(subject,msg,email_from,[email_to])
                messages.info(request, 'Send Email Successfully!')
                return redirect('/admin/testapp/select_property/')
            except BadHeaderError:
                messages.info(request, 'Somthing Wrong')
                return redirect('/admin/testapp/select_property/')


        return render(request, 'testapp/email.html',{'i':i})
    except:
        messages.info(request, 'Somthing Wrong')
        return redirect('/admin/testapp/select_property/')

