from rest_framework.serializers import ModelSerializer
from .models import Videos


class VideosSerializer(ModelSerializer):
    class Meta:
        model = Videos
        fields = "__all__"

