from django.http import HttpResponse
from django.views import View

from BoKe.forms import CommentForms


class AddCommentView(View):

    def post(self,request):
        Takes_form = CommentForms(request.POST)
        if Takes_form.is_valid():
            Takes_form.save()
            return HttpResponse('{"status":"success"}',content_type='application.json')
        else:
            return HttpResponse('{"status":"fail"}',content_type='application.json')
