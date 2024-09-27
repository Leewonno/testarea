from barcode import Code39
from barcode.writer import ImageWriter, Image
from django.http import HttpResponse


def barcode(request):
    part_number = '102050001'
    ean = Code39(part_number, add_checksum=False)
    ean.save('code39_barcode')

    return HttpResponse(ean)
