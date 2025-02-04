import os, joblib
from pathlib import Path
from json import JSONDecodeError
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import views, status
from rest_framework.response import Response

from .serializers import InputDataSerializer
from utils.preprocessing_data import preprocessing_input_data
from utils.min_max_normalization import input_data_normalization
from utils.output_labeling import output_labeling


class InputDataAPIView(views.APIView):
    """
    A simple APIView for saving input data.
    """
    serializer_class = InputDataSerializer

    def get_serializer_context(self):
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        }

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)

    def post(self, request):
        try:
            data = JSONParser().parse(request)
            serializer = InputDataSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()

                prepared_data = preprocessing_input_data(data)
                
                scaled_data = input_data_normalization(prepared_data)

                current_path = Path.cwd()
                model_path = os.path.join(current_path, "utils/my_regression_model.pkl")
                reg_model = joblib.load(model_path)

                data_prediction = reg_model.predict(scaled_data)
                print(data_prediction, "\n")
                
                label = output_labeling(data_prediction)
                print(label)

                # return Response(data_prediction)
                
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except JSONDecodeError:
            return JsonResponse({"result": "error", "message": "Json decoding error"}, status= 400)
