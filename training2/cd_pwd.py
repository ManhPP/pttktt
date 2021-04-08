import subprocess

n = int(input())
cmd= input()

for _ in range(n-1):
    cmd += " && " + input()
    
p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
for line in p.stdout.readlines():
    print(line.decode().replace("\n","/"))
retval = p.wait()

