# pyopengl-shadertoy
Simple base-line opengl shader toy written in python using PyOpenGL
  *on file save:* for shader files (for now)

```
pip install PyOpenGL PyOpenGL_accelerate
```

Demonstrating the use of the PyOpenGL library to create a window with an OpenGL context using vertex and fragment shaders.
Compiling vertex and fragment shaders from file paths, creating a shader program, adding a framebuffer object and a texture, and continuously updating that program based on the modification time of the shader files.

Using PyOpenGL to create a window with an OpenGL context, rendering to a textured quad.
Doeing so by setting up a vertex buffer object (VBO) with the vertex positions and texture coordinates, rendering the quad with the shader program.
The texture for the quad is stored in a framebuffer object (FBO), which allows for off-screen rendering.

Then continuously checking for modification time of the shader files, recompiling the shader program if any of the files have been modified.
