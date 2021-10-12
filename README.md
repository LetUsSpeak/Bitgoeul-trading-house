# ⚡ 빛고을상회 ⚡
### 👛 온라인 플리마켓 플랫폼 👜

![main](https://user-images.githubusercontent.com/64680512/137018517-5a3cc061-7ae9-4228-b71f-006ef4f26adf.png)

<br>

- ### 🔍프로젝트 동기🔍
    - COVID-19로 인하여 현대 사회에서 발생하는 문제 탐색
    - 지역 사회 전반에서 필요한 서비스를 찾는 것을 목적으로 프로젝트 구상

<br>

- ### 🎇프로젝트 필요성🎇
    - 대면이 어려운 현재 상황 ⏩ 지역 공동체가 함께 할 수 있는 "비대면 문화 공간"이 필요
    - 지역 공동체 커뮤니티 공간 개설의 필요 ⏩ 지역 특화 산업에 활용
    - 지역 사회 활성화를 돕고, 소상 공인들이 겪는 시공간적 제약을 해소 ⏩ 플리마켓을 통해 구현

<br>

- ### ❗프로젝트 소개❗
 
    - '빛고을상회'는 ❌시공간적인 제약❌ 없이 온라인에서 장터를 열어 상품을 거래 👛
    - 고객 맞춤 AI서비스를 함께 제공 하는 온라인 플리마켓 플랫폼 🤖📊📈
 
 
    - 거래 과정 속 현장감과 유대감 조성에 도움이 될 수 있는 🥽메타버스 공간🥽을 조성하여 체험 가능
    
    <br>

        💡유사 서비스와의 차별성💡
        - 다양한 지역별, 분야별 장터와 상품을 플랫폼에서 통합적으로 관리/운영 📝
        - AI개념을 활용하여, 분산되어있던 고객 맞춤 기능을 확대한 플리마켓 서비스를 제공 🔍


<br>

<h3>🧡 주요 서비스</h3>
<details>
<summary>🔍AI 고객 맞춤 추천 서비스🔍</summary>
<div markdown="1">       
<br>

## 카테고리 판별/분류 기능🔡🔠
- 입력한 상품이 속한 카테고리(주제)를 판별하고 추천
    <br>

    1. 아이디어스 사이트에서 카테고리 분류를 위한 데이터 크롤링
    2. label 축약 및 데이터 전처리
    3. 형태소 분석기를 통해 데이터를 형태소 단위로 분할
    4. Tokenizer을 이용하여 단어들을 시퀀스 형태로 변환
    
    <br>

    - Sequential 모델, Embedding, LSTM, Dense 레이어 사용
    - Loss는 categorical_crossentropy , optimizer는 adam, metrics는 acc 사용
    <br>
    <br>
---

## 유사 상품 추천 기능💌
- 입력한 상품과 유사한 상품을 추천/비교
<br>

- 사용모델: Doc2Vec
    - tagged_data를 학습하여 각 문장 별로 임베딩 벡터를 구하고,
    구해진 벡터를 통해 예측 과정에서 입력된 값과 유사한 단어 추천
    - 문장을 구성하는 단어 벡터와 
문서 자체의 벡터를 구해 유사도를 비교
<br>

- 주요 라이브러리: py-hanspell
    - 네이버 맞춤법 검사기를 이용한 
    파이썬용 한글 맞춤법 검사 라이브러리

    - 크롤링된 원형 데이터에서 맞춤법, 띄어쓰기를 교정한 후 토크나이징하여 학습 결과물의 정확도 향상
  <br>
  <br>
---
 

## ⭕리뷰 긍정/부정 감정 분석 기능❌

- 작성된 리뷰를 바탕으로 내용에서 긍정/부정 여부에 따라 감정 판별하여 상품 만족도 파악에 도움
    <br>

    1. 평점이 3점보다 크면 1(긍정리뷰), 작으면 0 (부정리뷰)
    2. Null값 확인, 정규 표현식을 통한 데이터 전처리
    3. 형태소분석기(okt)를 통해 데이터를 형태소 단위로 분할
    4. Tokenizer을 이용하여 단어들을 시퀀스 형태로 변환
    
    <br>

    - Sequential 모델, Embedding, LSTM, Dense 레이어 사용
    - Loss는 binary_crossentropy, optimizer는 rmsprop, metrics는 acc사용

</div>
</details>

<details>
<summary>🎡메타버스 온라인 플리마켓🎡</summary>
<div markdown="2">
<br>
    
![meta2](https://user-images.githubusercontent.com/64680512/137016979-9f1bc6e7-8244-4038-9d05-7f9d61d94de6.png)
    
- 장터 등록 /상품 판매를 위해 필요한 필수 기능 구축
- ZEPETO Build-it을 통해 가상의 장터 공간 구축
- 메타버스 가상공간에 플리마켓 환경이 실제로 구축되어 있어서 현실감과 유대감을 조성

</div>
</details>

<details>
<summary>🤖지역 챗봇 알림 서비스🤖</summary>
<div markdown="3">
<br> 
    
<img src="https://user-images.githubusercontent.com/64680512/137017604-6498eb5b-24ee-42c0-9a96-5b3b94b903ba.png" width="400"/>
    
<br>

- 이용자가 등록한 지역 정보, 관심 카테고리 등으로 원하는 장터/상품에 대한 소식을 챗봇을 통해 확인

</div>
</details>

<br>


<h3>💛 첨부 자료</h3>

- **유튜브(시연 영상) :** https://www.youtube.com/watch?v=fsj70WkJ4yI
- **구글 드라이브(모델 생성) :** https://drive.google.com/drive/folders/1Hynxwdq9hT8a-PnZGbZeiA2TbM63sGoY?usp=sharing
