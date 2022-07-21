from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.contrib.auth import get_user_model

User = get_user_model()

@receiver(post_save, sender=User)
def send_confirmation_email(sender, instance, created, **kwargs):
    if created:
        message = f"""Hi, {instance.first_name}.
Your account has been successfully created and activated. Your username is {instance.username}.

Cheers,
Femi Femo
"""     
        subject = "Welcome to FemoPay"
        send_mail(subject=subject,
                  message=message,
                  recipient_list=[instance.email],
                  from_email=None)
        