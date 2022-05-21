from cx_Freeze import setup, Executable

setup(name = "app" ,
      version = "1.0.0" ,
      description = "DESCRIPTION" ,
      executables = [Executable("main.py", base = "Win32GUI")]
)