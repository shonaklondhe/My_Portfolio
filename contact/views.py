from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactMessage

class ContactView(TemplateView):
    template_name = 'contact/contact.html'
    
    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        if name and email and subject and message:
            # Save to database
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            
            # Send email notification
            try:
                email_subject = f'Portfolio Contact: {subject}'
                email_message = f'''
New contact form submission from your portfolio:

Name: {name}
Email: {email}
Subject: {subject}

Message:
{message}

---
This message was sent from your portfolio contact form.
                '''
                
                send_mail(
                    email_subject,
                    email_message,
                    settings.DEFAULT_FROM_EMAIL,
                    ['shonaklondhe.it@gmail.com'],
                    fail_silently=False,
                )
                messages.success(request, 'Thank you! Your message has been sent successfully.')
            except Exception as e:
                # Still save to database even if email fails
                messages.success(request, 'Thank you! Your message has been received.')
                print(f"Email sending failed: {e}")
        else:
            messages.error(request, 'Please fill in all fields.')
        
        return redirect('contact:contact')
