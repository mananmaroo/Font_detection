
FontChange Detector
Detect and analyze font changes in PDF documents to identify text styling differences.

📋 Project Overview
FontChange Detector is a Python-based tool designed to parse PDF documents and identify changes in font styles. This utility can be used to analyze text formatting and ensure consistency or detect styling patterns in professional documents.

🚀 Features
Detects and highlights changes in font style across a PDF document.
Extracts the corresponding text and its associated font metadata.
Useful for auditing text styling or debugging PDF formatting issues.

🛠️ Technologies Used
Python: The primary language for the script.
PyMuPDF (fitz): To parse PDF files and extract text with font metadata.
re (Regular Expressions): For text cleaning and preprocessing.

🗂️ Project Structure
Input: A user-provided PDF file.
Process:
Extract text content from each page using PyMuPDF.
Track changes in font style line-by-line.
Store detected font changes along with the corresponding text.
Output:
A list of font changes with page numbers, text, and font details.

🧑‍💻 How to Use
Install Required Library:

pip install PyMuPDF

Prepare the Script:

Save the code as font_change_detector.py.

Replace path_to_your_pdf.pdf with the actual path to your PDF file in the script.

Run the Script:

python font_change_detector.py

View Results: The script will print details of font changes, including the page number, the font style, and the corresponding text.

🛠️ Potential Enhancements
Export results to a CSV or JSON file for better readability.
Add visualization to mark font changes directly on the PDF.
Support for font size and color detection.

🤝 Contributing
Contributions are welcome! Whether it's bug fixes, new features, or optimization, feel free to submit a pull request.

