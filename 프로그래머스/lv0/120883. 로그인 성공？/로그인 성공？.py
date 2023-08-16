def solution(id_pw, db):
    for id, pw in db:
        if id_pw[0] == id:
            if id_pw[1] == pw:
                return "login"  # 아이디와 비밀번호가 모두 일치하는 경우
            else:
                return "wrong pw"  # 아이디는 일치하지만 비밀번호가 일치하지 않는 경우
    return "fail"  # 아이디가 일치하는 회원이 없는 경우