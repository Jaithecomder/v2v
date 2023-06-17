#!/bin/bash

# Set the repository URL
REPO_URL="https://github.com/TyagiAkanksha/v2v.git"

# Set the branch name
BRANCH_NAME="main"

# Function to recursively add files
function add_files() {
  local target="$1"
  for file in "$target"/*; do
    if [ -f "$file" ]; then
      git add "$file"
      git commit -m "Add $file"
    elif [ -d "$file" ]; then
      git add "$file"
      git commit -m "Add $file"
      add_files "$file"
    fi
  done
}

# Loop through each file and folder in the current directory
for entry in *; do
  if [ -d "$entry" ]; then
    git add "$entry"
    git commit -m "Add $entry"
    add_files "$entry"
  elif [ -f "$entry" ]; then
    git add "$entry"
    git commit -m "Add $entry"
  fi
done

# Push the commits to the repository
git push origin $BRANCH_NAME
#!/bin/bash

git add .
git commit -m "Add files"
git push origin master
