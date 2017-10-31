# driver.py

import sys
from pyke import knowledge_engine, krb_traceback
from pyke import ask_tty

engine = knowledge_engine.engine(__file__)
engine.ask_module = ask_tty


def run():
    engine.reset()
    try:
        engine.activate('anime_suggestion')
        engine.prove_1_goal('anime_suggestion.getting_started()')
    except Exception:
        krb_traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    run()

