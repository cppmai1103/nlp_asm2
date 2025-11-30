# NLP701 – Assignment 2: Detecting AI-Generated Code

This repository contains code for training and evaluating models for **SemEval 2026 Task 13 (Subtask B)** using CodeBERT and UniXcoder. 

Learderboard team name: `cppmai`

## 1. Install dependencies
```bash
pip install -r requirements.txt
```

---

## 2. Dataset undersampling
Create an undersampled dataset where the number of Human samples equals the total number of LLM-generated samples.
```bash
python src/data_undersampling.py \
  --input data/train.parquet \
  --output data/train_undersampling.parquet
```

## 3. Training 

### Original training set 
Finetune CodeBERT
```bash
python src/train.py \
  --output_dir result_codebert \
  --model_name microsoft/codebert-base
```

Finetune UniXcoder
```bash
python src/train.py \
  --output_dir result_unixcoder \
  --model_name microsoft/unixcoder-base
```

### Undersampled training set
Finetune CodeBERT
```bash
python src/train.py \
  --output_dir result_codebert_undersampling \
  --model_name microsoft/codebert-base \
  --parquet_path data/train_undersampling.parquet
```

Finetune UniXcoder
```bash
python src/train.py \
  --output_dir result_unixcoder_undersampling \
  --model_name microsoft/unixcoder-base \
  --parquet_path data/train_undersampling.parquet
```
---

## 4. Predicting on TEST set
```bash
python predict.py \
  --model_path ./result_codebert \
  --parquet_path data/test.parquet \
  --output_path submission.csv
```
---

## 5. Repository Structure
```
nlp_asm2/
├── src/
│   ├── train.py
│   ├── data_undersampling.py
│   ├── predict.py
├── data/
│   ├── train.parquet
│   ├── test.parquet
├── requirements.txt
└── README.md
```
