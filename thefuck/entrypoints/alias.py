import six
from ..logs import failed, warn
from ..shells import shell
from ..utils import which


def _get_alias(known_args):
    if six.PY2:
        warn("The Fuck will drop Python 2 support soon, more details "
             "https://github.com/nvbn/thefuck/issues/685")

    if known_args.winpty:
        try:
            alias = shell.app_alias(known_args.alias, known_args.winpty)
        except TypeError:
            failed("Current shell does not support winpty")
            alias = ""
    else:
        alias = shell.app_alias(known_args.alias)

    if known_args.enable_experimental_instant_mode:
        if six.PY2:
            warn("Instant mode requires Python 3")
        elif not which('script'):
            warn("Instant mode requires `script` app")
        else:
            return shell.instant_mode_alias(known_args.alias)

    return alias


def print_alias(known_args):
    print(_get_alias(known_args))
