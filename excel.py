import pandas as pd
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import os

directory_path = "./files"

def get_ecfr_data(title):
    try:
        with open(f"{directory_path}/title-{title}.xml", "r", encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"File for title {title} not found")
        return None

def parse_ecfr_data(data):
    soup = BeautifulSoup(data, "xml")
    return soup

def create_dataframe(soup, title_num):
    sections = []
    
    # Find all DIV elements (DIV1, DIV2, DIV3, etc.)
    divs = soup.find_all(lambda tag: tag.name and tag.name.startswith('DIV'))
    
    for div in divs:
        # Extract HEAD text content (not attribute)
        head_element = div.find('HEAD')
        head_text = head_element.get_text(strip=True) if head_element else ""
        
        # Extract all text content from the div
        # Get text but exclude nested DIV content to avoid duplication
        div_copy = div.__copy__()
        for nested_div in div_copy.find_all(lambda tag: tag.name and tag.name.startswith('DIV')):
            nested_div.decompose()
        text_content = div_copy.get_text(strip=True)
        
        # Extract AUTH and SOURCE if present
        auth_element = div.find('AUTH')
        auth_text = auth_element.get_text(strip=True) if auth_element else ""
        
        source_element = div.find('SOURCE')
        source_text = source_element.get_text(strip=True) if source_element else ""
        
        section_data = {
            'Title_Number': title_num,
            'Level': div.name,  # DIV1, DIV2, etc.
            'Number': div.get('N', ''),
            'Type': div.get('TYPE', ''),
            'Node_Path': div.get('NODE', ''),
            'Heading': head_text,
            'Text_Content': text_content,
            'Authority': auth_text,
            'Source': source_text
        }
        sections.append(section_data)
    
    return pd.DataFrame(sections)

def main():
    print("=== Parsing ECFR data ===")
    
    # Create Excel writer object
    with pd.ExcelWriter('ecfr_data.xlsx', engine='openpyxl') as writer:
        
        for title in range(1, 51):
            print(f"Processing Title {title}...")
            
            data = get_ecfr_data(title)
            if data is None:
                continue
                
            soup = parse_ecfr_data(data)
            df = create_dataframe(soup, title)
            
            if not df.empty:
                # Create worksheet name (Excel has 31 char limit)
                sheet_name = f"Title_{title}"
                df.to_excel(writer, sheet_name=sheet_name, index=False)
                print(f"Title {title}: {len(df)} sections extracted")
            else:
                print(f"Title {title}: No data found")
    
    print("=== Extraction complete! Check 'ecfr_data.xlsx' ===")

if __name__ == "__main__":
    main()