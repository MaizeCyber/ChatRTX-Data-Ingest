# ChatRTX-Data-Ingest

A tool to convert PDF files and markdown files into text files for use in ChatRTX RAG. Converts and copies all files (including subdirectories) into a separate directory that can easily be set as the dataset directory for a ChatRTX instance with no file type compatability issues.

usage: TextExtract.py [-h] [--clearoutput] root_folder output_folder
positional arguments:
  root_folder    The root folder to check (including subdirectories)
  output_folder  The output folder for converted files

options:
  -h, --help     show this help message and exit
  --clearoutput  Clear the output folder before processing
