import os
import json
import re

# Directory containing your JSON files
input_dir = 'json_cases'
output_dir = 'cleaned_json_cases'
os.makedirs(output_dir, exist_ok=True)

def clean_text(text):
    if not text:
        return text
    text = re.sub(r'\bPage\s+\d+\s+of\s+\d+\b', '', text, flags=re.IGNORECASE)
    text = re.sub(r'\s+', ' ', text).strip()
    text = text[0].upper() + text[1:] if text else text
    text = re.sub(r'\s+([.,;!?])', r'\1', text)
    return text

def process_file(filepath, output_path):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Clean judgment_summary and full_text
    if 'judgment_summary' in data and isinstance(data['judgment_summary'], str):
        data['judgment_summary'] = clean_text(data['judgment_summary'])

    if 'full_text' in data and isinstance(data['full_text'], str):
        data['full_text'] = clean_text(data['full_text'])

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# Process all JSON files
for filename in os.listdir(input_dir):
    if filename.endswith('.json'):
        in_path = os.path.join(input_dir, filename)
        out_path = os.path.join(output_dir, filename)
        process_file(in_path, out_path)

print("✅ Cleaning complete. Output saved in 'cleaned_json_cases'")
