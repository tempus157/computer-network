## 서버 실행

먼저 다음과 같은 명령어로 서버를 실행합니다.

```
pip install flask bcrypt pyjwt
flask run
```

## 회원가입

이메일과 비밀번호, 이름을 바디에 담아 리퀘스트를 보냅니다. 

<img width="268" alt="스크린샷 2022-05-03 오후 1 17 13" src="https://user-images.githubusercontent.com/49771744/166404078-8620c374-9427-4f46-89a2-8b2b40225fe8.png">

서버로부터 201 리스폰스를 받게 됩니다. 데이터베이스에 암호화된 비밀번호와 함께 데이터가 생성된 것을 확인하실 수 있습니다.

<img width="333" alt="스크린샷 2022-05-03 오후 1 18 13" src="https://user-images.githubusercontent.com/49771744/166404123-39c57413-5542-4309-858d-5a9a53372675.png">
<img width="621" alt="스크린샷 2022-05-10 오전 3 43 05" src="https://user-images.githubusercontent.com/49771744/167476264-0516557d-98c1-434b-bd41-b4c3d95334b0.png">

만약 중복된 이메일로 요청을 보낸다면, 다음과 같이 409 리스폰스를 받게 됩니다.

<img width="334" alt="스크린샷 2022-05-03 오후 1 20 09" src="https://user-images.githubusercontent.com/49771744/166404242-a235c547-a317-4a00-9b64-e91d3dc405bc.png">

## 로그인

이메일과 비밀번호를 바디에 담아 리퀘스트를 보냅니다.

<img width="262" alt="스크린샷 2022-05-03 오후 1 23 02" src="https://user-images.githubusercontent.com/49771744/166404427-e9c9f88a-1be5-4abe-a648-90cdfa64d64f.png">

서버로부터 201 리스폰스를 받게 됩니다. 리스폰스와 함께 JWT로 암호화된 Credential 데이터를 받게 되는데, 클라이언트에서 이 정보를 로컬 스토리지에 보관합니다.

<img width="835" alt="스크린샷 2022-05-03 오후 1 24 15" src="https://user-images.githubusercontent.com/49771744/166404503-ebc6875e-e76b-4304-a3bd-a01abb8a6070.png">

만약 잘못된 이메일이나 비밀번호로 요청을 보낸다면, 다음과 같이 404 리스폰스를 받게 됩니다. 

<img width="334" alt="스크린샷 2022-05-03 오후 1 25 24" src="https://user-images.githubusercontent.com/49771744/166404553-864f88c8-04f6-4ffd-87ef-dbfb48b11f5e.png">

## 로그아웃

Authorization 헤더에 저장해둔 Credential을 담아 요청합니다. 

<img width="868" alt="스크린샷 2022-05-03 오후 1 27 01" src="https://user-images.githubusercontent.com/49771744/166404641-7bdac6d8-af05-40d4-b63c-ed30eae0532d.png">

서버로부터 200 리스폰스를 받게 됩니다. 이후 클라이언트는 로컬 스토리지에서 Credential 정보를 제거하게 됩니다.

<img width="334" alt="스크린샷 2022-05-03 오후 1 27 49" src="https://user-images.githubusercontent.com/49771744/166404684-e112fe8b-5df2-4b5c-889d-52ade86d6439.png">

만약 잘못된 헤더와 함께 요청을 보낸다면, 다음과 같이 401 리스폰스를 받게 됩니다. 

<img width="334" alt="스크린샷 2022-05-03 오후 1 28 51" src="https://user-images.githubusercontent.com/49771744/166404740-bf542ade-b336-41ec-8e0a-7a5cf58e46c9.png">

## 유저 가져오기

Authorization 헤더에 저장해둔 Credential을 담아 요청합니다. 

<img width="864" alt="스크린샷 2022-05-03 오후 1 29 51" src="https://user-images.githubusercontent.com/49771744/166404796-5e7c073e-7920-4019-8746-f9cbe256c3d9.png">

서버로부터 200 리스폰스를 받게 됩니다. 리스폰스에는 유저의 이메일, 이름이 바디에 담겨 옵니다.

<img width="333" alt="스크린샷 2022-05-03 오후 1 30 34" src="https://user-images.githubusercontent.com/49771744/166404835-44d60add-cef8-4259-a70f-732f05b24e02.png">

만약 잘못된 헤더와 함께 요청을 보낸다면, 로그아웃에서와 같은 401 리스폰스를 받게 됩니다.

## 회원 탈퇴

Authorization 헤더에 저장해둔 Credential을 담아 요청합니다. 

<img width="864" alt="스크린샷 2022-05-03 오후 1 31 24" src="https://user-images.githubusercontent.com/49771744/166404874-a808811c-aa6c-44c8-bc29-561ed61f8f4e.png">

서버로부터 200 리스폰스를 받게 됩니다. 데이터베이스에서 해당 회원의 정보가 제거됩니다.

<img width="331" alt="스크린샷 2022-05-03 오후 1 31 34" src="https://user-images.githubusercontent.com/49771744/166404882-23cac853-0053-43b3-b98d-5a2eb3e8d70f.png">

만약 존재하지 않는 유저의 Credential이나 잘못된 헤더와 함께 요청을 보낸다면, 로그아웃에서와 같은 401 리스폰스를 받게 됩니다.
