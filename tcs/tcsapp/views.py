import json

from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from .models import Theatre, Location


# Create your views here.
def welcome(request):
    return HttpResponse("hello worlds")


class Creating(View):
    def post(self, request):
        res = {
            "status": False,
            "data": [],
            "msg": "Failed"
        }
        try:
            data = json.loads(request.body.decode('utf-8'))
            name = data.get("name")
            no_of_seats = data.get("no_of_seats")
            ac = data.get("ac")
            theatres = Theatre.objects.create(name=name, no_of_seats=no_of_seats, ac=ac)
            theatres.save()
            res["status"] = True
            res["data"] = {"id": theatres.id, "name": theatres.name, "no_of_seats": theatres.no_of_seats,
                           "ac": theatres.ac}
            res["msg"] = "success"
            res['welcome'] = ["welcome", theatres.name]
        except Exception as e:
            print(e)
        return HttpResponse(str(res))


class Fetch(View):
    def post(self, request):
        res = {
            "status": False,
            "data": [],
            "msg": "Failed"
        }
        try:
            data = json.loads(request.body.decode('utf-8'))
            name = data.get("name")
            details = Theatre.objects.get(name=name)
            res["status"] = True
            res["data"] = {"ac": details.ac}
            if res["data"]["ac"] is True:
                res["info"] = f"yes, this theatre has AC"
            else:
                res["info"] = f"no, this theatre does not has AC"

            res["msg"] = "success"
        except Exception as e:
            print(e)
        return HttpResponse(str(res))


class Ac_Fetch(View):
    def post(self, request):
        res = {
            "status": False,
            "data": [],
            "msg": "Failed"
        }
        try:
            data = json.loads(request.body.decode('utf-8'))
            ac = data.get("ac")
            details = list(Theatre.objects.filter(ac=ac).values_list("no_of_seats", "name"))
            print(details)
            lst = list(details)
            if data["ac"]:
                for detail in lst:
                    res["data"].append(f" AC Theatre name is {detail[1]} and it's seats are {detail[0]}")
            else:
                for detail in lst:
                    res["data"].append(f"Non AC Theatre name is {detail[1]} and it's seats are {detail[0]}")
            res["status"] = True
            res["msg"] = "success"
        except Exception as e:
            print(e)
        return HttpResponse(str(res) )

# class Ac_city(View):
#     def post(self, request):
#         res = {
#             "status": False,
#             "data": [],
#             "msg": "Failed"
#         }
#         try:
#             data = json.loads(request.body.decode('utf-8'))
#             city = data.get("city")
#             name = data.get("name")
#             no_of_seats = data.get("no_of_seats")
#             ac = data.get("ac")
#             locations = Location.objects.get(city=city)
#             details = Theatre.objects.filter(ac=ac).values_list("name")
#             res["status"] = True
#             res["data"] = {"ac" : details.ac}
#             res["data"] = {"city": locations.city}
#             lst = list(details)
#             if data["ac"]:
#                 for detail in lst:
#                     res["data"].append(f" list{detail[1]} {detail[0]}")
#             else:
#                 for detail in lst:
#                     res["data"].append(f" list {detail[1]} {detail[0]}")
#         except Exception as e:
#             print(e)
#         return HttpResponse(str(res))