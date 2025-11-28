<img width="278" height="77" alt="image" src="https://github.com/user-attachments/assets/38d2b75d-efe9-4ea1-aa57-df9399f25c98" /># NLP701 – SemEval 2026 Task 13

This repository contains code for training and evaluating a CodeBERT-based classifier for SemEval 2026 Task 13 (Subtask B).  
It includes:

- `train.py` — main training pipeline  
- `train_weightCE.py` — training with weighted cross-entropy  
- `predict.py` — inference on \`.parquet\` files  
- `huggingface.py` — upload trained model to Hugging Face Hub  

---

## 🔧 1. Installation

### Clone the repository
```bash
git clone https://github.com/cppmai1103/nlp_asm2.git
cd nlp_asm2
```

### (Optional) Create a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate       # Linux/Mac
# .venv\Scripts\activate        # Windows
```

### Install dependencies
```bash
pip install -r requirements.txt
```

---

## 📚 2. Dataset Format

Training and inference scripts expect a \`.parquet\` file with at least:

- `code` — source code snippet  
- `label` — class label (integer)  
- Optional for inference: `ID`

Example:

| ID  | code                          | label |
|-----|-------------------------------|-------|
| 12  | \`def add(a, b): return a+b\` | 0     |
| 87  | \`public static void main...\`| 1     |

If no parquet is provided, \`train.py\` loads the SemEval dataset automatically.

---

## 🏋️‍♀️ 3. Training

### Basic usage
```bash
python train.py
```

### Advanced usage
```bash
python train.py \
  --task A \
  --output_dir ./results_undersampling \
  --epochs 3 \
  --batch_size 32 \
  --learning_rate 2e-5 \
  --max_length 128
```

Arguments:

| Argument | Default | Description |
|----------|---------|-------------|
| \`--task\` | A | SemEval subset |
| \`--output_dir\` | ./results_undersampling | Output folder |
| \`--epochs\` | 1 | Number of epochs |
| \`--batch_size\` | 32 | Batch size |
| \`--learning_rate\` | 2e-5 | Learning rate |
| \`--max_length\` | 128 | Max token length |

---

## ⚖️ 4. Weighted Cross Entropy Training

```bash
python train_weightCE.py \
  --output_dir ./results_weighted \
  --epochs 3 \
  --batch_size 32 \
  --learning_rate 2e-5
```

---

## 🔎 5. Inference

```bash
python predict.py \
  --model_path ./results_undersampling \
  --parquet_path test.parquet \
  --output_path predictions.csv
```

Output CSV format:

```
ID,prediction
101,0
102,1
```

---

## ☁️ 6. Upload to Hugging Face

1. Log in:
```bash
huggingface-cli login
```

2. Upload:
```bash
python huggingface.py \
  --model_dir ./results_undersampling \
  --repo_id your-username/your-model-name
```

---

## 📁 7. Repository Structure

```
nlp_asm2/
├── train.py
├── train_weightCE.py
├── predict.py
├── huggingface.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 📝 Notes

- Large files (.parquet, .bin, .pt) are ignored via .gitignore  
- Base model: \`microsoft/codebert-base\`  

---

## 📄 License

This project is part of NLP701 coursework.  
Feel free to reuse with attribution.
EOF

### Clone the repository
```bash
git clone https://github.com/cppmai1103/nlp_asm2.git
cd nlp_asm2

### Install dependencies
pip install -r requirements.txt
