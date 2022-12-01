from django.urls import path
from course import views
urlpatterns = [
    path('django/',views.learn_django),
    path('python/',views.learn_python),
    path('frontend/',views.learn_frontend),
    path('math/',views.learn_math),
    path('greet/',views.greet),
]
