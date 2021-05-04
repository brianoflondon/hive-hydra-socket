# hive-hydra-socket

Basic socket to run and listend for a connection. Anything sent will be put into a custom_json on Hive.

I presume this needs some other web engine and packaging in some way but this is all the Python you need.

The watching programs can be found in https://github.com/brianoflondon/hive-hydra/blob/main/watcher.py


## IMPORTANT:

This defaults to using a Hive Testnet not the main chain.

```
# Testnet instead of main Hive
USE_TEST_NODE = True
TEST_NODE = ['http://testnet.openhive.network:8091']
```

To use the main chain, all you have to do is set ```USE_TEST_NODE``` to False.

For testing, the watching program and the posting program have to be using the same Hive Node. If no node is specified (i.e. when testing is turned off) the program will automatically choose a live Hive node and will hunt for a new one if a timeout or failure occurs.


