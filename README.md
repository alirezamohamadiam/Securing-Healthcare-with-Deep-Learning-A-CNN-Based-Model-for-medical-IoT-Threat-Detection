# Advanced Cyberattack Detection in Internet of Medical Things (IoMT) Using Convolutional Neural Networks

Welcome to the repository accompanying our paper, "Advanced Cyberattack Detection in Internet of Medical Things (IoMT) Using Convolutional Neural Networks." This work was presented at the 2024 19th Iranian Conference on Intelligent Systems (ICIS) held from October 23-24, 2024, at Sirjan University of Technology in Sirjan, Kerman, Iran.

## Abstract

The integration of the Internet of Medical Things (IoMT) has brought unprecedented benefits to healthcare, enhancing patient care through seamless connectivity. However, this connectivity introduces critical security vulnerabilities that must be addressed to safeguard these systems. Our paper introduces a CNN-based approach to detect cyberattacks within IoMT environments, specifically designed to analyze the temporal characteristics of network traffic. Evaluated on the CICIoMT2024 dataset, which includes 18 unique attack types targeting IoMT devices, our model achieves 99% accuracy across binary, categorical, and multiclass classification tasks. This surpasses the performance of established models such as Logistic Regression, AdaBoost, DNNs, and Random Forests, underscoring CNNs' potential to enhance IoMT cybersecurity.

## Code Developer

Alireza Mohammadi (Department of Computer Engineering, Islamic Azad University - Kermanshah Branch, Kermanshah, Iran) 

## Project Overview

This repository includes the code and setup instructions for implementing our proposed CNN-based intrusion detection model for IoMT systems. The model performs multi-class classification on network traffic to distinguish between 19 attack types and benign traffic, based on the CICIoMT2024 dataset.

### Model Performance Metrics

| Model Classification Task | Accuracy | Precision | Recall | F1-Score |
|---------------------------|----------|-----------|--------|----------|
| Proposed Model (19 Class) | 0.99     | 0.98      | 0.99   | 0.98     |
| Proposed Model (2 Class)  | 0.99     | 0.99      | 0.99   | 0.99     |
| Proposed Model (6 Class)  | 0.99     | 0.99      | 0.99   | 0.99     |

![model_comparison_subplots_barchart_improved](https://github.com/user-attachments/assets/7dc2bd46-c2ea-49cb-b94f-7ee42b268d56)

## Dataset

Download the "CIC IoMT dataset 2024" dataset in CSV format from [here](https://www.unb.ca/cic/datasets/iomt-dataset-2024.html).

After downloading, extract and place the CSV files in the appropriate directories (`data/train/` and `data/test/`).

### Project Structure

```markdown
project/
├── data/
│   ├── train/ # Place training CSV files here (details in README_DATA.md)
│   └── test/  # Place testing CSV files here (details in README_DATA.md)
├── src/
│   ├── data_loader.py    # Handles data loading and preprocessing
│   ├── model.py          # Defines and trains the CNN model
│   └── main.py           # Main script to execute model training and evaluation
├── requirements.txt      # Project dependencies
└── README.md             # Project description (this file)
└── README_DATA.md        # Data Preparation Guide
```

For more information on organizing and preparing the `train` and `test` data files, please refer to the [Data Preparation Guide](README_DATA.md).

### Citation

If you find this work useful for your research, please cite:

```plaintext
@conference{ICIS2024,
  author = {Mohammadi, Alireza and Aminian, Mehdi and Ghahramani, Hosna and Asghari, Seyyed Amir},
  title = {Advanced Cyberattack Detection in Internet of Medical Things (IoMT) Using Convolutional Neural Networks},
  booktitle = {2024 19th Iranian Conference on Intelligent Systems (ICIS)},
  year = {2024},
  organization = {Sirjan University of Technology},
  address = {Sirjan, Kerman, Iran},
  month = {October 23-24}
}
```

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
