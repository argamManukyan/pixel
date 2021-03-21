from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings



class SendEmailContacts:

    @staticmethod
    def send_email(data):
        message = render_to_string('core/contact_email.html',context={
            "email":data['email'],
            "name":data['name'],
            "phone":data['phone'],
            "message": data['message']
        })

        send_mail('Contact request',message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[settings.EMAIL_HOST_USER],
        fail_silently=False)