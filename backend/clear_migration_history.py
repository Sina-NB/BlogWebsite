import os

def cleare_migration_history():
    # Path to your Django project's root directory
    project_path = './'

    # Iterate over each app in the project
    for app_name in os.listdir(os.path.join(project_path)):
        app_path = os.path.join(project_path, app_name)

        # Check if the app has a migrations folder
        migrations_path = os.path.join(app_path, 'migrations')
        if os.path.isdir(migrations_path):
            # Get a list of files in the migrations folder
            files = os.listdir(migrations_path)

            # Iterate over the files and delete the history files
            for file_name in files:
                if file_name.endswith('.py') and file_name != '__init__.py':
                    file_path = os.path.join(migrations_path, file_name)
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")

    print("Migration history files deleted successfully!")


# Call the function to delete the migration history files
cleare_migration_history()