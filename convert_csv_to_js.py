import csv
import json

print("開始します！") 

input_file = "trees_utf8.csv"
output_file = "trees.js"

trees = []

try:
    with open(input_file, newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        print("📌 読み込んだ列名（ヘッダー）:", reader.fieldnames)
        for row in reader:
            tree = {
                "id": row["id"],
                "species": row["species"],
                "difficulty": int(row["difficulty"]),
                "size": row["size"],
                "x": float(row["x"]),
                "y": float(row["y"]),
                "photos": [url.strip() for url in row["photos"].split(",")] if row["photos"].lower() != "なし" else []
            }
            trees.append(tree)

    with open(output_file, "w", encoding='utf-8') as jsfile:
        jsfile.write(f"const trees = {json.dumps(trees, ensure_ascii=False, indent=2)};")
    
    print("✅ trees.js に変換・保存しました！")

except FileNotFoundError:
    print("❌ trees.csv が見つかりませんでした。スクリプトと同じフォルダにありますか？")
except Exception as e:
    print(f"⚠️ エラーが発生しました: {e}")
