# Partilce Swarm Optimization demonstration
### Two-dimensional input and Single objective (finding minimum), with *Auto Hyperparameterization*

![PSO Demo](https://github.com/Vandalious/PSO-demonstration/blob/main/example_demonstrations/README-demo.gif "PSO on Levy function")

You may add your own functions as well, inside the `benchmark_functions.py` file. For that, you have to first define your function like a regular one, then you must insert the function attributes inside the dictionary, as this dictionary is what the other files use for getting the required information about the functions.

##### **NOTE**: In the resulting animation gif, a small *star symbol* can be seen on a specific part of each function. This star shows the function's **known** minimum, and is used to check how PSO is performing. If known, you may enter the function's known minimum in the *functions dictionary* (`minimum_x` and `minimum_y` keys), else just assign `None` value to them.
<br />

Whichever function you want to see the optimization get performed on, you can simply assign the *key* number that is mapped to your expected function in the functions dictionary, inside the `main.py` file. You can use `demonstrate` function's `file_path` argument to specify where you want to save the output gif.

##### **NOTE**: Output file is in `.gif` format, so your file name must end in *.gif*.
