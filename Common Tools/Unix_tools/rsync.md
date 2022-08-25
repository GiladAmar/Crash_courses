# rsync

## Options
|           Option           | Description                              |
|:--------------------------:|:-----------------------------------------|
|             -a             | Preserve dates/times and permission      |
|             -z             | Compress                                 |
|             -P             | Progress bar                             |
|          --delete          | Delete extraneous files from destination |
| -exclude <folder/filename> | Exclude files                            |
|             -v             | Verbose                                  |

## Rare use case:
```
-e 'ssh -p 3022'            To access files on remote with specific port
--iconv=CONVERT_SPEC
  
  Rsync can convert filenames between character sets using this option. Using a CONVERT_SPEC of "." tells rsync to look up the default character-set via the locale setting. Alternately, you can fully specify what conversion to do by giving a local and a remote charset separated by a comma in the order --iconv=LOCAL,REMOTE, e.g. --iconv=utf8,iso88591. This order ensures that the option will stay the same whether you’re pushing or pulling files.
  
  Try
  rsync --iconv=. --archive /source /destination 
```
**NB**
`folder_name/` - means the contents thereof.
`folder_name` - refers to the whole folder.

## Useful default:
```bash
rsync -azvP
```
