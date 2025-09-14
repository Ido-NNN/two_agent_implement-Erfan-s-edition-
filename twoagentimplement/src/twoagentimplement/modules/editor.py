import re

def code_editor(file_path):

    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    code_blocks = re.findall(r"```python\s+([\s\S]*?)\s+```", text)

    if code_blocks:
        extracted_code = "\n\n".join(code_blocks)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(extracted_code)

        print('Python file edited successfully ✅"')

    else:
        print('No Python code found ⚠️"')