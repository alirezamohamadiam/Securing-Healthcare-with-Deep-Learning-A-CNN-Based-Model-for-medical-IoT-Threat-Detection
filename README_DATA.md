```markdown
# Data Preparation Guide

This document provides instructions on organizing the training and testing data files required for our CNN-based cyberattack detection model in IoMT environments.

## Dataset

Download the "CIC IoMT dataset 2024" dataset in CSV format from [here](https://www.unb.ca/cic/datasets/iomt-dataset-2024.html).

After downloading, extract and place the CSV files in the appropriate directories (`data/train/` and `data/test/`) as detailed below.

### Directory Setup

Within the `data/` directory, create `train/` and `test/` folders to hold the CSV files for training and testing, respectively.

### Training Data (data/train)

The following files should be placed in `data/train`:
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

### Testing Data (data/test)

The following files should be placed in `data/test`:
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
```
### Notes

Please ensure that the CSV files follow the specified directory structure to prevent data loading errors.

## Additional Notes

You may notice a `.gitkeep` file in both the `train` and `test` folders. These files are simply placeholders to keep the folders visible in Git repositories when they are otherwise empty. They are not required for running the code and can be deleted at any time.
