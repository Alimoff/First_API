from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Videos
from .serializer import VideosSerializer
from rest_framework import status

# Create your views here.


class VideosViews(APIView):
    def get(self, request):
        all_videos = Videos.objects.all()

        serialized_data = VideosSerializer(data=all_videos, many=True)

        serialized_data.is_valid()

        return Response(data=serialized_data.data)

    def post(self, request):
        serialized_data = VideosSerializer(data=request.data)

        if serialized_data.is_valid():
            serialized_data.save()

            return Response(data=serialized_data.data)

        return Response({"error": serialized_data.errors})

    def delete(self, request):
        id = request.data["id"]

        try:
            Videos.objects.get(id=id).delete()

            return Response({"status": "success"}, status=status.HTTP_200_OK)
        except:
            return Response({"status": "not found"}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request):
        videos = Videos.objects.get(id=request.data["id"])

        serialized_data = VideosSerializer(Videos, data=request.data, partial=True)

        if serialized_data.is_valid():
            serialized_data.save()

            return Response(data=serialized_data.data)

        return Response({"error": serialized_data.errors})


class SingleVideos(APIView):
    def get(self, request, id):
        videos_data = Videos.objects.get(id=id)

        return Response(
            data={
                "id": videos_data.id,
                "name": videos_data.name,
                "text": videos_data.text,
                "created_at": videos_data.created_at,
                "updated_at": videos_data.updated_at,
            }
        )
