import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
from pydantic import BaseModel, Field

#.envファイルを読み込む
load_dotenv()

# データの定義
class WordList(BaseModel):
    words: list[str] = Field(description="List of random words")

#クライアントの初期化
api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    raise ValueError("APIキーが見つかりません。.envを確認してください")

client = genai.Client(api_key=api_key)

def words(prompt ,history=[]):
    # 既に出力した単語リストをプロンプトに追加し重複を避ける
    words_history_str = "\n".join(history)
    prompt = f"{prompt}\n既に出力した単語リストからは重複しないようにしてください:\n{words_history_str}\n"
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash", 
            contents=prompt, 
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=WordList,
            ),
        )
        result_data = response.parsed
        #print(f"JSONデータ: {response.text}")
        #print(f"リストとして取得: {result_data.words}")
        return result_data.words
    
    except Exception as e:
        print(f"エラーが発生しました: {e}")
        return WordList(words=[])  # エラー時は空のリストを返す
