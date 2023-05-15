# 2023-05-15

## Log

### Initial setup


Created AWS Cloud9 Codespace to have a fresh Ubuntu install to work from. Starting with 4GB of Ram and 2 Cores. Suspect I'll need more...

Started working from here: https://data-workspace.docs.trade.gov.uk/development/running-locally/#prerequisites

Forked to my own repo, set up SSH key, cloned to codespace

Checked prerequisites. Both docker and git are present in my environment

ran `sudo chmod 777 /etc/hosts` - obviously this would be bad practice in prod, but it's expedient

added localhost dns to /etc/hosts

Ran:

```sh
cp .envs/sample.env .envs/dev.env
cp .envs/superset-sample.env .envs/superset.dev.env
```

Running `docker compose up --build`...
    
    - got: `#0 56.64 ERROR: Could not install packages due to an OSError: [Errno 28] No space left on device`
    - Upping machinine size. Went with 2 cores and 8GB of ram. Upped volume size from 10GB to 30GB. 
    - followed [these steps](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/recognize-expanded-volume-linux.html) to extend the partition.
        - note, it was `sudo resize2fs /dev/nvme0n1p1`, not `sudo xfs_growfs -d /` for the final step.
        

Re-running `docker compose up --build`...

Space usage has stabilised at around 11GB
    
Now getting a repeated error:

    ```
    data-workspace-data-workspace-celery-1      | requests.exceptions.ConnectionError: HTTPSConnectionPool(host='url.to.activity.stream', port=443): Max retries exceeded with url: //v3/activities/_search (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection object at 0x7f27000a0400>: Failed to establish a new connection: [Errno -2] Name or service not known'))
    ```
    
Process retried multiple times, but has moved on to another task now. Not sure what this means... Update: this error is back.

After waiting a while, it `ctrl+c` to kill the process.

```
^CGracefully stopping... (press Ctrl+C again to force)
Aborting on container exit...
[+] Running 7/7
 ✔ Container data-workspace-data-workspace-1             Stopped         10.4s 
 ✔ Container data-workspace-data-workspace-celery-1      Stopped         10.5s 
 ✔ Container data-workspace-data-workspace-sso.test-1    Stopped          0.3s 
 ✔ Container data-workspace-data-workspace-localstack-1  Stopped          0.0s 
 ✔ Container data-workspace-data-workspace-es-1          Stopped          0.7s 
 ✔ Container data-workspace-data-workspace-redis-1       Stopped          0.6s 
 ✔ Container data-workspace-data-workspace-postgres-1    Stopped         10.5s 

```

Note: *data-workspace-1 appeared to run succesfully. Next step #TODO: remove celery task or inject some print statements into the python (cel.py within datasworkspace)