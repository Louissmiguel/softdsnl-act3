# api/views.py
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

            # Dummy classifier logic (can be replaced with real ML model)
            if tail_length < 2:
                breed = "chihuahua"
            elif tail_length < 5:
                breed = "beagle"
            else:
                breed = "german_shepherd"

            return JsonResponse({
                "input": {
                    "tail_length": tail_length,
                    "ear_size": ear_size
                },
                "predicted_breed": breed
            })
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({'error': 'POST request required'}, status=405)
