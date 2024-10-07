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

## Ensure the process runs when the terminal is closed
```bash
disown -a
```
## Attach to a process from a new terminal
```bash
setsid process
```

