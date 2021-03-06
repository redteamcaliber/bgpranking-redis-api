#!/bin/bash

while true; do
    echo ----- New Run -----
    date
    bash ./launch_local_redis.sh
    echo -n 'Preparing Redis database... '
    python ./init_redis.py
    echo 'done.'

    echo -n 'Exporting ranks to CSV... '
    for i in {1..10}; do
        python ./consumer.py &
    done
    python ./consumer.py
    echo 'done.'
    date

    sleep 10
    redis-cli -s ./redis_export.sock flushall

    # ------------------------------------------------------

    echo -n 'Preparing database...'
    python ./generate_aggs.py --push_known_asns

    echo -n 'Generating worldmap...'
    python ./generate_aggs.py --make_map
    echo 'done.'

    echo -n 'Fetching ASNs by country codes... '
    python ./generate_aggs.py --country_codes be ch de lu fr nl

    if [ $? -eq 0 ]; then
        echo 'done.'
        echo -n 'Preparing aggregations...'
        for i in {1..10}; do
            python ./agg_consummer.py &
        done
        python ./agg_consummer.py
        echo 'done.'
        date
        sleep 10

        # ------------------------------------------------------

        echo -n 'Dumping aggregations...'
        python ./generate_aggs.py --dump_country_codes world lu
        python ./generate_aggs.py --dump_country_codes be ch de lu fr nl
        echo 'done.'
    else
        echo ' unable to do so.'
    fi


    redis-cli -s ./redis_export.sock shutdown
    echo ----- End of Run. -----
    sleep 10000
done
