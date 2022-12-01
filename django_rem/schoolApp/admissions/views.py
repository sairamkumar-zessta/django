
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.conf import settings 
from django.db.models.signals import post_save
from django.dispatch import receiver 


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


# class CustomAuthToken(ObtainAuthToken):
#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class( data = request.data, context = {'request' : request})
#         serializer.is_valid(raise_exception = True)
#         user = serializer.validated_data['user']
#         token , created = Token.objects.get_or_create(user = user)
#         print( Token.objects.get_or_create(user = user) )
#         return Response({
#             'token' : token.key,
#             'user_id':user.pk,
#             'email' :user.email
#         })
# Create your views here.
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer 
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated] 

