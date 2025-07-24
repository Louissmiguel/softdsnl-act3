from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import joblib  # or pickle

# Load your ML model (assumes you trained and saved it before)
model = joblib.load('ml_model.pkl')  # make sure this file exists

@csrf_exempt
def predict_breed(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        tail_length = data.get('tail_length')
        ear_size = data.get('ear_size')

        if tail_length is None or ear_size is None:
            return JsonResponse({'error': 'Missing parameters'}, status=400)

        # Predict using model
        prediction = model.predict([[tail_length, ear_size]])[0]

        return JsonResponse({'breed': prediction})
    return JsonResponse({'error': 'Only POST method allowed'}, status=405)
