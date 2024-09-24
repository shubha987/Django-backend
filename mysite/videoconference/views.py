from django.shortcuts import render
from django.conf import settings
from agora_token_builder import RtcTokenBuilder
from django.http import JsonResponse
import random
import time
from dotenv import load_dotenv
import os
import json
from .models import RoomMember

from django.views.decorators.csrf import csrf_exempt
load_dotenv()
# Create your views here.
def getToken(request):
    appId = os.getenv('APP_ID')
    appCertificate = os.getenv('AGORA_APP_CERTIFICATE')
    channelName = request.GET.get('channel')
    uid =random.randint(1,230)
    expirationTimeInSeconds =3600*24
    currentTimestamp = time.time()
    privilegeExpiredTs = currentTimestamp + expirationTimeInSeconds
    role=1
    token = RtcTokenBuilder.buildTokenWithUid(appId, appCertificate, channelName, uid, role, privilegeExpiredTs)
    return JsonResponse({'token':token,'uid':uid},safe=False)


def lobby(request):
    return render(request,'video_lobby.html')

def room(request):
    return render(request,'video_room.html')

@csrf_exempt
def createUser(request):
    data =json.loads(request.body)
    member, created= RoomMember.objects.get_or_create(
        name=data['name'],
        uid=data['UID'],
        room_name=data['room_name']
    )
    return JsonResponse({'name':data['name']},safe=False)