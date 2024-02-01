<h1 align="left"> Fringe Pattern Profilometry with a Digital Twin in Blender </h1>
<h3 align="left">This is the main repository of the project "Implementing a digital twin in Fringe Projection Profilometry". </h3>
In this project we propose the implementation of a digital twin to simulate the reconstruction of 3D objects with the digital fringe projection technique. The main utility of this system is the flexibility to acquire the fringe images, obtaining a large number of images (faithful and with the same parameters of the real system) in a short time taking advantage of the GPU of the computer and thus being able to create feasible Datasets for the training of Deep Learning models.

## Dependencies
<a href="https://www.blender.org/" target="_blank" rel="noreferrer"> <img src="https://download.blender.org/branding/community/blender_community_badge_white.svg" alt="blender" width="40" height="40"/> </a><a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a><a href="https://opencv.org/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/opencv/opencv-icon.svg" alt="opencv" width="40" height="40"/> </a><a href="https://numpy.org/" target="_blank" rel="noreferrer"> <img src="https://cdn.worldvectorlogo.com/logos/numpy-1.svg" alt="numpy" width="38" height="38"/> </a>
- [Blender](https://www.blender.org/) 
- [Python3](https://www.python.org/)
- [NumPy](https://numpy.org/)
- [OpenCV](https://opencv.org/)
- [Projector Add-on for Blender](https://github.com/Ocupe/Projectors)

***All necessary dependencies and software are Open-Sourse**

## Set-up and Installation
1. Download and install the **Blender Projector Add-on** from this repository. [Guide to installing plugins in Blender](https://docs.blender.org/manual/en/latest/editors/preferences/addons.html)
2. If you have **CUDA-compatible graphics**, you can select it for rendering in the following settings. *Blender Preferences > System > Cycles Render Devices > CUDA.
3. Install OpenCV and Scipy in Blender. Aquí recomiendo instalar los paquetes en tu instalación de Python y luego copiarlos en la ruta `C:/Program Files/Blender Foundation/Blender 3.x/3.x/python/lib/site-packages/`
