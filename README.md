# Git Plugin

A simple Python CLI tool that helps automate common Git operations in your repositories.

## Overview

The `git-initial.py` script checks if a directory is a Git repository and automatically runs common Git commands like pull and push.

## Features

- Scans directories to find Git repositories
- Automatically runs `git pull` to update the repository
- Automatically runs `git push` to upload local changes
- Handles tag pushing with `git push --tags`

## Installation

1. Clone this repository:
```bash
git clone https://github.com/Abdallah-Afifi/Git_Plugin.git
```

2. Install the required dependencies:
```bash
pip install click
```

## Usage

Run the script with:

```bash
python git-initial.py
```

### Options

- `-d, --dir`: Specify the directory to scan (default: current directory)

```bash
python git-initial.py --dir /path/to/your/repo
```

## Requirements

- Python 3.x
- Click library
- Git installed and configured



