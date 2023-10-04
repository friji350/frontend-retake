import json
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Item  # Use relative import
from .serializers import ItemSerializer  # Use relative import
class ItemsView(APIView):
    @staticmethod
    def get(request):
        print(request.GET)
        if request.GET.get('id'):
            queryset_one = Item.objects.filter(id=request.GET.get("id")).first()
            return Response(ItemSerializer(queryset_one).data)
        else:
            queryset = Item.objects.all()
            return Response(ItemSerializer(queryset, many=True).data)

    @staticmethod
    def post(request):
        if request.data.get('name'):
            params = request.data
            Item.objects.create(name=params['name'],
                                description=params['description'],
                                img=params['img'],
                                type=params['type'])
            return Response(status=200, data="Success")
        else:
            return Response(status=400, data="No name")

    @staticmethod
    def delete(request):
        if request.GET.get('id'):
            params = request.GET
            delete = Item.objects.filter(id=params['id']).first()
            delete.delete()
            return Response(status=200, data="Success")
        else:
            return Response(status=400, data="No name")


class AddView(APIView):
    @staticmethod
    def post(request):
        response = add_item(request)
        return response

def add_item(request):
    data = request.data.get('item')
    name = data['name']
    description = data['description']
    type = data['type']
    img = data['img']
    new_item = Item.objects.create(name=name, description=description, type=type, img=img)
    new_item.save()
    response = {}
    response['data'] = 'ok'
    return Response(data=response, status=200)