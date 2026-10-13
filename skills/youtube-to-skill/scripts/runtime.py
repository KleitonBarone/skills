"""Discover newly installed Windows tools and use UTF-8 for subprocess output."""

import os
import shutil
import sys


def configure_runtime():
    if sys.platform == "win32":
        import winreg

        try:
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment") as key:
                user_path, _ = winreg.QueryValueEx(key, "Path")
            os.environ["PATH"] += os.pathsep + os.path.expandvars(user_path)
        except OSError:
            pass
    os.environ["PYTHONIOENCODING"] = "utf-8"
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")


def ytdlp_command():
    command = ["yt-dlp", "--ignore-config", "--encoding", "utf-8",
               "--socket-timeout", "30", "--retries", "3"]
    if not shutil.which("deno") and shutil.which("node"):
        command += ["--js-runtimes", "node"]
    return command


configure_runtime()
