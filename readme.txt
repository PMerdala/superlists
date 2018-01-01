komendy
uruchamia� z katalogu projektu
./superlists
# dodanie nowego projektu o nazwie superlists
django-admin.py startproject superlists
#dodanie aplikacji o naziw lists
python manage.py startapp lists
# wystartowanie serwera
python manage.py runserver
# wykonanie testow jednostkowych
python manage.py test
# wykonanie skryptu pythona
python functional_tests.py

#git usuniecie niepotrzebnych plik�w
git rm -r --cached superlists\__pycache_
git commit -am"komentarz"
#dodanie zewn�trzego repozytorium o nazwie superlists
git remote add origin https://github.com/PMerdala/superlists.git
#r�nice w stage
git diff --staged
#logi w postaci jednej linie
git log --oneline