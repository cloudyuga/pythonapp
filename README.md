
# Pythonapp
We have created the new Docker image `teamcloudyuga/pythonprog` with given `Dockerfile`. This image is using `python:2.7` as its base image. In it's `Dockerfile`, we have specified the all the configurations and the `ENTRYPOINT` instruction. All of the programs are copied inside the container at `/app/program/` with name `p1.py`, `p2.py`. We can choose to have it outside as well. 

While running the container we pass the program name as environment variable, which becomes an agrument `demo.py` program. `demo.py` program takes the program name from environment variable and executes it. The output of the program get inside the `/app/program/output` folder, which is being mounted from `/mnt/shared` directory of the host system. So all of the outputs are saved on host system `/mnt/shared` directory, with `.txt` suffix. So for program `p1.py`, the output would be saved as `p1.py.txt` 

Following is the workflow and some examples. 

- Create a directory for mounting volume in the container. We will have all the outputs here in this directory.
```
$ sudo mkdir -p /mnt/shared
```

- Now run the program  `p1.py`
```
$ docker run --rm -it -e PROGRAM_NAME='p1.py' -v /mnt/shared/:/app/program/output teamcloudyuga/pythonprog
output will be stored in file /mnt/shared/p1.py.txt
```

- Check the output File.
```
$ cat /mnt/shared/p1.py.txt
2002,2009,2016,2023,2037,2044,2051,2058,2072,2079,2086,2093,2107,2114,2121,2128,2142,2149,2156,2163,2177,2184,2191,2198,2212,2219,2226,2233,2247,2254,2261,2268,2282,2289,2296,2303,2317,2324,2331,2338,2352,2359,2366,2373,2387,2394,2401,2408,2422,2429,2436,2443,2457,2464,2471,2478,2492,2499,2506,2513,2527,2534,2541,2548,2562,2569,2576,2583,2597,2604,2611,2618,2632,2639,2646,2653,2667,2674,2681,2688,2702,2709,2716,2723,2737,2744,2751,2758,2772,2779,2786,2793,2807,2814,2821,2828,2842,2849,2856,2863,2877,2884,2891,2898,2912,2919,2926,2933,2947,2954,2961,2968,2982,2989,2996,3003,3017,3024,3031,3038,3052,3059,3066,3073,3087,3094,3101,3108,3122,3129,3136,3143,3157,3164,3171,3178,3192,3199
```

- Run the program `p24.py`.
```
$ docker run --rm -it -e PROGRAM_NAME='p24.py' -v /mnt/shared/:/app/program/output teamcloudyuga/pythonprog
output will be stored in file /mnt/shared/p24.py.txt
```
Check the output at `/mnt/shared/p24.py.txt`.

- Run the program `p8.py`. And in the console give input `without,hello,bag,world`
```
$ docker run --rm -it -e PROGRAM_NAME='p8.py' -v /mnt/shared/:/app/program/output teamcloudyuga/pythonprog

without,hello,bag,world

output will be stored in file /mnt/shared/p8.py.txt
```

Check the output at `/mnt/shared/p8.py.txt`.
