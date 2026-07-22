import os
import re

vault_dir = r"d:\Antigravity\love myself\.temp_learning_vault"
skill_dir = r"d:\Antigravity\love myself\.agents\skills\deep-learning"

cross_links_data = {
    "01-viva-women-buoi-1-tu-luc-canh-sinh.md": """### 3.3. Liên Kết Tri Thức Với Các Bài Học Khác Trong Tủ Sách

- Bài học liên quan 1: Tham khảo [02-viva-women-buoi-2-suc-manh-hien-dien.md](02-viva-women-buoi-2-suc-manh-hien-dien.md) để nâng cấp từ "Tự lực cánh sinh" lên "Sức mạnh hiện diện & Đạo của nước".
- Bài học liên quan 2: Tham khảo [04-perma-co-tho-buoi-1-ton-thuong-tuoi-tho.md](04-perma-co-tho-buoi-1-ton-thuong-tuoi-tho.md) để thấu hiểu gốc rễ tổn thương tuổi thơ ảnh hưởng đến cơ chế tự vệ trong công việc hiện tại.
- Bài học liên quan 3: Tham khảo [07-hoc-tieng-anh-25-phut.md](07-hoc-tieng-anh-25-phut.md) để áp dụng tư duy "Nhớ quy trình, không nhớ việc" vào xây dựng thói quen tự học hàng ngày.""",

    "02-viva-women-buoi-2-suc-manh-hien-dien.md": """### 3.3. Liên Kết Tri Thức Với Các Bài Học Khác Trong Tủ Sách

- Bài học liên quan 1: Tham khảo [01-viva-women-buoi-1-tu-luc-canh-sinh.md](01-viva-women-buoi-1-tu-luc-canh-sinh.md) để nắm vững nền tảng tư duy Tự chịu trách nhiệm 100% trước khi thực hành Tĩnh an.
- Bài học liên quan 2: Tham khảo [05-perma-co-tho-buoi-2-phan-ung-sinh-ton.md](05-perma-co-tho-buoi-2-phan-ung-sinh-ton.md) để nhận diện các phản ứng sinh tồn (Fight, Flight, Freeze, Fawn) khi tâm trí bị xáo động.
- Bài học liên quan 3: Tham khảo [03-viva-women-buoi-3-hanh-trinh-tim-minh.md](03-viva-women-buoi-3-hanh-trinh-tim-minh.md) để đưa sự hiện diện vào xây dựng Ngôi nhà nội lực 5 trụ cột.""",

    "03-viva-women-buoi-3-hanh-trinh-tim-minh.md": """### 3.3. Liên Kết Tri Thức Với Các Bài Học Khác Trong Tủ Sách

- Bài học liên quan 1: Tham khảo [02-viva-women-buoi-2-suc-manh-hien-dien.md](02-viva-women-buoi-2-suc-manh-hien-dien.md) để rèn luyện chất giọng an tĩnh xuất phát từ sự hiện diện nội tại.
- Bài học liên quan 2: Tham khảo [06-perma-co-tho-buoi-3-sang-chan-nghien-cam-xuc.md](06-perma-co-tho-buoi-3-sang-chan-nghien-cam-xuc.md) để tháo gỡ các nghiện cảm xúc tiêu cực đang cản trở trụ cột Tâm an.
- Bài học liên quan 3: Tham khảo [01-viva-women-buoi-1-tu-luc-canh-sinh.md](01-viva-women-buoi-1-tu-luc-canh-sinh.md) để củng cố tư tưởng xây dựng mối quan hệ là tài sản thực sự.""",

    "04-perma-co-tho-buoi-1-ton-thuong-tuoi-tho.md": """### 3.3. Liên Kết Tri Thức Với Các Bài Học Khác Trong Tủ Sách

- Bài học liên quan 1: Tham khảo [05-perma-co-tho-buoi-2-phan-ung-sinh-ton.md](05-perma-co-tho-buoi-2-phan-ung-sinh-ton.md) để nhận diện cách tổn thương tuổi thơ chuyển hóa thành các phản ứng tự vệ trong hiện tại.
- Bài học liên quan 2: Tham khảo [01-viva-women-buoi-1-tu-luc-canh-sinh.md](01-viva-women-buoi-1-tu-luc-canh-sinh.md) để chuyển hóa tư duy từ nạn nhân sang tự lực cánh sinh.
- Bài học liên quan 3: Tham khảo [06-perma-co-tho-buoi-3-sang-chan-nghien-cam-xuc.md](06-perma-co-tho-buoi-3-sang-chan-nghien-cam-xuc.md) để chữa lành em bé bên trong khỏi các vòng lặp nghiện cảm xúc.""",

    "05-perma-co-tho-buoi-2-phan-ung-sinh-ton.md": """### 3.3. Liên Kết Tri Thức Với Các Bài Học Khác Trong Tủ Sách

- Bài học liên quan 1: Tham khảo [04-perma-co-tho-buoi-1-ton-thuong-tuoi-tho.md](04-perma-co-tho-buoi-1-ton-thuong-tuoi-tho.md) để hiểu nguồn gốc của các cơ chế phản ứng sinh tồn.
- Bài học liên quan 2: Tham khảo [02-viva-women-buoi-2-suc-manh-hien-dien.md](02-viva-women-buoi-2-suc-manh-hien-dien.md) để áp dụng triết lý "Đạo của nước" giúp giải phóng sự gồng mình tự vệ.
- Bài học liên quan 3: Tham khảo [06-perma-co-tho-buoi-3-sang-chan-nghien-cam-xuc.md](06-perma-co-tho-buoi-3-sang-chan-nghien-cam-xuc.md) để bứt phá khỏi vòng lặp tiềm thức.""",

    "06-perma-co-tho-buoi-3-sang-chan-nghien-cam-xuc.md": """### 3.3. Liên Kết Tri Thức Với Các Bài Học Khác Trong Tủ Sách

- Bài học liên quan 1: Tham khảo [05-perma-co-tho-buoi-2-phan-ung-sinh-ton.md](05-perma-co-tho-buoi-2-phan-ung-sinh-ton.md) để đối chiếu cách tiềm thức tìm kiếm cảm xúc quen thuộc.
- Bài học liên quan 2: Tham khảo [03-viva-women-buoi-3-hanh-trinh-tim-minh.md](03-viva-women-buoi-3-hanh-trinh-tim-minh.md) để định hình nhân dạng mới tĩnh an trong Ngôi nhà 5 trụ cột.
- Bài học liên quan 3: Tham khảo [04-perma-co-tho-buoi-1-ton-thuong-tuoi-tho.md](04-perma-co-tho-buoi-1-ton-thuong-tuoi-tho.md) để hoàn tất chuỗi 3 buổi chữa lành Perma.""",

    "07-hoc-tieng-anh-25-phut.md": """### 3.3. Liên Kết Tri Thức Với Các Bài Học Khác Trong Tủ Sách

- Bài học liên quan 1: Tham khảo [01-viva-women-buoi-1-tu-luc-canh-sinh.md](01-viva-women-buoi-1-tu-luc-canh-sinh.md) để áp dụng tính kỷ luật tự học không chờ đợi hoàn cảnh.
- Bài học liên quan 2: Tham khảo [02-viva-women-buoi-2-suc-manh-hien-dien.md](02-viva-women-buoi-2-suc-manh-hien-dien.md) để duy trì sự tập trung trọn vẹn trong 25 phút học mỗi ngày.
- Bài học liên quan 3: Tham khảo [03-viva-women-buoi-3-hanh-trinh-tim-minh.md](03-viva-women-buoi-3-hanh-trinh-tim-minh.md) để nâng cấp kỹ năng ngôn ngữ cho trụ cột Phát triển bản thân."""
}

