import argparse
from pathlib import Path
import shutil

FILE_RULES = {
    "Documents":[".pdf",".txt",".docx", ".md",".json"],
    "Archives": [".zip", ".7z", ".rar"],
    "Code": [".py",".c",".cpp",".js",".html",".css",".conf",".css",".r"],
    "Binary": [".bat",".dat"],
    "Images": [".png",".jpg",".jpgeg",".webp",".gif"],
    "Music": [".mp3",".wav"],
    "Video":[".mp4",".mov",".mkv",".avi",".WebM"],
    "Others" :[".exe"]
}
#parser letting us run the script with extra functionality 

parser = argparse.ArgumentParser(description="Directory Cleaner")
parser.add_argument("--dry-run", action="store_true", help="Preview Changes")
#another optional argument, that takes a file header as input in case the user wants to only clean up certain files, eg: png
parser.add_argument("-ext", help="Clean up certain files, eg:pngs")
#argument for directory
parser.add_argument("-dir",default=".", help="Input directory for cleanup")
args = parser.parse_args()


#gets the category for the input file extension
def get_category(extension: str) -> str:
    for category in FILE_RULES:
        if extension in FILE_RULES[category]:
            return category

    return f"No category found"


def organize(dir):
    target_dir = Path(dir)
    for item in target_dir.iterdir():
        if args.ext is None:
            category = get_category(item.suffix.lower())
            if item.is_file():
                if category == "No category found":
                    continue   
                dest = target_dir/category
                dest_file_path = target_dir/category/item.name
                if args.dry_run:
                    print("DRY-RUN MODE IS ON")
                    print(f"[DRY-RUN] moved {item.name} -> {dest}")
                elif category != None:
                    dest.mkdir(exist_ok=True)
                    shutil.move(str(item), str(dest_file_path))
        else:
            clean_ext = f".{args.lstrip(".")}".lower()
            category = get_category(clean_ext)
            if item.is_file():
                if item.suffix == clean_ext:
                    dest = target_dir/category
                    dest_file_path = target_dir/category/item.name
                    if args.dry_run:
                        print("DRY-RUN MODE IS ON")
                        print(f"[DRY-RUN] moved {item.name} -> {dest}")
                    elif category != None:
                        dest.mkdir(exist_ok=True)
                        shutil.move(str(item), str(dest_file_path))



def main():
    organize(args.dir)

if __name__ == "__main__":
    main()