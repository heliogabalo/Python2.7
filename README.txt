Drop your multi-file modules inside a specific directory,
and name each one as the application name.
So this dir should contain ME, as unique file. You can add
paths to the python environment freely.

Import the sys module and look your path system environment.
To add paths to the list of configured -or system dependent
addresses: sys.path.insert(index, 'path_to_dir'). The empty
string refers to the current working directory, this is zero 0.

To remove an item from the list, just pop it up:
		sys.path.pop(index).

cmd variable used with mySystem module could be deprecated
on next updates.
NOTE: I think it is no needed any more; save the code in a 
new file and place it under a directory for the task. If
the directory is included as environment path, enchant the 
the import statement with the file name without extension.
