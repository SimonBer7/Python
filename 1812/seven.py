import os
import shutil

#1
folder_path = "folder"
if os.path.isdir(folder_path):
    print(f"Složka {folder_path} existuje.")
else:
    print(f"Složka {folder_path} neexistuje.")

#2
new_folder_path = "new_folder"
os.mkdir(new_folder_path)
print(f"Složka {new_folder_path} byla vytvořena.")

#3
empty_folder_path = "empty_folder"
os.mkdir(empty_folder_path)
os.rmdir(empty_folder_path)
print(f"Prazdná složka {empty_folder_path} byla smazána.")

#4
folder_to_delete = "folder_to_delete"
os.mkdir(folder_to_delete)
with open(os.path.join(folder_to_delete, "example_file.txt"), "w") as file:
    file.write("Obsah souboru")
shutil.rmtree(folder_to_delete)
print(f"Složka {folder_to_delete} byla smazána včetně obsahu.")

# Příklad 5: Výpis obsahu složky
folder_contents = os.listdir(".")
print(f"Obsah aktuální složky: {folder_contents}")

# Příklad 6: Výpis obsahu složky a všech podsložek
def list_all_files_and_subfolders(folder):
    print(f"Obsah složky {folder}:")
    for root, dirs, files in os.walk(folder):
        for name in files:
            print(os.path.join(root, name))
        for name in dirs:
            print(os.path.join(root, name))

folder_to_explore = "."
list_all_files_and_subfolders(folder_to_explore)
