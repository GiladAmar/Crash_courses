# Screen
|     Option      | Description                                           |
|:---------------:|:------------------------------------------------------|
|     screen      | Create and attach to screen session                   |
|       -r        | Reattach session (use either id num or name after -r) |
|     -h num      | Set history to n lines                                |
|       -L        | Auto logging                                          |
| -S session_name | Use name instead of standard id                       |
|       -x        | Steal and attach to screen                            |
|       -ls       | List sessions                                         |

# In-screen commands

`ctrl + a`

### Navigation
| Option | Description                   |
|:------:|:------------------------------|
|   c    | Create a new window           |
|   n    | Move to next window           |
|   p    | Move to previous window       |
|   d    | Detach                        |
|  esc   | Scroll through window history |
|  0-9   | Jump to window no #           |
        
### Regions
| Option | Description          |
|:------:|:---------------------|
|   S    | Split horizontally   |
| &#124; | Split vertically     |
|  Tab   | Move to next region  |
|   X    | Close current region |
        
### Misc
| Option | Description                |
|:------:|:---------------------------|
|   H    | Log from window            |
|   :    | Access screen command line |


## Command-line commands:
    sessionname dude - change the session name to dude