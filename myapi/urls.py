from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from myapi.views import EmployeeListCreateAPIView, EmployeeRetrieveUpdateDestroyAPIView, registration_view
from myapi.views import EmployeeListCreateAPIView, EmployeeRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/employees/', EmployeeListCreateAPIView.as_view(), name='employee-list-create'),
    path('api/employees/<int:pk>/', EmployeeRetrieveUpdateDestroyAPIView.as_view(), name='employee-retrieve-update-destroy'),
    path('api/register/', registration_view, name='register'),
    path('api/employees/<int:pk>/', EmployeeRetrieveUpdateDestroyAPIView.as_view(), name='employee-retrieve-update-destroy'),
    #path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
]
