import re
import json
import os

def clean_text(text):
    text = re.sub(r'Indian Kanoon - http.*?\n', '', text)
    text = re.sub(r'\n\d+\n', '\n', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def extract_info(text):
    case_name = None
    date = None
    lines = text.splitlines()
    for line in lines[:10]:
        m = re.search(r'(.+?)\s+v[\.s]*\s+(.+?)\s+on\s+(.+)', line, re.IGNORECASE)
        if m:
            case_name = f"{m.group(1).strip()} vs {m.group(2).strip()}"
            date = m.group(3).strip()
            break
        m2 = re.search(r'Date of Decision[:\-]?\s*(.+)', line, re.IGNORECASE)
        if m2:
            date = m2.group(1).strip()
    if not date:
        m = re.search(r'Date of Decision[:\-]?\s*(.+)', text, re.IGNORECASE)
        if m:
            date = m.group(1).strip()
    author = None
    bench = None
    for line in lines[:20]:
        m = re.search(r'Author[:\-]?\s*(.+)', line, re.IGNORECASE)
        if m:
            author = m.group(1).strip()
        m2 = re.search(r'Bench[:\-]?\s*(.+)', line, re.IGNORECASE)
        if m2:
            bench = m2.group(1).strip()
    petitioner = None
    respondent = None
    for i, line in enumerate(lines[:30]):
        if re.search(r'Petition(er)?', line, re.IGNORECASE):
            petitioner = lines[i-1].strip() if i > 0 else None
        if re.search(r'Responden(t)?', line, re.IGNORECASE):
            respondent = lines[i-1].strip() if i > 0 else None
    judgment_summary = None
    summary_candidates = re.findall(r'([^.]*?(ordered|allowed|dismissed|granted|rejected|costs)[^.]*\.)', text, re.IGNORECASE)
    if summary_candidates:
        judgment_summary = summary_candidates[-1][0].strip()
    return {
        "case_name": case_name,
        "date": date,
        "author": author,
        "bench": bench,
        "petitioner": petitioner,
        "respondent": respondent,
        "judgment_summary": judgment_summary
    }

def process_file(input_path, output_path):
    with open(input_path, encoding='utf-8') as f:
        raw_text = f.read()
    cleaned = clean_text(raw_text)
    info = extract_info(raw_text)
    info['full_text'] = cleaned
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(info, f, indent=2, ensure_ascii=False)
    print(f"Processed and saved to {output_path}")

if __name__ == "__main__":
    input_dir = r"C:\Users\HP\OneDrive\Desktop\dataset for project consumer protection\NLTk\extracted_txt"
    output_dir = r"C:\Users\HP\OneDrive\Desktop\dataset for project consumer protection\NLTk\json_cases"
    os.makedirs(output_dir, exist_ok=True)
    for filename in os.listdir(input_dir):
        if filename.lower().endswith('.txt'):
            input_path = os.path.join(input_dir, filename)
            output_filename = os.path.splitext(filename)[0] + ".json"
            output_path = os.path.join(output_dir, output_filename)
            process_file(input_path, output_path)