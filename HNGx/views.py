from rest_framework.views import APIView
from rest_framework import status
from django.http import JsonResponse
from datetime import datetime


class GetInternDetail(APIView):
    def get(self, request):
        """
        Endpoint to return specific intern information in JSON format.
        """
        #Get the query parameters from the request
        slack_name = request.query_params.get('slack_name')
        track = request.query_params.get('track')

        #get the date and utc time
        date = datetime.now()
        utc_time = datetime.utcnow()

        #format to desired format
        current_day = date.strftime("%A")
        current_utc_time = utc_time.strftime('%Y-%m-%dT%H:%M:%SZ')

        data = {
            "slack_name": slack_name,
            "current_day": current_day,
            "utc_time": current_utc_time,
            "track": track,
            "github_file_url": "https://github.com/fikayo1/HNGx-internship/blob/main/HNGx/views.py",
            "github_repo_url": "https://github.com/fikayo1/HNGx-internship",
            "status_code" : 200
        }

        return JsonResponse(data=data, status=status.HTTP_200_OK)
