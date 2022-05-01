# Install magicframe-flask as a system service

First, copy [magicframe_flask.service](./magicframe_flask.service) to `/etc/systemd/system`:
```
sudo cp magicframe_flask.service /etc/systemd/system/magicframe_flask.service
```

Then, start the system service with
```
sudo systemctl start magicframe_flask.service
```
and verify that it works:
```
sudo systemctl status magicframe_flask.service
```

To permanently enable the service, use:
```
sudo systemctl enable magicframe_flask.service
```
