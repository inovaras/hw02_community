from django.views.generic.base import TemplateView


class AboutAuthorView(TemplateView):
    template_name = 'about/author.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['github'] = 'Гитхаб: https://github.com/inovaras'
        context['telegram'] = 'Телеграмм: https://github.com/inovaras'
        return context


class AboutTechView(TemplateView):
    template_name = 'about/tech.html'
