from django.urls import path
from .views import UploadCSV
from .views import PDFReportView

urlpatterns = [
    path('upload/', UploadCSV.as_view()),
    path('report/', PDFReportView.as_view()),

]
