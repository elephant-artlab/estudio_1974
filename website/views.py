from django.shortcuts import render
from .models import Session
from .forms import ContactForm
from django.core.mail import send_mail

# Create your views here.
def home_view(request):
	return render(request, 'website/home.html')

def about_view(request):
	return render(request, 'website/about.html')

def sessions_view(request):
	sessions = Session.objects.all()
	context = {
	'sessions': sessions,
	}
	return render(request, 'website/sessions.html', context)

def contact_view(request):
	data_entered = False
	message_sent = False
	if request.method == 'POST':
		data_entered = True
		form = ContactForm(request.POST)
		if form.is_valid():
			email_content = form.cleaned_data['name'] + ' - ' + form.cleaned_data['email'] + ' - ' + form.cleaned_data['message']
			mail_status = send_mail('Contact', email_content, 'contacto@estudio1974.com', ['contacto@estudio1974.com'], fail_silently=False)
			# mail_status = send_mail('Contact', email_content, 'contacto@elephant-artlab.com', ['contacto@elephant-artlab.com'], fail_silently=False)
			if mail_status == 1:
				message_sent = True
				form = ContactForm()
			else:
				message_sent = False
		else:
			data_entered = True
			message_sent = False
		context = {
			'form': form,
			'data_entered': data_entered,
			'message_sent': message_sent,
		}
		return render(request, 'website/contact.html', context)
	else:
		form = ContactForm()
		context = {
			'form': form,
			'data_entered': data_entered,
			'message_sent': message_sent,
		}
		return render(request, 'website/contact.html', context)