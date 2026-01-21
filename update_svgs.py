
import os

files = ['1.svg', '2.svg', '3.svg', '4.svg', '5.svg',
         '6.svg', '8.svg', '9.svg', '10.svg', '13.svg', '14.svg']
base_path = 'Logos brancas'

for f in files:
    file_path = os.path.join(base_path, f'Prancheta {f}')
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        new_content = content.replace(
            'viewBox="0 0 250 50"', 'viewBox="0 -25 250 100"')

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f"Updated {f}")
    except Exception as e:
        print(f"Error updating {f}: {e}")
