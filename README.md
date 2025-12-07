# AI_talk_by_VOICEBOX
VOICEBOXと生成AIのAPIを連携させて、いろいろしゃべらせる。
今回は思考シャッフル睡眠法に使えるように単語をランダムに読み上げるようにpromptを設計する。    
  
使用するもの  
・docker voicevox_engineの構築済みコンテナ もしくは　製品版VOICEVOX（[VOICEVOXサイトリンク](https://voicevox.hiroshiba.jp/)）  
・Gemini API 使用モデル:gemini-2.5-flash-lite  
・Python 3.9.13  
・pip version 22.0.4  

構想  
　Youtubeには特定の目的をもって単語を羅列する動画があるが、これを生成するプログラムが作成できるのではと思った。  
　プログラムからGemini APIに対して文字列を生成するリクエストを送信し、これで得た文字列をテキストファイル等の適切な形に変形してVOICEBOX APIに送信することで音声ファイルを生成。これをプログラムが受け取り、再生する。  

プログラム構成：  
・play_wav.py  
    実行すると、文字列生成プロセスと音声ファイル化プロセスを呼び出し、生成された音声ファイルを再生する。  
    音声ファイルの再生がすべて終了すると再びプロセスをはじめから実行する。  
・request_Gemini.py  
    文字列生成プロセスを担う。Gemini apiを用いてpromptに合致した文字列を生成し、json形式で結果を返す。  
・request_VOICEVOX.py  
    文字列の音声ファイル化のプロセスを担う。voicevox_engineに対してHTTPリクエストを送信し、文字列を音声ファイル化させる。  

●VOICEVOX_ENGINE構築済みdockerコンテナを起動:  
(docker voicevox_engineの構築済みコンテナを使う人)  
docker pull voicevox/voicevox_engine:cpu-ubuntu20.04-latest  
docker run -d -p 50021:50021 voicevox/voicevox_engine:cpu-latest  　
docker ps #確認用  

●VOICEVOX起動:  
(製品版VOICEVOXを使う人)  
ダウンロードした製品版VIOCEVOXを起動する  


[どちらもこれが閲覧できればOK](http://127.0.0.1:50021/docs#/)

使用したpip:  
pip install simpleaudio  
pip install request  
pip install -q -U google-genai  
pip install python-dotenv  

これでOK:  
$ pip list  
Package            Version  
------------------ ----------  
annotated-types    0.7.0  
anyio              4.12.0  
cachetools         6.2.2  
certifi            2025.11.12  
charset-normalizer 3.4.4  
exceptiongroup     1.3.1  
google-auth        2.43.0  
google-genai       1.47.0  
h11                0.16.0  
httpcore           1.0.9  
httpx              0.28.1  
idna               3.11  
pip                22.0.4  
pyasn1             0.6.1  
pyasn1_modules     0.4.2  
pydantic           2.12.5  
pydantic_core      2.41.5  
python-dotenv      1.2.1  
requests           2.32.5  
rsa                4.9.1  
setuptools         58.1.0  
simpleaudio        1.0.4  
tenacity           9.1.2  
typing_extensions  4.15.0  
typing-inspection  0.4.2  
urllib3            2.6.0  
websockets         15.0.1  

参考、引用記事  
[Quita. VOICEVOXをDockerで起動する方法. 2025/08/17. H. Ogawa. 2025/12/6.](https://qiita.com/h-ogawa/items/501d9294340b277e4008)  
[Zenn.　【VOICEVOX,Docker】VOICEVOX ENGINEを建てる.　2025/03/29.　ずんずぃー.　2025/12/6.](https://zenn.dev/iwanorigoro/articles/9b9104b3513a56)  
[Zenn. Python経由でVoiceVoxの音声ファイルを作成する方法. 2024/10/04. zenn_kiitos. 2025/12/6.](https://zenn.dev/zenn24yykiitos/articles/fff3c954ddf42c)  
[Quita. READMEの使い方.  2020/06/05 Mai@mzmz__02. 2025/12/6.](https://qiita.com/mzmz__02/items/b219c1592404eabda52d)  
[Quita. Pythonでサウンドを扱う.　2020/02/11. @hisshi00. 2025/12/6.](https://qiita.com/hisshi00/items/62c555095b8ff15f9dd2)  
[Google. “Gemini API Quickstart”. Google AI for Developers. 2025-12-07.](https://ai.google.dev/gemini-api/docs/quickstart?hl=ja)  