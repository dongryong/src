python manage.py collectstatic

git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/dongryong/src.git
git push -u origin main

git clone https://github.com/dongryong/src.git

git remote -v
git remote update origin


pip freeze > requirements.txt

Open terminal and enter the folder of the github repository/project you want to update
Type into terminal: “git add .” and then hit enter
Type into terminal “git status” and then hit enter (this step is optional)
Type into terminal “git commit -m ‘type any message here” and then hit enter
Type into terminal “git push” and then hit enter