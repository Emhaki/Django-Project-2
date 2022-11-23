# 커뮤니티 모닥불
![001](https://user-images.githubusercontent.com/105331868/203469869-e3cb6f72-4968-4798-8843-dd1d3e836da0.png)

배포 주소: http://kdt6team-env.eba-rmvmzut2.ap-northeast-2.elasticbeanstalk.com/

# 목차

[1. 프로젝트 소개 🌲](#프로젝트-소개)

[2.[서비스 소개]](#서비스-소개)

[3. [주요 기능]](#주요-기능)

[4. [기여한 부분]](#기여한-부분)

[5. [프로젝트 후기]](#프로젝트-후기)

[6. [KPT]](#KPT)

<br>

## 1. 프로젝트 소개 🌲

### 1-1. 프로젝트 일정

<br>

| 날짜 | 내용 |
| --- | --- |
| 11.9 (수) ~ 11.21 (월) | 프로젝트 개발 |
| 11.22 (화) | 프로젝트 발표 |

### 1-2. 프로젝트 주제

<br>

<aside>
콘텐츠 정보 제공 및 후기 공유 커뮤니티 서비스를 개발합니다.
아래 네 개의 주제 중 하나의 주제를 선택해서 프로젝트를 진행합니다.

</aside>

| 주제 | 예시 |
| --- | --- |
| 여행지 정보 및 후기 공유 커뮤니티 서비스 | 인스타그램 |
| 맛집 정보 및 후기 공유 커뮤니티 서비스 | 망고플레이트 |
| 영화 정보 및 후기 공유 커뮤니티 서비스 | 키노라이츠 |
| 상품 정보 및 후기 공유 커뮤니티 서비스 | 오늘의집 |

## 2. 프로젝트 소개 🌲

<br>

![001](https://user-images.githubusercontent.com/105331868/203469869-e3cb6f72-4968-4798-8843-dd1d3e836da0.png)

> `커뮤니티 모닥불`은 크리스마스에 주변사람들에게 따뜻한 마음을 전하고, 마음이 맞는 사람들과 모임을 가질 수 있는 커뮤니티 서비스 입니다. 

<br>

## 3. 주요 기능 🌲

### 3-1. 메인 페이지

<br>

![Untitled (1)](https://user-images.githubusercontent.com/105331868/203472209-3ba784b2-6e3b-4515-ac60-ebc31c33ec28.png)

### 3-2. 벽난로 생성(개인)

<br>

![Untitled (4)](https://user-images.githubusercontent.com/105331868/203472736-833d1abd-ced6-42fa-807e-9470dea66b19.png)

> ⬆️카카오 API를 통해 소셜로그인 기능

![Untitled (5)](https://user-images.githubusercontent.com/105331868/203472953-a575231e-2798-49df-a21d-76d6c9e3388c.png)
![벽난로1-min](https://user-images.githubusercontent.com/105331868/203476224-acc95667-c0e9-4b18-bd1b-bb154b0b890f.gif)

> ⬆️로그인 후 개인벽난로를 생성해 다른 회원들이 메세지를 보낼 수 있음(다른 회원이 벽난로에 글을 작성하면 카카오톡 알림)

### 3-3. 벽난로 생성(그룹)

![벽난로2-min](https://user-images.githubusercontent.com/105331868/203485701-df12a6cf-1ba8-4e61-b0c4-b6d20fb33c60.gif)

> ⬆️ 그룹벽난로를 생성시 글이 많이 달린 순으로 메인페이지에 출력. 그룹 벽난로는 검색으로 찾기 쉽게 구현

### 3-4. 모임

<br>

![모임-min](https://user-images.githubusercontent.com/105331868/203486287-c84bf7b0-4481-4448-9ffc-bab34e059ff6.gif)
![모임2](https://user-images.githubusercontent.com/105331868/203486553-64b57c6b-5819-466d-8c19-d226423a8c92.gif)

> ⬆️ 메인페이지에서 지역을 선택해 모임생성 가능, 비밀번호 설정시 content가 안보이고, 비밀번호 불일치시 입장 불가

### 3-5. 모임 디테일

<br>

![모임디테일](https://user-images.githubusercontent.com/105331868/203491834-badc56fc-6946-485b-a90c-a239d787dca7.gif)

> ⬆️ 모임에 들어가서 참여버튼을 클릭과 댓글 작성 가능 `참여버튼 클릭시 다음에 입장할때 비밀번호 입력 없이 입장 가능`

### 3-6. 모임 차단

<br>

![차단-min](https://user-images.githubusercontent.com/105331868/203491982-1bf190b2-c348-42d1-8c62-d0f771489487.gif)

> ⬆️ 불쾌한 유저를 `차단시 그 유저가 생성했던 모임들을 필터링`

### 3-7. 쪽지

<br>

![쪽지-min](https://user-images.githubusercontent.com/105331868/203493131-00c5e22f-a3a2-4db2-ba42-1163d035dc8d.gif)

> ⬆️ 비밀번호 방 입장을 위해 유저에게 쪽지를 보낼 수 있음. 편지함에 보낸 편지함, 받은 편지함으로 구성, `보낸사람 입장에서 상대방이 읽었는지 안읽었는지 확인` 가능

### 3-8. 쇼핑

<br>

![쇼핑-min](https://user-images.githubusercontent.com/105331868/203492111-1896d457-21b7-4d1c-a211-97a1e800def8.gif)

> ⬆️ 네이버 API를 통해 `가격순, 날짜순, 정확도순으로 검색` 가능

## 4. 기여한 부분 🌲
![013](https://user-images.githubusercontent.com/105331868/203493562-8aea3649-09c7-4d77-aea5-0c2b5c71bb42.png)
![014](https://user-images.githubusercontent.com/105331868/203493611-bb254168-b106-45b6-a2be-807de8f068f5.png)
![015](https://user-images.githubusercontent.com/105331868/203493628-d007e8ec-9e39-4805-8f6c-b647b06d1bf5.png)
![016](https://user-images.githubusercontent.com/105331868/203493640-1bbf3efa-57c4-408c-85df-acf933e93677.png)
![017](https://user-images.githubusercontent.com/105331868/203493660-e4f54d83-9e09-477b-861f-1d513049e6c6.png)
![018](https://user-images.githubusercontent.com/105331868/203493671-ae2f8b04-f284-45d7-8fa0-3e62376e6c21.png)
![019](https://user-images.githubusercontent.com/105331868/203493721-6d20273a-f178-4336-bd96-e7a73a47e2bd.png)

> 프로젝트 시작 전 팀원들과 프로젝트 기획, 각 기능들의 모델설계

> 기능별로는 모임부분과 쪽지 부분의 HTML, CSS, django views를 담당.

> views의 복잡한 기능들은 팀원들과 함께 고민하고 작업

## 5. 프로젝트 후기 🌲

- 여러가지 기능들을 앱별로 분류해본 경험이 처음이었다. 잘하는 팀원들과 만나서 공동작업을 하면서 자극을 많이 받았고, 팀원들에게 도움이 되고 싶다는 생각이 많이 들었다. 팀원들마다 실력과 코드 작성 실력이 달랐다. 나와 같은 경우 코드 작성 속도가 느리다는 생각이 들었고, 팀원들에게 민폐가 되지 않으려면 앞으로도 공부를 열심히 해야겠다는 생각이 들었다.

- 한 HTML에서 많은 기능들을 렌더링하려고 하다보니 다양한 변수들에 부딪혔다. django HTML에서 For문을 통해 반복출력을 할때 서버단에서 컨트롤을 잘 해줘야한다는 것을 깨달았고, 각 모임의 비밀번호 입력을 위해 모달을 설정할 때 id값을 일치시키는 방법에도 애를 먹었었다. 

- 모임페이지에서 지역별로 검색이 가능한데, 지역별로 검색한 내용을 서버단으로 전송할 때 클린 코드를 구현하려고 노력했다. 또한, 페이지네이션 기능을 구현할때 HTML에서 넘어오는 a-link의 값을 views.py에서 strip()을 통해 컨트롤 해주는 경험을 했다.

- DB에서 데이터를 출력할 때, DB에서 필터링을 상세하게 해줘야 함을 깨달았다. 광범위하게 필터링할 경우 렌더링에도 시간이 걸리고, 서버에도 부담이 된다는 것을 깨달았다.

### Meeting HTML 클린코드
```html 
<div class="d-flex align-items-center">
    <form action="{% url 'meetings:index'%}" method="POST" class="m-1">
      {% csrf_token %}
      <button id="custom-btn" name="reset" value="reset" style="background-color:transparent;">
        모두보기
      </button>
    </form>
    {% for local in meetings_local_list %}
    <span class="mx-1">|
      <a href="?local={{local}}" class="mx-1 custom-link" style="text-decoration:none">
      {{ local }}
      </a>
    </span>
    {% endfor %}
  </div>
  ```
  ### Meeting Python 클린코드
  ```py
  @login_required
def index(request):
    meetings = Meeting.objects.order_by("-pk")
    # 사용자가 블락안한 모임
    block = Meeting.objects.exclude(user__in=request.user.blocking.all()).order_by("-pk")
    # 사용자가 블락한 모임
    non_block = Meeting.objects.filter(user__in=request.user.blocking.all()).order_by("-pk")
    img = [
        "https://images.unsplash.com/photo-1615097130643-12caeab3c625?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80",
        "https://images.unsplash.com/photo-1577042939454-8b29d442b402?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=774&q=80",
        "https://images.unsplash.com/photo-1638277267253-543e4c57cd7f?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80",
        "https://images.unsplash.com/photo-1543258103-a62bdc069871?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MjR8fGNocmlzdG1hc3xlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60",
        "https://images.unsplash.com/photo-1575549593677-012f18048ea1?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MzV8fGNocmlzdG1hc3xlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60",
        "https://images.unsplash.com/photo-1602678460152-719a9af1fb6c?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NDV8fGNocmlzdG1hc3xlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60",
        "https://images.unsplash.com/photo-1512474932049-78ac69ede12c?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NTh8fGNocmlzdG1hc3xlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60",
        "https://images.unsplash.com/photo-1511970093628-4e9f59378b4d?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NTZ8fGNocmlzdG1hc3xlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60",
        "https://images.unsplash.com/photo-1482330454287-3cf6611d0bc9?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NjN8fGNocmlzdG1hc3xlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60",
        "https://images.unsplash.com/photo-1545608444-f045a6db6133?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NjV8fGNocmlzdG1hc3xlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60",
    ]
    random.shuffle(img)
    # 총 모임 - 블락한 모임
    meetings_count = len(meetings) - len(non_block)

    # 지역별
    meetings_local_name = "모든지역"
    meetings_local_list = ["강남", "건대" ,"노원", "대학로", "부평", "신촌", "수원", "일산", "종로", "잠실", "홍대", "하남"]

    at_all = "모두보기"
    paginator = Paginator(block, 8)
    page_number = request.GET.get("local")
    page_obj = paginator.get_page(page_number)
    if request.POST.get("reset"):
        return redirect("meetings:index")
    if request.GET.get("local"):
        name = re.sub(r"[0-9]", "", request.GET.get("local"))
        block = (
            Meeting.objects.filter(location__contains=name)
            .exclude(user__in=request.user.blocking.all())
            .order_by("-pk")
        )
        if not name:
            meetings_local_name = "모든지역"
        else:
            meetings_local_name = name
        # 페이지네이션
        paginator = Paginator(block, 8)
        page_number = re.sub(r"[^0-9]", "", request.GET.get("local"))  # key 값이 local, value 값이 노원구
        page_obj = paginator.get_page(page_number)  # 숫자만 받음
        context = {
            "nw": name,
            "img": img,
            "page_obj": page_obj,
            "meetings_local_name": meetings_local_name,
            "meetings_count": len(block),
            "meetings_local_list": meetings_local_list,
        }
        return render(request, "meetings/index.html", context)
    else:

        context = {
            "at_all": at_all,
            "img": img,
            "page_obj": page_obj,
            "meetings_local_name": meetings_local_name,
            "meetings_count": meetings_count,
            "meetings_local_list": meetings_local_list,
        }
        return render(request, "meetings/index.html", context)
  ```

## 6. KPT 🌲

### KPT란?

- **Keep / Problem / Try**의 약자로 프로젝트 진행 과정을 돌아보고
1. 앞으로도 유지했으면 하는 좋은 점(Keep)
2. 고쳐졌으면 하는 문제점이나 아쉬운 점(Problem)
3. 문제점을 해결하기 위해 시도해볼 수 있는 해결책(Try)
에 대해 논의해보는 방법론입니다.

### Keep

<aside>
🎉 프로젝트를 진행하며 만족스러웠던, 성취감을 느꼈던 부분을 작성해주세요.

다른 프로젝트를 진행하면서도 유지하면 좋을 것이라 생각되는 접근 방식 / 업무 수행 방식 / 태도 등을 작성해주세요.

</aside>

- 처음에 아이스브레이킹 주도해준 경욱님 고마워요~
- 서로 편하게 의견 나누고, 각자 원하는 것도 말한 것 같아서 즐겁게 시간을 보낼 수 있었다.
- 생각했던 기능들을 팀원들의 도움으로 구현할 수 있어서 좋았다.
- 내가 생각했던 기능을 구현해서 좋았고 팀원들과 문제에대해서 의논하고 해결하려고 했던 과정들이 소중했다.
- 내가 몰랐던 기능들을 많이 알게 되서 좋았고, 서로 알게 된 것에 대해 공유해 주는게 너무 좋았다.

### Problem

<aside>
🤔 프로젝트를 진행하며 마주한 문제점이나 아쉬운 점을 작성해주세요.

</aside>

- 개인적으로 실력이 부족해서 다른 팀원들의 도움이 필요했고, 그래서 팀원분들의 몰입을 방해해서 미안하다.
- 한 페이지에 많은 내용을 담으려다보니 다양한 변수에 부딪혔는데, 해결방법이 쉽게 떠오르지 않았다.  고민하는 시간이 길어서 내 개인적으로 생산성이 떨어졌던 것 같아 아쉬웠다.
- 생각했던 기능을 다 구현하지 못해서 아쉬웠지만 선택과 집중의 중요성을 알수있었다
- 간단하게 생각했던 문제들이 생각보다 시간을 먹고 어려운 게 많아서 효율적으로 하는 방법을 생각해 봐야겠다.
- 영어의 한계..

### Try

<aside>
🛠️ 앞서 정의한 Problem을 해결하기 위한 시도가 있었다면 작성해주세요.
만약 별도 시도가 없었다면, 어떠한 시도를 하면 좋을지 작성해주세요.

</aside>

- 처음으로 돌아가서 공부를 다시 꼼꼼히하고 싶지만, 현실적으로 불가능하기 때문에, 시간을 갈아넣고, 좀 더 몰입을 해야겠다.
- 코드가 어떻게 동작하는 지에 대한 깊이 있는 이해도가 부족했던 것 같다. 시간을 더 투자해서 지식을 늘려가야 될 것 같다.
- 코드리뷰를 하면서 어떻게 해야 구현이 될지 고민했던것 같다
- 검색을 통해 얻을 수 있는 것도 있지만 팀원들과 재밌게 이야기하면서 해결해면 재밌을 거 같다.
- 최대한 머리 박으면서 영어 돌파..!

### Others

<aside>
😘 선택 프로젝트 II를 진행하며 남기고 싶은 말씀이 있으시다면 자유롭게 작성해주세요!

</aside>

- 다들 각자 자리에서 너무 열심히 해줘서 고맙습니다 😃
- 많이 부족했는데 다들 내색하지 않고 잘 받아줘서 너무 고맙습니다.
- 덕분에 많이 배웠습니다 고마워요~ 😘
- 좋은 경험을 만들수 있어서 감사했습니다. 마지막 프로젝트까지 화이팅합시다 ^^
- 마음가짐의 중요성을 깨닫게 해줘서 고마웠습니다.
