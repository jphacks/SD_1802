# タソカレ ~ 君の名は？ X Tech ~

[![Product Name](https://raw.githubusercontent.com/jphacks/SD_1802/img1/Image/top.png)](https://www.youtube.com/watch?v=BT4jsEthNRc&feature=youtu.be)

## 製品概要
### 君の名は？ X Tech

### 背景（製品開発のきっかけ、課題等）
「うわ〜、、この人誰だっけ、、、」

久しぶりに会った人。一度しか会っていない人。見た事はあるけれど、どうしても名前が思い出せない！  
でも「誰でしたっけ？」なんて言えないし...

![lady](https://raw.githubusercontent.com/jphacks/SD_1802/img1/Image/lady.jpg)

**そんな誰もが抱える悩みを解決しました！！**


### 製品説明（具体的な製品の説明）
名刺や手帳など「人を忘れないようにするツール」は数多く存在しますが、「忘れた人を思い出せるツール」は存在しません。

私たちは、**顔画像からその人の名前を逆引きするシステム**を実装する事で、自分の記憶に頼る事なく、人の名前を思い出せるツールを実現しました。

ユーザーは対象人物を専用デバイスで撮影します。撮影された写真はすぐにサーバにアップロードされ、データベース上の顔写真と照合。最も近い人物の名前がユーザーに通知されます。

結果はLINEで通知されるので、スマートウォッチなどのウェアラブル端末を用い、相手の気分を害する事なくこっそりと確認することも可能です。

#### 想定されるシチュエーション
+ 久しぶりに会った人で名前を忘れてしまっているとき
+ 学校の先生などで、不特定多数の人と日常的に接する必要があるとき
+ テレビを見ていて、タレントの名前が思い出せないとき

\* 本製品は盗撮を推奨するものではありません \*

### 特長

#### 0. Webサイトでの登録（前準備）
全てのユーザーは専用のWebサイトでアカウントを作成する必要があります。  
自分の顔画像をアップロードし、データベースに登録しましょう。  
この登録をもって、デバイスからの撮影に同意したものとみなします。

![website](https://raw.githubusercontent.com/jphacks/SD_1802/img1/Image/website.jpg)  

#### 1. Raspberry Pi で写真を撮影・アップロード
撮影デバイスには Raspberry Pi 3 Model B+ を用いました。  
ポケットサイズなのでユーザーは素早く手軽に写真を撮影することが可能です。

![raspi](https://raw.githubusercontent.com/jphacks/SD_1802/img1/Image/raspi.jpg)

#### 2. OpenFace を用いた顔認証
撮影された写真はサーバにアップロードされ、 Python + OpenFace で解析されます。  
サーバー上に保存されている顔写真と一番近い人物が出力されます。
  
![okano](https://raw.githubusercontent.com/jphacks/SD_1802/img1/Image/okano.jpg)    
(実際に検出している様子)

#### 3. 認証の結果をLINEで通知
結果はユーザーへ LINE Notify で通知されます。  
スマートウォッチなどのウェアラブルデバイスを用いることで、相手に悟られる事なく名前を知ることができます。

![model_image](https://raw.githubusercontent.com/jphacks/SD_1802/img1/Image/model.png)

ユーザに関する+αの情報を受け取る事で、さらに会話を盛り上げる事ができます。

![result](https://raw.githubusercontent.com/jphacks/SD_1802/img1/Image/line-notify.png) 

(通知の様子)

### 解決出来ること
顔写真から登録しているユーザーを逆引きすることができます。

例えば、人の名前を忘れてしまっても、その人の名前を知ることができます。

### 今後の展望
+ 撮影デバイス
    * お互いに登録していない場合はカメラを起動しないようにする。などでセキュリティを向上する。
+ WEBサイト
    * 使いやすいデザインを目指す。
    * SNSのように友達登録機能を実装することで、無関係な人を撮影した際には結果を返さないようにする。
    * 撮影用デバイスを識別できるようにする。
+ LINE Bot
    * 現在はWEBサイトを通じて画像を登録しているが、LINE Messaging API を用いる事でより手軽にアカウントの作成・更新・削除を行えるようにする。
+ スマートグラスの活用
    * スマートグラス + AR を用いる事で、さらに手軽に認証・通知を行うことができる。

## 開発内容・開発技術
### 活用した技術
#### API・データ
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

### 独自開発技術（Hack Dayで開発したもの）
#### 2日間に開発した独自の機能・技術
予定していた全ての機能をHack Day内で実現することができた。

* 撮影用デバイスの作成（Raspberry Pi + カメラモジュール）
* Raspberry Pi からサーバーへ画像のアップロード（Python）
* 顔認証システム（Python + OpenFace）
* ユーザー情報登録用のWebサイト作成（Ruby on Rails + SQLite3）
* ユーザーへ結果を返す（LINE Notify）