def clean_and_fix_table_lines(text):
    # Regex to catch table rows smashed into one line with ||
    lines = text.split('\n')
    new_lines = []
    
    for line in lines:
        if '||' in line:
            # Split smashed table row by ||
            parts = line.split('||')
            for p in parts:
                p_str = p.strip()
                if p_str:
                    if not p_str.startswith('|'):
                        p_str = '| ' + p_str
                    if not p_str.endswith('|'):
                        p_str = p_str + ' |'
                    new_lines.append(p_str)
        else:
            new_lines.append(line)
            
    res = '\n'.join(new_lines)
    
    # Fix any table separator line syntax
    res = re.sub(r'\|\s*:\s*---\s*\|', '| :--- |', res)
    res = re.sub(r'\|\s*:\s*---:\s*\|', '| :---: |', res)
    
    return res

def process_vault_files():
    for filename, cross_link_text in cross_links_data.items():
        fp = os.path.join(vault_dir, filename)
        if not os.path.exists(fp):
            continue
            
        with open(fp, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Fix smashed tables
        content = clean_and_fix_table_lines(content)
        
        # Replace Section 3.3 with clear cross-links
        if "### 3.3. Phân Loại Và Lưu Trữ Tri Thức" in content:
            parts = content.split("### 3.3. Phân Loại Và Lưu Trữ Tri Thức")
            # Find end of section 3.3 before 3.4
            sub_parts = parts[1].split("### 3.4. Bộ Câu Hỏi Phản Tư Nội Tâm")
            content = parts[0] + cross_link_text + "\n\n### 3.4. Bộ Câu Hỏi Phản Tư Nội Tâm" + sub_parts[1]
            
        with open(fp, "w", encoding="utf-8") as f:
            f.write(content)

process_vault_files()
print("FIX TABLES AND CROSSLINKS SUCCESSFUL")
