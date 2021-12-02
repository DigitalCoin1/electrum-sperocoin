#!/usr/bin/env bash
export HOME=~
set -eux pipefail
mkdir -p ~/.SperoCoin
cat > ~/.SperoCoin/SperoCoin.conf <<EOF
regtest=1
txindex=1
printtoconsole=1
rpcuser=doggman
rpcpassword=donkey
rpcallowip=127.0.0.1
zmqpubrawblock=tcp://127.0.0.1:28332
zmqpubrawtx=tcp://127.0.0.1:28333
fallbackfee=0.0002
[regtest]
rpcbind=0.0.0.0
rpcport=18554
EOF
rm -rf ~/.SperoCoin/regtest
screen -S SperoCoind -X quit || true
screen -S SperoCoind -m -d SperoCoind -regtest
sleep 6
SperoCoin-cli createwallet test_wallet
addr=$(SperoCoin-cli getnewaddress)
SperoCoin-cli generatetoaddress 150 $addr > /dev/null
