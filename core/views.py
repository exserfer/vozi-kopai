from django.shortcuts import render
from core.models import DumperModels, MachinesOperation
from django.views.decorators.csrf import requires_csrf_token
from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    template_name = 'core/index.html'
    http_method_names = ["get", "post"]

    def the_quarry_context(self, context):
        dumper_models = DumperModels.objects.all()
        dumper_models_filter = self.request.POST.get('dumper_models', 0)
        active_machines = MachinesOperation.objects

        if int(dumper_models_filter) == 0:
            active_machines = active_machines.all()
        else:
            active_machines = active_machines.filter(machines__manufacturer=dumper_models_filter)

        context['dumper_models'] = dumper_models
        context['active_machines'] = active_machines
        context['dumper_models_filter'] = int(dumper_models_filter)

        return context

    def get_context_data(self, *args, **kwargs):
        context = super(HomePageView, self).get_context_data(*args, **kwargs)
        return self.the_quarry_context(context=context)

    def post(self, request, *args, **kwargs):
        context = super(HomePageView, self).get_context_data(*args, **kwargs)
        context = self.the_quarry_context(context=context)
        return self.render_to_response(context)
