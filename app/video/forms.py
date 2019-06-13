from django import forms
from dal import autocomplete

from .models import Video

TRUE_FALSE_CHOICES = (
    (False, "No"),
    (True, "Yes"),
)

class VideoUploadForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['public'] = forms.ChoiceField(
            choices=TRUE_FALSE_CHOICES
        )

        # bootstrap css on all fields
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

        self.fields['collections'].widget.attrs.update({
            'data-theme': 'bootstrap',
        })

        self.fields['upload_id'].label = ''

    def save(self, commit=True):
        old_video_title = self.instance.title
        video = super().save(commit=False)

        # if the videos title was the default title
        if Video._meta.get_field('title').get_default() == old_video_title:
            # nullify the slug so it can autopopulate again
            video.slug = None

        if commit:
            video.save()

        return video


    class Meta:
        model = Video
        fields = ['title', 'description', 'collections', 'public', 'upload_id']
        widgets = {
            'collections': autocomplete.ModelSelect2Multiple(url='api_collection_autocomplete'),
            'upload_id': forms.HiddenInput()
        }


