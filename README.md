# ADC
## If you want to generate requirements.txt
**pipreqs ./ --encoding=utf8 --force** 

## db migrate and init
```
1. python3 -m flask db init

2. python3 -m flask db migrate -m "init"

3. python3 -m flask db upgrade
```
**or only run**
```
python3 -m flask init
```

## generate DB data to model
**flask-sqlacodegen postgresql://postgres:root@localhost:5432/imedtac?options=-c%20search_path=core --outfile "module.py"**

