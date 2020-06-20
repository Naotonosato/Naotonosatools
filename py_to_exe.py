import os, sys


filename = sys.argv[1]

os.system("cython --embed "+filename)

c_source = os.path.splitext(filename)[0]+".c"

output_filename = os.path.splitext(filename)[0]+".out"

options = f"\"-I`python3-config --prefix`/Headers\" `python3 -c \"import distutils.sysconfig;print(distutils.sysconfig.get_config_var('LIBS'),distutils.sysconfig.get_config_var('SYSLIBS'),distutils.sysconfig.get_config_var('LINKFORSHARED'))\"` -O3 -o {output_filename}"

cc = "`python3 -c \"import distutils.sysconfig;print(distutils.sysconfig.get_config_var('CC'))\"`"


command = " ".join([cc,options,c_source])

os.system(command)
