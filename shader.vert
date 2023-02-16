#version 330 core

in vec3 position;
in vec2 uv;

out vec2 uv_out;


void main() {
    gl_Position = vec4(position, 1.0);
    uv_out = vec2(uv.x, uv.y);
}

