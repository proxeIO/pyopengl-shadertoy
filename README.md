# pyopengl-shadertoy
Simple base-line opengl shader toy written in python using PyOpenGL
  *on file save:* for shader files (for now)

```
pip install PyOpenGL PyOpenGL_accelerate
```

Demonstrating the use of the PyOpenGL library to create a window with an OpenGL context and render graphics using vertex and fragment shaders.
The script compiles vertex and fragment shaders from file paths, creating a shader program, adding a framebuffer object and a texture, and continuously updates the program based on the modification time of the shader files.

The script uses PyOpenGL to create a window with an OpenGL context and renders a textured quad.
It does so by setting up a vertex buffer object (VBO) with the vertex positions and texture coordinates, compiling shaders from source files, creating a shader program, and rendering the quad with the shader program.
The texture for the quad is stored in a framebuffer object (FBO), which allows for off-screen rendering.

The script continuously checks the modification time of the shader files and recompiles the shader program if any of the files have been modified.
This allows for dynamic updating of the shader program without having to restart the script.
