from django.shortcuts import render, redirect
from django.db.models import Q
from django.core.mail import send_mail
from django.conf import settings
from .models import BribeReport
from .forms import BribeReportForm, ContactForm


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = form.save()

            # Email subject & body
            subject = f"Thanks for contacting us - {contact_message.subject}"
            message_to_user = (
                f"Dear {contact_message.name},\n\n"
                "We have received your message:\n\n"
                f"{contact_message.message}\n\n"
                "Our team will respond as soon as possible.\n\n"
                "Best regards,\nNo Bribe Zambia Admin"
            )

            # Send confirmation email to visitor
            send_mail(
                subject,
                message_to_user,
                settings.DEFAULT_FROM_EMAIL,
                [contact_message.email],
                fail_silently=False,
            )

            # Notify admin with the original message
            admin_subject = f"New Contact Message: {contact_message.subject}"
            admin_message = (
                f"New message received:\n\n"
                f"From: {contact_message.name} <{contact_message.email}>\n"
                f"Subject: {contact_message.subject}\n\n"
                f"Message:\n{contact_message.message}\n"
            )
            send_mail(
                admin_subject,
                admin_message,
                settings.DEFAULT_FROM_EMAIL,
                [settings.ADMIN_EMAIL],  # set in settings.py
                fail_silently=False,
            )

            return redirect("contact_success")
    else:
        form = ContactForm()

    return render(request, "reports/contact.html", {"form": form})

def contact_success(request):
    return render(request, "reports/contact_success.html")


def home(request):
    total_reports = BribeReport.objects.count()
    institutions_count = BribeReport.objects.values('institution').distinct().count()
    last_report = BribeReport.objects.order_by('-reported_at').first()
    
    context = {
        'total_reports': total_reports,
        'institutions_count': institutions_count,
        'last_report_date': last_report.reported_at if last_report else None,
    }
    return render(request, 'reports/home.html', context)

def report_bribe(request):
    if request.method == 'POST':
        form = BribeReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bribes_list')
    else:
        form = BribeReportForm()
    return render(request, 'reports/report_bribe.html', {'form': form})

def bribes_list(request):
    query = request.GET.get("q")
    bribes = BribeReport.objects.all()

    if query:
        bribes = bribes.filter(
            Q(description__icontains=query) |
            Q(institution__icontains=query) |
            Q(ministry__icontains=query)
        )

    return render(request, "reports/bribes_list.html", {"bribes": bribes, "query": query})


def info(request):
    return render(request, 'reports/info.html')