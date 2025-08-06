def get_sftp():
    print('sftp 작업을 시작합니다.')


def regist(name, sex, *args):
    print(f'이름: {name}')
    print(f'성별: {sex}')
    print(f'기타 옵션: {args}')


def regist2(name, sex, *args, **kwargs):
    print(f'이름: {name}')
    print(f'성별: {sex}')
    print(f'기타 옵션: {args}')

    email = kwargs.get('email') or None
    phone = kwargs.get('phone') or None
    instagram_id = kwargs.get('instagram_id') or None

    if email:
        print(f'이메일: {email}')
    if phone:
        print(f'번호: {phone}')
    if instagram_id:
        print(f'인스타 계정: {instagram_id}')