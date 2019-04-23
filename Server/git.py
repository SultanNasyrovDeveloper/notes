сщташп -- дGit
-----
Хранит данные в виде снимков всех файлов.

Три состояния файлов:
- committed - сохранен в локальной базе
- modified - изменены но не были зафиксированы
- staged - измененные файлы включенные в следующий коммит(индексированы)

Три секции:
- git repository - место, где хранится база и метаданные
- staging area - информация о том, какие изменения попадут в след. коммит
- working directory - файлы снимка разпакованы на диск, чтобы их можно было изменять


Первоначальная настройка:
-------------------------
Эти настройки глобальные и делаются 1 раз на системе

git config --list - проверка всех настроек
git config <key> - проверка конкретной настройки

Каждый коммит содержит эту информацию
git config --global user.name "User Name"
git config --global user.email "samle@example.com"

Псевдонимы:
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.unstage 'reset HEAD --'
git config --global alias.last 'log -1 HEAD' --> git last


Основы
------

Создание репозитория:
git init - создаст git розиторий(.git) в текущей директории

Клонирование репозитория:
git clone [url]

Игнорирование файлов:
.gitignore
glob templates:
* - 0 или более любых символов
[abc] - любому символу из указаыннх в скобках
? - любой 1 символ
[0-9] - интревал

фалы могут быть в одном из 4 состояний:
untracked, unmodified, modified, staged.


git status - определение состояния файлов
git status -s/--short - сокращенный вывод

git add filename/dirname - добавление файла в след коммит

git commit
    -m "Comment here"
    -a - автоматическое индексирование всех отслеживаемых файлов

git rm - удаление из индексируемых файлов и коммит
    --cached - перестанет индексировать, но оставит на диске


Просмотр истории Коммитов:
---------------------------
git log
    -p - разницу которую внесли в каждый коммит
    -int - количество выводимых коммитов
    --stat - сокращенная статистика для каждого коммита
    --shortstat -
    --name-status - список файлов и их статус(добавлен/удален/изменен)
    --pretty - удобный формат вывода
        =short
        =full
        =fuller
        =oneline
        =format
    --graph - текущая ветка и история слияний
    --since
    --until

Операции отмены:
git commit --amend - добавить область индексации в последний коммит
git reset HEAD filename
git checkout -- filename - вернуть файл в состоние предыдущего коммита(откат)

Работа с удаленными репозиториями:
-----------------------------------
git remote  # list of current remote repositories
git remote add [shortname] [url]
git remote show [remote name]  # информация об репозитории
git remote rename [repote name] [new remote name]
git remote rm [remote name]

git fetch [remote-name]  # забирает все данные из репо которых нет на компьютере
git pull  # git fetch(забирает данные)  и merge(соединяет с имеющимися)
git push [remote-name] [branch name]  # отправляет изменения на сервер
git push [remote] --delete [branch]  удалить ветку


Работа с метками:
-----------------
Метка это способ отметить коммит
git tag  # просмотр имеющихся меток(в алфавитном порядке)
    -l 'v1*'  # просмотр определенных тэгов
    -a v1.0  - добавить метку
    -m 'Description'  - описание метки

git show - тэги вмести с коммитами

Работа с ветками:
------------------
git branch  - список веток
    -v  - последний коммит на каждой из веток
git branch [branch] - создать новую веку
git branch -d [branch]  - удалить ветку
git checkout [branch]  - переключиться на существующую ветку
git checkout -b [branch]  - создать ветку и сразу на нее переключиться
git merge [branch]  - add [branch] to current branch


Карман
------
git stash  - спрятать все изменения
git stash pop применить последний карман
git stash list
git stash apply stash@{}
git stash drop stash@{}
git stash clear

Работа с git на сервере:
------------------------
