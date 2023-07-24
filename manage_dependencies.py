import subprocess

def install_dependencies():
    try:
        subprocess.run(["py", "-m", "pip", "install", "-r", "requirements.txt"], check=True)
        print("Dependencies installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while installing dependencies: {e}")
        exit(1)

def upgrade_dependencies():
    try:
        subprocess.run(["py", "-m", "pip", "install", "--upgrade", "-r", "requirements.txt"], check=True)
        print("Dependencies upgraded successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while upgrading dependencies: {e}")
        exit(1)

def main():
    while True:
        print("1. Install Dependencies")
        print("2. Upgrade Dependencies")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            install_dependencies()
        elif choice == "2":
            upgrade_dependencies()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()
