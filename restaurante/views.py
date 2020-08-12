from django.http import HttpResponse
from datetime import datetime
from django.views.generic import View
from django.template.loader import get_template

from .utils import render_to_pdf #created in step 4

class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
    	template = get_template('pdf/invoice.html')
    	html = template.render()
    	context = {
    		"invoice_id": 123,
    		"customer_name": "John Cooper",
    		'today': datetime.today(), 
            'amount': 39.99,
    	}
    	html = template.render(context)
    	pdf = render_to_pdf('pdf/invoice.html', context)
    	if pdf:
    		response = HttpResponse(pdf, content_type='application/pdf')
    		filename = "Invoice_%s.pdf" %("123456789")
    		content = "inline; filename=%s" %(filename)
    		download = request.GET.get("download")
    		if download:
    			content = "attachment; filename=%s"%(filename)
    		response ['Content-Disposition']= content	
    		return response
    	return HttpResponse("Not found")
    	