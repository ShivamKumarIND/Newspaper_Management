from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import (
    StartNewspaperForm, CloseNewspaperForm, PaymentCheckForm,
    ComplaintForm, JoinDistributorForm, NewspaperSoldForm
)
from .models import (
    NewspaperSubscription, ClosedNewspaper, Payment,
    Complaint, Distributor, NewspaperSoldRecord, PROFIT_PER_NEWSPAPER
)


def home(request):
    return render(request, 'agency/home.html')


# ─── 1. Start Newspaper ────────────────────────────────────────────────────────
def start_newspaper(request):
    if request.method == 'POST':
        form = StartNewspaperForm(request.POST)
        if form.is_valid():
            NewspaperSubscription.objects.create(
                newspaper=form.cleaned_data['newspaper'],
                location=form.cleaned_data['location'],
                name=form.cleaned_data['name'],
                mobile=form.cleaned_data['mobile'],
            )
            return render(request, 'agency/success.html', {
                'title': 'Subscription Started!',
                'icon': '🗞️',
                'message': (
                    f"Dear <strong>{form.cleaned_data['name']}</strong>, "
                    f"your subscription for <strong>{form.cleaned_data['newspaper']}</strong> "
                    f"at <strong>{form.cleaned_data['location']}</strong> has been started successfully."
                ),
                'sub_message': 'Your newspaper delivery will begin shortly. Thank you for choosing Newspaper Agency Bakhtiyarpur!',
            })
    else:
        form = StartNewspaperForm()
    return render(request, 'agency/start_newspaper.html', {'form': form})


# ─── 2. Close Newspaper ────────────────────────────────────────────────────────
def close_newspaper(request):
    if request.method == 'POST':
        form = CloseNewspaperForm(request.POST)
        if form.is_valid():
            ClosedNewspaper.objects.create(
                name=form.cleaned_data['name'],
                mobile=form.cleaned_data['mobile'],
                address=form.cleaned_data['address'],
                reason=form.cleaned_data['reason'],
            )
            return render(request, 'agency/success.html', {
                'title': 'Subscription Closed',
                'icon': '📭',
                'message': (
                    f"Dear <strong>{form.cleaned_data['name']}</strong>, "
                    f"your newspaper subscription at <strong>{form.cleaned_data['address']}</strong> "
                    f"has been closed as requested."
                ),
                'sub_message': 'We are sorry to see you go. You can always re-subscribe by using the "Start a Newspaper" option.',
            })
    else:
        form = CloseNewspaperForm()
    return render(request, 'agency/close_newspaper.html', {'form': form})


# ─── 3. Payment Details ────────────────────────────────────────────────────────
def payment_details(request):
    payment_record = None
    searched = False
    not_found = False

    if request.method == 'POST':
        form = PaymentCheckForm(request.POST)
        if form.is_valid():
            searched = True
            name = form.cleaned_data['name']
            mobile = form.cleaned_data['mobile']
            try:
                payment_record = Payment.objects.get(mobile=mobile, name__iexact=name)
            except Payment.DoesNotExist:
                not_found = True
    else:
        form = PaymentCheckForm()

    return render(request, 'agency/payment_details.html', {
        'form': form,
        'payment_record': payment_record,
        'searched': searched,
        'not_found': not_found,
        'today': timezone.now().date(),
    })


# ─── 4. Register a Complaint ───────────────────────────────────────────────────
def register_complaint(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            Complaint.objects.create(
                name=form.cleaned_data['name'],
                mobile=form.cleaned_data['mobile'],
                issue=form.cleaned_data['issue'],
            )
            return render(request, 'agency/success.html', {
                'title': 'Complaint Registered!',
                'icon': '📋',
                'message': (
                    f"Dear <strong>{form.cleaned_data['name']}</strong>, "
                    f"your complaint has been registered successfully."
                ),
                'sub_message': 'Our team will review your complaint and get back to you within 24 hours. Thank you for your patience.',
            })
    else:
        form = ComplaintForm()
    return render(request, 'agency/register_complaint.html', {'form': form})


# ─── 5. Join as Distributor ───────────────────────────────────────────────────
def join_distributor(request):
    if request.method == 'POST':
        form = JoinDistributorForm(request.POST)
        if form.is_valid():
            Distributor.objects.create(
                name=form.cleaned_data['name'],
                mobile=form.cleaned_data['mobile'],
                age=form.cleaned_data['age'],
            )
            return render(request, 'agency/success.html', {
                'title': 'Application Submitted!',
                'icon': '🤝',
                'message': (
                    f"Dear <strong>{form.cleaned_data['name']}</strong>, "
                    f"your application to join as a distributor has been submitted successfully."
                ),
                'sub_message': 'Our team will contact you on your mobile number within 2-3 working days. Welcome aboard!',
            })
    else:
        form = JoinDistributorForm()
    return render(request, 'agency/join_distributor.html', {'form': form})


# ─── 6. Newspaper Sold / Left ─────────────────────────────────────────────────
def newspaper_sold(request):
    result = None

    if request.method == 'POST':
        form = NewspaperSoldForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            newspaper_details = {
                'Hindustan': cd['hindustan_qty'],
                'Dainik Jagaran': cd['dainik_jagaran_qty'],
                'Dainik Bhaskar': cd['dainik_bhaskar_qty'],
                'Prabhat Khabar': cd['prabhat_khabar_qty'],
                'AAJ': cd['aaj_qty'],
                'The Times Of India': cd['times_of_india_qty'],
                'The Hindu': cd['the_hindu_qty'],
                'Hindustan Times': cd['hindustan_times_qty'],
            }
            total_taken = sum(newspaper_details.values())
            total_received = cd['total_received']
            total_sold = cd['total_sold']
            total_remaining = total_received - total_sold
            if total_remaining < 0:
                total_remaining = 0
            net_profit = total_sold * PROFIT_PER_NEWSPAPER

            record = NewspaperSoldRecord.objects.create(
                name=cd['name'],
                mobile=cd['mobile'],
                total_received=total_received,
                newspaper_details=newspaper_details,
                total_taken=total_taken,
                total_sold=total_sold,
                total_remaining=total_remaining,
                net_profit=net_profit,
            )

            result = {
                'record': record,
                'newspaper_details': {k: v for k, v in newspaper_details.items() if v > 0},
                'total_taken': total_taken,
                'net_profit': net_profit,
                'profit_per_paper': PROFIT_PER_NEWSPAPER,
            }
    else:
        form = NewspaperSoldForm()

    return render(request, 'agency/newspaper_sold.html', {'form': form, 'result': result})
