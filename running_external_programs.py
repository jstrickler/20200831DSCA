from subprocess import run, CalledProcessError, PIPE
import shlex

raw_command = "netstat -an"   #  "mail -s mysubject blah-blah"
command_words = shlex.split(raw_command)
print("command_words:", command_words)

run(command_words)
print('-' * 60)

try:
    proc = run(command_words, stdout=PIPE)
except CalledProcessError as err:
    print(err.returncode, err)
else:
    lines = proc.stdout.decode().splitlines()
    for line in lines:
        if "ESTAB" in line:
            print(line)

