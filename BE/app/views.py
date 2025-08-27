from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import re

from django.contrib.auth.hashers import make_password

from .models import User
from .utils import generate_custom_salted_hash

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

        # Basic presence check
        if not all([name, email, mobile, password]):
            return JsonResponse({'error': 'All fields are required'}, status=400)

        # Email format check
        email_regex = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
        if not re.match(email_regex, email):
            return JsonResponse({'error': 'Invalid email format'}, status=400)

        # Mobile number check (12 digits)
        mobile_regex = r'^\d{12}$'
        if not re.match(mobile_regex, mobile):
            return JsonResponse({'error': 'Mobile number must be 12 digits (country code + 10-digit number)'}, status=400)

        # Password strength check
        password_regex = r'^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_\+\[\]{}:;<>,.?~\\/\-]).{6,}$'

        if not re.match(password_regex, password):
            return JsonResponse({
                'error': 'Password must contain at least one uppercase letter, one number, and one special character.'
            }, status=400)

        # Check for existing email or mobile
        if User.objects.filter(email=email).exists():
            return JsonResponse({'error': 'Email already registered'}, status=409)

        if User.objects.filter(mobile=mobile).exists():
            return JsonResponse({'error': 'Mobile number already registered'}, status=409)

        # Generate salted hash
        salt, hashed_password = generate_custom_salted_hash(password)
        

        # Create and save user
        user = User(name=name, email=email, mobile=mobile, password_hash=hashed_password,salt=salt,role=1)
        user.save()


        # All validations passed
        return JsonResponse({'message': 'User Created'}, status=200)

    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON format'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)