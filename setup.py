import cx_Freeze
executables = [
    cx_Freeze.Executable(script="main.py", icon="space.ico")
]
cx_Freeze.setup(
    name = "Space Marker",
    options={
        "build_exe":{
            "packages":["pygame"],
            "include_files":["espaco.png",
                            "foguete.png",
                            "musicaFundo.mp3",
                            "funcoes.py"]
        }
    }, executables = executables
)
