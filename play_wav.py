import simpleaudio as sa
import request_Gemini as rGem
import request_VOICEVOX as rVOICE

speaker = 19  #九州そら(ひそひそ)

prompt ="""
    思考シャッフル睡眠法（Cognitive Shuffle Sleep Method）に使用するため、
    互いに全く関連性がなく、脈絡のない「日本語の名詞」を100個挙げてください。
    【重要な条件】
    1. 誰でも容易に映像化できる「具体的な物体」であること。（例: カメラ、ライオン、トマト）
    2. 抽象的な概念（例: 幸せ、未来、関係）は絶対に含めないこと。
    3. カテゴリをバラバラにすること。（すべて動物、すべて食べ物にならないように分散させる）
    4. 不安や興奮を煽る言葉は避けること。
    5. 同じカテゴリーの言葉が連続しないようにすること。（犬、猫（動物）や、ナイフ、フォーク（食器）が続かないようにするなど）
    """
cnt = 0
word_history = []

while True:

    #print(f"---{cnt+1}回目---")
    # Gemini からテキストを取得
    text = rGem.words(prompt, word_history[-100:])
    word_history.extend(text)
    cnt += 1
    # 音声ファイルをリストの要素ごとに生成して再生
    for i, word in enumerate(text):
        wav_data = rVOICE.voice(word, speaker)
        filename = f"text.wav"
        with open(filename, "wb") as f:
            f.write(wav_data)
        #print(f"{filename} を出力しました")

        # 生成した音声ファイルを再生
        filename = f"text.wav"
        wave_obj = sa.WaveObject.from_wave_file(filename)
        play_obj = wave_obj.play()
        #print(f"再生中: {word}")
        play_obj.wait_done()
        sa.sleep(12)  # 12秒待機
    #print("再生が終了しました")

    if cnt % 6 == 5:
        print("継続しますか？ (y/n): ", end="")
        choice = input().strip().lower()
        if choice != 'y':
            break
        else:
            print("続行します")
