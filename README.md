# AI_talk_by_VOICEBOX
VOICEBOXと生成AIのAPIを連携させて、いろいろしゃべらせる。  
  
使用するもの  
・docker  
・voicevox_engine  
・Gemini API  
・Python 3.9.13  

構想  
　Youtubeには特定の目的をもって単語を羅列する動画があるが、これを生成するプログラムが作成できるのではと思った。  
　プログラムからGemini APIに対して文字列を生成するリクエストを送信し、これで得た文字列をテキストファイル等の適切な形に変形してVOICEBOX APIに送信することで音声ファイルを生成。これをプログラムが受け取り、再生する。  

プログラム構成：
・play_wav.py  
    実行すると、文字列生成プロセスと音声ファイル化プロセスを呼び出し、生成された音声ファイルを再生する。  
    音声ファイルが終了すると再びプロセスをはじめから実行する  
・request_Gemini.py  
    文字列生成プロセスを担う。Gemini apiを用いて特定の要件に合致した文字列を生成し、json形式で結果を返す。  
・request_VOICEVOX.py  
    文字列の音声ファイル化のプロセスを担う。voicevox_engineに対してHTTPリクエストを送信し、文字列を音声ファイル化させる。  

参考  
[Quita VOICEVOXをDockerで起動する方法 2025/08/17 H. Ogawa 2025/12/6参照](https://qiita.com/h-ogawa/items/501d9294340b277e4008)  
[Zenn Python経由でVoiceVoxの音声ファイルを作成する方法 2024/10/04 zenn_kiitos 2025/12/6参照](https://zenn.dev/zenn24yykiitos/articles/fff3c954ddf42c)  
[Quita READMEの使い方  2020/06/05 Mai@mzmz__02 2025/12/6参照](https://qiita.com/mzmz__02/items/b219c1592404eabda52d)  
