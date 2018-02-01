from django.shortcuts import render, get_list_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from .parser import parser_file
from .models import TextFile, Invoice
from .forms import TextFilesForm


def upload_file_view(request):
    if request.method == 'POST':
        form = TextFilesForm(request.POST, request.FILES)
        if form.is_valid():
            file_instance = TextFile(file=request.FILES['file'])
            file_instance.save()

            file_content = parser_file(file_instance.file.path)
            for item in file_content:
                invoice_instance = Invoice(purchaser_name=item.get('purchaser name'),
                                           item_description=item.get('item description'),
                                           item_price=item.get('item price'),
                                           purchase_count=item.get('purchase count'),
                                           merchant_address=item.get('merchant address'),
                                           merchant_name=item.get('merchant name'),
                                           text_file=file_instance,)
                invoice_instance.save()
            return HttpResponseRedirect(reverse_lazy('invoices:upload'))
    else:
        form = TextFilesForm()

    text_files = TextFile.objects.all()

    context = {'form': form, 'text_files': text_files}

    return render(request, 'invoices/upload_list.html', context)


def income_view(request, **kwargs):
    invoices = get_list_or_404(Invoice, text_file=kwargs.get('text_file_slug'))
    income = 0
    for item in invoices:
        income += item.item_price * item.purchase_count

    context = {'income': income, 'invoices': invoices}

    return render(request, 'invoices/invoices_detail.html', context)

