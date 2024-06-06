import subprocess

# Prompt the user for backup confirmation
backup_confirmation = input("Do you want to backup the database? (yes/no): ")

if backup_confirmation.lower() == "yes":
    # Prompt the user for the database name
    database_name = input("Enter the name of the database to backup: ")

    # Specify the backup file name
    backup_file = f"backup_file2.sql"

    try:
        # Execute the mysqldump command to create the backup
        subprocess.run(["mysqldump", "-u", "root", "-p", database_name, "--result-file", backup_file])

        print(f"Backup of database '{database_name}' has been created in '{backup_file}'")
    
    except subprocess.CalledProcessError as error:
        print(f"An error occurred during backup: {error}")
else:
    print("Backup canceled by user.")