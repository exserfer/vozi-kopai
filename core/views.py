from django.shortcuts import render
from core.models import DumperModels, MachinesOperation
from django.views.decorators.csrf import requires_csrf_token


@requires_csrf_token
def index(request):
    """ Main (singleton) template """
    dumper_models = DumperModels.objects.all()
    dumper_models_filter = request.POST.get('dumper_models', 0)

    active_machines = MachinesOperation.objects

    if int(dumper_models_filter) == 0:
        active_machines = active_machines.all()
    else:
        active_machines = active_machines.filter(machines__manufacturer=dumper_models_filter)

    return render(request,
                  'core/index.html',
                  {
                      'dumper_models': dumper_models,
                      'active_machines': active_machines,
                      'dumper_models_filter': int(dumper_models_filter)
                  })
