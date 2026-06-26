from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import QuotationForm


def quotation_create(request):

    if request.method == 'POST':

        form = QuotationForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Your enquiry has been submitted successfully.'
            )

            return redirect('quotation')

    else:

        form = QuotationForm()

    context = {
        'form': form
    }

    return render(
        request,
        'quotations/quotation_form.html',
        context
    )
