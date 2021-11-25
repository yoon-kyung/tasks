# TASK
----

## TASK 구현 개요
- DB는 AWS RDS MySQL 8.0을 이용 했습니다.
- 배포를 위한 클라우드 서버는 AWS EC2를 이용 했습니다.
- 과제 DB 스키마에는 들어가 있지 않았지만 "created_at", "updated_at", "deleted_at" 컬럼을 넣었습니다.
- DELETE 구현 시 논리적으로 삭제되어 사용자가 삭제를 하여도 DB상에는 남도록 구현했습니다. (실제 서비스라면 삭제된 글도 필요한 경우가 생길 수 있다고 생각했습니다.)

----

## 사용방법
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
```
- 데이터가 없는 경우
```
```
- 실패
```
```

### 2. GET /task/:task_id
Response Body
- 성공
```
```
- 데이터가 없는 경우
```
```
- 실패
```
```

### 3. POST /task
Request Body
```
```

Response Body
- 문제에서는 no response body지만 추후 필요한 경우가 생길 수 있으니 작성한 내용을 Response Body로 지정했습니다.

- 성공
```
```
- 데이터가 없는 경우
```
```
- 실패
```
```

### 4. PATCH /task/:task_id
Request Body
```
```

Response Body
- 문제에서는 no response body지만 추후 필요한 경우가 생길 수 있으니 수정한 내용을 Response Body로 지정했습니다.

- 성공
```
```
- 데이터가 없는 경우
```
```
- 실패
```
```

### 5. DELETE /task/:task_id
Response Body
- 문제에서는 no response body지만 추후 필요한 경우가 생길 수 있으니 삭제한 내용을 Response Body로 지정했습니다.
```
```

### 6. DELETE /task
Response Body
- 문제에서는 no response body지만 추후 필요한 경우가 생길 수 있으니 삭제한 게시글 수를 Response Body로 지정했습니다.
```
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
        |— settings.py
    |— /database
        |— session.py
        |— models.py
        |— /sql
            |— crud.py
    |— main.py
    |— task.env
```
