# side_read
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
