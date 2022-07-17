from urllib import request
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Questions
from django.utils import timezone
from .forms import QueryForm
import requests
from .serializers import QuestionSerializer
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework.throttling import AnonRateThrottle
from .throttling import UserMinThrottle, UserDayThrottle


class All_ques_view(ListAPIView):
    queryset=Questions.objects.all()
    serializer_class=QuestionSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticated]
    throttle_classes=[AnonRateThrottle,UserMinThrottle,UserDayThrottle]

class HomeView(APIView):
    def get(self,request):
        return render(request,"api/home.html")

class QueryView(APIView):
    questions_details=[]
    quota=0
    form_class= QueryForm
    def post(self, request,*args, **kwargs):
        questions_details=[]
        form=self.form_class(request.POST)
        if form.is_valid():
            form.save()
            print(Questions.objects.all())
            scope= "https://api.stackexchange.com/2.3/search/advanced"    

            params = {
                        "page": request.POST['page'],
                        "pagesize": request.POST['pagesize'],
                        "fromdate": request.POST["fromdate"],
                        "todate": request.POST['todate'],
                        "order": request.POST['order'],
                        "sort": request.POST['sort'],
                        "min": request.POST['min'],
                        "max": request.POST['max'],
                        "q": request.POST['q'],
                        "accepted": request.POST.get('accepted', False),
                        "answers": request.POST['answers'],
                        "body": request.POST['body'],
                        "closed": request.POST.get('closed', False),
                        "migrated": request.POST.get('migrated', False),
                        "notice": request.POST.get('notice', False),
                        "nottagged": request.POST['nottagged'],
                        "tagged": request.POST['tagged'],
                        "title": request.POST['title'],
                        "user": request.POST['user'],
                        "url": request.POST['url'],
                        "views": request.POST['views'],
                        "wiki": request.POST.get('wiki', False),
                        "site": "stackoverflow"
                    }
            response = requests.get(scope,params=params)
            print(response.json())
            questions = response.json()['items']
            print(response.url)

            for index, question in enumerate(questions):
                format_code = "{}. {}\n".format(index + 1, question["title"])
                questions_details.append(format_code)
                quota = "\nYou have {} requests left today.".format(response.json()["quota_remaining"])
                print("\nYou have {} requests left today.".format(response.json()["quota_remaining"]))
        else:
            form=QueryForm()
        context={'form':form,'question':questions_details,'quota':quota}
        return render(request,'api/query.html',context)



   

