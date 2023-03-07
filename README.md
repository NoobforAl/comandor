# comandor
Very Simple Script for Run your command!

### How Install

> pip install comandor

### How Use

- make file .comandor  
- setup config like this 

```json
{
  "name": "Update Apps!",
  "actions": [
    {
      "action_name": "scoop update pkg",
      "path": "C:/",
      "commands": [
        "scoop update -g *"
      ],
      "timeout": 5000
    }
    // you can add more action
  ]
}
```  

- you can see .comandor.example for more example  
- and run this command

> comandor 

### Command Line Help

<div>

| Command |                                      Info                                              |
| -----   | :--------------------------------------------------------------------------------------: |
| -h      |                                      see help                                            |
| -l < path log file >  | where save logFile, if don't use this, not save logs |
| -c  < path config file > | setup yor config file instead of .comandor file |
| -d   | run program debug mode |

</div>