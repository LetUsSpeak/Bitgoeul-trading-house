from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView

from reviewapp.forms import ReviewCreationForm
from reviewapp.models import Review


class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewCreationForm
    template_name = 'reviewapp/create.html'
    # def form_valid(self, form):
    #     self.object = form.save(commit=False)
    #     output = pos_result(self.object.content)
    #     self.object.sentiment = output
    #     self.object.save()
    #     return super().form_valid(form)
    #     # form.instance.sentiment = pos_result(form.instance.content)
    #     # if form.instance.sentiment == 1:
    #     #     self.output = 1
    #     # else:
    #     #     self.output = 0
    #     # return super().form_valid(form)
    #
    # def get_success_url(self):
    #     return reverse('productapp:result', {'output': self.output})

from django.shortcuts import render

from konlpy.tag import Okt
from keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import csv

okt = Okt()
model = load_model('models/review_model.h5')

vocab_size = 42019
X_train = []
path = 'data/review_train.csv'
with open(path, 'r', encoding='UTF8') as f:
    reader = csv.reader(f)
    for idx, list in enumerate(reader):
        X_train.append(list)

max_len = 50
tokenizer = Tokenizer(vocab_size, oov_token='OOV')
tokenizer.fit_on_texts(X_train)
X_train = tokenizer.texts_to_sequences(X_train)
X_train = pad_sequences(X_train, maxlen=max_len)
# X_test = tokenizer.texts_to_sequences(X_test)

stopwords = ['도', '는', '다', '의', '가', '이', '은', '한', '에', '하', '고', '을', '를', '인', '듯', '과', '와', '네', '들', '듯', '지', '임', '게']


def pos_result(full):
    full = okt.morphs(full)
    full = [word for word in full if not word in stopwords]
    encoded = tokenizer.texts_to_sequences([full])
    # error !!!!
    pad_new = pad_sequences(encoded, maxlen=80)
    score = float(model.predict(pad_new))
    if score > 0.5:
        output = 1
    else:
        output = 0

    return output