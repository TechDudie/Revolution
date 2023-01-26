#!/bin/bash
# Run this command: chmod 777 install-mac.sh && ./install-mac.sh

function fix {
	chmod 777 *
	xattr -d com.apple.quarantine *
}

export PATH=/bin/:$PATH && export PATH=/usr/bin:$PATH
fix
cd main.app/Contents/MacOS/
fix
