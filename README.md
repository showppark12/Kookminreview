# **Kookminreview**
국민대 멋쟁이사자처럼 2회 미니 아이디어톤 프로젝트
</br>  
</br>

## **소개**  
### 1. 서비스 이름
    kmu hidden area : 국민대 대학가 리뷰 사이트

### 2. 예상 서비스 사용자
    국민대 재학생

### 3. 서비스 구상 동기
> 코로나19로 화상 강의를 듣는 신입생 및 지하세계 정보가 부족한 모든 국민대 재학생을 위한 서비스를 고민하다 리뷰 사이트를 구상하게 되었습니다.

### 4. 서비스 목표
    국민대 주변 상권 활성화

### 5. 서비스 소개
> 해당 대학의 재학생들을 대상으로 대학가 근처에 스터디공간, 식사공간, 휴식공간을 여러 사람들의 생생한 리뷰를 통해 추천해주는 사이트.

</br>

- - -

## **페이지 구성** ##
</br>

### **메인화면**
1. 서비스 및 카테고리 소개
2. 카테고리별 베스트 리뷰 및 오늘의 추천 장소 소개

</br>

### **스터디공간/휴식공간/식사공간 : 카테고리별 게시글**
1. 리스트뷰
   * 여러 게시글의 제목, 작성시간, 내용 확인
   * 클릭 시 해당 게시글의 디테일뷰로 이동
2. 디테일뷰
   * 작성자와 현재 로그인한 사용자 정보가 일치할 경우 게시글 수정 및 삭제 가능.
   * 로그인한 경우, 게시글에 덧글 작성, 삭제 가능
   * 로그인한 경우, 게시글 스크랩 및 스크랩 취소 가능 (추후 스크랩한 글 페이지에서 확인)  

</br>

### **스크랩한 글** ###
카테고리별 해당 사용자가 스크랩한 글 확인

</br>

### **로그인 / 회원가입 페이지** ###
로그인, 로그아웃, 회원가입 기능


- - -
## **프로젝트 구조** ##

</br>

### **전체 구조** ###
1. main: 앱 - 메인화면 및 계정 관련(로그인/회원가입/스크랩)
2. beerboard/foodboard/restboard/studyboard: 앱 - 카테고리별로 앱을 작성하여 관리, 해당 카테고리의 게시글, 덧글 및 CRUD 관련
3. reviewproject: 프로젝트 - 상속받을 템플릿 제공

</br>

### **모델 구조** ###
카테고리별로 앱 및 모델을 작성하였으며 아래는 휴식공간의 예시입니다.

1. 게시글 모델
   ``` python
    class RestBoard(models.Model):
        title = models.CharField(max_length = 200)
        writer = models.ForeignKey(User, on_delete=models.CASCADE)
        pub_date = models.DateTimeField()
        img = models.ImageField(upload_to='beerboard/', blank=True, null=True)
        text = models.TextField()
        rscrap_users = models.ManyToManyField(User, related_name="rscraps")

        def __str__(self):
            return self.title

    ```
    게시글 모델 - 필드 : 제목, 작성자, 작성일(최종수정일), 사진, 내용, 스크랩한 유저  
    - - -
2. 덧글 모델
    ``` python
    class RestBoardComment(models.Model):
        writer = models.ForeignKey(User, on_delete = models.CASCADE)
        board = models.ForeignKey(RestBoard, on_delete = models.CASCADE, related_name="comments")
        text = models.TextField()
        pub_date = models.DateTimeField()
    ```
    덧글 모델 - 필드 : 작성자, (덧글이 작성될) 게시글, 내용, 작성일(최종수정일)