from supplements.models import Supplement
from django.views import View
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import LoginForm, SignUpForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import UserTotalIntake
from supplements.models import RecommendedIntake, RecommendedNutrient, Interaction
from django.contrib import messages

def index_view(request):
    # 로그인되어 있지 않은 사용자에 대해 로그인 페이지로 리디렉션
    if not request.user.is_authenticated:
        return redirect('login')
    supplements = Supplement.objects.filter(user=request.user)

    intake_percentages = {}
    #사용자의 총섭취량 데이터 가져오기
    userdosage = {u.nutrient.name: u.dosage for u in UserTotalIntake.objects.filter(user=request.user)}
    #사용자의 적정섭취량 데이터 가져오기
    recommended_intakes = {r.nutrient.name: r.dosage for r in RecommendedNutrient.objects.filter(recommended_intake=request.user.recommended)}
    limitnutrients = {qn.nutrient.name: qn.limit for qn in RecommendedNutrient.objects.filter(recommended_intake=request.user.recommended)}

    overintake = {}
    underintake = {}
    remainintake = {}

    for nutrient, dosage in userdosage.items():
        recommendeddosage = recommended_intakes.get(nutrient)
        limitdosage = limitnutrients.get(nutrient)
        if recommendeddosage:
            percentage = (dosage/ recommendeddosage) * 100
            if limitdosage and limitdosage < dosage :
                overintake[nutrient] = percentage
            elif percentage < 50 :
                underintake[nutrient] = percentage
            else:
                remainintake[nutrient] = percentage
        # 상호작용 객체를 담을 빈 리스트를 만듭니다.
    interactions = []

    # 영양제의 SupplementNutrient 객체들 중에서 용량이 0이 아닌 것만 선택합니다.
    user_nutrients_with_dosage = [usr_nut for usr_nut in UserTotalIntake.objects.filter(user=request.user) if usr_nut.dosage > 0]

    # 모든 상호작용 객체를 순회합니다.
    all_interactions = Interaction.objects.all()
    for interaction in all_interactions:
        # 상호작용의 두 성분이 모두 영양제에 포함되어 있고, 용량이 0이 아닌지 확인합니다.
        if interaction.nutrient1 in [usr_nut.nutrient for usr_nut in user_nutrients_with_dosage] and interaction.nutrient2 in [usr_nut.nutrient for usr_nut in user_nutrients_with_dosage]:
            # 두 성분이 모두 포함되어 있고 용량이 0이 아니라면 interactions 리스트에 추가합니다.
            interactions.append(interaction)


    return render(request, 'user/index.html', {
        'supplements': supplements,
        'overintake': overintake,
        'underintake': underintake,
        'remainintake': remainintake,
        'interactions': interactions
    })

class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'user/signup.html'
    success_url = reverse_lazy('user:login')  # 회원가입 성공 후 로그인 페이지로 이동

    def form_valid(self, form):
        # 모든 필드가 제대로 채워졌는지 검사
        if form.is_valid():  # 이 부분이 폼의 유효성을 확인합니다.
            user = form.save()
            # 여기에서 필요한 경우 로그인 처리 등 추가 작업을 수행할 수 있습니다.
            return super().form_valid(form)
        else:
            return self.form_invalid(form) 
    
        
def root_redirect(request):
    User = get_user_model()
    if request.user.is_authenticated:
        return redirect('user:index')
    else:
        return redirect('user:login')


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('user:index')  # 로그인 성공 시 이동할 URL
            else:
                # 로그인 실패 시 오류 메시지 추가
                messages.error(request, '로그인 실패: 아이디 또는 비밀번호가 잘못되었습니다.')
                form = LoginForm()  # 폼을 비워서 다시 표시
    else:
        form = LoginForm()
    return render(request, 'user/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('user:login')