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
    got: `#0 56.64 ERROR: Could not install packages due to an OSError: [Errno 28] No space left on device`
    
Upping machinine size.

