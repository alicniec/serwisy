from rest_framework import serializers

from .models import Visit


class VisitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Visit
        fields = (
            'doctor', 'patient', 'address', 'date'
        )

    def create(self, validated_data):
        validated_data['doctor'] = self.context['request'].user
        return super().create(validated_data)
