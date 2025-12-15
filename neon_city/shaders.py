"""
GLSL shader code for post-processing effects.
"""

# Simple Scanline + Bloom-ish effect GLSL
FRAGMENT_SHADER = """
#version 330

in vec2 fragTexCoord;
in vec4 fragColor;

out vec4 finalColor;

uniform sampler2D texture0;
uniform vec2 resolution;
uniform float time;

void main()
{
    vec4 texel = texture(texture0, fragTexCoord);

    // 1. Scanlines
    float scanline = sin(fragTexCoord.y * resolution.y * 3.1415 * 2.0);
    texel.rgb -= scanline * 0.05;

    // 2. Vignette
    vec2 uv = fragTexCoord;
    uv *=  1.0 - uv.yx;
    float vig = uv.x*uv.y * 15.0;
    vig = pow(vig, 0.2);
    texel.rgb *= vig;

    // 3. Simple color boost (fake bloom contrast)
    texel.rgb = pow(texel.rgb, vec3(0.9)); // Gamma correction

    finalColor = texel * fragColor;
}
"""
