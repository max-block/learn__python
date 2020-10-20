import shlex
import subprocess


def f1():
    cmd = "ls -l /"
    process = subprocess.run(shlex.split(cmd), timeout=30, capture_output=True)
    out = process.stdout.decode("utf-8")
    print(out)


def exec_command_on_remote_host(ssh_file, host, command):
    cmd = f"ssh -i {ssh_file} {host} '{command}'"
    process = subprocess.run(shlex.split(cmd), timeout=30, capture_output=True)
    out = process.stdout.decode("utf-8")
    print(out)


if __name__ == "__main__":
    f1()
    # exec_command_on_remote_host("~/key1", "test", "top")
