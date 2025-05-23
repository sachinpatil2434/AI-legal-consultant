import os
import json
import re

def extract_sections(text):
    sections = ['FACTS', 'ARGUMENTS', 'ANALYSIS', 'DECISION']
    extracted = {}

    pattern = '|'.join(f'(?P<{sec}>{sec}:)' for sec in sections)
    matches = list(re.finditer(pattern, text))

    for i, match in enumerate(matches):
        section = match.lastgroup
        start = match.end()
        end = matches[i+1].start() if i + 1 < len(matches) else len(text)
        extracted[section] = text[start:end].strip()

    return extracted

# 📁 Path to the folder with cleaned JSON files
input_folder = "cleaned_jsons"
output_folder = "structured_jsons"
os.makedirs(output_folder, exist_ok=True)

# 🔁 Process all JSON files in the folder
for filename in os.listdir(r"C:\\Users\\HP\\OneDrive\\Desktop\\dataset for project consumer protection\\NLTk\\cleaned_json_cases"):
    if filename.endswith(".json"):
        input_path = os.path.join(r"C:\\Users\\HP\\OneDrive\\Desktop\\dataset for project consumer protection\\NLTk\\cleaned_json_cases", filename)
        with open(input_path, "r", encoding="utf-8") as file:
            case_data = json.load(file)
            full_text = case_data.get("cleaned_text", "")

        structured = extract_sections(full_text)

        # Save result
        output_path = os.path.join(output_folder, filename)
        with open(output_path, "w", encoding="utf-8") as out:
            json.dump(structured, out, indent=4)

        print(f"✅ Processed: {filename}")
