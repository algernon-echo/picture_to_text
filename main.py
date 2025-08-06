from PIL import Image
import pytesseract
import os

# 设置Tesseract路径（macOS通常不需要设置，但如果找不到可以取消注释下面这行）
# pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'

def extract_text_from_image(image_path, output_txt_path, language='chi_sim'):
    """
    从图像文件中提取文字并保存为TXT文件
    
    Args:
        image_path (str): 图像文件路径
        output_txt_path (str): 输出TXT文件路径
        language (str): 识别语言，默认为简体中文
                       'chi_sim' - 简体中文
                       'chi_tra' - 繁体中文
                       'eng' - 英文
                       'chi_sim+eng' - 中英文混合
    """
    try:
        # 检查图像文件是否存在
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"找不到文件: {image_path}")
        
        # 打开图像文件
        image = Image.open(image_path)
        
        # 使用pytesseract进行OCR识别
        print(f"正在识别 {language} 文字...")
        text = pytesseract.image_to_string(image, lang=language)
        
        # 去除多余的空白行
        lines = [line.strip() for line in text.split('\n') if line.strip()]
        cleaned_text = '\n'.join(lines)
        
        # 将提取的文字保存到TXT文件中
        with open(output_txt_path, 'w', encoding='utf-8') as f:
            f.write(cleaned_text)
        
        print(f"✅ 文字提取成功！")
        print(f"📄 输入文件: {image_path}")
        print(f"💾 输出文件: {output_txt_path}")
        print(f"📝 提取内容预览:")
        print("-" * 40)
        print(cleaned_text[:300] + "..." if len(cleaned_text) > 300 else cleaned_text)
        print("-" * 40)
        
        return cleaned_text
        
    except Exception as e:
        print(f"❌ 处理过程中出现错误: {e}")
        return None

def extract_text_with_preprocessing(image_path, output_txt_path, language='chi_sim'):
    """
    带预处理的OCR识别（提高识别率）
    """
    try:
        # 检查图像文件是否存在
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"找不到文件: {image_path}")
        
        # 打开图像文件
        image = Image.open(image_path)
        
        # 预处理图像
        print("正在进行图像预处理...")
        
        # 转换为灰度图
        image = image.convert('L')
        
        # 如果图像较小，进行放大
        if image.width < 300 or image.height < 300:
            image = image.resize((image.width * 2, image.height * 2), Image.Resampling.LANCZOS)
        
        # 使用pytesseract进行OCR识别
        print(f"正在识别 {language} 文字...")
        text = pytesseract.image_to_string(image, lang=language)
        
        # 去除多余的空白行
        lines = [line.strip() for line in text.split('\n') if line.strip()]
        cleaned_text = '\n'.join(lines)
        
        # 将提取的文字保存到TXT文件中
        with open(output_txt_path, 'w', encoding='utf-8') as f:
            f.write(cleaned_text)
        
        print(f"✅ 文字提取成功！")
        print(f"📄 输入文件: {image_path}")
        print(f"💾 输出文件: {output_txt_path}")
        print(f"📝 提取内容预览:")
        print("-" * 40)
        print(cleaned_text[:300] + "..." if len(cleaned_text) > 300 else cleaned_text)
        print("-" * 40)
        
        return cleaned_text
        
    except Exception as e:
        print(f"❌ 处理过程中出现错误: {e}")
        return None

if __name__ == "__main__":
    print("🔍 图像文字提取工具 (支持中文)")
    print("=" * 50)
    
    # 获取用户输入
    image_path = input("请输入PNG文件路径: ").strip()
    
    # 如果是相对路径，转换为绝对路径
    if not os.path.isabs(image_path):
        image_path = os.path.abspath(image_path)
    
    # 设置输出文件路径
    output_txt_path = os.path.splitext(image_path)[0] + '.txt'
    
    language = 'chi_sim'
    extract_text_from_image(image_path, output_txt_path, language)