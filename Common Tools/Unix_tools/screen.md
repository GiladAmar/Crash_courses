# Screen

    screen                      Create and attach to screen session
        -r                      Reattach session (use either id num or name following -r)
        -h num                  Set history to n lines
        -L                      Auto logging
        -S session_name         Use name instead of standard id
        -x                      Steal and attach to screen
        -ls                     List sessions

## In-screen commands

`ctrl + a`

### Navigation
    c           Create a new window
    n           Move to next window
    p           Move to previous window
    d           Detach
    esc         Scroll through window history
    0-9         Jump to window no #
        
### Regions
    S           Split horizontally
    |           Split vertically
    Tab         Move to next region
    X           Close current region
        
### Misc
    H           Log from window
    :           Access screen command line


## Command-line commands:
    sessionname dude - change the session name to dude