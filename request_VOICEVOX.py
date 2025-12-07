import requests

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
    sample_text = "こんにちは、これはVOICEVOXのテストです。"
    speaker_id = 36  # ずんだもん(ささやき)
    wav_data = voice(sample_text, speaker_id)
    with open("voicevox_test.wav", "wb") as f:
        f.write(wav_data)
    print("voicevox_test.wav を出力しました")
    