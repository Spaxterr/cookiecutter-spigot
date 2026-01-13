import os
import subprocess
import shutil

main_class_name = "{{ cookiecutter.main_class_name }}"
group_id = "{{ cookiecutter.group_id }}"
artifact_id = "{{ cookiecutter.artifact_id }}"

include_pmd = bool("{{ cookiecutter.include_pmd }}")

package_name = f"{group_id}.{artifact_id.lower()}"

package_path = package_name.replace(".", os.sep)

source_dir = os.path.join("src", "main", "java")
target_dir = os.path.join(source_dir, package_path)

def move_files():
    os.makedirs(target_dir, exist_ok=True)

    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)

        if os.path.isfile(file_path):
            # Rename the main file to the main class name
            if filename == "Main.java":
                filename = f"{main_class_name.replace(".java", "")}.java"
            shutil.move(file_path, os.path.join(target_dir, filename))

    if not include_pmd:
        os.remove("pmd-rules.xml")

    print(f">> Moving files to generated target path {target_dir}")


def setup_maven():
    print(">> Setting up maven wrapper...")
    subprocess.call(["mvn", "-N", "io.takari:maven:wrapper"])

move_files()
setup_maven()
print("Ensure the PMD linter is configured to use 'pmd-rules.xml'")
