from django.db import models
from utils.model_abstracts import Model
from django_extensions.db.models import (
	TimeStampedModel, 
	ActivatorModel,
	TitleDescriptionModel
)

class InputData(
	TimeStampedModel, 
	ActivatorModel,
	TitleDescriptionModel,
	Model
	):
	
	class Meta:
		verbose_name_plural = "data_inputs"

    
	orientation_value = {
		"North": "N",
		"East": "E",
		"South": "S",
		"West": "W",
    }
	
	orientation = models.CharField(verbose_name="orientation", max_length=1)	
	window_wall_ratio = models.FloatField(verbose_name="window_wall_ratio")
	depth_of_shade = models.FloatField(verbose_name="depth_of_shade")
	wall_r_value = models.FloatField(verbose_name="wall_R_value")
	glass_U_factor = models.FloatField(verbose_name="glass_u_factor")
	
	cooling = models.FloatField(verbose_name="cooling", blank=True)
	heating = models.FloatField(verbose_name="heating", blank=True)
	lighting = models.FloatField(verbose_name="lighting", blank=True)
	
	

	def __str__(self):
		return f'{self.title}'