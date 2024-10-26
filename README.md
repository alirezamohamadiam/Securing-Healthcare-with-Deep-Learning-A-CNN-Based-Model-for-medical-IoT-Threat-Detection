# Advanced Cyberattack Detection in Internet of Medical Things (IoMT) Using Convolutional Neural Networks

Welcome to the repository accompanying our paper, "Advanced Cyberattack Detection in Internet of Medical Things (IoMT) Using Convolutional Neural Networks." This work was presented at the 2024 19th Iranian Conference on Intelligent Systems (ICIS) held from October 23-24, 2024, at Sirjan University of Technology in Sirjan, Kerman, Iran.

## Achievements and Contributions

The proposed model achieved a perfect accuracy of 0.99 across binary, categorical, and multiclass classification tasks, outperforming previous state-of-the-art methods. This code was developed for a paper accepted at the 2024 IEEE Conference on Intelligent Systems (ICIS).

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
![fcn8_page-0001 (2)](https://github.com/user-attachments/assets/a3fcd742-4e0b-469f-9e07-72b02447cff3)
Architecture of the CNN model for IoMT attack classification

## Getting Started

### 1. Prerequisites

- **Python 3.7+**
- **Required Libraries:** Install dependencies by running:
   ```bash
   pip install -r requirements.txt
   ```

### 2. Data Preparation

**Dataset:**  
Download the "CIC IoMT dataset 2024" dataset in CSV format from [here](https://www.unb.ca/cic/datasets/iomt-dataset-2024.html).

After downloading, extract and place the CSV files in the appropriate directories (`data/train/` and `data/test/`).

### 3. Training and Evaluation

Navigate to the `src` directory:
```bash
cd src
```

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

### Code Overview

- **data_loader.py**: Manages data loading, preprocessing, and splitting into training/testing sets.
- **model.py**: Defines the CNN architecture, including layers optimized for network traffic data.
- **main.py**: Executes training and evaluation processes based on specified configuration.

## Citation

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
