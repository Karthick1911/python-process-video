from django.shortcuts import render
from django.conf import settings
import os

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import speech_recognition as sr

from .serializers import VideoSerializer
from .models import Video

# Create your views here.

@api_view(['GET'])
def showAll(request):
    videos = Video.objects.all()
    serializer = VideoSerializer(videos, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def save(request):
    def word_count(str):
      counts = dict()
      words = str.split()

      for word in words:
        if word in counts:
          counts[word] += 1
        else:
          counts[word] = 1  

      return counts
      
    serializer = VideoSerializer(data = request.data)
    if serializer.is_valid():
      res = serializer.save()
      #print(vars(res))
      #print(res.file)
      #data2 = request.POST.get('title')
      #print(data2); 

      ### Using the hardcoded video for testing ###
      inputdir = settings.MEDIA_ROOT + '\\video'
      outputdir = settings.MEDIA_ROOT + '\\video-wav'
      #for filename in os.listdir(inputdir):
        #actual_filename = filename[:-4]
        #os.system('ffmpeg -i {}/{} -acodec pcm_s16le -ar 16000 {}/{}.wav'.format(inputdir, filename, outputdir, actual_filename))
  
      os.system('ffmpeg -i {}/{} -acodec pcm_s16le -ar 16000 {}/{}.wav'.format(inputdir, "videoplayback.mp4", outputdir, "videoplayback"))
      
      audioFile = outputdir + "\\videoplayback.wav";

      r = sr.Recognizer()
      audio = sr.AudioFile(audioFile)

      with audio as source:
        audio = r.record(source, duration=100)
        text = r.recognize_google(audio)
        print(word_count(text))
    
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

