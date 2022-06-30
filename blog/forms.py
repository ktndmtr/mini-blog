from django import forms


class AddCommentForm(forms.Form):
    content = forms.CharField(
        label='Description', max_length=200, widget=forms.Textarea()
    )


class AddBlogForm(forms.Form):
    name = forms.CharField(label='Title', max_length=50)
    content = forms.CharField(
        label='Description', max_length=200, widget=forms.Textarea()
    )
