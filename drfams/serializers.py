from rest_framework import serializers
from .models import Assets,Bookings

class AssetSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Assets
        fields = ['id','title','details','created_at']

class AssetField(serializers.RelatedField):
    def to_representation(self, value):
        return value.title
    
    def to_internal_value(self, data):
        for item in data:
            print('item:',item)
        try:
            try:
                value_id = data
                return Assets.objects.get(id=value_id)
            except KeyError:
                raise serializers.ValidationError(
                    'id is a required field.'
                )
            except ValueError:
                raise serializers.ValidationError(
                    'id must be an integer.'
                )
        except Assets.DoesNotExist:
            raise serializers.ValidationError(
            'Obj does not exist.'
            )

class BookingSerializer(serializers.ModelSerializer): 
    asset = AssetField(many=True,queryset=Assets.objects.all())
    class Meta:
        model = Bookings
        fields = ['id','asset','user','time_block','created_at']

class MaskAssetBookingSerializer(serializers.ModelSerializer): 
    asset = AssetField(many=True,queryset=Assets.objects.all())
    class Meta:
        model = Bookings
        fields = ['id','asset','time_block','created_at']