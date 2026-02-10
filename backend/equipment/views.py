from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from .serializers import CSVUploadSerializer
import pandas as pd
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

class UploadCSV(GenericAPIView):
    permission_classes = [AllowAny]

    parser_classes = [MultiPartParser, FormParser]
    serializer_class = CSVUploadSerializer

    def get(self, request):
        return Response({"message": "Upload endpoint ready. Use POST."})

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        file = serializer.validated_data["file"]
        df = pd.read_csv(file)

        summary = {
             "total": len(df),
             "avg_flowrate": df["Flowrate"].mean(),
             "avg_pressure": df["Pressure"].mean(),
             "avg_temperature": df["Temperature"].mean(),
             "type_distribution": df["Type"].value_counts().to_dict()
          }

        return Response(summary)


        
from reportlab.pdfgen import canvas
from django.http import FileResponse
import io

class PDFReportView(GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        buffer = io.BytesIO()
        p = canvas.Canvas(buffer)

        p.drawString(100, 800, "Equipment Summary Report")
        p.drawString(100, 760, "PDF working!")

        p.showPage()
        p.save()

        buffer.seek(0)
        return FileResponse(buffer, as_attachment=True, filename="report.pdf")
