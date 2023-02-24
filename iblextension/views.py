from django.http import JsonResponse, HttpResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from oauth2_provider.decorators import protected_resource
from .models import Greeting
from rest_framework.decorators import api_view
import requests
import os

@csrf_exempt
@protected_resource()
@api_view(['POST', 'GET'])
def save_greeting(greeting):
    if greeting.method == 'POST' or greeting.method == 'GET':
        print("The request", greeting.data)
        text = greeting.data.get('text')

        # check to see if there is text in the POST request and save it
        if text:
            print(text)
            try:
                the_greeting = Greeting(text=text)
                the_greeting.save()
            except Exception as e:
                print(e)
                return JsonResponse({'message': 'Unable to save greeting.'})
            
            # check to see if the text is hello
            if text.lower() == 'hello':
                try:
                    url = os.getenv("BASE_API") + '?text=goodbye'
                    client_id = os.getenv("CLIENT_ID")
                    client_secret = os.getenv("CLIENT_SECRET")
                    username = os.getenv("USERNAME")
                    password = os.getenv("PASSWORD")
                    token_url = os.getenv("TOKEN_URL")
                    
                    # get a new access token
                    try:
                        access_token = get_access_token(client_id, client_secret, username, password, token_url)
                        
                        print("The access token", access_token)
                    except Exception as e:
                        print("The error: ==>", e)
                        return JsonResponse({'message': 'There was a server error, its not you, its us'})
                    
                    # call the original API with the goodbye parameter as a GET request
                    headers = {
                        'Authorization': 'Bearer ' + access_token,
                        'Content-Type': 'application/json',
                    }

                    response = requests.get(url, headers=headers)
                    print("The response", response.json())
                except Exception as e:
                    print("The error: ==>", e)
                    return JsonResponse({'message': 'There was a server error, its not you, its us'})
                return JsonResponse({'message': 'Goodbye!'})
            else:
                return JsonResponse({'message': 'Greeting saved.'})
        else:
            # get the parameter from the GET request and save the greeting
            text = greeting.GET.get('text')
            if text:
                print(text)
                try:
                    the_greeting = Greeting(text=text)
                    the_greeting.save()
                except Exception as e:
                    print(e)
                    return JsonResponse({'message': 'Unable to save greeting.'})
                return JsonResponse({'message': 'Greeting saved.'})
            return JsonResponse({'message': 'No greeting provided.'})
    else:
        return JsonResponse({'message': 'DANG!! Something really went wrong.'})

@csrf_exempt
@protected_resource()
@api_view(['POST'])
# method to get a new access token
def get_access_token(client_id, client_secret, username, password, token_url):
   
    request_data = {
        'grant_type': 'password',
        'username': username,
        'password': password,
    }
    response = requests.post(
        token_url,
        data=request_data,
        auth=(client_id, client_secret),
        headers={'Content-Type': 'application/x-www-form-urlencoded'}
    )
    token = JsonResponse(response.json())
    return token.access_token



