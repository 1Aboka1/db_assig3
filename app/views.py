from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import User, Caregiver, Member, Address, Job, JobApplication, Appointment
from .forms import UserForm, CaregiverForm, MemberForm, AddressForm, JobForm, JobApplicationForm, AppointmentForm

class UserListView(ListView):
    model = User
    template_name = 'app/user_list.html'

class UserDetailView(DetailView):
    model = User
    template_name = 'app/user_detail.html'

class UserCreateView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'app/user_form.html'
    success_url = reverse_lazy('user_list')

class UserUpdateView(UpdateView):
    model = User
    form_class = UserForm
    template_name = 'app/user_form.html'
    success_url = reverse_lazy('user_list')

class UserDeleteView(DeleteView):
    model = User
    template_name = 'app/user_confirm_delete.html'
    success_url = reverse_lazy('user_list')

class CaregiverListView(ListView):
    model = Caregiver
    template_name = 'app/caregiver_list.html'

class CaregiverDetailView(DetailView):
    model = Caregiver
    template_name = 'app/caregiver_detail.html'

class CaregiverCreateView(CreateView):
    model = Caregiver
    form_class = CaregiverForm
    template_name = 'app/caregiver_form.html'
    success_url = reverse_lazy('caregiver_list')

class CaregiverUpdateView(UpdateView):
    model = Caregiver
    form_class = CaregiverForm
    template_name = 'app/caregiver_form.html'
    success_url = reverse_lazy('caregiver_list')

class CaregiverDeleteView(DeleteView):
    model = Caregiver
    template_name = 'app/caregiver_confirm_delete.html'
    success_url = reverse_lazy('caregiver_list')

class MemberListView(ListView):
    model = Member
    template_name = 'app/member_list.html'

class MemberDetailView(DetailView):
    model = Member
    template_name = 'app/member_detail.html'

class MemberCreateView(CreateView):
    model = Member
    form_class = MemberForm
    template_name = 'app/member_form.html'
    success_url = reverse_lazy('member_list')

class MemberUpdateView(UpdateView):
    model = Member
    form_class = MemberForm
    template_name = 'app/member_form.html'
    success_url = reverse_lazy('member_list')

class MemberDeleteView(DeleteView):
    model = Member
    template_name = 'app/member_confirm_delete.html'
    success_url = reverse_lazy('member_list')

class AddressListView(ListView):
    model = Address
    template_name = 'app/address_list.html'

class AddressDetailView(DetailView):
    model = Address
    template_name = 'app/address_detail.html'

class AddressCreateView(CreateView):
    model = Address
    form_class = AddressForm
    template_name = 'app/address_form.html'
    success_url = reverse_lazy('address_list')

class AddressUpdateView(UpdateView):
    model = Address
    form_class = AddressForm
    template_name = 'app/address_form.html'
    success_url = reverse_lazy('address_list')

class AddressDeleteView(DeleteView):
    model = Address
    template_name = 'app/address_confirm_delete.html'
    success_url = reverse_lazy('address_list')

class JobListView(ListView):
    model = Job
    template_name = 'app/job_list.html'

class JobDetailView(DetailView):
    model = Job
    template_name = 'app/job_detail.html'

class JobCreateView(CreateView):
    model = Job
    form_class = JobForm
    template_name = 'app/job_form.html'
    success_url = reverse_lazy('job_list')

class JobUpdateView(UpdateView):
    model = Job
    form_class = JobForm
    template_name = 'app/job_form.html'
    success_url = reverse_lazy('job_list')

class JobDeleteView(DeleteView):
    model = Job
    template_name = 'app/job_confirm_delete.html'
    success_url = reverse_lazy('job_list')

class JobApplicationListView(ListView):
    model = JobApplication
    template_name = 'app/jobapplication_list.html'

class JobApplicationDetailView(DetailView):
    model = JobApplication
    template_name = 'app/jobapplication_detail.html'

class JobApplicationCreateView(CreateView):
    model = JobApplication
    form_class = JobApplicationForm
    template_name = 'app/jobapplication_form.html'
    success_url = reverse_lazy('jobapplication_list')

class JobApplicationUpdateView(UpdateView):
    model = JobApplication
    form_class = JobApplicationForm
    template_name = 'app/jobapplication_form.html'
    success_url = reverse_lazy('jobapplication_list')

class JobApplicationDeleteView(DeleteView):
    model = JobApplication
    template_name = 'app/jobapplication_confirm_delete.html'
    success_url = reverse_lazy('jobapplication_list')

class AppointmentListView(ListView):
    model = Appointment
    template_name = 'app/appointment_list.html'

class AppointmentDetailView(DetailView):
    model = Appointment
    template_name = 'app/appointment_detail.html'

class AppointmentCreateView(CreateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = 'app/appointment_form.html'
    success_url = reverse_lazy('appointment_list')

class AppointmentUpdateView(UpdateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = 'app/appointment_form.html'
    success_url = reverse_lazy('appointment_list')

class AppointmentDeleteView(DeleteView):
    model = Appointment
    template_name = 'app/appointment_confirm_delete.html'
    success_url = reverse_lazy('appointment_list')
