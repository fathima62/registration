from django.shortcuts import render,redirect
from .models import Form


# Create your views here.
def form(request):
     if request.method == 'POST':
      
              name = request.POST['full_name']
              sec_name = request.POST['second_name']
              email = request.POST['email']
              phone = request.POST['phone']
              city = request.POST['city']
              address = request.POST['address']
              country = request.POST['country']
              postcode = request.POST['code']
              purpose = request.POST['purpose']
              amount = request.POST['amount']
              tentor = request.POST['tentor']
              tentormonthly = request.POST['monthly']
              asset_cost = request.POST['asset_cost']
              photo = request.FILES['photo']
              document = request.FILES['document']

             
        
              obj = Form(first_name=name,
                         
                            second_name=sec_name,
                               email=email,
                            phone=phone,
                            address=address,
                       country=country,
                       city=city,
                       asset_cost = asset_cost,
                       postcode=postcode,
                       purpose=purpose,
                       amount=amount,
                        tentor= tentor,
                         tentormonthly= tentormonthly,

                            photo=photo,
                            document=document)
              obj.save()
              return redirect ('register:form')
     return render(request,'register_form/form.html')
            