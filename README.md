# タソカレ

[![Product Name](image.png)](https://www.youtube.com/watch?v=G5rULR53uMk)

## 製品概要
### 君の名は？ X Tech

### 背景（製品開発のきっかけ、課題等）
「うわ〜、、この人誰だっけ、、、」

久しぶりに会った人。一度しか会っていない人。見た事はあるけれど、どうしても名前が思い出せない！  
でも「誰でしたっけ？」なんて言えないし...

我々はそんな誰もが抱える悩みを解決しました。


### 製品説明（具体的な製品の説明）
名前を忘れてしまった人に会ったときに、撮影用デバイスで対象となる人物を撮影します。

写真はデータベース上の写真と照合され、最も近い人物の名前がユーザーに通知されます。

こっそりと結果を確認することで、相手の気分を害することなくコミュニケーションが始められます。

### 特長
全てのユーザーは写真登録用のWEBサイトでアカウントを作成する必要があります。  
そのサイトを通じて自分の写真をアップロードし、データベースに名前と写真を登録しましょう。その登録をもって、撮影用デバイスから撮影されることに同意したものとみなします。

#### 1. Raspberry Pi で写真を撮影・アップロード
撮影デバイスには**Raspberry Pi 3 Model B+**を用いました。  
ポケットサイズなのでユーザーは素早く手軽に写真を撮影することが可能です。

#### 2. OpenFace を用いた顔認証
撮影された写真はサーバにアップロードされ、**Python + OpenFace**で解析されます。  
サーバー上に保存されている顔写真と一番近い人物が出力されます。

#### 3. 認証の結果をLINEで通知
結果はユーザーへ**LINE Notify**で通知されます。  
スマートウォッチなどのウェアラブルデバイスを用いることで、相手に悟られる事なく名前を知ることができます。

### 解決出来ること
名前を忘れてしまった人に会ったとしても、円滑なコミュニケーションを行うことができます。

### 今後の展望
+ WEBサイトの機能拡張
    * SNSのように友達登録機能を実装することで、無関係な人を撮影した際には結果を返さないようにする
    * 撮影用デバイス

今回は実現できなかったが、今後改善すること、どのように展開していくことが可能かについて記載をしてください。


## 開発内容・開発技術
### 活用した技術
#### API・データ
今回スポンサーから提供されたAPI、製品などの外部技術があれば記述をして下さい。

* LINE Notify

#### フレームワーク・ライブラリ・モジュール
* Raspberry Pi Camera Module V2
* Ruby on Rails
* SQLite3
* OpenFace

#### デバイス
* Raspberry Pi 3 Model B+
* AWS EC2/ubuntu
* スマートブレスレット V07S

### 研究内容・事前開発プロダクト（任意）
なし

ご自身やチームの研究内容や、事前に持ち込みをしたプロダクトがある場合は、こちらに実績なども含め記載をして下さい。

* 
* 


### 独自開発技術（Hack Dayで開発したもの）
#### 2日間に開発した独自の機能・技術
* 予定していた全ての機能をHack Day内で実現することができた。

* 独自で開発したものの内容をこちらに記載してください
* 特に力を入れた部分をファイルリンク、またはcommit_idを記載してください（任意）
