import os
import re
import shutil
import sys
from pathlib import Path

def localize_images(root_dir):
    """
    Scans for .master.md files, finds external image references, 
    copies images to a local 'image' folder, and updates the markdown.
    """
    
    # Define regex to find markdown images: ![alt](path)
    # This also captures optional title: ![alt](path "title")
    img_pattern = re.compile(r'!\[(.*?)\]\(([^"\)\s]+)(?:\s*".*?")?\)')

    count_processed = 0
    count_images = 0

    root_path = Path(root_dir).resolve()
    print(f"Scanning directory: {root_path}")

    for md_file in root_path.rglob("*.master.md"):
        print(f"\nProcessing: {md_file.relative_to(root_path)}")
        
        try:
            content = md_file.read_text(encoding='utf-8')
        except Exception as e:
            print(f"  Error reading file: {e}")
            continue

        parent_dir = md_file.parent
        image_dir = parent_dir / "image"
        
        # New content builder
        new_content = content
        modified_file = False

        # Find all matches
        matches = list(img_pattern.finditer(content))
        
        if not matches:
            continue

        for match in matches:
            full_match = match.group(0)
            alt_text = match.group(1)
            original_path_str = match.group(2)
            
            # Check if path is external ("../../" or absolute, but logic suggests mainly relative ups)
            # We are identifying paths that traverse UP or are absolute (not standard local)
            # OR simply paths that are not starting with "image/" or "./"
            
            # User specifically mentioned "../../" but let's be robust.
            # If it's already local (e.g. "image/foo.png" or "foo.png"), skip.
            is_external = original_path_str.startswith("../") or original_path_str.startswith("/") or (not original_path_str.startswith("image/") and "/" in original_path_str and not original_path_str.startswith("./"))
            
            # Specifically user asked for checking "external, like ../../"
            # Let's check strict existence.
            if not is_external:
                continue

            # Resolve source path
            try:
                # Handle relative paths from the MD file location
                src_path = (parent_dir / original_path_str).resolve()
            except Exception as e:
                print(f"  Invalid path resolution: {original_path_str} -> {e}")
                continue

            if not src_path.exists():
                print(f"  [X] Image not found: {original_path_str} (Resolved: {src_path})")
                continue
            
            # It exists and is considered external/needs moving.
            if not image_dir.exists():
                image_dir.mkdir(parents=True, exist_ok=True)
                print(f"  Created directory: {image_dir.relative_to(root_path)}")

            # Target filename
            filename = src_path.name
            dest_path = image_dir / filename
            
            # Handle duplicates? (If src and dest are different files but same name)
            if dest_path.exists() and not dest_path.samefile(src_path):
                # Simple collision avoidance
                stem = src_path.stem
                suffix = src_path.suffix
                import time
                timestamp = int(time.time())
                filename = f"{stem}_{timestamp}{suffix}"
                dest_path = image_dir / filename
                print(f"  Duplicate name found, renaming to: {filename}")

            # Copy file if it's not the same file
            if not dest_path.exists() or not dest_path.samefile(src_path):
                shutil.copy2(src_path, dest_path)
                print(f"  [+] Copied: {src_path.name} -> image/{filename}")
                count_images += 1
            else:
                 print(f"  [.] Skipped self-copy: {src_path.name}")

            # Update markdown content
            # The regex match group 2 is the path. We need to replace it.
            # Beware of simple string replace if same image appears multiple times with different contexts (unlikely but possible)
            # We construct the new relative path
            new_rel_path = f"image/{filename}"
            
            # We have to be careful replacing. The 'original_path_str' matches the exact string in the file.
            # But replace() creates global replacement. 
            # Ideally we perform replacement on the specific match span, OR we assume global consistency.
            # Given markdown, global replace of a unique relative path string is usually safe within one file.
            
            # However, replace(original_path_str, new_rel_path) might replace parts of other URLs.
            # Safer: replace the Full Match string (reconstruct it).
            # original match: ![alt](path)
            # new match: ![alt](new_path)
            
            # Reconstruct the match
            # Note: match.group(0) is the entire ![...](...) string
            # But the path might be `../../foo.png`.
            
            # Let's replace the path inside the match.
            new_tag = full_match.replace(original_path_str, new_rel_path)
            new_content = new_content.replace(full_match, new_tag)
            modified_file = True

        if modified_file:
            md_file.write_text(new_content, encoding='utf-8')
            print(f"  Updated: {md_file.name}")
            count_processed += 1

    print(f"\nDone. Processed {count_processed} files, localized {count_images} images.")

if __name__ == "__main__":
    # Default to current directory or 'content' if explicit
    target = "content" if os.path.exists("content") else "."
    if len(sys.argv) > 1:
        target = sys.argv[1]
    
    localize_images(target)
