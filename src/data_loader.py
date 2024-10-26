import os
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split

# --- Attack Category Mapping ---
attack_categories = {
    2: {
        'attack': ['ARP_Spoofing', 'MQTT-DDoS-Connect_Flood', 'MQTT-DDoS-Publish_Flood',
                   'MQTT-DoS-Connect_Flood', 'MQTT-DoS-Publish_Flood', 'MQTT-Malformed_Data',
                   'Recon-OS_Scan', 'Recon-Ping_Sweep', 'Recon-Port_Scan', 'Recon-VulScan',
                   'TCP_IP-DDoS-ICMP', 'TCP_IP-DDoS-SYN', 'TCP_IP-DDoS-TCP', 'TCP_IP-DDoS-UDP',
                   'TCP_IP-DoS-ICMP', 'TCP_IP-DoS-SYN', 'TCP_IP-DoS-TCP', 'TCP_IP-DoS-UDP'],
        'Benign': ['Benign']
    },
    6: {  # CORRECTED MAPPING FOR 6 CLASSES 
        'Spoofing': ['ARP_Spoofing'],
        'MQTT': ['MQTT-DDoS-Connect_Flood', 'MQTT-DDoS-Publish_Flood',
                  'MQTT-DoS-Connect_Flood', 'MQTT-DoS-Publish_Flood', 'MQTT-Malformed_Data'],
        'Recon': ['Recon-OS_Scan', 'Recon-Ping_Sweep', 'Recon-Port_Scan', 'Recon-VulScan'],
        'DDoS': ['TCP_IP-DDoS-ICMP', 'TCP_IP-DDoS-SYN', 'TCP_IP-DDoS-TCP', 'TCP_IP-DDoS-UDP'],
        'DoS': ['TCP_IP-DoS-ICMP', 'TCP_IP-DoS-SYN', 'TCP_IP-DoS-TCP', 'TCP_IP-DoS-UDP'],
        'Benign': ['Benign']
    },
    19: {
        'ARP_Spoofing': ['ARP_Spoofing'],
        'MQTT-DDoS-Connect_Flood': ['MQTT-DDoS-Connect_Flood'],
        'MQTT-DDoS-Publish_Flood': ['MQTT-DDoS-Publish_Flood'],
        'MQTT-DoS-Connect_Flood': ['MQTT-DoS-Connect_Flood'],
        'MQTT-DoS-Publish_Flood': ['MQTT-DoS-Publish_Flood'],
        'MQTT-Malformed_Data': ['MQTT-Malformed_Data'],
        'Recon-OS_Scan': ['Recon-OS_Scan'],
        'Recon-Ping_Sweep': ['Recon-Ping_Sweep'],
        'Recon-Port_Scan': ['Recon-Port_Scan'],
        'Recon-VulScan': ['Recon-VulScan'],
        'DDoS-ICMP': ['TCP_IP-DDoS-ICMP'],
        'DDoS-SYN': ['TCP_IP-DDoS-SYN'],
        'DDoS-TCP': ['TCP_IP-DDoS-TCP'],
        'DDoS-UDP': ['TCP_IP-DDoS-UDP'],
        'DoS-ICMP': ['TCP_IP-DoS-ICMP'],
        'DoS-SYN': ['TCP_IP-DoS-SYN'],
        'DoS-TCP': ['TCP_IP-DoS-TCP'],
        'DoS-UDP': ['TCP_IP-DoS-UDP'],
        'Benign': ['Benign']
    }
}[19]  # Set to desired number of classes


def load_data(file_path):
    """Loads a CSV file into a Pandas DataFrame."""
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
        return None

def get_attack_category(file_name):
    """Determines the attack category from the file name."""
    for category, attacks in attack_categories.items():
        if any(attack in file_name for attack in attacks):
            return category
    return "Unknown"

def load_and_preprocess_data(dataset_path, num_classes):
    """Loads, preprocesses the dataset, and prepares it for training."""
    train_file = os.path.join(dataset_path, 'train.csv')
    test_file = os.path.join(dataset_path, 'test.csv')

    train_df = load_data(train_file)
    test_df = load_data(test_file)

    if train_df is None or test_df is None:
        return None, None, None, None

    train_df['Attack_Type'] = train_df['file'].apply(get_attack_category)
    test_df['Attack_Type'] = test_df['file'].apply(get_attack_category)

    X_train = train_df.drop(['Attack_Type', 'file'], axis=1)
    y_train = train_df['Attack_Type']
    X_test = test_df.drop(['Attack_Type', 'file'], axis=1)
    y_test = test_df['Attack_Type']

    label_encoder = LabelEncoder()
    y_train = label_encoder.fit_transform(y_train)
    y_test = label_encoder.transform(y_test)

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    return X_train, X_test, y_train, y_test
