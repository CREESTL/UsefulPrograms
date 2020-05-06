# UsefulPrograms
While working on training a YOLOv3 neural network for my other projects I faced a problem.
For training we need to have a `obj` folder with:
- All out images
- All `.txt` files. One per image. Every file contains float numbers corresponding to object box coordinates.
Usually, this folder might be quite heavy.
Also the problem is that it's really hard to see if for each image there is a `.txt` file. Or if this file is not empty, which is also important while training.
So... I've created this program to help you (and me) get done with this routine faster
