#!/usr/bin/env sh

goto_dir() {
    cd "$@"
}

label() {
    ARGS="$@"
    bootstrap_goto.py label $ARGS
}

goto() {
    ARGS="$@"
    bootstrap_goto.py goto $ARGS

    if [ "$?" = "0" ]; then
        if [ -f /tmp/goto ]; then
            DIR=$(head -1 /tmp/goto)

            if [ "$DIR" == "<PATH>" ]; then
                DIR=$(sed -n '2p' /tmp/goto)
                goto_dir "$DIR"
            fi

            rm /tmp/goto
        fi
    fi
}
