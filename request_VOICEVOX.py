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
        data=query.text,  # ← json() ではなく text で渡す
        headers={"Content-Type": "application/json"}
    )

    return synthesis.content

