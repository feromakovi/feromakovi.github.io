import os

def generate_docs():
    cv_path = "assets/cv.md"
    if not os.path.exists(cv_path):
        print(f"Error: {cv_path} not found.")
        return

    with open(cv_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Split by the first occurrence of '## '
    parts = content.split("## ", 1)
    if len(parts) < 2:
        print("Error: Could not find any '## ' headers in cv.md.")
        return

    header_part = parts[0].strip()
    body_part = "## " + parts[1]

    # Generate index.md (Jekyll entrance point)
    # The Jekyll Cayman theme displays the title and description at the top automatically,
    # so we only include the body portion of the CV, plus an avatar and social icons.
    avatar_header = """<div align="center">
  <img src="https://github.com/feromakovi.png" width="150" style="border-radius: 50%; border: 3px solid #1e90ff; margin-bottom: 20px;" alt="Richard Samela Avatar" />
  <br />
  <a href="https://github.com/feromakovi"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub Badge" /></a>
  <a href="mailto:feromakovi@gmail.com"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email Badge" /></a>
</div>

"""
    index_content = avatar_header + body_part
    with open("index.md", "w", encoding="utf-8") as f:
        f.write(index_content)
    print("Generated index.md")

    # Generate README.md (GitHub repo page)
    # This includes the title/subtitle of cv.md, followed by badges including PDF download, then the body.
    badges_block = """
<div align="center">
  <a href="https://github.com/feromakovi"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub Badge" /></a>
  <a href="mailto:feromakovi@gmail.com"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email Badge" /></a>
  <a href="https://feromakovi.github.io/assets/richard_samela_cv.pdf"><img src="https://img.shields.io/badge/Download%20PDF-0077B5?style=for-the-badge&logo=adobe-acrobat-reader&logoColor=white" alt="Download PDF Badge" /></a>
</div>

---
"""
    readme_content = f"{header_part}\n{badges_block}\n{body_part}"
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)
    print("Generated README.md")

if __name__ == "__main__":
    generate_docs()
