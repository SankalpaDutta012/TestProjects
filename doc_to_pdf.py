import sys
import subprocess
import re
from docx2pdf import convert

def convert_to_pdf_using_libreoffice(folder, source, timeout=None):

    try:
        args = [libreoffice_exec(), '--headless', '--convert-to', 'pdf', '--outdir', folder, source]
        process = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=timeout)
        
        # Extract the converted filename from the output
        match = re.search(r'-> (.*?) using filter', process.stdout.decode())
        if match:
            return match.group(1)
        else:
            print("Error: Conversion failed.")
            return None
    except subprocess.TimeoutExpired:
        print("Error: Conversion process timed out.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def libreoffice_exec():

    if sys.platform == 'darwin':
        return '/Applications/LibreOffice.app/Contents/MacOS/soffice'
    elif sys.platform.startswith('win'):
        return 'C:\\Program Files\\LibreOffice\\program\\soffice.exe'
    else:
        return 'libreoffice'

def convert_docx_to_pdf(input_path, output_path=None):

    try:
        if output_path:
            convert(input_path, output_path)
        else:
            convert(input_path)
        print("Conversion successful.")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    # Using LibreOffice for conversion
    folder = "./output"
    source_file = "example.docx"
    timeout = 15

    converted_file = convert_to_pdf_using_libreoffice(folder, source_file, timeout)
    if converted_file:
        print(f"File successfully converted: {converted_file}")

    # Using docx2pdf for conversion
    input_docx = "example.docx"
    output_pdf = "example_converted.pdf"

    convert_docx_to_pdf(input_docx, output_pdf)
