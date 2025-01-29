from . import models
from rest_framework import serializers
from rest_framework.fields import CharField, FloatField



class InputDataSerializer(serializers.ModelSerializer):

	orientation = CharField(required=True)
	window_wall_ratio = FloatField(required=True)
	depth_of_shade = FloatField(required=True)
	wall_r_value = FloatField(required=True)
	glass_U_factor = FloatField(required=True)
	
	cooling = FloatField()
	heating = FloatField()
	lighting = FloatField()
	
	class Meta:
		model = models.InputData
		fields = (
			'orientation',
			'window_wall_ratio',
			'depth_of_shade',
			'wall_r_value',
			'glass_U_factor',
			'cooling',
			'heating',
			'lighting',
		)