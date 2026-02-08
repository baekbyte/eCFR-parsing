# eCFR Parsing Tool

A Python-based tool for downloading and parsing the Electronic Code of Federal Regulations (eCFR) data into structured Excel format.

## Overview

This project provides automated tools to:
- Download XML data for all 50 titles of the Code of Federal Regulations from the eCFR API
- Parse the XML structure to extract regulatory sections, headings, and content
- Export the parsed data into a structured Excel workbook with multiple sheets

## Features

- **Automated Data Download**: Fetches XML data for all 50 CFR titles from the official eCFR API
- **Structured Parsing**: Extracts regulatory sections, headings, text content, authorities, and sources
- **Excel Export**: Creates a comprehensive Excel workbook with separate sheets for each title
- **Hierarchical Data**: Preserves the regulatory hierarchy (DIV1, DIV2, DIV3, etc.)
- **Metadata Extraction**: Captures section numbers, types, node paths, and other structural information

## Project Structure

```
eCFR-parsing/
├── ecfr.py          # Downloads XML data from eCFR API
├── excel.py         # Parses XML and exports to Excel
├── files/           # Directory containing downloaded XML files
│   ├── title-1.xml
│   ├── title-2.xml
│   └── ... (all 50 titles)
├── ecfr_data.xlsx   # Output Excel file with parsed data
└── README.md
```

## Requirements

- Python 3.6+
- Required packages:
  - `requests` - For API calls
  - `pandas` - For data manipulation
  - `beautifulsoup4` - For XML parsing
  - `openpyxl` - For Excel file creation

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd eCFR-parsing
```

2. Install required dependencies:
```bash
pip install requests pandas beautifulsoup4 openpyxl
```

## Usage

### Step 1: Download eCFR Data

Run the download script to fetch XML data for all 50 CFR titles:

```bash
python ecfr.py
```

This will:
- Create a `files/` directory if it doesn't exist
- Download XML data for titles 1-50 from the eCFR API
- Save each title as `title-{number}.xml` in the `files/` directory

### Step 2: Parse and Export to Excel

Run the parsing script to convert the XML data to Excel format:

```bash
python excel.py
```

This will:
- Parse all downloaded XML files
- Extract structured data including sections, headings, and content
- Create `ecfr_data.xlsx` with separate worksheets for each title

## Output Format

The Excel file contains the following columns for each regulatory section:

- **Title_Number**: The CFR title number (1-50)
- **Level**: Hierarchical level (DIV1, DIV2, DIV3, etc.)
- **Number**: Section number or identifier
- **Type**: Section type classification
- **Node_Path**: XML node path for navigation
- **Heading**: Section heading text
- **Text_Content**: Full text content of the section
- **Authority**: Authority citation if present
- **Source**: Source citation if present

## Data Source

This tool downloads data from the official eCFR API:
- **Base URL**: `https://www.ecfr.gov/api/versioner/v1/full/`
- **Date**: 2025-07-01 
- **Format**: XML

## Notes

- The download process may take some time due to the large volume of data
- Each title is processed separately to handle memory efficiently
- The Excel file may be large due to the comprehensive nature of CFR data
- XML files are preserved locally for future processing without re-downloading
