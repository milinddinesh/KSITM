from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import re

@csrf_exempt
def signup(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Invalid request method'}, status=405)

    try:
        data = json.loads(request.body)
        name = data.get('name', '').strip()
        email = data.get('email', '').strip()
        mobile = data.get('mobile', '').strip()
        password = data.get('password', '')

        

        return JsonResponse({'message': 'Validation passed'}, status=200)

    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON format'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
