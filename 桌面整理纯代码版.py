import os
import shutil

def safe_move(src, dst_dir, filename):
    dst_path = os.path.join(dst_dir, filename)
    counter = 1
    name, ext = os.path.splitext(filename)
    while os.path.exists(dst_path):
        new_name = f"{name}_{counter}{ext}"
        dst_path = os.path.join(dst_dir, new_name)
        counter += 1
    shutil.move(src, dst_path)
    return os.path.basename(dst_path)

desktop = os.path.expanduser("~/Desktop")

img_folder = os.path.join(desktop, "图片")
doc_folder = os.path.join(desktop, "文档")
zip_folder = os.path.join(desktop, "压缩包")
lnk_folder = os.path.join(desktop, "快捷方式")
exe_folder = os.path.join(desktop, "软件安装包")
url_folder = os.path.join(desktop, "网页书签")

os.makedirs(img_folder, exist_ok=True)
os.makedirs(doc_folder, exist_ok=True)
os.makedirs(zip_folder, exist_ok=True)
os.makedirs(lnk_folder, exist_ok=True)
os.makedirs(exe_folder, exist_ok=True)
os.makedirs(url_folder, exist_ok=True)

img_suffix = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"}
doc_suffix = {".txt", ".md", ".docx", ".xlsx", ".pptx", ".pdf", ".csv"}
zip_suffix = {".zip", ".rar", ".7z", ".tar", ".gz"}
lnk_suffix = {".lnk"}
exe_suffix = {".exe", ".msi"}
url_suffix = {".url"}

unclassified = []

for filename in os.listdir(desktop):
    file_path = os.path.join(desktop, filename)
    if os.path.isfile(file_path):
        ext = os.path.splitext(filename)[1].lower()
        try:
            if ext in img_suffix:
                new_name = safe_move(file_path, img_folder, filename)
                print(f"移动图片：{filename} -> {new_name}")
            elif ext in doc_suffix:
                new_name = safe_move(file_path, doc_folder, filename)
                print(f"移动文档：{filename} -> {new_name}")
            elif ext in zip_suffix:
                new_name = safe_move(file_path, zip_folder, filename)
                print(f"移动压缩包：{filename} -> {new_name}")
            elif ext in lnk_suffix:
                new_name = safe_move(file_path, lnk_folder, filename)
                print(f"移动快捷方式：{filename} -> {new_name}")
            elif ext in exe_suffix:
                new_name = safe_move(file_path, exe_folder, filename)
                print(f"移动安装包：{filename} -> {new_name}")
            elif ext in url_suffix:
                new_name = safe_move(file_path, url_folder, filename)
                print(f"移动网页书签：{filename} -> {new_name}")
            else:
                unclassified.append(filename)
        except Exception:
            print(f"跳过占用文件：{filename}")

print("\n✅ 分类完成！")
if unclassified:
    print("\n📋 未归类，留在桌面：")
    for f in unclassified:
        print(f"  {f}")