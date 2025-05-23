# 🧠 AI Legal Consultant  
**Status**: 🚧 *In Development*  
> An AI-powered legal assistant designed to analyze and interpret Indian legal case documents.

---

## 📁 Project Structure


---

## 📊 Workflow Progress

### ✅ Data Collection & Preprocessing (Completed)

**Steps followed:**
1. 📄 **Collected** PDF case files from [kanon.org](https://kanon.org)
2. 🔁 **Converted** PDFs to plain text
3. 📦 **Transformed** text into raw JSON format
4. 🧹 **Cleaned** the raw JSON files (removal of noise, formatting issues, etc.)
5. 🏗️ **Structured** the cleaned data into a standardized JSON format for model training

All datasets are stored in the **`datasets/`** folder.

---

## 🔜 Upcoming Tasks

- Implement **word embeddings** using pre-trained or fine-tuned language models
- Train/validate legal document classifiers or retrieval systems
- Integrate backend with **GUI interface**
- Perform inference and testing

---

## 🛠 Tech Stack

- Python
- NLP: spaCy, NLTK, HuggingFace Transformers
- GUI: (e.g., Tkinter/Streamlit — update as applicable)
- JSON, Pandas
- Legal Data Source: [kanon.org](https://kanon.org)

---

## 📌 Disclaimer

This is an academic/personal research project and **not intended for real-world legal advice or services.**  
Always consult a qualified legal professional for legal matters.

---
