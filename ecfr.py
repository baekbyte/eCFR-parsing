import requests
import os

directory_path = "./files"

def get_ecfr_data(title):
    url = f"https://www.ecfr.gov/api/versioner/v1/full/2025-07-01/title-{title}.xml"
    response = requests.get(url)
    return response.text

def save_ecfr_data(title, data):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
    with open(f"{directory_path}/title-{title}.xml", "w") as f:
        f.write(data)
    print(f"Saved data for title {title}")

def main():
    print("=== Getting ECFR data ===")
    for title in range(1, 51):
        data = get_ecfr_data(title)
        save_ecfr_data(title, data)

if __name__ == "__main__":
    main()