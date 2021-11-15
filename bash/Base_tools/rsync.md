# rsync

## Options
```
-z                          compress
-P                          progress
--delete                    delete extraneous files from destination
-exclude <folder/filename   exclude files
-a                          preserves dates/times and permission
```
### Rare use case:
```
-e 'ssh -p 3022'            To access files on remote with specific port
```
`folder_name/` means the contents thereof.

`folder_name` refers to the whole folder.

Default:
```bash
rsync -azvP
```
