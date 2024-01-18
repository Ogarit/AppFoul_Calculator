from cx_Freeze import setup, Executable

setup(
    name="Foul Calculator",
    version="2",
    executables=[Executable("main.py", base="Win32GUI", icon="1492693845-calculator_83582.ico")],
    options={"build_exe": {"packages": ["customtkinter"],
                           "include_files": ["1492693845-calculator_83582.ico"]}},
)