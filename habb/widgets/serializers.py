from rest_framework import serializers
from .models import Leed, Widget


class LeedSerializer(serializers.ModelSerializer):
	class Meta:
		model = Leed
		fields = ('id', 'widget', 'first_name', 'last_name', 'email', 'phone_number', 'token', 'referal',)


class WidgetSerializer(serializers.ModelSerializer):
	class Meta:
		model = Widget
		fields = ('id', 'status', 'competition')

'''
class LeedSerializer(serializers.Serializer):
	name = serializers.CharField(required=False, allow_blank=True, max_length=50)
	email = serializers.CharField(required=False, allow_blank=True, max_length=50)
	phone_number = serializers.CharField(required=False, allow_blank=True, max_length=50)

	def create(self, validated_data):
	"""
	Create and return a new `Leed` instance, given the validated data.
	"""
	return Leed.objects.create(**validated_data)

	def update(self, instance, validated_data):
	"""
	Update and return an existing `Leed` instance, given the validated data.
	"""
	instance.name = validated_data.get('name', instance.name)
	instance.email = validated_data.get('email', instance.email)
	instance.phone_number = validated_data.get('phone_number', instance.phone_number)
	instance.save()
	return instance
'''