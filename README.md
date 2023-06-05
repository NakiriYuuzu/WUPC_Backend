## Insert Data into docker container databases
```shell
#cp sql to container
docker cp Documentation/SQL/backup.sql pcbuilder_db_1:/backup.sql
# if
docker exec -it pcbuilder_db_1 mysql -uyuuzu -pqwer pcbuilder < /backup.sql
# else
docker exec -it pcbuilder_db_1 bash
mysql -uyuuzu -pqwer pcbuilder < backup.sql

# run scraper
docker exec -it pcbuilder_web_1 python /app/Documentation/scraper/scraper.py
```