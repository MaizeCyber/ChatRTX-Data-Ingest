import os
import PyPDF2
import shutil

def remove_previous_output_files(output_folder):
    for filename in os.listdir(output_folder):
        file_path = os.path.join(output_folder, filename)
        os.remove(file_path)
    print("Removed previous output files\n" + "-" * 50 + "\n")

def extract_text_from_pdf(pdf_path):
    try:
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            text = ''
            for page_number in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_number]
                text += page.extract_text()
            return text
    except Exception as e:
        print(f"Error extracting text from {pdf_path}: {e}")
        return None

def process_pdf_files(root_folder):
    for folder_path, _, files in os.walk(root_folder):
        for filename in files:
            if filename.endswith(".pdf"):
                pdf_path = os.path.join(folder_path, filename)
                extracted_text = extract_text_from_pdf(pdf_path)
                if extracted_text:
                    # Append the extracted text to the "output.txt" file
                    output_file_path = os.path.join(output_path, filename + ".txt")
                    with open(output_file_path, 'a', encoding='utf-8') as output_file:
                        output_file.write(f"Text extracted from {pdf_path}:\n\n")
                        output_file.write(extracted_text)
                        output_file.write("\n\n" + "-" * 50 + "\n\n")
                    print(f"Text extracted from {pdf_path} and appended to {output_file_path}")
            else:
                # Copy non-PDF files to the "output" folder
                print(f"Copying {filename} to {output_path}")
                source_file_path = os.path.join(folder_path, filename)
                destination_file_path = os.path.join(output_path, filename)
                shutil.copy2(source_file_path, destination_file_path)

# Replace 'input_path' with the path to the folder you want to check
input_path = r"C:/Users/1889b/AppData/Local/NVIDIA/ChatWithRTX/RAG/trt-llm-rag-windows-main/dataset"
# Replace 'output_path' with the path to the folder where you want to save the extracted text
output_path = r"C:/Users/1889b/AppData/Local/NVIDIA/ChatWithRTX/RAG/trt-llm-rag-windows-main/dataset_input"

if os.path.isdir(output_path):
    remove_previous_output_files(output_path)
else:
    print(f"Invalid folder path: {output_path}")

if os.path.isdir(input_path):
    process_pdf_files(input_path)
else:
    print(f"Invalid folder path: {input_path}")

