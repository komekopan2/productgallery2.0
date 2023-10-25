## アプリケーション名
「ProductGallery」
## アプリケーション概要
個人開発やチーム開発で作成したプロダクトを投稿するサイトです。
## URL
https://yo-tech.shimizu-v.net/
## テスト用アカウント
- ユーザ ID：あんぱん
- パスワード：Zx74107410

## 制作しようと思ったきっかけ
以前とあるwebアプリを制作したのですが、その際に家族や友人に実際に使ってもらうと、「使い方がいまいちわからない」、「もっと処理速度を上げてほしい」、「〇〇な機能がほしい」などのレビューを頂きました。自分一人で開発しているときには気づかなかったような課題点、改善案を教えて頂くことで、さらにユーザーが使いやすくなるよう改善していきたいというモチベーションの向上につながりました。私だけではなく、より多くの学生がユーザーの声を聞けるような環境を作りたいと思い、アプリの投稿サイトを制作しました。

## 機能一覧
### 基本機能
- プロダクト投稿：投稿したいプロダクトの内容を設定できます。  
<img src="https://user-images.githubusercontent.com/103621657/230879646-9091c2c9-c30f-421f-a577-be486ceb3862.png" height="300px">

- プロダクト一覧閲覧：他ユーザーが制作したプロダクトの一覧画面を閲覧できます。ソート機能もあり新しい順、人気順で並び替えができます。  
<img src="https://user-images.githubusercontent.com/103621657/230882465-f6a342c7-9b76-47ec-b916-58a237f43e20.png" height="200px">

- プロダクト詳細閲覧：他ユーザーが制作した任意のプロダクトの詳細画面を閲覧できます。プロダクトに対するレビューがある場合はここでレビューも閲覧できます。  
<img src="https://user-images.githubusercontent.com/103621657/230881166-fd6bf3fd-dc24-4ace-8070-3a04c9874ce5.png" height="300px">

- プロダクトに対するレビュー投稿：他ユーザーが制作した任意のプロダクトに対するレビューを投稿できます。  
<img src="https://user-images.githubusercontent.com/103621657/230883427-828af476-cb12-425c-aba4-4d40e8705616.png" height="300px">

### その他の基本機能
- プロダクト投稿の編集：投稿したプロダクト投稿の内容を編集できます。
- プロダクト投稿の削除：投稿したプロダクト投稿を削除できます。
### 認証機能
- サインアップ
- ログイン
- ログアウト

## ER図
<img src="https://user-images.githubusercontent.com/103621657/230900984-3b77fdce-ac99-4cba-b45e-18b6463d16a9.png" height="750px">

## 使用技術
### フロントエンド
- HTML
- CSS
- JavaScript
- BootStrap

### バックエンド
- Python3
- Django

### インフラ
- AWS(EC2)
- Nginx
- Gunicorn
- PostgreSQL
- SQLite

### その他
- Git/GitHub
- Let's Encrypt

## システム構成図
<img src="https://github.com/komekopan2/productgallery2.0/assets/103621657/246591e5-be66-4522-b1d4-ca131da08e09" height="300px">

## 実装予定の機能
- プロダクト一覧画面にフィルター機能を付け、投稿したユーザーで絞り込みできる機能
- ソーシャルログインの導入
- 投稿しているユーザーのプロフィール画面