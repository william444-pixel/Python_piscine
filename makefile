PACKAGE_NAME = mazegen
DIST_DIR = dist

.PHONY: all build install clean fclean re

# Default rule: Build the package
all: build

# Create the .tar.gz and .whl files
build:
	python3 -m build

# Install the package locally
install: build
	pip install .

# Clean temporary build files
clean:
	rm -rf build/
	rm -rf *.egg-info/

# Clean everything including the dist folder
fclean: clean
	rm -rf $(DIST_DIR)/

# Rebuild everything from scratch
re: fclean all

# Run the project with a default config (optional)
run:
	python3 a_maze_ing.py config.txt