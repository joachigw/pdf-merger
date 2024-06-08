import sys
import os
import PyPDF2


def merge_pdfs(files: list):
    """Merge PDF-files specified in the command-line arguments (argv).
    :param files: list, the files to be merged together
    """
    merged_filename = "combined_pdfs"
    merger = PyPDF2.PdfMerger()

    for file in files:
        if file.endswith(".pdf"):
            merger.append(file)
        else:
            raise ValueError(f"'{file}' is not a pdf-file.")

    if (merged_filename + ".pdf") in os.listdir(os.curdir):
        print(f"{merged_filename} already exists. Merging with a unique name...")
        merged_filename = merged_filename + str(len(os.listdir(os.curdir)))

    merger.write(merged_filename + ".pdf")
    print("PDF-files successfully merged.")


if len(sys.argv) > 1:
    try:
        merge_pdfs(sys.argv[1::])
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print(f"An unknown error occured ({e}). Please try again later.")
else:
    print("Please specify PDF-files to be merged as arguments when running the script.")
