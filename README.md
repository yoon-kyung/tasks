# TASK
----

## TASK 구현 개요
- DB는 AWS RDS MySQL 8.0을 이용 했습니다.
- 배포를 위한 클라우드 서버는 AWS EC2를 이용 했습니다.
- 과제 DB 스키마에는 들어가 있지 않았지만 "created_at", "updated_at", "deleted_at" 컬럼을 넣었습니다.
- DELETE 구현 시 논리적으로 삭제되어 사용자가 삭제를 하여도 DB상에는 남도록 구현했습니다. (실제 서비스라면 삭제된 글도 필요한 경우가 생길 수 있다고 생각했습니다.)
- GET 구현시(전체목록조회시) 완료된과제/완료되지 않은 과제 검색 기능을 추가했습니다.
----

## 사용방법
1. task.env에 다음 정보를 입력한다.
```
# DB
DB_USER_NAME=[DB 사용자 이름]
DB_PASSWORD=[DB 비밀번호]
DB_SERVER=[DB 서버주소]
DB_PORT=[DB 포트번호]
DB_DBNAME=[DB NAME]
```

2. 다음을 실행한다.
```
git clone https://github.com/yoon-kyung/tasks.git
cd ~/tasks
docker-compose up -d
```

----

## API 정의서
- Swagger URL: http://13.124.93.107:8000/docs

### 1. GET /task
Response Body
- 성공
```
[
  {
    "id": 3,
    "created_at": "2021-11-25T13:55:35",
    "updated_at": "2021-11-25T13:55:35",
    "deleted_at": null,
    "name": "백엔드 과제 만들기",
    "completed": false
  },
  {
    "id": 4,
    "created_at": "2021-11-25T13:55:39",
    "updated_at": "2021-11-25T13:55:39",
    "deleted_at": null,
    "name": "백엔드 과제 만들기",
    "completed": false
  }
]
```
- 데이터가 없는 경우 (STATUS CODE 404)
```
{
  "msg": "데이터가 없습니다."
}
```
- 완료된과제/완료되지 않은 과제 검색 시 (완료된 과제로 검색)
```
[
  {
    "id": 2,
    "created_at": "2021-11-25T20:44:55",
    "updated_at": "2021-11-25T20:44:55",
    "deleted_at": null,
    "name": "완료된 과제1",
    "completed": true
  },
  {
    "id": 3,
    "created_at": "2021-11-25T20:44:59",
    "updated_at": "2021-11-25T20:44:59",
    "deleted_at": null,
    "name": "완료된 과제2",
    "completed": true
  },
  {
    "id": 4,
    "created_at": "2021-11-25T20:45:04",
    "updated_at": "2021-11-25T20:45:04",
    "deleted_at": null,
    "name": "완료된 과제3",
    "completed": true
  }
```

### 2. GET /task/:task_id
Response Body
- 성공
```
{
  "id": 3,
  "created_at": "2021-11-25T13:55:35",
  "updated_at": "2021-11-25T13:55:35",
  "deleted_at": null,
  "name": "백엔드 과제 만들기",
  "completed": false
}
```
- 데이터가 없는 경우 (STATUS CODE 404)
```
{
  "msg": "데이터가 없습니다."
}
```

### 3. POST /task
Request Body
```
{
  "name": "백엔드 과제하기",
  "completed": false
}
```

Response Body
- 문제에서는 no response body지만 실제 서비스라면 추후 필요한 경우가 생길 수 있으니 작성한 내용을 Response Body로 지정했습니다.

- 성공
```
{
  "id": 1,
  "created_at": "2021-11-25T13:53:03.976369",
  "updated_at": "2021-11-25T13:53:03.976377",
  "deleted_at": null,
  "name": "백엔드 과제하기",
  "completed": false
}
```
- 실패
- name 필드는 빈값이면 안됩니다. (STATUS CODE 400)
```
{
  "msg": "name은 반드시 입력해야 합니다."
}
```
- completed의 데이터 타입은 boolean 입니다.
```
{
  "msg": "1 validation error for Request\nbody -> 38\n  Expecting value: line 3 column 16 (char 38) (type=value_error.jsondecode; msg=Expecting value; doc={\n  \"name\": \"완료된 과제3\",\n  \"completed\": 'haha'\n}; pos=38; lineno=3; colno=16)"
}
```

### 4. PATCH /task/:task_id
Request Body
```
{
  "name": "백엔드 과제 수정하기",
  "completed": true
}
```

Response Body
- 문제에서는 no response body지만 실제 서비스라면 추후 필요한 경우가 생길 수 있으니 수정한 내용을 Response Body로 지정했습니다.

- 성공
```
{
  "id": 1,
  "created_at": "2021-11-25T20:40:53",
  "updated_at": "2021-11-25T20:47:15.718270",
  "deleted_at": null,
  "name": "백엔드 과제 수정하기",
  "completed": true
}
```
- 실패 (STATUS CODE 400)
- name은 빈값이 되면 안됩니다.
```
{
  "msg": "name은 반드시 입력해야 합니다."
}
```
- completed의 데이터 타입은 boolean 입니다.
```
{
  "msg": "1 validation error for Request\nbody -> completed\n  value could not be parsed to a boolean (type=type_error.bool)"
}
```

### 5. DELETE /task/:task_id
Response Body
- 문제에서는 no response body지만 실제 서비스라면 추후 필요한 경우가 생길 수 있으니 삭제한 내용을 Response Body로 지정했습니다.
```
{
  "id": 1,
  "created_at": "2021-11-25T13:53:04",
  "updated_at": "2021-11-25T13:54:53.356743",
  "deleted_at": "2021-11-25T22:54:53.355970",
  "name": "백엔드 과제 만들기",
  "completed": true
}
```

### 6. DELETE /task
Response Body
- 문제에서는 no response body지만 실제 서비스라면 추후 필요한 경우가 생길 수 있으니 삭제한 게시글 수를 Response Body로 지정했습니다.
```
{
  "msg": "삭제된 게시글은 총 1개 입니다."
}
```

----

## 프로젝트 구조
```
/backends
    |— /apps
    |— /api
        |— get_api.py
        |— post_api.py
        |— patch_api.py
        |— delete_api.py
    |— /core
        |— consts.py
        |— config.py
    |— /database
        |— session.py
        |— models.py
        |— /sql
            |— crud.py
    |— main.py
    |— task.env
    |— .gitignore
    |— requirememts.txt
```
