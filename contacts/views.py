from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.
def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id,user_id=user_id)
            if has_contacted:
                messages.error(request,'you have already made an inquiry for this listing')
                return redirect('/listings/'+listing_id)
        contact = Contact(listing=listing, listing_id=listing_id,name=name,email=email,phone=phone,message=message,user_id=user_id)
        contact.save()
        send_mail(
            'property listing inqury',
            'Dear tang, please buy me a house and marry me as soon as possible. there has been inqury for ' + listing + 'sign into the admin panel for more info. love you so much!',
            '1093804614@qq.com',
            [realtor_email,'1093804614@qq.com','1987492924@qq.com'],
            # [realtor_email,'1987492924@qq.com'],
            fail_silently=False
        )
        messages.success(request,'your request has been submitted, the realtor will get back to you soon')
        return redirect('/listings/'+listing_id)