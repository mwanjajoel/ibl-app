from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from oauth2_provider.decorators import protected_resource
from models import Greeting

@csrf_exempt
@protected_resource()
def save_greeting(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        if text:
            print(text)
            Greeting.objects.create(text=text)
            if text.lower() == 'hello':
                response = requests.get('http://localhost:8000/api/v1/greeting?text=goodbye', headers={
                    'Authorization': 'Bearer {}'.format(request.access_token.token),
                    'Client-Id': 'my-client-id',
                    'Client-Secret': 'my-client-secret'
                })
                return JsonResponse({'message': 'Greeting saved and original greeting called again with "goodbye".'})
            else:
                return JsonResponse({'message': 'Greeting saved.'})
        else:
            return JsonResponse({'message': 'No greeting provided.'})
    else:
        return JsonResponse({'message': 'Invalid request method.'})


