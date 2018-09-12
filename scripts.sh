#!/bin/bash

us_dir="$HOME/.local/share/qutebrowser/userscripts"

if [ $1 = "pocket" ]; then
    python $us_dir/pocket/pocket.py $2
    if [ $? -eq 0 ]; then
        echo "message-info 'Successfully saved \"$2\" in pocket'" >> "$QUTE_FIFO"
    else
        echo "message-error 'Cannot saved \"$2\" in pocket'" >> "$QUTE_FIFO"
    fi
elif [ $1 = "ejdict" ]; then
    word='"'$(python $us_dir/ejdict/ejdict.py $QUTE_SELECTED_TEXT)'"'
    if [ $? -eq 0 ]; then
        echo "message-info $word" >> "$QUTE_FIFO"
    else
        echo "message-error 'Cannot find \"$QUTE_SELECTED_TEXT\" in a dictionary'" >> "$QUTE_FIFO"
    fi
fi
