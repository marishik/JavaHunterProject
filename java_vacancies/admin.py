from django.contrib import admin
from .models import top_vacancies_skillls
from .models import demand_model
from .models import geography_model

admin.site.register(top_vacancies_skillls)
admin.site.register(demand_model)
admin.site.register(geography_model)
