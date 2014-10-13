from django import forms
from django.db.models import get_model
from django.contrib.auth.models import User
from sodclan.widgets import AdvancedEditor
from sodclan.models import Article
 
class ArticleModelAdminForm(forms.ModelForm):
	title = forms.CharField(max_length=50)
	author = forms.ModelChoiceField(queryset=User.objects.all())
	content = forms.CharField(widget=AdvancedEditor())
 
	class Meta:
		model = Article
