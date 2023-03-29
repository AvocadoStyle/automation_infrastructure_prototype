import os
from subprocess import *


def run_process(
        cmd: str, timeout=1200, print_flag=True, attach=True, shell=False
) -> [int, str]:
    err = ""
    out = ""
    try:
        # cmd = replace_path_slash(cmd)
        # log.write(f"Run in Process the command:\n{cmd}\n")
        # if attach is True:
        #     allure.attach(cmd, "Command", allure.attachment_type.TEXT)
        # cmd = shlex.split(cmd) if shell is False else cmd
        process = Popen(
            cmd,
            env=get_env_parameters(),
            encoding="ISO-8859-1",
            stdout=PIPE,
            stderr=PIPE,
            universal_newlines=True,
            shell=shell,
        )
        out, err = process.communicate(timeout=timeout)
        # if print_flag:
        #     log.write(out)
        # if attach is True:
        #     allure.attach(out, "Process Output", allure.attachment_type.TEXT)
        exit_code = process.returncode
        # if exit_code != 0 and err:
        #     log.write(f"Process exit with status {exit_code}.\n{err}")
        return exit_code, out
    except TimeoutExpired as ex:
        # log.write(f"Subprocess timeout {out}, {err} {ex}", LOG_LEVEL.ERROR)
        process.kill()
        out, err = process.communicate(timeout=timeout)
        # log.write(f"Subprocess killed {out}, {err} {ex}", LOG_LEVEL.ERROR)
    except Exception as e:
        msg = f"Unable to Run Sub-process {out}. {err}.\n {str(e)}"
        # log.write(msg, LOG_LEVEL.ERROR)
        process.kill()
        out, err = process.communicate(timeout=timeout)
        # log.write(f"Sunprocess killed {out}. Status {err}", LOG_LEVEL.ERROR)
        raise Exception(msg)


def get_env_parameters():
    os_env = dict(os.environ.copy())
    return os_env
