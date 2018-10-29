Bai tap lon thu vien DHBK

- Nam:
1) data model 
2) schema 
3) admin

- Tam:
1) front end (student login=student_id + password => gan' student ID vao` session)  ( view - controller - sql query )
2) sample data generation trong file data.py (insert hon 100 records) 
3) lam phan UML 

note : 

#uml
generate command : python manage.py graph_models -a -o myapp_models.png
cach khac ?!?

#authentication
https://docs.djangoproject.com/en/2.1/topics/auth/default/#how-to-log-a-user-in

- Kien:

1) lam phan front end student xem sach da muon / mua ,dua tren student ID va table SinhVienMuaSach / SinhVienMuonSach sau khi student login 
2) listing tat ca sach trong thu vien + danh gia review & rating cho moi cuon sach ( view - controller - sql query ) sau khi student login





Set up moi truong lam viec :
- Cai python 3.6.4 
- Django 2.0.7
- Pycharm / Visual Studio Code 
- venv
- python3 -m venv testenv
- source testenv/bin/activate
- pip install nhung thu bao' lo^i~
- Postgres , tao db name BTL_thuvien truoc khi chay app 
- python manage.py flush # xoa het db
- python manage.py migrate # tao tables
- python manage.py createsuperuser #tao account admin
- python manage.py data # insert data mau
- python manage.py runserver # chay local server port 8000

