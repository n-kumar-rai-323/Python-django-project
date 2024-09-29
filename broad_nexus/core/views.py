from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView,CreateView
from .models import Job,Category,JobApplication
from commons.pagination import CustomPagination
from commons.utils import get_base_url, is_profile_complete
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .forms import ContactForm

class HomeView(ListView):
    template_name = 'core/home.html'
    queryset = Job.objects.filter(is_active=True)
    pagination_class = CustomPagination

    def get_pagination(self):
        return self.pagination_class()

    def get_queryset(self):
        category  = self.request.GET.get('category')
        search = self.request.GET.get('search')
        Job_filter={"is_active": True}
        exclude = dict()
        if self.request.user.is_authenticated:
            exclude={"job_applications__user":self.request.user}
        if category:
            Job_filter.update(category__uuid=category)
        if search:
            Job_filter.update(title__icontains=search)
        return Job.objects.filter(**Job_filter).exclude(**exclude).order_by('id')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "home"
        pagination = self.get_pagination()
        qs = pagination.get_paginated_qs(view=self)
        paginated_qs = pagination.get_nested_pagination(qs, nested_size=2)
        context['jobs_lists']=paginated_qs
        context['categories'] = Category.objects.all()
        page_number, page_str = pagination.get_current_page(view=self)
        context[page_str]='active'
        context["next_page"]= page_number + 1
        context["prev_page"]= page_number - 1
        context['base_url'] = get_base_url(request=self.request)
        if page_number >= pagination.get_last_page(view=self):
            context["next"] = "disabled"
        if page_number <= 1:
            context["prev"]="disabled"
        context['home_active']= 'active'
        return context
@login_required
def job_apply(request, uuid):
    try:
        job=Job.objects.get(uuid=uuid)
    except Job.DoesNotExits:
        messages.error(request, "Something went wrong !!")
        return redirect('home')
    if is_profile_complete(request.user):
        JobApplication.objects.get_or_create(user=request.user, job=job, defaults={"status":"APPLIED"})
        messages.success(request, "Successfully Applied For The Job !!")
        return redirect('home')
    messages.error(request, "Please Activate Your Account And Complete Your Profile !!")
    return redirect('home')



class JobDetailView(DetailView):
    template_name = "core/job_detail.html"
    queryset = Job.objects.filter(is_active=True)
    slug_field = 'uuid'
    slug_url_kwarg = 'uuid'
    context_object_name = 'job'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Job Detail"
        return context

class MyJobView(ListView):
    template_name = "core/my_job.html"
    context_object_name = 'job_applications'

    def get_queryset(self):
        status=self.request.GET.get('status')
        application_filter =dict(user=self.request.user)
        if status:
            application_filter.update(status=status)
        return JobApplication.objects.filter(**application_filter)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "My Jobs"
        context["statuses"]= ["APPLIED", "SCREENING", "SHORT_LISTED","REJECTED"]
        context['my_jobs_active']= 'active'
        return context

class ContactView(CreateView):
    template_name = "core/contact.html"
    form_class = ContactForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"]= "Contact Us"
        context["contact_active"]="active"
        return context

