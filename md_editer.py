import os
import json

def extract_content(input_dir="output", output_dir="txt_results"):
    """
    从 JSON 文件中提取 overall_ocr_res → rec_texts 中
    含中文冒号且冒号后有内容的字段，并保存到 txt 文件。
    """
    os.makedirs(output_dir, exist_ok=True)

    for file_name in os.listdir(input_dir):
        if not file_name.endswith("_res.json"):
            continue  # 跳过非结果文件

        file_path = os.path.join(input_dir, file_name)

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            print(f"读取 {file_name} 出错: {e}")
            continue

        # 提取 rec_texts
        results = []
        rec_texts = data.get("overall_ocr_res", {}).get("rec_texts", [])
        for text in rec_texts:
            if "：" in str(text):
                parts = text.split("：", 1)
                if len(parts) > 1 and parts[1].strip():  # 确保冒号后有内容
                    results.append(text)

        # 写入 txt
        txt_name = os.path.splitext(file_name)[0] + ".txt"
        txt_path = os.path.join(output_dir, txt_name)

        with open(txt_path, "w", encoding="utf-8") as out:
            out.write(f"识别结果 - {file_name}\n")
            out.write("=" * 50 + "\n")
            if results:
                for idx, r in enumerate(results, 1):
                    out.write(f"{idx}. {r}\n")
            else:
                out.write("未找到含有中文冒号且有内容的字段。\n")

        print(f"已处理: {file_name} → {txt_path}")


# 调用示例
extract_content("output", "txt_results")
