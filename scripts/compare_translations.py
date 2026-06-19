#!/usr/bin/env python3
import os
import sys

def get_relative_files(dir_path):
    """Walks a directory and returns a set of relative file paths."""
    relative_files = set()
    if not os.path.exists(dir_path):
        return relative_files
    for root, _, files in os.walk(dir_path):
        for file in files:
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, dir_path)
            relative_files.add(rel_path)
    return relative_files

def main():
    base_path = './hugo-site/content/'
    
    # If languages are passed as arguments, use them; otherwise, auto-detect from folders
    if len(sys.argv) > 1:
        languages = sys.argv[1:]
    else:
        if not os.path.exists(base_path):
            print(f"Error: '{base_path}' directory not found.")
            sys.exit(1)
        languages = [d for d in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, d))]

    if len(languages) < 2:
        print("Error: Need at least 2 languages to compare.")
        sys.exit(1)

    # Map language -> set of relative files
    lang_files = {}
    all_combined_files = set()

    for lang in languages:
        lang_dir = os.path.join(base_path, lang)
        files = get_relative_files(lang_dir)
        lang_files[lang] = files
        all_combined_files.update(files)

    print(f"=== Multi-Language Translation Audit ===")
    print(f"Comparing: {', '.join(languages)}")
    print(f"Total unique content files expected: {len(all_combined_files)}\n")

    # Check what each language is missing compared to the global master set
    for lang in languages:
        missing_files = all_combined_files - lang_files[lang]
        print(f"--- Language: [{lang}] ---")
        if missing_files:
            print(f"[x] Missing {len(missing_files)} file(s):")
            for f in sorted(missing_files):
                print(f"  - {f}")
        else:
            print(":D 100% complete! No missing files.")
        print()

if __name__ == "__main__":
    main()
