import os
import json
from natsort import natsorted

# 根目录（放 audios 的路径）
AUDIO_ROOT = "/Users/user/Desktop/vscode/SynParaSpeech/assets/demo-924"
OUTPUT_FILE = "/Users/user/Desktop/vscode/SynParaSpeech/assets/tts_data_new.json"

def generate_folder_data(root_dir):
    folder_data = {}
    for model in os.listdir(root_dir):
        model_path = os.path.join(root_dir, model)
        if not os.path.isdir(model_path):
            continue

        folder_data[model] = {}
        for category in os.listdir(model_path):
            category_path = os.path.join(model_path, category)
            if not os.path.isdir(category_path):
                continue

            # text.txt
            text_file = os.path.join(category_path, "audio_text.txt")
            texts = []
            if os.path.exists(text_file):
                with open(text_file, "r", encoding="utf-8") as f:
                    texts = [line.strip() for line in f if line.strip()]

            # 所有 wav 文件（按文件名排序）
            audios = []
            for fname in natsorted(os.listdir(category_path)):
                if fname.lower().endswith(".wav"):
                    abs_path = os.path.join(category_path, fname)
                    # 生成相对路径（相对于项目根目录）
                    rel_path = os.path.relpath(abs_path, start=os.path.dirname(__file__))
                    audios.append(rel_path.replace("\\", "/"))  # 确保跨平台

            folder_data[model][category] = {
                "texts": texts,
                "audios": audios
            }
    return folder_data


if __name__ == "__main__":
    data = generate_folder_data(AUDIO_ROOT)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✅ 已生成 {OUTPUT_FILE}")
