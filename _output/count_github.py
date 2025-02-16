import os

home_dir = os.path.expanduser("~")
git_count = sum(1 for root, dirs, files in os.walk(home_dir) if ".git" in dirs)

print(f"Number of Git repositories: {git_count}")


