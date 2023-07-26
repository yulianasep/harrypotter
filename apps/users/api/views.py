from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404

from .serializers import UserSerializer, HouseSerializer, SpellSerializer
from apps.users.models import House, Spell, User

# class UserList(APIView):
#     def get(self, request, *args, **kwargs):
#         return Response(status=status.HTTP_200_OK)
    
#     def post(self, request, *args, **kwargs):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             print("Es valido", serializer.data)
#             return Response(serializer.data)
#         else:
#             print("No es valido", serializer.errors)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def spell_api_view(request, *args, **kwargs):

    if request.method == 'GET':
        queryset =  Spell.objects.all()
        serializers = SpellSerializer(queryset, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = SpellSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Spell created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def spell_detail_view (request, pk=None):
    spell = Spell.objects.filter(id=pk).first()

    if spell:

        if request.method == 'GET':
            serializer = SpellSerializer(spell)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        elif request.method =='PUT':
            serializer = SpellSerializer(spell, data= request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'Spell updated successfully'}, status=status.HTTP_200_OK)   
            return Response({"error": "Invalid input"},status=status.HTTP_400_BAD_REQUEST)
        
        elif request.method == 'DELETE':
            spell.delete()
            return Response(
                {"success":"The spell has been deleted."},
                status=status.HTTP_204_NO_CONTENT
            )
        
    return Response({"Error" : f"{spell} does not exist!"} ,status=status.HTTP_400_BAD_REQUEST)


# class HouseAPIView(APIView):

#     def get(self, request, *args, **kwargs):
#         houses = House.objects.all()
#         serializer = HouseSerializer(instance=houses, many=True)
#         return Response(serializer.data)

#     def post(self, request, *args, **kwargs):
#         serializer = HouseSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)

        
# class HouseDetailView(APIView):

#     def get(self, request, pk=None, *args, **kwargs):
#         house = get_object_or_404(House, pk=pk)
#         serializer = HouseSerializer(instance=house)
#         return Response(serializer.data)
    
#     def put(self, request, pk=None, *args, **kwargs):
#         house = get_object_or_404(House, pk=pk)
#         serializer = HouseSerializer(instance=house, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
        
#     def delete(self, request, pk=None, *args, **kwargs):
#         house = get_object_or_404(House, pk=pk)
#         house.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT) 


class HouseViewSet(viewsets.ModelViewSet):
    serializer_class = HouseSerializer
    queryset = House.objects.all()

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter()
        return self.get_serializer().Meta.model.objects.filter(pk=pk).first()
    
    def list(self, request, *args, **kwargs):
        house_serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(house_serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None, *args, **kwargs):
        if self.get_queryset(pk):
            house_serializer= self.serializer_class(self.get_queryset(pk), data=request.data)
            if house_serializer.is_valid():
                house_serializer.save()
                return Response(house_serializer.data, status= status.HTTP_200_OK)
            return Response(house_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, pk=None, *args, **kwargs):
        house = self.get_queryset().filter(pk=pk).first()
        if house:
            house.delete()
            response = {'message': 'Successfully deleted'}
            return Response(response, status=status.HTTP_200_OK)
        return Response({'error': 'No existe un producto con esos datos!'}, status=status.HTTP_400_BAD_REQUEST)

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter()
        return self.get_serializer().Meta.model.objects.filter(pk=pk).first()
    
    def list(self, request, *args, **kwargs):
        user_serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(user_serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None, *args, **kwargs):
        if self.get_queryset(pk):
            user_serializer= self.serializer_class(self.get_queryset(pk), data=request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data, status= status.HTTP_200_OK)
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, pk=None, *args, **kwargs):
        user = self.get_queryset().filter(pk=pk).first()
        if user:
            user.delete()
            response = {'message': 'Successfully deleted'}
            return Response(response, status=status.HTTP_200_OK)
        return Response({'error': 'No existe un producto con esos datos!'}, status=status.HTTP_400_BAD_REQUEST)