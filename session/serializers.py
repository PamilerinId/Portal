from rest_framework import serializers
from session.models import Session


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = [
            'id',
            'session',
            'is_current'
        ]
