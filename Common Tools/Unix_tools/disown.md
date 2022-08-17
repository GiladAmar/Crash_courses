# Disown
Better yet, use screen or tmux

## Push command to the background
```bash
mv a b/
cntl + z
bg
````

## Run command in the background
```bash
mv a b/&
```

## Ensure process runs when terminal is closed
```bash
disown -a
```
## Attach to process from a new terminal
```bash
setsid process
```

