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

### Project Structure

```markdown
project/
├── data/
│   ├── train/ # Place training CSV files here (list below)
│   └── test/  # Place testing CSV files here (list below)
├── src/
│   ├── data_loader.py    # Handles data loading and preprocessing
│   ├── model.py          # Defines and trains the CNN model
│   └── main.py           # Main script to execute model training and evaluation
├── requirements.txt      # Project dependencies
└── README.md             # Project description (this file)
```

## Getting Started

### 1. Prerequisites

- **Python 3.7+**
- **Required Libraries:** Install dependencies by running:
   ```bash
   pip install -r requirements.txt
   ```

### 2. Data Preparation

**Dataset:**  
Download the "IoMT-Traffic-Traces-2024" dataset in CSV format from [here](https://www.unb.ca/cic/datasets/iomt-dataset-2024.html).

**Directory Setup:**  
Within the `data/` directory, create `train/` and `test/` folders to hold the CSV files for training and testing, respectively.

**Populate the Directories:**  
Place the following files in the respective directories after extracting them from the downloaded dataset:

**Training Data (data/train):**
- ARP_Spoofing_train.pcap.csv
- Benign_train.pcap.csv
- MQTT-DDoS-Connect_Flood_train.pcap.csv
- MQTT-DDoS-Publish_Flood_train.pcap.csv
- MQTT-DoS-Connect_Flood_train.pcap.csv
- MQTT-DoS-Publish_Flood_train.pcap.csv
- MQTT-Malformed_Data_train.pcap.csv
- Recon-OS_Scan_train.pcap.csv
- Recon-Ping_Sweep_train.pcap.csv
- Recon-Port_Scan_train.pcap.csv
- Recon-VulScan_train.pcap.csv
- TCP_IP-DDoS-ICMP1_train.pcap.csv
- TCP_IP-DDoS-ICMP2_train.pcap.csv
- TCP_IP-DDoS-ICMP3_train.pcap.csv
- TCP_IP-DDoS-ICMP4_train.pcap.csv
- TCP_IP-DDoS-ICMP5_train.pcap.csv
- TCP_IP-DDoS-ICMP6_train.pcap.csv
- TCP_IP-DDoS-ICMP7_train.pcap.csv
- TCP_IP-DDoS-ICMP8_train.pcap.csv
- TCP_IP-DDoS-SYN1_train.pcap.csv
- TCP_IP-DDoS-SYN2_train.pcap.csv
- TCP_IP-DDoS-SYN3_train.pcap.csv
- TCP_IP-DDoS-SYN4_train.pcap.csv
- TCP_IP-DDoS-TCP1_train.pcap.csv
- TCP_IP-DDoS-TCP2_train.pcap.csv
- TCP_IP-DDoS-TCP3_train.pcap.csv
- TCP_IP-DDoS-TCP4_train.pcap.csv
- TCP_IP-DDoS-UDP1_train.pcap.csv
- TCP_IP-DDoS-UDP2_train.pcap.csv
- TCP_IP-DDoS-UDP3_train.pcap.csv
- TCP_IP-DDoS-UDP4_train.pcap.csv
- TCP_IP-DDoS-UDP5_train.pcap.csv
- TCP_IP-DDoS-UDP6_train.pcap.csv
- TCP_IP-DDoS-UDP7_train.pcap.csv
- TCP_IP-DDoS-UDP8_train.pcap.csv
- TCP_IP-DoS-ICMP1_train.pcap.csv
- TCP_IP-DoS-ICMP2_train.pcap.csv
- TCP_IP-DoS-ICMP3_train.pcap.csv
- TCP_IP-DoS-ICMP4_train.pcap.csv
- TCP_IP-DoS-SYN1_train.pcap.csv
- TCP_IP-DoS-SYN2_train.pcap.csv
- TCP_IP-DoS-SYN3_train.pcap.csv
- TCP_IP-DoS-SYN4_train.pcap.csv
- TCP_IP-DoS-TCP1_train.pcap.csv
- TCP_IP-DoS-TCP2_train.pcap.csv
- TCP_IP-DoS-TCP3_train.pcap.csv
- TCP_IP-DoS-TCP4_train.pcap.csv
- TCP_IP-DoS-UDP1_train.pcap.csv
- TCP_IP-DoS-UDP2_train.pcap.csv
- TCP_IP-DoS-UDP3_train.pcap.csv
- TCP_IP-DoS-UDP4_train.pcap.csv

**Testing Data (data/test):**
- ARP_Spoofing_test.pcap.csv
- Benign_test.pcap.csv
- MQTT-DDoS-Connect_Flood_test.pcap.csv
- MQTT-DDoS-Publish_Flood_test.pcap.csv
- MQTT-DoS-Connect_Flood_test.pcap.csv
- MQTT-DoS-Publish_Flood_test.pcap.csv
- MQTT-Malformed_Data_test.pcap.csv
- Recon-OS_Scan_test.pcap.csv
- Recon-Ping_Sweep_test.pcap.csv
- Recon-Port_Scan_test.pcap.csv
- Recon-VulScan_test.pcap.csv
- TCP_IP-DDoS-ICMP1_test.pcap.csv
- TCP_IP-DDoS-ICMP2_test.pcap.csv
- TCP_IP-DDoS-SYN_test.pcap.csv
- TCP_IP-DDoS-TCP_test.pcap.csv
- TCP_IP-DDoS-UDP1_test.pcap.csv
- TCP_IP-DDoS-UDP2_test.pcap.csv
- TCP_IP-DoS-ICMP_test.pcap.csv
- TCP_IP-DoS-SYN_test.pcap.csv
- TCP_IP-DoS-TCP_test.pcap.csv
- TCP_IP-DoS-UDP_test.pcap.csv

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
