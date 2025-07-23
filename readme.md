AES Key wrap code from - https://gist.github.com/kurtbrose/4243633

Watchguard Key info from https://serverfault.com/questions/790339/merge-vpns-of-two-watchguard-firewalls-into-one-firewall

This code takes a watchguard PSK from the exported XML config file and returns plaintext value.
PSKs starting with '+' character are able to be decrypted.



NEEDED:
- Python 3
- pip install pycryptodome

## Docker

Build the Docker image and run the tool:

```bash
docker build -t decrypt-wg .
echo "+HEXPSK" | docker run -i decrypt-wg
```

You can also pass the PSK as the first command line argument:

```bash
docker run decrypt-wg +HEXPSK
```
