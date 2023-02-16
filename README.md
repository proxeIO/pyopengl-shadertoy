# pyopengl-shadertoy
Simple base-line opengl shader toy written in python using PyOpenGL
  *on file save:* for shader files (for now)

```
pip install PyOpenGL PyOpenGL_accelerate
```

Demonstrating the use of the PyOpenGL library to create a window with an OpenGL context using vertex and fragment shaders.
Compiling vertex and fragment shaders from file paths, creating a shader program, adding a framebuffer object and a texture.

Rendering to a textured quad. Doing so by setting up a vertex buffer object (VBO) with the vertex positions and texture coordinates, quad texture is stored in a framebuffer object (FBO), which allows for off-screen rendering.

Checking for modification time of the shader files, recompiling the shader program if any of the files have been modified.
