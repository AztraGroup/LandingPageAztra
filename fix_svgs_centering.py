import os
import re

folder_path = r"c:\Users\Matheus\AppData\Aztra\site aztra 3\Logos brancas"

# Target pattern: existing viewBox (likely the one we just set or similar variants)
# We want to force it to "0 0 250 100" to ensure top alignment and sufficient height.
# Regex to find any viewBox attribute
viewbox_pattern = re.compile(r'viewBox="[^"]+"')


def update_svg(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if file has viewBox
    if 'viewBox=' in content:
        # Replace with 0 0 250 100
        new_content = viewbox_pattern.sub('viewBox="0 0 250 100"', content)

        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated: {os.path.basename(file_path)}")
        else:
            print(f"No match/change for: {os.path.basename(file_path)}")
    else:
        print(f"Skipping (no viewBox): {os.path.basename(file_path)}")


# Iterate over files
for filename in os.listdir(folder_path):
    if filename.endswith(".svg"):
        update_svg(os.path.join(folder_path, filename))
