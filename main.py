from paddleocr import PPStructureV3
import os
from low_quality import resize_and_save
from md_editer import extract_content
from check_name import rename_images
pipeline = PPStructureV3()

# ocr = PPStructureV3(use_doc_orientation_classify=True) # 通过 use_doc_orientation_classify 指定是否使用文档方向分类模型
ocr = PPStructureV3(use_doc_unwarping=True) # 通过 use_doc_unwarping 指定是否使用文本图像矫正模块
# ocr = PPStructureV3(use_textline_orientation=True) # 通过 use_textline_orientation 指定是否使用文本行方向分类模型
# ocr = PPStructureV3(device="gpu") # 通过 device 指定模型推理时使用 GPU



img_dir = 'picture'
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)
rename_images(img_dir)
# 遍历图片
for img_name in os.listdir(img_dir):
    img_path = os.path.join(img_dir, img_name)

    if not img_name.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp')):
        continue

    print(f"正在处理: {img_path}")


    try:

       #调整图片分辨率
        resize_and_save(img_path,img_path, max_size=1500)
        # 调用 OCR
        output = pipeline.predict(img_path)

        base_name = os.path.splitext(img_name)[0]
        for idx, res in enumerate(output):
            #save_prefix = os.path.join(output_dir, f"{base_name}_{idx}")
           res.save_to_json(save_path=output_dir)
               # res.save_to_img(save_path=output_dir)
           # res.save_to_markdown(save_path=save_prefix)




    except Exception as e:
        print(f"❌ 处理失败 {img_path} ：{e}")
        continue

extract_content(output_dir,output_dir)