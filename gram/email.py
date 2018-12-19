from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from .token import account_activation_token


def activation_email(user, current_site, receiver):
    subject = 'Account Activation'

    message = render_to_string('registration/confirm.html', {
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user)
    })

    email = EmailMessage(subject, message, to=[receiver])
    email.send()
