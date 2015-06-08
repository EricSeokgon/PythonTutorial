__author__ = 'sklee'
input_id = input("아이디를 입력해주세요.\n")
input_pw = input("비밀번호를 입력해주세요.\n")
real_id = "hadeslee"
real_pw = "11"
if real_id == input_id and real_pw == input_pw:
    print("Hello!!! "+input_id)
else:
    print("로그인에 실패했습니다.")
