from django.shortcuts import render
from .excel_handler import UploadExcel


def main_page(request):
    if request.POST:
        # print(request.POST)
        # print(request.FILES)
        file = request.FILES['excel_file']
        upload_excel = UploadExcel(file)
    return render(request, 'mainapp/index.html')