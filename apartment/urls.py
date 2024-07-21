from django.urls import path
from .views import MyRentCreate, MyRentList, MyRentDelete, MyRentRetrieve, ApartMentList, ApartMentRetrieve

urlpatterns = [
    path('rent_create/', MyRentCreate.as_view()),
    path('rent_list/', MyRentList.as_view()),
    path('rent_retrieve/<int:pk>/', MyRentRetrieve.as_view()),
    path('rent_delete/<int:pk>/', MyRentDelete.as_view()),
    path('apartment_list/', ApartMentList.as_view()),
    path('apartment/<int:id>/', ApartMentList.as_view())
]



# urlpatterns = [
#     path('rent_list/', MyRentsView.as_view({'get': 'list'})),
#     path('rent_delete/<int:id>/', MyRentsView.as_view({'delete': 'destroy'})),
#     path('rent_create/', MyRentsView.as_view({'post': 'create'})),
#     path('rent_retrieve/<int:id>/', MyRentsView.as_view({'post': 'create'})),

#     path('apartment_list/', ApartmentViewSet.as_view({'get': 'list'})),
#     path('apartment_retrieve/<int:id>/', ApartmentViewSet.as_view({'get': 'retrieve'}))
# ]