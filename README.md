# 커뮤니티 모닥불
![001](https://user-images.githubusercontent.com/105331868/203469869-e3cb6f72-4968-4798-8843-dd1d3e836da0.png)

배포 주소: http://kdt6team-env.eba-rmvmzut2.ap-northeast-2.elasticbeanstalk.com/

# 목차

[1. 프로젝트 소개](#1프로젝트-소개)

[2. 서비스 소개](#2프로젝트-소개)

[3. 주요 기능](#3주요-기능)

[4. 기여한 부분](#4기여한-부분)

[5. 프로젝트 후기](#5프로젝트-후기)

[6. 팀원 후기](#팀원-후기)

<br>

## 1.프로젝트 소개

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

## 2.프로젝트 소개

<br>

![001](https://user-images.githubusercontent.com/105331868/203469869-e3cb6f72-4968-4798-8843-dd1d3e836da0.png)

> `커뮤니티 모닥불`은 크리스마스에 주변사람들에게 따뜻한 마음을 전하고, 마음이 맞는 사람들과 모임을 가질 수 있는 커뮤니티 서비스 입니다. 

<br>

## 3.주요 기능

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

## 4.기여한 부분
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

## 5.프로젝트 후기

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

## 6.팀원 후기

### 문경욱
<aside>
😍 실력이 뛰어난 팀원들을 만나 생각을 했던 것들을 실제로 구현하는 좋은 기회를 가질 수 있었습니다. 제가 부족한 것들을 팀원분들이 잘 채워줘서 프로젝트를 잘 마무리했습니다.
</aside>

### 이명학
<aside>
🐻‍❄️ 여러가지 기능들을 앱별로 분리해서 작업해보는 경험을 했다. 또한 인덱스 페이지에 여러가지 기능을 한꺼번에 넣다보니 여러가지 변수에 부딪혔습니다.

생각했던 기능들을 팀원들의 도움으로 다 구현해서 뿌듯했고, 실력있는 팀원들을 만나 많이 배웠습니다.
</aside>

### 이상백
<aside>
🐶 배울 점이 많은 팀원들과 같이 프로젝트를 했다는 것 자체가 너무 좋았고, 다들 재밌는 분위기에 열정적인 모습들을 보면서 이번 프로젝트 기간이 빠르게 지나간 것 같아서 좋았습니다.
</aside>

### 이용환
<aside>
🐻 프로젝트 기간 중 코로나에 걸려 제 역할을 다 하지 못한 것 같아 너무 아쉬웠습니다. 하지만 다른 팀원분들이 너무 너무 잘해주셔서 만족할만한 결과물이 나온 것 같아 너무 좋았습니다. 여태 접근하던 방식과 다르게 생각하던 것도 배웠으며 배울 점이 많은 팀원들을 만나서 너무 좋았습니다.
</aside>

### 이준엽
<aside>
🦔 이번 프로젝트를 통해서 좋은 팀원들과 함께할수 있어서 좋았고 어려움이 생겼을때 팀원들과 함께 문제를 해결하는 즐거움 또한 배울수 있었습니다. 프로젝트를 하면서 많이 배울 수 있었습니다.
</aside>
