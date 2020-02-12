from django import forms
from lotto.models import GuessNumbers

class PostForm(forms.ModelForm):
# Form 을 통해 받아들여야할 데이터가 명시되어 있는 메타 데이터 (DB 테이블을 연결
    class Meta:
        model = GuessNumbers
        fields = ('name', 'text',) #
