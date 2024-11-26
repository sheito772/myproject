from django.shortcuts import render
from django.http import JsonResponse

def change_text(request):
    if request.is_ajax():
        story = [
            "かつて、遥か彼方の宇宙に、ひとつの美しい星がありました。",
            "そこには、様々な生命が共存し、平和な時代が続いていました。",
            "しかし、ある日、暗黒の力が星を覆い始めました。",
            "暗黒の力は、星の生命たちを次々と闇へと変えていきました。",
            "星の生命たちが絶望する中、一筋の光が現れました。",
            "それは、星の守護神が遣わしたとされる、勇者の光でした。",
            "勇者は、星を救うため、一人で暗黒の力に立ち向かう決意をしました。",
            "長い戦いが続き、勇者は何度も傷つきながらも、決して諦めませんでした。",
            "そしてついに、勇者は暗黒の力を封じ、星に平和を取り戻しました。",
            "それ以降、星の生命たちは勇者を祝福し、平和な時代が再び訪れました。"
        ]
        new_image_url = "/static/images/new_image.jpg" if index == 5 else "/static/images/default_image.jpg"
        return JsonResponse({'story': story, 'new_image_url': new_image_url})

def index(request):
    return render(request, 'index.html')
