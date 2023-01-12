from django.contrib.auth import (
    authenticate,
    login,
)
from django.shortcuts import redirect, render
from django.views.generic import (
    TemplateView,
    FormView,
    DetailView,
    CreateView
)
from .AES import AesAlgorithm
from .form import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import *


class BaseView(TemplateView):
    template_name = 'base.html'


class LogInView(FormView):
    form_class = AuthenticationForm
    template_name = 'logIn.html'
    success_url = reverse_lazy('Medical-Image-App:user_home')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(self.request, username=username, password=password)
        login(self.request, user)
        return super().form_valid(form)


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        patients = Patient.objects.all()
        doctors = Doctor.objects.all()

        context['doctors'] = doctors
        context['patients'] = patients
        return context


class PatientDetails(LoginRequiredMixin, DetailView):
    template_name = 'patient_details.html'
    model = Patient
    patient_id = None

    def dispatch(self, *args, **kwargs):
        self.patient_id = kwargs['pk']
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['patient'] = Patient.objects.filter(
            id=self.patient_id
        ).values_list(
            'id',
            'user__first_name',
            'user__middle_name',
            'user__last_name',
            'user__gender',
            'user__date_of_birth',
        )
        context['medical_image'] = MedicalImage.objects.filter(
            patient_id=self.patient_id
        ).values_list(
            'Description',
            'Medical Image'
        )
        context['doctor'] = Doctor.objects.filter(
            patient__exact=self.patient_id
        ).get()
        return context


class AddRecordForPatient(LoginRequiredMixin, FormView):
    template_name = 'add_record.html'
    form_class = AddRecordForm
    success_url = reverse_lazy("Medical-Image-App:user_home")
    def post(self, request, *args, **kwargs):
        form = AddRecordForm(data=request.POST)
        if form.is_valid():
            MedicalImage.objects.create(
                patient=form.cleaned_data.get('patient'),
                Description=form.cleaned_data.get('Description'),
                # medical_image=form.cleaned_data.get('Medical Image'),
            )

        return render(request, self.template_name, {'form': form})


class AddAccount(LoginRequiredMixin, FormView):
    template_name = 'add_account.html'
    form_class = AddAccountForm
    success_url = reverse_lazy('Medical-Image-App:user_home')

    def post(self, request, *args, **kwargs):
        form = AddAccountForm(data=request.POST)
        if form.is_valid():
            user = UserInformation.objects.create_user(
                first_name=form.cleaned_data.get('first_name'),
                middle_name=form.cleaned_data.get('middle_name'),
                last_name=form.cleaned_data.get('last_name'),
                gender=form.cleaned_data.get('gender'),
                date_of_birth=form.cleaned_data.get('date_of_birth'),
                user_type=form.cleaned_data.get('user_type'),
            )

            if user.is_authenticated and user.is_active:
                login(request, user)
                return redirect('main:user_home')

        return render(request, self.template_name, {'form': form})


class AddUserView(LoginRequiredMixin, FormView):
    template_name = 'add_account.html'
    form_class = AddUserForm
    success_url = reverse_lazy('Medical-Image-App:user_home')

    def post(self, request, *args, **kwargs):
        user_form = AddAccountForm(data=request.POST)
        if user_form.is_valid():
            user = User.objects.create_user(
                username=user_form.cleaned_data.get('username'),
                password=user_form.cleaned_data.get('password2')
            )

            if user.is_authenticated and user.is_active:
                login(request, user)
                return redirect('main:user_home')

        return render(request, self.template_name, {'user_form': user_form})
