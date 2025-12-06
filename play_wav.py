import simpleaudio as sa
import request_Gemini as rGem
import request_VOICEVOX as rVOICE

# Gemini からテキストを取得
prompt = "単語を３つ教えてください。"
text = rGem.words(prompt)
speaker = 1  # ずんだもん(ノーマル)

# 音声ファイルを出力
wav_data = rVOICE.voice(text, speaker)
with open("test.wav", "wb") as f:
    f.write(wav_data)

print("OK: test.wav を出力しました")

# 音声ファイルを再生
wave_obj = sa.WaveObject.from_wave_file("test.wav")
play_obj = wave_obj.play()
play_obj.wait_done()

print("再生が終了しました")
