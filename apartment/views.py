from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.filters import OrderingFilter
from rest_framework import generics 
from rest_framework.permissions import AllowAny, IsAuthenticated

from .permissions import IsOwnerOrReadOnly
from .models import ApartmentModel, MyRentsModel
from .serializer import AparmentSerializer, MyRentSerializer
from .filters import RoomFilter

User = get_user_model()

#views для списка орендованных домов пользавателя
class MyRentList(generics.ListAPIView):
    queryset = MyRentsModel.objects.all()
    serializer_class = MyRentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_classes = [RoomFilter]

class MyRentRetrieve(generics.RetrieveAPIView):
    queryset = MyRentsModel.objects.all()
    serializer_class = MyRentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    lookup_field = 'pk'

class MyRentCreate(generics.CreateAPIView):
    queryset = MyRentsModel.objects.all()
    serializer_class = MyRentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    apart = ApartmentModel.objects.all()
    apart.active = True


class MyRentDelete(generics.DestroyAPIView):
    queryset = MyRentsModel.objects.all
    serializer_class = MyRentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    apart = ApartmentModel.objects.all()
    apart.active = False
    lookup_field = 'pk'


#views  для всех домов/квартир на сайте
class ApartMentList(generics.ListAPIView):
    queryset = ApartmentModel.objects.all()
    serializer_class = AparmentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_classes = [RoomFilter]



class ApartMentRetrieve(generics.RetrieveAPIView):
    queryset = ApartmentModel.objects.all()
    serializer_class = AparmentSerializer
    lookup_field = 'pk'



    





# from rest_framework import status
# from rest_framework.viewsets import ViewSet
# from rest_framework.response import Response
# from rest_framework.permissions import AllowAny, IsAuthenticated

# from .models import ApartmentModel
# from .serializer import AparmentSerializer
# from .permissions import IsOwnerOrReadOnly


# class ApartmentViewSet(ViewSet):
#     model_query = ApartmentModel.objects.all()
 
#     def get_object(self, pk):
#         return get_object_or_404(self.model_query, pk=pk)
        

#     def retrieve(self, request, pk=None):
#         apartment = self.get_object(pk)
#         serializer = AparmentSerializer(apartment)
#         return Response(serializer.data)
    
#     def list(self, request):
#         serializer = AparmentSerializer(self.model_query, many=True)
#         return Response(serializer.data)
    
    

# class MyRentsView(ViewSet):

#     model_query = ApartmentModel.objects.all()
#     permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

#     def get_object(self, pk):
#         return get_object_or_404(self.model_query, pk=pk)
        
    
#     def list(self, request):
#         serializer = AparmentSerializer(self.model_query, many=True)
#         return Response(serializer.data)
    
#     def retrieve(self, request, pk=None):
#         my_rent = self.get_object(pk=pk)
#         serializer = AparmentSerializer(my_rent)
#         return Response(serializer.data)
    
#     def create(self, request):
#         serializer = AparmentSerializer(self.model_query, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(status=status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)
       
#     def destroy(self, request, pk=None):
#         my_rent = self.get_object(pk)
#         my_rent.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)