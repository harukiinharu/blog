serverPath=$(cd $(dirname $0); pwd)

if [ -f $serverPath/server.pid ];
then
    kill $(cat $serverPath/server.pid)
    rm $serverPath/server.pid
fi
