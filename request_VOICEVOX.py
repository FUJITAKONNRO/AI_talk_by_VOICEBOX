import requests
import simpleaudio as sa

def voice(text, speaker):
    # ① audio_query を取得
    query = requests.post(
        "http://127.0.0.1:50021/audio_query",
        params={"text": text, "speaker": speaker}
    )

    # ② synthesis（Content-Type を必ず指定）
    synthesis = requests.post(
        "http://127.0.0.1:50021/synthesis",
        params={"speaker": speaker},
        data=query.text,
        headers={"Content-Type": "application/json"}
    )

    return synthesis.content

#テスト用
if __name__ == "__main__":
    sample_text = input("音声合成したいテキストを入力してください: ")
    speaker_id = 19 # 九州そら(ひそひそ)
    wav_data = voice(sample_text, speaker_id)
    with open("voicevox_test.wav", "wb") as f:
        f.write(wav_data)
    #print("voicevox_test.wav を出力しました")

    # 生成した音声ファイルを再生
    wave_obj = sa.WaveObject.from_wave_file("voicevox_test.wav")
    play_obj = wave_obj.play()
    play_obj.wait_done()
    #print("再生が終了しました")