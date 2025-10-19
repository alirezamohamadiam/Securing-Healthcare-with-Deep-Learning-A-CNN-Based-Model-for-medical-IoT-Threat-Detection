# 🏥 Securing Healthcare with Deep Learning
### A CNN-Based Model for Medical IoT Threat Detection

<div align="center">

[![IEEE Conference](https://img.shields.io/badge/IEEE-ICIS%202024-blue.svg)](https://doi.org/10.1109/ICIS64839.2024.10887510)
[![arXiv](https://img.shields.io/badge/arXiv-2410.23306-b31b1b.svg)](https://arxiv.org/abs/2410.23306)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Presentation](https://img.shields.io/badge/YouTube-Presentation-red.svg)](https://youtu.be/hPV5H9kTbYM?si=fWtb_eaIiLQ3uGEy)

*Official Implementation - Presented at the 19th Iranian Conference on Intelligent Systems (ICIS 2024)* **IEEE Indexed**

[**Paper (IEEE)**](https://doi.org/10.1109/ICIS64839.2024.10887510) | [**arXiv**](https://arxiv.org/abs/2410.23306) | [**Presentation**](https://youtu.be/hPV5H9kTbYM?si=fWtb_eaIiLQ3uGEy) | [**Dataset**](https://www.unb.ca/cic/datasets/iomt-dataset-2024.html)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Achievements](#-achievements)
- [Performance Metrics](#-performance-metrics)
- [Model Architecture](#-model-architecture)
- [Installation](#-installation)
- [Data Preparation](#-data-preparation)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Citation](#-citation)
---

## 🔬 Overview

This repository contains the implementation of our CNN-based intrusion detection model for Internet of Medical Things (IoMT) systems. The model performs multi-class classification on network traffic to distinguish between **19 attack types** and benign traffic, based on the **CICIoMT2024 dataset**.

**Key Features:**
- Multi-classification support: Binary (2-class), Categorical (6-class), and Multiclass (19-class)
- Perfect accuracy of 0.99 across all classification tasks
- Outperforms previous state-of-the-art methods
- Optimized for IoMT network security

---

## 🏆 Achievements

✅ **Perfect Performance**: The proposed model achieved an accuracy of **0.99** across binary, categorical, and multiclass classification tasks

✅ **State-of-the-Art**: Outperforms previous state-of-the-art methods in IoMT threat detection

✅ **Comprehensive Coverage**: Detects 19 different attack types plus benign traffic

---

## 📊 Performance Metrics

| Model Classification Task | Accuracy | Precision | Recall | F1-Score |
|---------------------------|:--------:|:---------:|:------:|:--------:|
| **Proposed Model (19 Class)** | 0.99 | 0.98 | 0.99 | 0.98 |
| **Proposed Model (2 Class)**  | 0.99 | 0.99 | 0.99 | 0.99 |
| **Proposed Model (6 Class)**  | 0.99 | 0.99 | 0.99 | 0.99 |

<div align="center">

![Model Comparison](https://github.com/user-attachments/assets/7dc2bd46-c2ea-49cb-b94f-7ee42b268d56)

*Performance comparison across different classification tasks*

</div>

---

## 🧠 Model Architecture

<div align="center">

![CNN Architecture](https://github.com/user-attachments/assets/e76e8cb4-a185-4726-abcb-b50482786088)

*Architecture of the CNN model for IoMT attack classification*

</div>

---

## 🚀 Quick Start

### Step 1: Clone Repository
```bash
git clone https://github.com/yourusername/iomt-cnn-threat-detection.git
cd iomt-cnn-threat-detection
```

### Step 2: Install Requirements
```bash
pip install -r requirements.txt
```
> **Note:** Python 3.7+ is required

### Step 3: Download Dataset
Download the **CIC IoMT Dataset 2024** from:  
🔗 [https://www.unb.ca/cic/datasets/iomt-dataset-2024.html](https://www.unb.ca/cic/datasets/iomt-dataset-2024.html)

### Step 4: Prepare Data
Place the CSV files in the data directories:
```
data/
├── train/     ← Put training CSV files here
└── test/      ← Put testing CSV files here
```
> **Detailed instructions:** See [`README_DATA.md`](https://github.com/alirezamohamadiam/Securing-Healthcare-with-Deep-Learning-A-CNN-Based-Model-for-medical-IoT-Threat-Detection/blob/main/README_DATA.md)

### Step 5: Run Training
To run the model, execute `main.py` and specify the classification configuration:
```bash
python main.py --class_config <num_classes>
```

Replace `<num_classes>` with:
- **2** for binary classification,
- **6** for categorical,
- **19** for multiclass.

**Example (binary classification):**
```bash
python main.py --class_config 2
```
---

## 💻 Usage Examples

### Binary Classification (Benign vs Attack)
```bash
cd src
python main.py --class_config 2
```

### Categorical Classification (6 Attack Categories)
```bash
cd src
python main.py --class_config 6
```

### Multiclass Classification (19 Attack Types)
```bash
cd src
python main.py --class_config 19
```

| Configuration | Description |
|:-------------:|:------------|
| `--class_config 2` | Binary: Benign vs Attack |
| `--class_config 6` | Categorical: 6 attack categories |
| `--class_config 19` | Multiclass: 19 specific attack types |

---

## 📂 Project Structure

```
project/
├── data/
│   ├── train/            # Training CSV files (see README_DATA.md)
│   └── test/             # Testing CSV files (see README_DATA.md)
├── src/
│   ├── data_loader.py    # Data loading and preprocessing
│   ├── model.py          # CNN model definition and training
│   └── main.py           # Main execution script
├── requirements.txt      # Project dependencies
├── README.md             # Project documentation (this file)
└── README_DATA.md        # Data preparation guide
```

### Code Overview

- **`data_loader.py`**: Manages data loading, preprocessing, and splitting into training/testing sets
- **`model.py`**: Defines the CNN architecture, including layers optimized for network traffic data
- **`main.py`**: Executes training and evaluation processes based on specified configuration

---

## 📚 Citation

If you use this code or find our work helpful, please cite our paper:
```bibtex
@inproceedings{mohammadi2024securing,
  title={Securing Healthcare with Deep Learning: A CNN-Based Model for medical IoT Threat Detection},
  author={Mohammadi, Alireza and Ghahramani, Hosna and Asghari, Seyyed Amir and Aminian, Mehdi},
  booktitle={2024 19th Iranian Conference on Intelligent Systems (ICIS)},
  pages={168--173},
  year={2024},
  organization={IEEE}
}
```
**Plain Text Citation:**
```
Mohammadi, A., Ghahramani, H., Asghari, S. A., & Aminian, M. (2024). 
Securing healthcare with deep learning: A CNN-based model for medical IoT threat detection. 
In 2024 19th Iranian Conference on Intelligent Systems (ICIS) (pp. 168-173). IEEE. 
https://doi.org/10.1109/ICIS64839.2024.10887510
```

**Links:**
- 📄 **IEEE Xplore**: [DOI: 10.1109/ICIS64839.2024.10887510](https://doi.org/10.1109/ICIS64839.2024.10887510)
- 📄 **arXiv**: [arXiv:2410.23306](https://arxiv.org/abs/2410.23306)

---

<div align="center">

**⭐ If you find this work useful, please consider giving it a star! ⭐**

Made with ❤️ by Alireza Mohamadi

</div>




