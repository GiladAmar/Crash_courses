#TMUX
Create a session 
```
tmux new -s session_name
```

Join a live session 
```
tmux attach-session -t session_name
```

List sessions: 
```
tmux ls
``` 

## Options
`Cntl + b + <>`

### Session Commands
    ?: List commands
    S: List sessions.

    $: Rename current session.
    d: Detach current session.

### Window Commands
    c           - Create a new window.
    ,           - Rename the current window.
    w           - List the windows.

    n           - Move to the next window.
    p           - Move to the previous window.
    0-9         - Move to the window number specified.

### Pane Commands
    %           - Create a horizontal split.
    “           - Create a vertical split.

    h/l_arrow   - Move to the pane on the left.
    i/r_arrow   - Move to the pane on the right.
    j/d_arrow   - Move to the pane below.
    k/u_arrow   - Move to the pane above.

    q           - Briefly show pane numbers.
    o           - Move through panes in order
    }           - Swap the position of the current pane with the next.
    {           - Swap the position of the current pane with the previous.
    x           - Close the current pane.