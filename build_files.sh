echo "BUILD START"
python3.10 -m pip install -r requirements.txt
python3.10 manage.py collectstatic --noimput --clear
echo "BUILD END"