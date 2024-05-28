from django.shortcuts import render

# Create your views here.
def main(request):
    blog_list = ["Lasha says: სერგო გაუმარჯოს, როგორ ხარ, რა ხდება შენსეკენ?",
                 "Sergo answers: გამარჯობა ლაშა, კარგათ, შენ? რავი არაფერი საზღვარგარეთ გავედი 3 დღით ჯერ და დრო თუ მექნება დავიწყებ დავალების წერას",
                 "Lasha answers: არამიშავს მეც კარგად ვარ, კი ბატონო, რასაც მოახერხებ ის გააკეთე და თუ რამეა ხო იცი აქ ვარ"
                 ] 
    return render(request, 'blog.html', {'data': blog_list})