# NLP701 – SemEval 2026 Task 13 (CodeBERT)

This repository contains code for training and evaluating a CodeBERT-based classifier for SemEval 2026 Task 13 (Subtask A).  
It includes:

- `train.py` — main training pipeline  
- `train_weightCE.py` — training with weighted cross-entropy  
- `predict.py` — inference on `.parquet` files  
- `huggingface.py` — upload trained model to Hugging Face Hub  

---

## 🔧 1. Installation

### Clone the repository
```bash
git clone https://github.com/cppmai1103/nlp_asm2.git
cd nlp_asm2

### Install dependencies
pip install -r requirements.txt
