פרסונה
אתה מפתח פול סטאק מקצועי עם 20 שנות ניסיון בפייתון. אתה בונה אפליקציות ושרתים בצורה חכמה, מינימלית, ברורה ופשוטה להבנה. 

המשימה:
במשימה הזו אנחנו צריכים לבנות REST API ב-Python המאפשר למשתמש לקבל מידע על מוצרים בחנות מקוונת באמצעות בקשת API לצד שלישי. 


רקע:
תלמיד בג׳וןברייס שמגיש מבחן בקורס Fullstack.

טכנולוגיות פיתוח:
• Python REST API המיושם ע"י FastAPI
ולידציה באמצעות Pydantic 
• Database מסוג MySQL באמצעות Docker.

להשתמש במידע המגיע מה-API של האתר https://fakestoreapi.com — API חינמי שאינו דורש הרשמה או API Key. כלומר, כאשר משתמש גולש ל-REST API שלכם, עליכם לבצע גלישה ל-API של האתר הזה, לקבל מידע, לעבד אותו אם צריך ולהחזיר ללקוח מידע בהתאם לאפיון הבא.
בכל ה-Routes יש לגלוש לכתובת https://fakestoreapi.com/products, המחזירה מערך של כל 20 המוצרים בחנות. כל מוצר במערך נראה כך:
{
  "id": 1,
  "title": "Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops",
  "price": 109.95,
  "description": "...",
  "category": "men's clothing",
  "image": "https://fakestoreapi.com/img/...",
  "rating": { "rate": 3.9, "count": 120 }
}
להלן ה-Routes שעליכם לבנות:

1. כל המוצרים
http://localhost:4000/api/products
ב-Route זה עליכם לגלוש לכתובת https://fakestoreapi.com/products ולהחזיר ב-Response בדיוק את המערך שהתקבל.


2. חיפוש לפי שם מוצר
http://localhost:4000/api/search/<text>
ב-Route זה יש להחזיר רק מוצרים שהמאפיין title שלהם שווה למחרוזת החיפוש שהתקבלה בפרמטר <text> או מכיל אותה (Case-Insensitive). אם לא קיימים מוצרים מתאימים יש להחזיר מערך ריק.
לדוגמה, גלישה לנתיב http://localhost:4000/api/search/jacket תחזיר את ארבעת המוצרים שבשמם מופיע הטקסט "jacket" (שימו לב שבשמות המוצרים המילה מתחילה באות גדולה):

[{"title": "Mens Cotton Jacket" … }, {"title": "BIYLACLESEN Women's 3-in-1 Snowboard Jacket Winter Coats" … }, {"title": "Lock and Love Women's Removable Hooded Faux Leather Moto Biker Jacket" … }, {"title": "Rain Jacket Women Windbreaker Striped Climbing Raincoats" … }]


3. מחיר מקסימלי
http://localhost:4000/api/price/<max>
ב-Route זה יש להחזיר רק מוצרים שמחירם (price) קטן או שווה לפרמטר <max>. הפרמטר יכול להיות מספר שלם או מספר עשרוני. אם לא קיימים מוצרים מתאימים יש להחזיר מערך ריק.
לדוגמה, גלישה לנתיב http://localhost:4000/api/price/15 תחזיר את חמשת המוצרים שמחירם 15 
או פחות:

[{"title": "White Gold Plated Princess", "price": 9.99 … }, {"title": "Pierced Owl Rose Gold Plated Stainless Steel Double", "price": 10.99 … }, {"title": "MBJ Women's Solid Short Sleeve Boat Neck V", "price": 9.85 … }, {"title": "Opna Women's Short Sleeve Moisture", "price": 7.95 … }, {"title": "DANVOUY Womens T Shirt Casual Cotton Short", "price": 12.99 … }]


4. דירוג מינימלי
http://localhost:4000/api/rating/<min>
ב-Route זה יש להחזיר רק מוצרים שהדירוג שלהם גדול או שווה לפרמטר <min> (מספר עשרוני בין 0 ל-5). שימו לב: הדירוג נמצא במאפיין פנימי — rating.rate. אם לא קיימים מוצרים מתאימים יש להחזיר מערך ריק.
לדוגמה, גלישה לנתיב http://localhost:4000/api/rating/4.6 תחזיר את חמשת המוצרים שדירוגם 4.6 ומעלה:

[{"title": "Mens Cotton Jacket" … }, {"title": "John Hardy Women's Legends Naga Gold & Silver Dragon Station Chain Bracelet" … }, {"title": "Silicon Power 256GB SSD 3D NAND A55 SLC Cache Performance Boost SATA III 2.5" … }, {"title": "WD 4TB Gaming Drive Works with Playstation 4 Portable External Hard Drive" … }, {"title": "MBJ Women's Solid Short Sleeve Boat Neck V" … }]

כי לכל המוצרים הללו יש בתוך המאפיין rating מאפיין פנימי בשם rate הגדול או שווה ל-4.6.

מסד נתונים
צרו מסד נתונים ב-MySQL בשם logs_db. 0. על מסד הנתונים להכיל טבלה/אוסף בשם logs עבור תיעוד הבקשות של הלקוחות, עם העמודות/מאפיינים הבאים:

עמודה / מאפיין
Description  - התיאור/הודעה
Method - ה-Method של ה-Request.
Route - ה-Route המלא אליו גלשו, כולל ערך ה-Route Parameter אם יש.
Duration_ms - הזמן שלקח לבקשה להסתיים בהצלחה.

תבדוק באמצעות בקשות HTTP בעצמך, ושבכל בקשה נשמרת שורה חדשה בטבלת logs.

לאחר שהכל תקין - תכין Collection עבור Postman לבדיקה מהירה, בנוסף תעלה את הדוקומנטציה האוטומטית שנוצרת מFastAPI (Swagger(


1. מחיקת תיקיית ה-venv. וקבצים רגישים או סיסמאות.
2. העלאה לGithub.
3. ולידציה תקינה באמצעות Pydantic. 
4. לשמור על קוד מינימלי, קצר, פשוט. 
5. אם יש סיסמאות, או מידע רגיש - להשתמש בקובץ .env

הגבלות:
להשתמש במינימום ספריות.
קוד פשוט, ברור, קל להבנה גם למתחילים.
הערות comments בקוד אבל לא יותר מדי. בעברית. 
לארגן את הקוד, כך שתהיה תיקייה עבור routes, וקובץ לכל Route בנפרד. 
הדבר היחידי שצריך להישמר בדאטהבייס זה רק logs. 
הכל צריך להיות מתועד בגיט מההתחלה, ולבצע כמה commits עם הערות ומידע שימושי.
להיזהר מלעשות commit לקבצים רגישים, או לסיסמאות, או לpycache / venv.  
לא לשכוח gitignore. 


*** לפני שאתה מתחיל לבנות ***
תציג לי את תוכנית הפיתוח.
תציג לי את ארכיטקטורה ומבנה הקבצים והתיקיות. 
אם יש לך הצעות לשיפור ודיוק הפרויקט - מוזמן להגיד. 
אם יש שאלות או בירורים נוספים - תשאל אותי לפני שאתה מתחיל. 

