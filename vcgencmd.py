import subprocess


vcgencmd_base = ["vcgencmd", "display_power"]


def get_status() -> int:
    out = subprocess.check_output(vcgencmd_base)
    _, status = out.decode("ascii").strip().split("=")
    return int(status)


def set_status(newstatus: int):
    cmd = vcgencmd_base + [str(newstatus)]
    out = subprocess.check_output(cmd)
    _, status = out.decode("ascii").strip().split("=")
    if int(status) != newstatus:
        raise Exception("The vcgencmd did not succeed as expected!")
