from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def predict_breed(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            tail_length = data.get("tail_length")
            ear_size = data.get("ear_size")

            return JsonResponse({
                "received": {
                    "tail_length": tail_length,
                    "ear_size": ear_size
                },
                "breed": "beagle"
            })
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    return JsonResponse({'error': 'POST request required'}, status=405)
