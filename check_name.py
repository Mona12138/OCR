import os


def rename_images(folder_path, prefix="img_", start_num=1):
    """
    批量对文件夹中的图片进行顺序编号命名（不会跳号）

    参数:
        folder_path (str): 图片所在的文件夹路径
        prefix (str): 重命名前缀，默认为 "img_"
        start_num (int): 编号起始值，默认为 1
    """
    # 获取并筛选图片文件
    files = os.listdir(folder_path)
    img_files = [f for f in files if f.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif'))]
    img_files.sort()

    # 先生成目标名字，避免冲突
    rename_plan = []
    counter = start_num
    for filename in img_files:
        ext = os.path.splitext(filename)[1]
        new_filename = f"{prefix}{counter:04d}{ext}"
        rename_plan.append((filename, new_filename))
        counter += 1

    # 如果新名字和旧名字重叠，先改成临时名
    temp_map = {}
    for old, new in rename_plan:
        if old == new:  # 名字没变，跳过
            continue
        temp_name = f"__temp__{old}"
        os.rename(os.path.join(folder_path, old),
                  os.path.join(folder_path, temp_name))
        temp_map[temp_name] = new

    # 再从临时名改到最终名
    for temp, new in temp_map.items():
        os.rename(os.path.join(folder_path, temp),
                  os.path.join(folder_path, new))
        print(f"重命名: {temp} -> {new}")

    print("批量顺序重命名完成！")
