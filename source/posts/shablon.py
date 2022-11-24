class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = (
            'institution_name',
            'speciality',
            'category_education',
            'begin_date',
            'end_date',
            'faculty'
        )

#+++++++++++++++++++++++++

from hh_app.views.education_add import EducationAddView

path('resume/add/edu/<int:pk>', EducationAddView.as_view(), name='resume_add_edu'),

#+++++++++++++++++++++++++

from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404, redirect

from hh_app.models import Resume, Education
from hh_app.forms import EducationForm


class EducationAddView(LoginRequiredMixin, CreateView):
    model = Education
    form_class = EducationForm
    template_name = 'resume_add_edu.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'education'

    def form_valid(self, form):
        resume = get_object_or_404(Resume, pk=self.kwargs.get('pk'))
        print("PRINT1", resume)
        education = form.save(commit=False)
        education.resume = resume
        education.save()
        return redirect('resume_detail', pk=resume.pk)

#+++++++++++++++++++++++++


