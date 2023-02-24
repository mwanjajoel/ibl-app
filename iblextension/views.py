from django.http import JsonResponse, HttpResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from oauth2_provider.decorators import protected_resource
from .models import Greeting
from rest_framework.decorators import api_view
import requests
import os

@csrf_exempt
@protected_resource()
@api_view(['POST'])
def save_greeting(greeting):
    if greeting.method == 'POST':
        print("The request", greeting.data)
        text = greeting.data.get('text')
        if text:
            print(text)
            try:
                the_greeting = Greeting(text=text)
                the_greeting.save()
            except Exception as e:
                print(e)
                return JsonResponse({'message': 'Unable to save greeting.'})
            if text.lower() == 'hello':
                try:
                    url = os.getenv("BASE_API") + '?text=goodbye'
                    access_token = greeting.data.get('access_token')
                    print("The access token", access_token)
                    headers = {
                        'Authorization': 'Bearer {}'.format(access_token),
                    }
                    response = requests.get(url, headers=headers)
                    print("The response", response.json())
                except Exception as e:
                    print("The error: ==>", e)
                    return JsonResponse({'message': 'There was a server error, its not you, its us'})
                return JsonResponse({'message': 'Greeting saved and original greeting called again with "goodbye".'})
            else:
                return JsonResponse({'message': 'Greeting saved.'})
        else:
            return JsonResponse({'message': 'No greeting provided.'})
    else:
        return JsonResponse({'message': 'Invalid request method.'})


