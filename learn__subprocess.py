import shlex
import subprocess


def f1():
    cmd = "ls -l /"
    process = subprocess.run(shlex.split(cmd), timeout=30)
    print(process.stdout)


def exec_command_on_remote_host(ssh_file, host, command):
    cmd = f"ssh -i {ssh_file} {host} '{command}'"
    process = subprocess.run(shlex.split(cmd), timeout=30)
    print(process.stdout)


if __name__ == "__main__":
    exec_command_on_remote_host("~/key1", "test", "top")
