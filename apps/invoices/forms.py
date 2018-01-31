from django import forms


class TextFilesForm(forms.Form):
    title = forms.CharField(max_length=255, required=False, label='Title',)
    file = forms.FileField(label='Select a text file',
                           help_text='Files upload separated by '
                                     'TAB with following columns: '
                                     'purchaser name, item description, item price, purchase count, '
                                     'merchant address, merchant name.')

