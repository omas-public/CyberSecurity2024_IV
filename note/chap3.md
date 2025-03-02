# Chapter3 ParrotOS で遊ぼう

## 3-1 ParrotOS 内を探検する(p130)

重要度 ☆☆☆

FHS(Filesystem Hiearchy Standard) という標準があり，Linux の各ディストリビューションはそれに従っている。各ディレクトリがそれぞれどういうファイルを格納する役割を持っているかを知る。

## 3-2 more コマンドと less コマンド(p138)

重要度 ☆☆☆

more も less もページャーの一種であり，less は使用頻度が高いのでキーバインドを覚えておく必要がある。

## 3-3 ファイルの探し方

重要度 ☆☆☆

Linux での検索はまず locate コマンドとワイルドカード及び簡単な正規表現をおぼえて次に find コマンドを使えるようにすること，GUI は特に必要ない。

## 3-4 man を活用する(p151)

重要度 ☆☆☆☆

新しいコマンドがでたらまず man をみるクセをつけよう，ふだんから man に目をとおして置くことでオプションが使えるようになる。

## 3-5 ファイル操作とパーミッション(162)

### ファイルを扱う基本コマンド(p162)

重要度 ☆☆☆☆

ファイルを扱う基本コマンドは基本なので rmdir と more 以外は皆普段遣いである。

### ユーザーの種類(p163)

重要度 ☆☆☆☆

root, system, 一般ユーザーの役割を知りなぜ別れているかを説明できるようにせよ

下記のコマンドがどのような情報を返すか確認し man からオプションを確認して試してみよ

- whoami
- id
- groups

### ユーザーとグループの情報ファイル(p167)

重要度 ☆☆☆

- /etc/passwd
- /etc/shadow
- /etc/group

### ファイルの属性情報(p171 - p180 )

重要度 ☆☆☆☆

ファイル種別とユーザ，グループ，パーミッションを理解し変更できるようにしよう

- パーミッションの変更はオクタルもシンボリックもどちらも使えるように
- デフォルトパーミッションと umask の関係を理解しよう
- ファイルの所有者やグループを変更できるようにしよう

## 3-6 テキスト編集をマスターする(p181-p187)

重要度 ☆☆☆☆

vi をまともに使えるようになろう，その他のエディタはお試しくらいでよい

## 3-7 ParrotOS におけるインストールテクニック(p188 - p206)

重要度 ☆☆☆

ディストリビューションによってパッケージ管理は違うが，Ubuntu も ParrotOS も同じ Debian けいなので`dpkg`と`apt`が使える，何が違うのかを理解すること。
また OS 以外でもパッケージ管理の仕組みはたくさん出てくるので(pip, npm 等)パ ッケージ管理でなにができるのかを理解すること，ここでも GUI のパッケージ管理(Synaptic)は特に覚える必要はない。

## 3-8 プロセスを理解する(p206)

重要度 ☆☆☆☆☆

このセクションは非常に重要なので，何度もサンプルを実行して理解をすること

### プログラム，ソフトウェア，アプリケーション(p206)

重要度 ☆☆

コンピューティングの中心にプログラムがあることを理解する，タイトルの単語以外にもスレッド，プロセス，ジョブ，バッチなどの用語があるがすべてプログラムの一形態に過ぎないことを理解する

### プロセスの状態を確認する(p207)

重要度 ☆☆☆☆☆

プロセスの状態遷移を知り，表示される出力項目の内容がわかり基本的な ps コマンドのオプションが使えるようになろう。

- R 実行(可能)状態(running, ready)
- T 停止状態(terminate)
- S 割り込み可能停止状態(sleep)
- Z ゾンビ状態(zombi)
- PID(proccess id)
- TTY(teletypewriter)
- CMD(command)

### プロセスを追跡する(p213)

重要度 ☆☆☆☆

top コマンドの見方と覚え対話コマンドを試してみよう。

### プロセスには親子関係がある(p215)

重要度 ☆☆☆

UNIX のブートストラップから，どのようにプロセスが管理されているかは後々重要になるが今の段階ではプロセスの親子関係にあることを理解できていれば良い。

### プロセスを停止・終了する(p219)

重要度 ☆☆☆☆

kill コマンドを使ってシグナルを送信する方法を覚え，下記のシグナルは覚えよう
シグナル名は単に番号のエイリアスである，つまり `$ kill -KILL PID` は `$ kill -9 PID` と同等の効力を持つ。SIGTERM と SIGKILL の違いは覚えよう。
ドレスを割り当てて良い。どちらかというと固定 I

- 1 HUP
- 9 KILL
- 15 TERM
- 20 TSTP

### ジョブコントロールでプロセスを操る(p223)

重要度 ☆☆☆☆

p224 の図を理解して，状態遷移を行えるようにしよう

- jobs
- % $JOBID
- bg
- fg
- ^Z
- &

## 3-9 シェル変数と環境変数(p229)

重要度 ☆☆☆

シェル変数と環境変数の違いを理解してどちらも定義できるようにする

シェル変数の定義は `変数名=値` (＝の前後に空白を入れない)，シェル変数は子シェルに引き継がれない，`echo $変数名` で参照できる

環境変数の定義は ` export 変数名=値` 環境変数は子シェルに引き継がれる，環境
変数の一覧を見るには `printenv` を使う

### コマンドパスを含む環境変数 PATH(p236)

重要度 ☆☆☆

PATH とは何か，なぜ便利なのかを説明できること。また$PATH に PATH の追加ができるようになること。

### ビルトインコマンド(p239)

重要度 ☆☆

UNIX のコマンドは外部コマンド(プログラムが bin などのディレクトリにある)と内部コマンド(ビルトインコマンド)がある。以下のコマンドを用いてコマンドの種別や場所を確認しよう

- type
- which
- whereis
