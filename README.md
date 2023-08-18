# 2023-05-23-ds-pt-au

Follow these steps to get started:

1. Use your terminal to go to the document folder and clone this repository:
    ```
    git clone https://github.com/suryarb/2023-05-23-ds-pt-au.git
    ```
2. cd into the 2023-05-23-ds-pt-au folder:
    ```
    cd 2023-05-23-ds-pt-au
    ```
3. Switch to a new branch with your first name and last name (lower cases):
    ```
    git checkout -b firstname-lastname
    ```
4. Create a new folder with your first name and last name (lower cases):
    ```
    mkdir firstname_lastname
    ```
5. Copy your files and folders into the newly created folder firstname_lastname.
6. Update the `.gitignore` file by adding the following entries to ignore specific types of files:
    ```
    firstname_lastname/DATA
    firstname_lastname/data
    firstname_lastname/Data
    *.csv
    *.pdf
    *.pptx
    *.docx
    *.xlsx
    *.zip
    *.mp4
    *.ipynb_checkpoints
    ```

   These entries will exclude files and directories with the specified extensions or names from being tracked by Git. This is based on the IOD learning materials. Please ensure to add the new file extensions if you are working with any other large file formats.

7. Save the `.gitignore` file.
8. Run this code to ensure you are checked out to your branch.
   ```
   git branch -a
   ```
9. Run this code to add files/folders to staging.
   ```
   git add "file_name" or git add --all
   ```
10. Run this code to check no unintended large files have been added.
    ```
    git status
    ```
    If unintended files have been added, run this code to remove those files from staging.
    ```
    git rm -r directory
    ```
    or 
    ```
    git rm -r path/filename
    ```
11. Run this code to commit
    ```
    git commit -m "your commit message i.e. summary of work you have done"
    ```
    Ensure no large files have been added. The files with extensions in .gitignore should have been ignored
12. Run this code to commit
    ```
    git push
    ```
