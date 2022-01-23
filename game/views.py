from django.http import HttpResponse

def index(request):
    line1 = '<h1 style="text-align: center">The Battle Of Warlock</h1>'
    line3 = '<hr>'
    line4 = '<a href="/play/">Enter Game</a>'
    line2 = '<img src="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fimg.3dmgame.com%2Fuploads%2Fimages%2Fnews%2F20210331%2F1617177020_121756.jpg&refer=http%3A%2F%2Fimg.3dmgame.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1645492360&t=61bfcf728572a6b003d66b0722f0956d" width=1500>'
    return HttpResponse(line1 + line4 + line3 + line2)

def play(request):

    line1 = '<h1 style="text-align: center">The Battle Of Warlock</h1>'
    line3 = '<hr>'
    line4 = '<a href="/">Return</a>'
    line2 = '<img src="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fi0.hdslb.com%2Fbfs%2Farticle%2Ff10db09530539b311c7284a6b11f25c9c61da383.jpg&refer=http%3A%2F%2Fi0.hdslb.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1645493339&t=962c05db6276d109138e9799ae6f40cb" width=1500>'
    return HttpResponse(line1 + line4 + line3 + line2)

