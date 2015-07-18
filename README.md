pinpin
==============

a e-commerce website


so far so cool
~~~

## run env
instal nginx
pip install gevent
pip install gunicorn


## config nginx
location / {
	try_files @uri @pp;
}
location @pp {
	proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
	proxy_set_header Host $http_host;
	proxy_pass http://127.0.0.1:5000;
}




## Run Gunicorn
gunicorn -c gun.conf myapp:app



## Flask
### Common
####set environment
- FLASK_KEY
- FLASK_ENV
- alipay_PID
- alipay_KEY
- alipay_acct

###PRODUCTION
####set environment
- mysql
- mysqlpw
