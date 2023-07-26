from rest_framework import serializers

from apps.users.models import House, Spell, User

""" class UserSerializer(serializers.Serializer):
    nombre = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, write_only=True)

    def validate(self, attrs):
        email = attrs.get("email")

        if "@" not in email :
            raise serializers.ValidationError("No hay @")
        if "gmail.com" not in email:
            raise serializers.ValidationError({"email": "No es gmail"})
      
        return super().validate(attrs)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["nombre"] = representation["nombre"].upper()
        return representation """
    
 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = "__all__"


class SpellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spell
        fields = "__all__"
  