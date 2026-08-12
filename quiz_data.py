from quiz import Quiz


DEFAULT_QUIZZES = [
    # =========================
    # Terminal
    # =========================

    Quiz(
        "현재 위치가 /project/src이고, /project/data/a.txt를 src/backup/으로 복사하려 한다. 올바른 명령은?",
        [
            "cp ../data/a.txt backup/",
            "cp ../../data/a.txt backup/",
            "cp ../data/a.txt ./backup/",
            "cp /data/a.txt ./backup/"
        ],
        3,
        "현재 위치는 src입니다. data와 backup의 위치를 각각 현재 위치와 비교해 보세요."
    ),

    Quiz(
        "다음 권한의 파일을 소유자는 수정할 수 있고, 그룹은 읽을 수만 있으며, 나머지는 접근할 수 없게 변경하려 한다. 필요한 chmod 값은?",
        [
            "640",
            "620",
            "460",
            "600"
        ],
        1,
        "소유자, 그룹, 기타 사용자 순서입니다. 각각 필요한 r/w/x 권한을 숫자로 바꿔보세요."
    ),


    # =========================
    # Git
    # =========================

    Quiz(
        "app.py와 README.md를 수정했다. app.py만 다음 커밋에 포함하고 싶다. 이후 두 파일 모두 수정된 상태를 유지하려면 어떤 순서가 적절한가?",
        [
            "git add . → git commit",
            "git add app.py → git commit",
            "git commit → git add app.py",
            "git add README.md → git commit"
        ],
        2,
        "commit은 Working Tree가 아니라 Staging Area에 올라간 변경을 대상으로 합니다."
    ),

    Quiz(
        "A-B-C 순서의 커밋에서 현재 HEAD가 C다. C의 커밋을 취소하되 C의 변경 내용은 수정할 수 있도록 남겨두려 한다. 어떤 명령이 적절한가?",
        [
            "git reset --hard HEAD~1",
            "git reset --soft HEAD~1",
            "git reset --hard HEAD",
            "git reset --soft HEAD~2"
        ],
        2,
        "목표는 C를 가리키던 HEAD를 B로 옮기면서 C의 변경 내용을 버리지 않는 것입니다."
    ),


    # =========================
    # Docker
    # =========================

    Quiz(
        "nginx 컨테이너의 80번 포트로 접속해야 한다. 호스트에서는 8080으로 접속하고 싶다. 올바른 실행 명령은?",
        [
            "docker run -p 80:8080 nginx",
            "docker run -p 8080:80 nginx",
            "docker run -p 8080 nginx",
            "docker run -p 80 nginx"
        ],
        2,
        "포트 매핑은 외부에서 접근하는 호스트 포트와 컨테이너가 사용하는 포트를 연결합니다."
    ),

    Quiz(
        "호스트의 ./app에서 파일을 수정하면 실행 중인 컨테이너의 /app에서도 즉시 확인하고 싶다. 컨테이너를 삭제해도 호스트의 파일은 유지되어야 한다. 가장 적절한 방법은?",
        [
            "Image를 수정한 뒤 새 Container를 실행한다.",
            "docker exec로 컨테이너 내부에서 파일을 수정한다.",
            "호스트 ./app을 컨테이너 /app에 bind mount한다.",
            "docker attach로 컨테이너에 연결한다."
        ],
        3,
        "컨테이너의 파일 시스템과 호스트의 특정 디렉터리를 연결하는 방법을 생각해 보세요."
    ),
]