from django.contrib import admin
from .models import InputData


@admin.register(InputData)
class InputDataAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'orientation',
                    'window_wall_ratio',
                    'depth_of_shade',
                    'wall_r_value',
                    'glass_u_factor',
                    'cooling',
                    'heating',
                    'lighting',
                    )