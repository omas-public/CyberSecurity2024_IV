# UNIX Commands & vi

## Network Command

- hostname
- ping
  - ping -c [count]
- tracepath(traceroute)
- ip(ifconfig)
  - ip address show(ip -a)
  - ip link set [devname] (up|down)
  - ip address add 192.168.1.254/24 dev [devname]
  - ip route add default via 192.168.1.254 dev [devname]
- ss(netstat)
  - ss -atn
  - ss -lp
  - ss -ntr
  - ss -pantu
- tcpdump
  - tcpdump -i [devname]
  - tcpdump host [target_ip]
  - tcpdump port [port_num]
  - tcpdump host 192.168.56.102 and port 80
- dig(nslookup)
  - dig www.it-college.ac.jp
  - dig ns std.it-college.ac.jp
  - dig mx std.it-college.ac.jp
  - dig -x 8.8.8.8

## Process

- ps
- kill
- &
- ^Z
- jobs
- fg
- bg
- free
- top

## vi

[vim tutor](https://gist.github.com/omas-public/d713308c82ec3bf69fc2f1024b399a31)

- char
- word
- sentence
- paragraph

### Motion

| Direction | Key                              |
| --------- | -------------------------------- |
| Upper     | k \# **) } ?** ^U ^B **gg**      |
| Left      | 0 ^ F B b h                      |
| Right     | e w E W **f** $                  |
| Bottom    | Enter j \* **( { /** ^D ^F **G** |

### InsertMode

| Direction | Key           |
| --------- | ------------- |
| Upper     | O             |
| Left      | I i           |
| Right     | a R c C s S A |
| Bottom    | o             |

### CommandMode

#### range

- n
- n, m
- ., .+- n
- /RE/

#### command

- [range]s/old/new/[g]
- [range]s/^.\*\\(RE\\).\*$/\1/
- [range]d
- e filename
- e #
- !python3 %

#### vi tricks

- :help command
- ~
- r
- xp
- ddp
- /searchword[enter]cw[replaceword]ESCn.n.

### Script

#### Python でシェルプログラム

os モジュールを使う方法

```py
import os
command = 'ls -al'
os.system(command)
```

subprocess モジュールを使う方法

```py
from subprocess import run
output = run(["ls", "-al" ], capture_output=True, text=True)
print(output.stdout)
```

より使いやすくしてみる

```py
from subprocess import run, PIPE

# util abstruct function with lambda
command = lambda command, *fix_args:  lambda *args:  run([command, *fix_args, *args], capture_output=True, text=True)

# concrete function
stdout = lambda process: print(process.stdout)
ping1 = command('ping', '-c1')

# test code
output = ping1('localhost')
print(output)

# loop code
adresses = [f'192.168.56.{i}' for i in range(1,10)]
for address in adresses:
  stdout(ping1(address))
```
