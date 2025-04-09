#!/bin/bash
if [[ "$1" == "success" ]]; then
    echo "STATUS=success" >> $GITHUB_OUTPUT
else
    echo "STATUS=failure" >> $GITHUB_OUTPUT
fi