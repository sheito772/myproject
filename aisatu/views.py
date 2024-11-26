from django.shortcuts import render
from django.views.generic import TemplateView # <-追加する

#---------------------------------------------------------------
#htmlページに表示内容をクラスで作成する。
#---------------------------------------------------------------
class IndexView(TemplateView):
	template_name = "greeting.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		opinion = [
			"ええかげんにせ、やってまるや。(青森)",
			"いいかげんにしろ、かっぱじくぞ。(千葉)",
			"いいかげんにしろでこの、ぶっちめっつぉ。(福島)",
			"たいぎゃにしとかんかこら、うちころすぞぬしゃ。(熊本)",
			"えーかげんにさらせ、いてこますぞわれ。(関西)",
			
        ]
		context["opinion"] = opinion
		return context
