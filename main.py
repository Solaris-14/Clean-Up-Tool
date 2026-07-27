import argparse
import pathlib



FILE_RULES = {
    "Documents":[".pdf",".txt",".docx"],
    "Archives": [".zip", ".7z", ".rar"],
    "Images": [".png",".jpg",".jpgeg",".webp",".gif"]
}
#parser letting us run the script with extra functionality 

parser = argparse.ArgumentParser(description="Directory Cleaner")

parser.add_argument("--dry-run", action="store_true", help="Preview Changes")
#another optional argument, that takes a file header as input in case the user wants to only clean up certain files, eg: png
parser.add_argument("-ext", help="Clean up certain files, eg:pngs")

args = parser.parse_args()

if args.dry_run:
    print("Dry-run mode is now active")
if args.ext:
    print(f"Cleaning for {args.ext.lstrip(".")} files")

#gets the category for the input file extension
def get_category(extension: str) -> str:
    for category in FILE_RULES:
        if extension in FILE_RULES[category]:
            return category

    return f"{extension} not found in file categories"

