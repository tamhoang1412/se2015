from django.views.generic.base import TemplateView
# from django.utils.decorators import method_decorator


class IndexView(TemplateView):
    template_name = 'main/index.html'

# def index(request):
#    return render(request, 'main/index.html')
