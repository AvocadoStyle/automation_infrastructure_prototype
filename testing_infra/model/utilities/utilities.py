import os
import platform
from subprocess import *
import json


def run_process(
        cmd: list, timeout=1200, print_flag=True, attach=True, shell=False
) -> [int, str]:
    """
    will run the process via subprocess.Popen with a default values that acceptable with the system, the default values
    that we set can be edited.
    :param cmd: the command that we want to execute
    :param timeout: timeout untill the process will shutdown
    :param print_flag: in the future we'll use this flag as a indicator of printing the process output
    :param attach: in the future we'll use this flag as a indicator of printing the process output into CI process
    :param shell: use the current shell or not
    :return: the output of the executed process and the exit code as tuple (out, exit).
    """
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
            # encoding="ISO-8859-1",
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
    """
    get the environment variables of the system
    :return:
    """
    os_env = dict(os.environ.copy())
    return os_env

def read_json_file(jfile: str):
    """
    will open and convert a json file into the mem as dict type. get only json type and validate the input
    :param jfile: json file
    :return: dict
    """
    try:
        if not jfile.endswith('.json'):
            raise TypeError('file is not json type')
        with open(jfile, 'r') as jf:
            return json.load(jf)
    except Exception as e:
        print(e)
        raise f'err {e}'

def read_json_for_specific_platform(jfile: str):
    """
    load the jfile configuration by platform into the mem
    :param jfile:
    :return:
    """
    try:
        current_platform = platform.system()
        config = read_json_file(jfile)
        platform_config = config.get(current_platform.upper(), {})
        for key, value in platform_config.items():
            os.environ[key] = value
    except Exception as e:
        raise Exception(f'could get and load the file {e}')

