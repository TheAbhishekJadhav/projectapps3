from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Assets,Bookings
from .serializers import BookingSerializer,AssetSerializer,MaskAssetBookingSerializer

# Create your views here.
class AssetView(APIView):
    def get(self, request, *args, **kwargs):
        qs = Assets.objects.all()
        serializer = AssetSerializer(qs, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        uname = request.POST.get("username")
        if uname=="admin":
            serializer = AssetSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        else:
            return Response('{"detail": "User is not admin"}')


class GetBookingView(APIView):
    def post(self, request, *args, **kwargs):
        uname = request.POST.get("username")
        if uname=="admin":
            print('admin user')
            qs = Bookings.objects.all().order_by('created_at').reverse()
            serializer = BookingSerializer(qs, many=True)
            print(qs.ordered)
        else:
            print(uname)
            qs = Bookings.objects.filter(user=uname).order_by('created_at').reverse()
            serializer = BookingSerializer(qs, many=True)
        return Response(serializer.data)

class AddBookingView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = BookingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class GetAssetBookingView(APIView):
    def post(self, request, *args, **kwargs):
        uname = request.POST.get("username")
        assetId = request.POST.get("asset")
        if uname=="admin":
            print('admin user')
            qs = Bookings.objects.filter(asset__id=assetId).order_by('created_at').reverse()
            serializer = BookingSerializer(qs, many=True)
            print(qs.ordered)
        else:
            print(uname)
            qs = Bookings.objects.filter(asset__id=assetId).defer("user").order_by('created_at').reverse()
            serializer = MaskAssetBookingSerializer(qs, many=True)
        return Response(serializer.data)
