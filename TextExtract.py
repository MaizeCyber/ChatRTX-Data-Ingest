import os
import shutil
import PyPDF2
import argparse


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


def convert_md_to_txt(md_file_path):
    try:
        # Read the Markdown file content
        with open(md_file_path, 'r', encoding='utf-8') as md_file:
            md_content = md_file.read()
            text = ''
            for line in md_content:
                text += line
            return text
    except Exception as e:
        print(f"Error converting {md_file_path} to text file: {e}")


def remove_previous_output_files(output_folder):
    for filename in os.listdir(output_folder):
        file_path = os.path.join(output_folder, filename)
        os.remove(file_path)
    print("Removed previous output files\n" + "-" * 50 + "\n")


def process_files(root_folder, output_path):
    for folder_path, _, files in os.walk(root_folder):
        for filename in files:
            source_file_path = os.path.join(folder_path, filename)
            if filename.endswith(".pdf"):
                extracted_text = extract_text_from_pdf(source_file_path)
                if extracted_text:
                    output_file_path = os.path.join(output_path, filename + ".txt")
                    with open(output_file_path, 'a', encoding='utf-8') as output_file:
                        output_file.write(f"Text extracted from {source_file_path}:\n\n")
                        output_file.write(extracted_text)
                        output_file.write("\n\n" + "-" * 50 + "\n\n")
                    print(f"Text extracted from {source_file_path} and appended to {output_file_path}")
            elif filename.endswith(".md"):
                extracted_text = convert_md_to_txt(source_file_path)
                if extracted_text:
                    output_file_path = os.path.join(output_path, filename + ".txt")
                    with open(output_file_path, 'a', encoding='utf-8') as output_file:
                        output_file.write(f"Text extracted from {source_file_path}:\n\n")
                        output_file.write(extracted_text)
                        output_file.write("\n\n" + "-" * 50 + "\n\n")
                    print(f"Text extracted from {source_file_path} and appended to {output_file_path}")
            elif filename.endswith(".txt") or filename.endswith(".doc") or filename.endswith(".docx") or filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".gif") or filename.endswith(".xml"):
                print(f"Copying {filename} to {output_path}")
                destination_file_path = os.path.join(output_path, filename)
                try:
                    shutil.copy2(source_file_path, destination_file_path)
                    print(f"Successfully copied {filename} to {destination_file_path}")
                except Exception as e:
                    print(f"Error copying {filename}: {e}")
            else:
                print(f"Unable to move {filename} to {output_path}. Bad file type.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process PDF, Markdown, and other files.')
    parser.add_argument('root_folder', type=str, help='The root folder to check (including subdirectories)')
    parser.add_argument('--clearoutput', action='store_true', help='Clear the output folder before processing')
    parser.add_argument('output_folder', type=str, help='The output folder for converted files')

    args = parser.parse_args()

    root_folder_to_check = args.root_folder
    output_folder = args.output_folder

    if os.path.isdir(root_folder_to_check):
        os.makedirs(output_folder, exist_ok=True)
        if args.clearoutput:
            remove_previous_output_files(output_folder)
        process_files(root_folder_to_check, output_folder)
    else:
        print(f"Invalid folder path: {root_folder_to_check}")
