# Use ./quikgit.sh <number> to run this

git status

echo "Adding file day$1.py"
git add day$1.py README.md

echo "Committing file day$1.py"
git commit -m "Day $1 Challenge"

git status

git push