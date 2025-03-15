import click
import os
import subprocess

@click.command()
@click.option('-d', '--dir', default='.', type=str, help="Directory to scan")
def run(dir):
    is_git = _walk_dir(dir)
    if is_git:
        _run_git_commands(dir)

def _walk_dir(dir):
    for filename in os.listdir(dir):
        f = os.path.join(dir, filename)
        if os.path.isdir(dir):
            if filename.basename() == ".git":
                return True
    return False

def _run_git_commands(repo_dir):
    subprocess.run(["git", "pull"])
    subprocess.run(["git", "push"])
    subprocess.run(["git", "push", "--tags"])

if __name__ == '__main__':
    run()