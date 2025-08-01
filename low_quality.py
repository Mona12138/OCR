import cv2
import numpy as np
import os

def cv2_imread_chinese(path):
    """支持中文路径的 imread"""
    data = np.fromfile(path, dtype=np.uint8)
    return cv2.imdecode(data, cv2.IMREAD_COLOR)

def cv2_imwrite_chinese(path, img):
    """支持中文路径的 imwrite"""
    ext = os.path.splitext(path)[1]  # 获取扩展名
    ok, encoded_img = cv2.imencode(ext, img)
    if ok:
        encoded_img.tofile(path)
    return ok

def resize_and_save(img_path, save_path, max_size=2000):
    # 读取原图
    img = cv2_imread_chinese(img_path)
    if img is None:
        raise Exception(f"图片读取失败: {img_path}")

    h, w = img.shape[:2]
    print(f"原始尺寸: {w}x{h}")

    # 缩放比例（仅缩小）
    scale = min(max_size / max(h, w), 1.0)
    if scale < 1.0:
        new_w, new_h = int(w * scale), int(h * scale)
        img_resized = cv2.resize(img, (new_w, new_h), interpolation=cv2.INTER_AREA)
        print(f"缩小后尺寸: {new_w}x{new_h}")
    else:
        img_resized = img
        print("无需缩放，尺寸已在阈值内。")

    # 保存
    success = cv2_imwrite_chinese(save_path, img_resized)
    if success:
        print(f"✅ 已保存缩小后的图片到: {save_path}")
    else:
        print(f"❌ 保存失败: {save_path}")

