from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import joblib
from django.conf import settings
import os

# Load model and encoder using correct paths
model_path = os.path.join(settings.BASE_DIR, "ml_api", "model.pkl")
encoder_path = os.path.join(settings.BASE_DIR, "ml_api", "label_encoder.pkl")

# Load model and label encoder
model = joblib.load(model_path)
label_encoder = joblib.load(encoder_path)

class PredictView(APIView):
    def post(self, request):
        try:
            tail_length = float(request.data.get("tail_length"))
            ear_size = float(request.data.get("ear_size"))

            prediction = model.predict([[tail_length, ear_size]])
            breed_label = label_encoder.inverse_transform(prediction)[0]

            return Response({"prediction": breed_label})
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
