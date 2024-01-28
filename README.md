# WS-EPHEMERAL

This project aims to automate setting up ephemeral port on Windscribe VPN
service for the purpose of port forwarding. It delete the ephemeral port setting if any and
set the new one. Useful for some torrent application which are running behind
Windscribe VPN and need to open the ports.

This is a custom version where it has to be automated externally (i.e. systemd timer)
and also writes the port number to a KEY=VALUE file.


### Environment Variables

| Variable             | Comment                                                                          |
| -------------------- | -------------------------------------------------------------------------------- |
| WS_USERNAME          | WS username                                                                      |
| WS_PASSWORD          | WS password                                                                      |
| WS_DEBUG             | Enable Debug logging                                                             |
| WS_COOKIE_PATH       | Persistent location for the cookie. (v3.x.x only)                                |
| QBIT_USERNAME        | QBIT username                                                                    |
| QBIT_PASSWORD        | QBIT password                                                                    |
| QBIT_HOST            | QBIT web address like, https://qbit.xyz.com or http://192.168.1.10               |
| QBIT_PORT            | QBIT web port number like, 443 or 8080                                           |
| QBIT_PRIVATE_TRACKER | get QBIT ready for private tracker by disabling dht, pex and lsd (true or false) |
| REQUEST_TIMEOUT      | configurable http api timeout for slow network/busy websites                     |


## Changelog

Located [here](./CHANGELOG.md)

## Privacy

I assure you that nothing is being collected or logged. Your credentials are
safe and set via environment variable only. Still If you have further questions
or concerns, please open an issue here.

## License

[GPL3](LICENSE.md)
