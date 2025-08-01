import json
import cv2
import numpy as np

def draw_boxes_from_json(image_path, json_path, output_path="vis_result.jpg"):
    # 读取JSON文件
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # 打开图像
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"图像读取失败: {image_path}")

    # 提取框
    overall_res = data.get("overall_ocr_res", {})
    rec_polys = overall_res.get("rec_polys", [])

    # 遍历每个框
    for poly in rec_polys:
        pts = np.array(poly, dtype=np.int32)
        cv2.polylines(image, [pts], True, (0, 255, 0), 2)  # 绿色矩形框

    # 保存结果
    cv2.imwrite(output_path, image)
    print(f"结果已保存到 {output_path}")

# 使用示例
draw_boxes_from_json("picture/img_0001.jpg", "output/img_0001_res.json", "0001_with_boxes.jpg")
