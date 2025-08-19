# How to deploy a Minecraft Server

Use the Docker image `itzg/minecraft-bedrock-server`.

## Server Properties

You can edit things like `tick distance`.

```text
tick-distance=4
# The world will be ticked this many chunks away from any player.
# Allowed values: Integers in the range [4, 12]
```

["Server Properties"](https://minecraft.fandom.com/wiki/Server.properties)

## Useful commands

You can run commands in the container terminal

Whitelist users:

`allowlist add <USERNAME>`

Set the setting to show coordinates:

`gamerule showcoordinates true`
