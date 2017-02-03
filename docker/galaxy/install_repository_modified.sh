#!/bin/sh

# start Galaxy
service postgresql start

# check if postgresql is started
pg_isready
while [ "$?" -ne 0 ];
do
    sleep 1
    pg_isready
done

install_log='galaxy_install.log'
sudo -E -u galaxy ./run.sh --daemon --log-file=$install_log --pid-file=galaxy_install.pid

galaxy_install_pid=`cat galaxy_install.pid`

while : ; do
    tail -n 2 $install_log | grep -E -q "Removing PID file galaxy_install.pid|Daemon is already running"
    if [ $? -eq 0 ] ; then
        echo "Galaxy could not be started."
        echo "More information about this failure may be found in the following log snippet from galaxy_install.log:"
        echo "========================================"
        tail -n 60 $install_log
        echo "========================================"
        echo $1
        exit 1
    fi
    tail -n 2 $install_log | grep -q "Starting server in PID $galaxy_install_pid"
    if [ $? -eq 0 ] ; then
        echo "Galaxy is running."
        break
    fi
done

for repository in "$@"; do
    echo "Processing:\t $repository"
    python ./scripts/api/install_tool_shed_repositories.py --api admin -l http://localhost:8080 --tool-deps --repository-deps $repository
done

exit_code=$?

if [ $exit_code != 0 ] ; then
    exit $exit_code
fi

# stop everything
sudo -E -u galaxy ./run.sh --stop-daemon --log-file=$install_log --pid-file=galaxy_install.pid
rm $install_log
service postgresql stop
