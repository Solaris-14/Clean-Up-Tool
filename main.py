import argparse



#parser letting us run the script with extra functionality 

parser = argparse.ArgumentParser(description="Directory Cleaner")

parser.add_argument("--dry-run", action="store_true", help="Preview Changes")
#another optional argument, that takes a file header as input in case the user wants to only clean up certain files, eg: png
parser.add_argument("-ext", help="Clean up certain files, eg:pngs")

args = parser.parse_args()

if args.dry_run:
    print("dry-run mode is now active")
if args.ext:
    print(f"Cleaning for {args.ext.lstrip(".")} files")
    