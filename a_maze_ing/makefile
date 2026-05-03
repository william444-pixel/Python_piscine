PACKAGE_NAME = mazegen
DIST_DIR = dist

.PHONY: all build install clean fclean re

run:
	python3 a_maze_ing.py config.txt
# Default rule: Build the package
all: build

# Create the .tar.gz and .whl files
build:
	python3 -m build


lint:
	python3 -m mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs
	python3 -m flake8 .
# Install the package locally
install: build
	pip install .

# Clean temporary build files
clean:
	rm -rf */__pycache__ .mypy_cache .pytest_cache build dist
	rm -rf *.egg-info/

# Clean everything including the dist folder
fclean: clean
	rm -rf $(DIST_DIR)/

# Rebuild everything from scratch
re: fclean all

