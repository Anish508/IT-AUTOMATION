import os
import subprocess

my_env = os.environ.copy()
my_env["PATH"] = os.pathsep.join(["mnt/e/myapp", my_env["PATH"]])

result = subprocess.run(["myapp"], env=my_env)