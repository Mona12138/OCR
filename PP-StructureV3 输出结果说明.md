# PP-StructureV3 输出结果说明

调用 `print()` 方法会将结果打印到终端，字段解释如下：

## 输入信息
- **input_path**: `(str)`  
  待预测图像或 PDF 的输入路径
- **page_index**: `(Union[int, None])`  
  如果输入是 PDF，表示第几页；否则为 `None`
- **model_settings**: `(Dict[str, bool])`  
  配置产线所需的模型参数

## 子产线开关
- **use_doc_preprocessor**: `(bool)` 是否启用文档预处理子产线
- **use_seal_recognition**: `(bool)` 是否启用印章文本识别
- **use_table_recognition**: `(bool)` 是否启用表格识别
- **use_formula_recognition**: `(bool)` 是否启用公式识别

---

## 文档预处理结果（仅当 use_doc_preprocessor=True 时存在）
- **doc_preprocessor_res**: `(Dict[str, Union[List[float], str]])`  
- **use_doc_orientation_classify**: `(bool)` 是否启用文档方向分类
- **use_doc_unwarping**: `(bool)` 是否启用文本扭曲矫正
- **angle**: `(int)` 文档方向分类预测结果（角度）

---

## 版面解析结果
- **parsing_res_list**: `(List[Dict])`  
  每个元素为一个版面区域的结果，按阅读顺序排序

每个区域包含：
- **block_bbox**: `(np.ndarray)` 版面区域边界框
- **block_label**: `(str)` 区域标签，如 `text`, `table`
- **block_content**: `(str)` 区域内容
- **seg_start_flag**: `(bool)` 是否为段落起始
- **seg_end_flag**: `(bool)` 是否为段落结束
- **sub_label**: `(str)` 子标签，如 `title_text`
- **sub_index**: `(int)` 子索引，用于恢复 Markdown
- **index**: `(int)` 区域索引，用于排序

---

## 全局 OCR 结果
- **overall_ocr_res**: `(Dict)`  
  包含以下信息：
  - **dt_polys**: `(List[np.ndarray])` 文本检测多边形框 (shape=(4,2))
  - **dt_scores**: `(List[float])` 文本检测置信度
  - **rec_texts**: `(List[str])` 文本识别结果
  - **rec_scores**: `(List[float])` 文本识别置信度
  - **rec_polys**: `(List[np.ndarray])` 置信度过滤后的检测框
  - **textline_orientation_angles**: `(List[int])` 文本行方向预测结果

---

## 公式识别结果
- **formula_res_list**: `(List[Dict])`
  - **rec_formula**: `(str)` 公式识别结果
  - **rec_polys**: `(np.ndarray)` 检测框
  - **formula_region_id**: `(int)` 区域编号

---

## 印章识别结果
- **seal_res_list**: `(List[Dict])`
  - **dt_polys**: `(List[np.ndarray])` 检测框
  - **rec_texts**: `(List[str])` 印章文本
  - **rec_scores**: `(List[float])` 印章识别置信度
  - **rec_boxes**: `(np.ndarray)` 矩形边界框

---

## 表格识别结果
- **table_res_list**: `(List[Dict])`
  - **cell_box_list**: `(List[np.ndarray])` 单元格边界框
  - **pred_html**: `(str)` 表格 HTML
  - **table_ocr_pred**: `(dict)` OCR 结果
  - **rec_polys**: `(List[np.ndarray])` 单元格检测框
  - **rec_texts**: `(List[str])` 单元格文本
  - **rec_scores**: `(List[float])` 单元格识别置信度
  - **rec_boxes**: `(np.ndarray)` 单元格矩形边界框

---

## 保存方法
- `save_to_json(save_path)`  
  将结果保存为 JSON（numpy 转换为 list）
- `save_to_img(save_path)`  
  保存可视化结果图像（推荐指定目录）
- `save_to_markdown(save_path)`  
  保存 Markdown 文件  
  - 输出路径为：`save_path/{your_img_basename}.md`
  - 对于 PDF 建议保存目录
- `concatenate_markdown_pages(markdown_list)`  
  将多页 Markdown 合并为一个完整文档并返回