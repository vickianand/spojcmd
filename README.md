   spojcmd
==============
Rachit Nimavat
==============


Config File (optional)
---------------
	Create a file named .spojcmdrc  in your home folder, with the following  contents -

	[user]
	user_name = YOUR_USERNAME
	password = YOUR_PASSWORD
	wait_time = 4	(time interval in seconds for querying status of your submission)
	pyver = 2.7	(version for python compiler - 2.7 / 3.2.3 / nbc )
	cppver = 4.3.2	(version for gcc cpp compiler - 4.3.2 / 4.0.0.0-8 )
	cver = 4.3.2	(version for gcc c compiler - 4.3.2 / 99 )
	pasver = fpc	(version for pascal compiler - fpc / gpc )


Хэрхэн суулгах
--------------

`pip` ашиглан хялбархан суулгаж болно. Хэрвээ таны үйлдлийн систем дээр `pip` суугаагүй
бол дараах коммандаар суулгаарай.

    >sudo apt-get install python-pip
    >sudo pip install spoj


Системд нэвтрэх
---------------

`login` коммандаар системд нэвтрэн орно. Үүний тулд http://spoj.com дээр
бүртгүүлсэн байх шаардлагатай.
Жишээ:
	
	>spoj login <username>
	>password: <password>


Шинээр бүртгүүлэх!!!!
-----------------

`register` коммандаар шинэ хэрэглэгч бүртгүүлнэ.


Хэрэглэгчийн мэдээлэл
---------------------

`status <user_name>` коммандаар тухайн хэрэглэгчийн мэдээллийг харна. Хэдэн
бодлого бүрэн бодсон болон хэдэн бодлого дутуу бодсон талаар мэдээлнэ. Хэрвээ
`<user_name>` тодорхойлогдоогүй байвал системд нэвтэрсэн хэрэглэгчийн
мэдээллийг харуулна.


Бодлого илгээх
--------------

`tackle` коммандаар бодлогоо илгээнэ, үүний тулд кодын файлын нэрээ
аргументэд нь өгнө. Кодын файлын нэр бодлогын дугаарыг, өргөтгөл нь 
тухайн бодлогыг ямар хэл дээр шийдсэнийг илэрхийлнэ. 
Жишээ нь:

	>spoj tackle problem_id.c


Бодлогууд
---------

`list' коммандаар нийт бодологуудын жагсаалтыг харах боломжтой. Мөн баганы
дугаараар хүснэгтийн эрэмбэлэх боломжтой.
Жишээ нь:

    >spoj list --page=2 --sort=1


Бодлогын дэлгэрэнгүй
--------------------
`desc` коммандаар бодлогын дэлгэрэнгүйг харна. Үүнд бодлогын өгүүлбэр болон,
жишээ оролт, гаралтын утгууд агуулагдана. Мөн зөвхөн жишээ оролт эсвэл
гаралтын утгыг авах боломжтой.

    >spoj desc problem_id # дэлгэрэнгүй мэдээлэл
    >spoj desc --input problem_id # зөвхөн жишээ оролтын утга
