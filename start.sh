serverPath=$( cd "$( dirname "${BASH_SOURCE[0]}")" && pwd )

if [ ! -f $serverPath/server.pid ];
then
    nohup $(conda info --base)/envs/blog/bin/python $serverPath/server.py \
    > $serverPath/log/$(date "+%Y-%m-%d_%H-%M-%S.log") 2>&1 & echo $! > $serverPath/server.pid
fi
