# git remote set-url 원격저장소 URL 변경하기

```
$ git remote -v  # View existing remotes
origin  https://github.com/username/repository.git (fetch)
origin  https://github.com/username/repository.git (push)

#Change existing remotes to new url
$ git remote set-url origin https://github.com/username/newrepository.git
```