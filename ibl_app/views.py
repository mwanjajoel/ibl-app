from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from oauth2_provider.decorators import protected_resource
from .models import Greeting
from rest_framework.decorators import api_view

@csrf_exempt
@protected_resource()
@api_view(['POST'])
def save_greeting(request):
    if request.method == 'POST':
        print("The request", request.data)
        text = request.data.get('text')
        if text:
            print(text)
            try:
                greeting = Greeting(text=text)
                greeting.save()
            except Exception as e:
                print(e)
                return JsonResponse({'message': 'Unable to save greeting.'})
            if text.lower() == 'hello':
                response = request.get(os.getenv("BASE_API") + '?text=goodbye', headers={
                    'Authorization': 'Bearer {}'.format(request.access_token.token),
                })
                return JsonResponse({'message': 'Greeting saved and original greeting called again with "goodbye".'})
            else:
                return JsonResponse({'message': 'Greeting saved.'})
        else:
            return JsonResponse({'message': 'No greeting provided.'})
    else:
        return JsonResponse({'message': 'Invalid request method.'})


