from .apps import ApiConfig
from rest_framework.views import APIView
from rest_framework.response import Response
#import necessary libraries




class Prediction(APIView):
    def post(self, request):
        data = request.data
        value = data['url']
        print(value)
        print("===========")
        print(request.data.get("sentence"))
        model = ApiConfig.model
        predicted = model.predict([value])[0]
        print(predicted)
        
        response_dict = {"result": predicted}
        return Response(response_dict, status=200)