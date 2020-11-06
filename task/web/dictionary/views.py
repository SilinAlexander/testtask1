from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from django.views.generic import TemplateView
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Word
from .serializers import WordSerializer
# Create your views here.


class HomePageView(TemplateView):
    template_name = 'home.html'


class WordView(APIView):
    def get(self, request):
        words = Word.objects.all()
        serializer = WordSerializer(words, many=True)
        return Response({"words": serializer.data})

    def post(self, request):
        word = request.data.get('word')
        serializer = WordSerializer(data=word)
        if serializer.is_valid(raise_exception=True):
            word_saved = serializer.save()
        return Response({"success": "Word ' { } ' created successfully".format(word_saved.title)})

    def put(self, request, pk):
        saved_word = get_object_or_404(Word.objects.all(), pk=pk)
        data = request.data.get('word')
        serializer = WordSerializer(instance=saved_word, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            word_saved = serializer.save()

        return Response({"success": "Word ' { } ' updated successfully".format(word_saved.title)})

    def delete(self, request, pk):
        word = get_object_or_404(Word.objects.all(), pk=pk)
        word.delete()
        return Response({"message": "Word with id' { } ' has been deleted".format(pk)}, status=204)
