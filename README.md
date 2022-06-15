# ikamate
splatoon3 レーティングシステム

## Dockerコマンド
```
docker-compose up -d
docker-compose down
```
```
docker-compose ps
docker-compose restart
```

## 初期設定
- `.env`ファイルを作成
```
MYSQL_ROOT_PASSWORD=
MYSQL_PASSWORD=
WEBAPP_PORT=5943
```
- `adminユーザーを作成
```
python manage.py createsuperuser
```

## 参考リンク
- https://qiita.com/satamame/items/69839ded9d54dffeb9bf