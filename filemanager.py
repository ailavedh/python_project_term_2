import os

class FileManager:
    
    def create_file(self, filename):
        try:
            with open(filename, 'x') as f:
                print(f"File '{filename}' created successfully.")
        except FileExistsError:
            print(f"Error: File '{filename}' already exists.")
        except Exception:
            print("An unexpected error occurred.")

    def view_all_files(self):
        files = [f for f in os.listdir() if os.path.isfile(f)]
        if not files:
            print("No files found in the current directory.")
        else:
            print("Files in directory:")
            for file in files:
                print(f" - {file}")

    def delete_file(self, filename):
        try:
            os.remove(filename)
            print(f"File '{filename}' has been deleted successfully.")
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
        except Exception:
            print("An unexpected error occurred.")

    def read_file(self, filename):
        try:
            with open(filename, 'r') as f:
                content = f.read()
                print(f"\n--- Content of '{filename}' ---\n{content}\n---------------------------")
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
        except Exception:
            print("An unexpected error occurred.")

    def edit_file(self, filename):
        try:
            with open(filename, 'a') as f:
                content = input("Enter data to append: ")
                f.write(content + "\n")
                print(f"Content added to '{filename}' successfully.")
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
        except Exception:
            print("An unexpected error occurred.")


class FileManagerApp:
    def __init__(self):
        self.file_manager = FileManager()

    def display_menu(self):
        print("\n=== FILE MANAGEMENT APP ===")
        print("1: Create file")
        print("2: View all files")
        print("3: Delete file")
        print("4: Read file")
        print("5: Edit file")
        print("6: Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-6): ").strip()

            if choice == '1':
                filename = input("Enter the file name to create: ").strip()
                self.file_manager.create_file(filename)

            elif choice == '2':
                self.file_manager.view_all_files()

            elif choice == '3':
                filename = input("Enter the file name to delete: ").strip()
                self.file_manager.delete_file(filename)

            elif choice == '4':
                filename = input("Enter the file name to read: ").strip()
                self.file_manager.read_file(filename)

            elif choice == '5':
                filename = input("Enter the file name to edit: ").strip()
                self.file_manager.edit_file(filename)

            elif choice == '6':
                print("Closing the application. Goodbye!")
                break

            else:
                print("Invalid input. Please choose a valid option.")


app = FileManagerApp()
app.run()
