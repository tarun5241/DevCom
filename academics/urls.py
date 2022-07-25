"""project1 URL Configuration

    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from . import views

urlpatterns = [ 
    path('', views.academics , name="academics" ),
    path('student/<str:pk>/', views.student , name="student" ),
    path('add-student/', views.addStudent, name='add-student'),
    path('add-marks/', views.addMarks, name='add-marks'),

]
