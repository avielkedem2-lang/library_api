"# library_api" 
לפנכים מערכת של ניהול ספרייה כוללת נתונים של הספרים חברים
הטבלת ספרים :
היא יוצרת ספר חדש, היא מדפיסה לי את כל הספרים או ספר מסויים, והיא יכולה לעדכן ספר, 
והיא מציגה אם הספר מושאל או לא,


הטבלת חברים:
היא יוצרת חבר חדש,היא מציגה את כל החברים שבמערכת או חבר אחד, היא יכולה לעדכן חבר במערכת, ןהיא יכולה להשבית חבר  ולהפעיל.



docker run --name my-mysql-library \ -e MYSQL_ROOT_PASSWORD=1234 \ -e MYSQL_DATABASE=library_db \ -p 3306:3306 \ -v mysql_data-library:/var/lib/mysql \ -d mysql:latest


library-api/
│
│
├── main.py
├── database/
│ ├── db_connection.py
│ ├── book_db.py
│ └── member_db.py
├── routes/
│ ├── book_routes.py
│ ├── member_routes.py
│ └── report_routes.py
├── logs/
│ └── app.log
│
├── README.md
├── requirements.txt
└── .gitignore


מבנה הטבלאות:
books:
id | title | author | genre | is_available | id_member_by_borrowed

members:
id | name | email | is_active | borrows_total




חוקי המערכת:
יצרית ספר:
בשביל שהמשתמש יכול להכניס ספר חדש הוא חייב שהיה בו את 
title | author | genre 
והמערכת מוסיפה האם הוא זמין או שמישהו השאיל אותו


ז'אנר:
כשהמשתמש מכניס לי genre חייב להיות בו אחד מהדברים הבאים:
fiction | non-fiction | science | history | other
אם המשתמש הכניס משהו אחר יפול שגיאה 



יצירת חבר:
בשביל ליצור חבר המשתמש צריך להכניס  name and email:



איימל:
email חייב להיות יחודי:



חבר לא פעיל:
אם החבר לא פעיל הוא לא יכול להשאיל ספרץ



ספר לר זמין:
אם הספר לא זמין אי אפשר להזמין אותו.



מקסימום ספרים:
חבר לא יכול להחזיק יותר משלושה ספרים.


החזר ספר:
ניתן להחזיר ספר רק אם הוא מושאל לאותו חבר שמחזיר אותו.







list of endpoints:
1. POST /books -> מוסיף ספר חדש


2. GET /books -> מביא לי את כל הרשימה של הספרים


3. GET /books/{id} -> מחזיר לי ספר


4. PATCH /books/{id} -> מעדכן ספר


5. PATCH /books/{id}/borrow/{member_id} -> השאלת ספר מחבר


6. PATCH /books/{id}/return/{member_id} -> החזרת ספר מחבר


7. POST /members -> יוצר חבר


8. GET /members -> מדפיס את כל החברים שבטבלה


9. GET /members/{id} -> מביא לי חבר לפי ה ID


10. PUT /members/{id} -> מעדכן חבר


11. PATCH /members/{id}/deactivate -> משבית חבר


12. PATCH /members/{id}/activate -> מפעיל חבר


13. GET /reports/summary -> מביא דוח בללי


14. GET /reports/books-by-genre -> מביא לי ספרים לפי ז'אנר


15. GET /reports/top-member -> החבר הכי פעיל






זרימת המערכת :
POST:
אם המשתמש בוחר באופציה של להכניס post,
המערכת מקבלת את הפוסט ובודקת עם זה תקין, אם זה תקין אז המערכת מוסיפה ל database


GET:
אם המשתמש בוחר באופציה של get, 
המערכת מחזריה לו רשימה של כל הטבלה



GET{id}:
אם המשתמש בוחר באופציה של get(id),
המערכת מקבלת את id ובודקת האם זה תקין,
אם זה תקין המערכת תחזיר לי את ספר\חבר.



PUT:
אם המשתמש רוצה לעדכן ספר\חבר,
המערכת מקבלת את body and id ובודקת אם זה תקין,
אם זה תקין המערכת מעדכנת את database.



PATCH:
אם המשתמש רוצה שחבר ישאיל ספר,
המערכת מקבלת את ה ID של הספר ומקבלת את ה id של חבר
ובודקת אם זה תקין, ואם זה תקין המערכת תעדכן את database.



PATCH:
אם המשתמש רוצה להחזיר ספר,
המערכת תתצטרך לקבל id and member id,
ואם זה תקין המערכת מעדכנת את database.




PATCH:
אם המשתמש רוצה להשבית חבר,
המערכת צריכה לקבל id,
אם זה תקין המערכת מעדכנת את  ה database.



PATCH:
אם המשתמש רוצה להפעיל חבר,
המערכת צרכיה לקבל id,
אם זה תקין אז המערכת מעדכנת את ה database.
